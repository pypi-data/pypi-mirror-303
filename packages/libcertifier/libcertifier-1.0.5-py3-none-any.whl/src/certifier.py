
from src.log import log
from src.property import CertifierPropMap, property_new, property_get, property_set, property_set_defaults_from_cfg_file, property_is_option_set
from src.constants import *
from src.error import CertifierError, gen_application_error_msg, certifier_create_info

from cryptography import x509
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import ec, utils
from cryptography.hazmat.primitives.serialization import pkcs12, pkcs7, Encoding, PublicFormat
from cryptography.hazmat.backends import default_backend
from argparse import Namespace
from os import access, R_OK, path
from datetime import datetime, timedelta, UTC
import base64, base58, json, secrets, hashlib, psutil, time

class certifier_cfg():
    def __init__(self, file_name = None, level = 4, quiet = 1, max_size = 5000000):
        self._file_name: str = file_name
        self._level: int = level
        self._quiet: int = quiet
        self._newlines: int = 0
        self._stripped: int = 0
        self._max_size: int = max_size
        self._http_connect_timeout: int = None

class Map():
    node_address: str = None
    base64_public_key: str = None
    der_public_key: bytes = None
    der_public_key_len: int = None
    private_ec_key = None
    x509_cert: x509.Certificate = None
    
class Certifier():
    def __init__(self) -> None:
        self.CertifierPropMap: CertifierPropMap = CertifierPropMap()
        self.tmp_map: Map = Map()
        self.last_error: CertifierError = CertifierError()

def assign_last_error(certifier: Certifier, error: CertifierError):
    '''
    Clears certifier instance's last error and assigns error passed as argument
    '''
    certifier.last_error.clear()
    certifier.last_error = error

def set_last_error(certifier: Certifier, error_code: int, error_string: str):
    '''
    Sets certifier instance's last error with application error code and message passed as arguments
    '''
    certifier.last_error.application_error_code = error_code
    certifier.last_error.application_error_msg = error_string

def get_last_error(certifier: Certifier):
    '''
    Returns certifier instance's last error assigned
    '''
    return certifier.last_error
        
def certifier_new(args: Namespace):
    '''
    Creates a new certifier instance. 
    
    Returns certifier instance on success.
    
    Returns None on failure
    '''
    rc = CertifierError()

    cfg_file = None

    certifier = Certifier()

    certifier.CertifierPropMap = property_new()

    if args.config and path.exists(args.config):
        property_set(certifier.CertifierPropMap, CERTIFIER_OPT.CERTIFIER_OPT_CFG_FILENAME, args.config)

    cfg_file = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_CFG_FILENAME)

    verbose = True if args.verbose else False
        
    if cfg_file and path.exists(cfg_file) and access(cfg_file, R_OK):
        certifier_load_cfg_file(certifier, verbose)
        
    if args.command != 'get-crt-token' and args.command != 'print-cert' and args.ca_path:
        property_set(certifier.CertifierPropMap, CERTIFIER_OPT.CERTIFIER_OPT_CA_PATH, args.ca_path)
    
    assign_last_error(certifier, rc)

    return certifier

def certifier_set_property(certifier: Certifier |  None, name: int, value):    
    '''
    Function vets the name of property and value to set. If valid, will attempt to set certifier instance's CertifierPropMap accordingly
        
    '''
        
    if name is None:
        set_last_error(certifier, 1, gen_application_error_msg("Property name was None", None))
        certifier_create_info(get_last_error(certifier), property_error + 1, None)
    if value is None:
        set_last_error(certifier, 2, gen_application_error_msg(f"Property value was None", None))
        certifier_create_info(get_last_error(certifier), property_error + 2, None)
    if name <= 0:
        set_last_error(certifier, 3, gen_application_error_msg("Property name was <= 0", None))
        certifier_create_info(get_last_error(certifier), property_error + 3, None)
    elif (name > max(CERTIFIER_OPT, key = lambda e: e.value)):
        log("invalid property [" + str(name) + "]", "ERROR")
        set_last_error(certifier, 4, gen_application_error_msg("Property name was > than max in CERTIFIER_OPT enum.", None))
        certifier_create_info(get_last_error(certifier), property_error + 4, None)
    
    if (isinstance(value, int) and value < 0):
        set_last_error(certifier, 5, gen_application_error_msg("Property integer value was < 0", None))
        certifier_create_info(get_last_error(certifier), property_error + 5, None)

    if name == CERTIFIER_OPT.CERTIFIER_OPT_CFG_FILENAME:
        log("Configuration file changed' loading settings", "INFO")

        # Blow away all settings and reload from config to avoid mixed configs
        certifier.CertifierPropMap = property_new()
        
        property_set(certifier.CertifierPropMap, name, value)

        certifier_load_cfg_file(certifier)
    else:
        property_get(certifier.CertifierPropMap, name)
        property_set(certifier.CertifierPropMap, name, value)

def certifier_get_property(certifier: Certifier | None, name: int):
    '''
    Attempts to retrieve property from certifier instance's CertifierPropMap
    
    Returns value of property on success
    
    Program exits and reports an error with property-related code mapping via helper on failure
    '''
    if (certifier is None):
        log("certifier cannot be None", "ERROR")
        return None
        
    return property_get(certifier.CertifierPropMap, name)

def certifier_load_cfg_file(certifier: Certifier | None, verbose: bool):
    '''
    Attempts to set properties in certifier instance's CertifierPropMap from either default config file or user-provided config through CLI
    
    Returns None on success
    
    Program exits and reports an error with property-related code mapping via helper on failure
    '''
    property_set_defaults_from_cfg_file(certifier.CertifierPropMap, verbose)
        
def load_pkcs12_file(certifier: Certifier, p12_path, password = None):  
    '''
    Attempts to load given PKCS12 file with the provided password.
    
    Returns private key, certificate, and any additional certificates from the bundle on success
    
    Constructs a CertifierError() and returns tuple of that error on failure
    '''  
    file = p12_path if (isinstance(p12_path, str)) else p12_path.name
        
    with open (file, "rb") as p12_file:
        p12_data = p12_file.read()

    if p12_data is None:
        set_last_error(certifier, 3, gen_application_error_msg("Failed to read PKCS12 file. The file may be empty or unreadable", None))
        return [get_last_error(certifier)] * 3
    
    try:
        private_key, certificate, additional_certs = pkcs12.load_key_and_certificates(p12_data, str.encode(password, encoding="utf-8"), default_backend())
    except ValueError:
        set_last_error(certifier, 4, gen_application_error_msg("Invalid password or PKCS12 data while trying to load file.", None))
        return [get_last_error(certifier)] * 3

    if private_key is None:
        set_last_error(certifier, 5, gen_application_error_msg("Failed to load private key from PKCS12 file", None))
        return [get_last_error(certifier)] * 3
        
    if certificate is None:
        set_last_error(certifier, 6, gen_application_error_msg("Failed to load certificate from PKCS12 file", None))
        return [(get_last_error(certifier))] * 3

    if not isinstance(additional_certs, (list, type(None))):
        set_last_error(certifier, 7, gen_application_error_msg("Additional certificates from PKCS12 file must be a list or None", None))
        return [get_last_error(certifier)] * 3

    return private_key, certificate, additional_certs

def verify_certificate(certifier: Certifier, certificate, as_helper: bool):
    '''
    Function to compare certificate's validity against current system time.
    
    Returns None and sets the output field of certifier instance's last_error as the validity of the certificate on success
    
    Returns CertifierError() on failure
    '''
    try:
        current_time = datetime.now(UTC)
            
        if (current_time < certificate.not_valid_before_utc):
            if not as_helper:
                log("Certificate is not yet valid. Not valid before: " + str(certificate.not_valid_before_utc), "INFO")
            assign_last_error(certifier, CertifierError(output=CERTIFIER_ERR_REGISTRATION_STATUS_CERT_EXPIRED_1))
        elif current_time > certificate.not_valid_after_utc:
            if not as_helper:
                log("Certificate has expired. Not valid after: " + str(certificate.not_valid_after_utc), "ERROR")
            assign_last_error(certifier, CertifierError(output=CERTIFIER_ERR_REGISTRATION_STATUS_CERT_EXPIRED_2))          
        elif (certificate.not_valid_after_utc - current_time).days < timedelta(seconds=certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_CERT_MIN_TIME_LEFT_S)).days:
            if not as_helper:
                log("Certificate is close to expiring. Please renew it using the 'renew-cert' command. Expires on: " + str(certificate.not_valid_after_utc), "WARN")
            assign_last_error(certifier, CertifierError(output=CERTIFIER_ERR_REGISTRATION_STATUS_CERT_ABOUT_TO_EXPIRE))
        else:
            if not as_helper:
                log("Certificate is valid and not close to expiring. Expires on: " + str(certificate.not_valid_after_utc), "INFO")
            assign_last_error(certifier, CertifierError(output=CERTIFIER_ERR_REGISTRATION_STATUS_CERT_TIME_VALID))
    except AssertionError:
        return get_last_error(certifier)
              
def certifier_setup_keys(certifier: Certifier):   
    '''
    Loads private key from provided PKCS12 file. If not in keystore, creates it before calling certifier_set_key_addresses_with_cn_prefix()
    
    Returns None on Success
    
    Program exits and reports an error with certifier-related code mapping on failure
    '''
    try: 
        p12_filename = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PATH)
        password = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PASSWORD)
        cn_prefix = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_CN_PREFIX)
    
        private_key = None
        
        file = p12_filename if (isinstance(p12_filename, str)) else p12_filename.name

        if path.exists(file):
            private_key, _, _ = load_pkcs12_file(certifier, file, password)

        assert not isinstance(private_key, CertifierError)
        
        if private_key is None:
            # Key not found in keystore, need to create
            log("\nGenerating Elliptic Curve Key Pair...\n", "DEBUG")
            private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())

        certifier_set_keys_and_node_addresses_with_cn_prefix(certifier, private_key, cn_prefix)
    except AssertionError:
        last_error = get_last_error(certifier)
        certifier_create_info(last_error, certifier_error + last_error.application_error_code + last_error.library_error_code, None)

def certifier_create_x509_crt(certifier: Certifier):
    '''
    Function to create CRT (certificate request token) by means of x509 authentication with seed certificate
    
    Returns CRT on success
    
    Returns CertifierError() on failure
    '''
    try:
        generated_crt = None

        cert = None
        private_key = None

        log("calling get_cert()", "INFO")

        cert = get_cert(certifier)

        if cert is None:
            set_last_error(certifier, 2, gen_application_error_msg("Failed to retrieve certificate to create CRT", None))
            assert False
        
        private_key = _certifier_get_privkey(certifier)

        if private_key is None:
            set_last_error(certifier, 3, gen_application_error_msg("Failed to retrieve private key to create CRT", None))
            assert False
        
        root_obj = {}
        root_obj["tokenType"] = "X509"
        
        der_cert, der_base64 = get_der_cert_and_b64_der_cert(certifier, cert)
        
        assert not isinstance(der_cert, CertifierError) and not isinstance(der_base64, CertifierError)
        
        root_obj["certificate"] = str(der_base64)
        
        current_time = datetime.now()
        timestamp = str(int(current_time.timestamp() * 1000))
        
        root_obj["timestamp"] = timestamp
        
        nonce = ''.join(secrets.choice(ALLOWABLE_CHARACTERS) for i in range(16))
                
        root_obj["nonce"] = nonce
            
        try:
            sha256_input = der_cert + timestamp.encode('utf-8') + nonce.encode('utf-8') + b"X509"
            digest = hashlib.sha256(sha256_input).digest()
            
        except Exception as e:
            set_last_error(certifier, 4, gen_application_error_msg(f"SHA256 hashing failed with exception: {e}", None)) 
            assert False
                    
        try:
            signature = private_key.sign(
                digest,
                ec.ECDSA(utils.Prehashed(hashes.SHA256()))
            )
        except Exception as e:
            set_last_error(certifier, 5, gen_application_error_msg(f"Signature creation failed with exception: {e}", None))
            assert False
                
        signature_base64 = base64.b64encode(signature).decode('utf-8')
        
        root_obj["signature"] = signature_base64   

        generated_crt = json.dumps(root_obj, indent=4)

        log(f"Generated CRT is: {generated_crt}\n", "INFO")

        return generated_crt
    except AssertionError:
        return get_last_error(certifier)

def certifier_create_crt(certifier: Certifier, token_type):
    '''
    Function to create CRT (certificate request token) by means of SAT authentication
    
    Returns CRT on success
    
    Returns CertifierError() on failure 
    '''
    try:
        transaction_id = None
        serialized_string = None
        token = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_AUTH_TOKEN)
                
        if not token:
            set_last_error(certifier, 6, gen_application_error_msg("Authentication token couldn't be retrieved", None))
            assert False
                
        transaction_id = ''.join(secrets.choice(ALLOWABLE_CHARACTERS) for i in range(16))

        log(f"Transaction ID is: {transaction_id}", "DEBUG")
        
        try:
            date = datetime.now()
            timestamp_msec = str(int(date.timestamp() * 1000))
        except Exception as e:
            set_last_error(certifier, 7, gen_application_error_msg(f"Failed to retrieve system time in milliseconds: {e}", None))
            assert False
        
        log("timestamp in milliseconds since epoch is: " + str(timestamp_msec), "DEBUG")

        obj = {
            "tokenType": token_type,
            "token": token,
            "nonce": transaction_id,
            "timestamp": timestamp_msec
        }

        serialized_string = json.dumps(obj, indent=4)
        
        log(f"Generated CRT is: {serialized_string}\n", "INFO")
                
        return str(serialized_string)
    except AssertionError:
        return get_last_error(certifier)

def certifier_get_device_registration_status(certifier: Certifier, as_helper: bool):   
    '''
    Function to get validity of certificate by calling helper verify_certificate(). 
    
    Returns None and sets the output field of certifier instance's last_error as the validity of the certificate on success
    
    Returns CertifierError() if function or any of its helpers fail
    '''
    try:                 
        p12_filename = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PATH)
        password = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PASSWORD)
        
        file = p12_filename if (isinstance(p12_filename, str)) else p12_filename.name

        if (os.path.exists(file)):
            if not as_helper:
                log("PKCS12 file " + file + " exists. Loading x509 to check certificate validity", "DEBUG")
        else:
            set_last_error(certifier, 2, gen_application_error_msg("Could not find the PKCS12 file with the path configured in Certifier instance", None))
            return get_last_error(certifier)
        
        _, certificate, _ = load_pkcs12_file(certifier, file, password)
                       
        assert not isinstance(certificate, CertifierError)
        
        assert verify_certificate(certifier, certificate, as_helper) == None
    except AssertionError:
        return get_last_error(certifier)

def certifier_get_device_certificate_status(certifier: Certifier, as_helper: bool): 
    from src.certifier_client import check_certificate_status

    '''
    Function to get status of certificate by calling helper check_certificate_status(). 
    
    Returns None and sets the output field of certifier instance's last_error as the status of the certificate on success
    
    Returns CertifierError() if function or any of its helpers fail
    '''             
    try:
        p12_filename = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PATH)
        password = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PASSWORD)

        file = p12_filename if (isinstance(p12_filename, str)) else p12_filename.name

        if (os.path.exists(file)):
            if not as_helper:
                log(msg="PKCS12 file " + file + " exists. Loading x509 to check certificate status (good, unknown, revoked)", lvl="DEBUG")
        else:        
            set_last_error(certifier, 2, gen_application_error_msg("Could not find the PKCS12 file with the path configured in Certifier instance", None))
            return get_last_error(certifier)

        der_data = None

        _, certificate, _ = load_pkcs12_file(certifier, file, password)

        assert not isinstance(certificate, CertifierError)

        der_data = certificate.public_bytes(encoding= serialization.Encoding.DER)

        if (not der_data or not isinstance(der_data, (bytes, bytearray))):
            set_last_error(certifier, 8, gen_application_error_msg("Failed to serialize certificate to DER format.", None))
            return get_last_error(certifier)

        sha1_hash = hashlib.sha1(der_data).hexdigest()

        # Check certificate's status (good, unknown or revoked)        
        # assert check_certificate_status(certifier, sha1_hash, as_helper) == None    
        assert check_certificate_status(certifier, sha1_hash, as_helper) == None        

    except AssertionError:
        return get_last_error(certifier)

def certifier_renew_certificate(certifier: Certifier): 
    from src.certifier_client import renew_x509_certificate
    '''
    Loads certificate to be renewed and computes SHA1 hash of serialized certificate. Calls helpers to make API request and save new certificate chain to filesystem.
    
    Returns None on success
    
    Returns CertifierError() on failure
    '''     
    try:      
        der_data = None
        
        p12_filename = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PATH)
        password = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PASSWORD)

        file = p12_filename if (isinstance(p12_filename, str)) else p12_filename.name

        # If there is a .p12 file, then we were already registered
        if (os.path.exists(file)):

            _, certificate, _ = load_pkcs12_file(certifier, file, password)
            
            assert not isinstance(certificate, CertifierError)

            der_data = certificate.public_bytes(encoding = serialization.Encoding.DER)

            sha1_hash = hashlib.sha1(der_data).hexdigest()

        x509_certs = renew_x509_certificate(certifier, sha1_hash)
        
        if isinstance(x509_certs, CertifierError):
            log("\n<<< Failed to Request X509 Certificate! >>>\n", "ERROR")
            assert False
        else:
            log("\nObtained x509 Certificate Successfully!\n", "INFO")
            
        if (_certifier_get_privkey(certifier) == None or certifier.tmp_map.der_public_key == None or certifier.tmp_map.base64_public_key == None):
            set_last_error(certifier, 17, gen_application_error_msg("Failed to retrieve private key or public key setup failed", None))
            assert False                

        assert save_x509_certs_to_filesystem(certifier, x509_certs, True, file, password) == None
    except AssertionError:
        return get_last_error(certifier)
    
def _certifier_get_privkey(certifier: Certifier):
    '''
    Function to retrieve private key from PKCS12 bundle. If not set, will call helper certifier_setup_keys() to generate and return key.
    
    Returns private key on success
    
    Program exits and reports an error with certifier-related code mapping on failure
    '''
    if (certifier.tmp_map.private_ec_key == None):
        certifier_setup_keys(certifier)
        
    return certifier.tmp_map.private_ec_key

def get_cert(certifier: Certifier):
    '''
    Attempts to load certificate and update certifier instance's tmp_map.x509_cert field.
        
    Returns certificate on success
        
    Returns None on failure
    '''
    try:
        if certifier.tmp_map.x509_cert == None:
            p12_filename = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PATH)
            p12_password = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PASSWORD)
            
            if path.exists(p12_filename):    
                _, certifier.tmp_map.x509_cert, _ = load_pkcs12_file(certifier, p12_filename, p12_password)
                
                assert not isinstance(certifier.tmp_map.x509_cert, CertifierError)
        return certifier.tmp_map.x509_cert
    except AssertionError:
        return get_last_error(certifier)
            
def save_x509_certs_to_filesystem(certifier: Certifier, x509_certs, renew_mode, p12_filename, password):
    '''
    Attempts to save x509 certs bundle received from API to filesystem. Saves to path corresponding to certifier instance's output path. If not provided on command line, will default to "output.p12".
    Stores leaf certificate from bundle as certifier instance's cert_x509_out property. 
    
    Returns None on success
    
    Returns CertifierError() on failure
    '''
    try:        
        certs = []
        
        file = p12_filename if (isinstance(p12_filename, str)) else p12_filename.name
            
        if path.exists(file) and not renew_mode:
            log(f"PKCS12 file {file} exists. NOT overwriting!", "INFO")
            return      

        try:
            log("\nTrimming x509 certificates...\n", "INFO")
            x509_certs = x509_certs.strip()
        
            log("Loading Certs from PKCS7...\n", "INFO")
            certs = pkcs7.load_pem_pkcs7_certificates(x509_certs.encode())
        except Exception as e:
            log("Failed to load certs from PEM: " + str(e), "ERROR")
            set_last_error(certifier, 18, gen_application_error_msg(f"Failed to load certs from PEM: {e}", None))
            assert False
            
        log_level = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_LOG_LEVEL)
        
        if log_level != 4:
            for cert in certs:
                log(cert.public_bytes(Encoding.PEM).decode('utf-8'), "DEBUG")
        
        leaf = certs.pop(0) if certs else None
        
        if leaf is None:
            log("Failed to retrieve leaf certificate from chain", "ERROR")
            set_last_error(certifier, 19, gen_application_error_msg("Failed to retrieve leaf certificate from chain", None))
        else:
            certifier.tmp_map.x509_cert = leaf
            certifier_set_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_CERT_X509_OUT, leaf)
        
        output = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_OUTPUT_P12_PATH)
                        
        try:            
            log(f"Saving PKCS12 file {file}...", "INFO")
            
            pkcs12_data = pkcs12.serialize_key_and_certificates(
                name = None,
                key=certifier.tmp_map.private_ec_key,
                cert=leaf,
                cas=certs,
                encryption_algorithm=serialization.NoEncryption() if password is None else serialization.BestAvailableEncryption(password.encode())
            )
            
            with open(output, "wb") as p12_file:
                p12_file.write(pkcs12_data)
                log(f"Persisted PKCS12 file {file}", "INFO")

        except Exception as e:
            log("Failed to save PKCS12 file: " + str(e), "ERROR")
            set_last_error(certifier, 20, gen_application_error_msg(f"Failed to save PKCS12 file: {e}", None))
            assert False
                        
    except AssertionError:
        return get_last_error(certifier)
    
def certifier_revoke_certificate(certifier: Certifier):
    from src.certifier_client import revoke_x509_certificate
    '''
    Loads certificate to be revoked and computes SHA1 hash of serialized certificate. Calls helper to make API request
    
    Returns None on success
    
    Returns CertifierError() on failure
    '''
    try:      
        der_data = None
        
        p12_path = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PATH)
        password = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PASSWORD)

        file = p12_path if (isinstance(p12_path, str)) else p12_path.name

        # If there is a .p12 file, then we were already registered
        if (os.path.exists(file)):

            _, certificate, _ = load_pkcs12_file(certifier, file, password)
    
            assert not isinstance(certificate, CertifierError)

            der_data = certificate.public_bytes(encoding= serialization.Encoding.DER)

            if (not der_data or not isinstance(der_data, (bytes, bytearray))):
                    set_last_error(certifier, 8, gen_application_error_msg("Failed to serialize certificate to DER format.", None))
                    assert False
                    
            sha1_hash = hashlib.sha1(der_data).hexdigest()
        else:
            set_last_error(certifier, 2, gen_application_error_msg("Could not find the PKCS12 file with the path configured in Certifier instance", None))
            assert False
            
        assert revoke_x509_certificate(certifier, sha1_hash) == None        
    except AssertionError:
        return get_last_error(certifier)
            
def certifier_set_keys_and_node_addresses_with_cn_prefix(certifier: Certifier, new_key, cn_prefix):
    '''
    Sets private key (used for signing CSR) and both standard/base64 encoded public key. Creates node address using public key if CN prefix isn't set. 

    Returns None on Success
    
    Program exits and reports an error with certifier-related code mapping on failure    
    '''
    try:        
        certifier.tmp_map.private_ec_key = new_key    
        
        input_p12_path = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PATH)
        input_p12_password = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PASSWORD)
        
        file = input_p12_path if (isinstance(input_p12_path, str)) else input_p12_path.name
        
        if path.exists(file):
            _, certificate, _ = load_pkcs12_file(certifier, input_p12_path, input_p12_password)
            
            assert not isinstance(certificate, CertifierError)

            certifier.tmp_map.x509_cert = certificate
        
        certifier.tmp_map.der_public_key = None
        
        public_key = new_key.public_key()
        
        der_public_key = public_key.public_bytes(
            encoding=Encoding.DER,
            format=PublicFormat.SubjectPublicKeyInfo
        )
        
        if (not der_public_key or not isinstance(der_public_key, (bytes, bytearray))):
            set_last_error(certifier, 8, gen_application_error_msg("Failed to serialize certificate to DER format.", None))
            assert False
        
        certifier.tmp_map.der_public_key = der_public_key
                
        certifier.tmp_map.base64_public_key = base64.b64encode(certifier.tmp_map.der_public_key)
            
        if cn_prefix != None:
            certifier.tmp_map.node_address = cn_prefix
        else:
            tmp_node_address = certifier_create_node_address(certifier.tmp_map.der_public_key, certifier)
            
            assert get_last_error(certifier).application_error_code + get_last_error(certifier).library_error_code != 0
            
            certifier.tmp_map.node_address = tmp_node_address
        
        log("\nNode Address: " + str(certifier.tmp_map.node_address) + "\n", "DEBUG")        
    except AssertionError:
        last_error = get_last_error(certifier)
        certifier_create_info(last_error, certifier_error + last_error.application_error_code + last_error.library_error_code, None)

def certifier_create_node_address(input, certifier):
    '''
    Uses public key to derive node address via the following algorithm:
    
    Version = 1 byte of 0's |
    Key hash = Version concatenated with RIPEMD-160(SHA-256(input value)) |
    Checksum = 1st 4 bytes of SHA-256(SHA-256(Key hash)) | 
    Ledger Address = Base58Encode(Key hash concatenated with Checksum)

    Returns node address on success
    
    Program exits and reports an error with certifier-related code mapping on failure
    '''
    try:        
        if input == None or not isinstance(input, bytes):
            set_last_error(certifier, 9, gen_application_error_msg(f"Input passed was of type: {type(input)}. Expected type bytes"))
            return get_last_error(certifier)
            
        version = b'\x00'
        
        sha256_1 = hashlib.sha256(input).digest()
        
        ripemd160 = hashlib.new('ripemd160').update(sha256_1)
        rmd160_result = ripemd160.digest()
        
        if not rmd160_result:
            set_last_error(certifier, 10, gen_application_error_msg("RIPEMD160 hashing failed."))
            assert False
        
        versioned_payload = version + rmd160_result
        
        checksum = hashlib.sha256(hashlib.sha256(versioned_payload).digest()).digest()[:4]
        
        if not checksum:
            set_last_error(certifier, 11, gen_application_error_msg("Checksum calculation failed."))
            assert False
        
        final_payload = versioned_payload + checksum
        
        encoded_address = base58.b58encode(final_payload)
                 
        node_address = encoded_address.decode('utf-8')
        
        assert get_last_error(certifier).application_error_code + get_last_error(certifier).library_error_code != 0
        
        return node_address
    except AssertionError:
        last_error = get_last_error(certifier)
        certifier_create_info(last_error, certifier_error + last_error.application_error_code + last_error.library_error_code, None)

def certifier_get_node_address(certifier: Certifier):
    '''
    Function to retrieve node address and call helper certifier_setup_keys() if needed to create it
    
    Returns node address on success
    
    Program exits and reports an error with certifier-related code mapping on failure
    '''
    if certifier.tmp_map.node_address == None:
        certifier_setup_keys(certifier)
    
    return certifier.tmp_map.node_address

def get_der_cert_and_b64_der_cert(certifier: Certifier, certificate: x509.Certificate):
    '''
    Function to retrieve certificate in DER format and base64 encoded version
    
    Returns certificate in DER format and base64 encoded version on success
    
    Constructs CertifierError() and returns tuple (size two) of error on failure
    '''
    der_cert = certificate.public_bytes(serialization.Encoding.DER)      
  
    if der_cert == None or len(der_cert) == 0:
        application_error_msg = gen_application_error_msg("While generating x509 CRT, serializing certificate to DER format failed.", None)
        set_last_error(certifier, 8, application_error_msg)
         
        return get_last_error(certifier), get_last_error(certifier)

    der_base64 = base64.b64encode(der_cert).decode('utf-8')

    return der_cert, str(der_base64)

def certifier_register(certifier: Certifier):
    from src.certifier_client import request_x509_certificate
    '''
    Function will time performance metrics if option is set in config. Calls generate_certificate_signing_request() for CSR and later request_x509_certificate() to send request with CSR.
    Will attempt to save received certificate chain by calling helper save_x509_certs_to_filesystem().
    
    Returns None on success
    
    Returns CertifierError() on failure
    '''
    try:
        x509_certs = None
            
        p12_filename = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PATH)
        password = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PASSWORD)
                
        renamed_p12_filename = None

        start_user_cpu_time = 0
        start_system_cpu_time = 0
        start_memory_used = 0
        start_cpu_time = 0
        start_wall_time = 0
        
        measure_performance = property_is_option_set(certifier.CertifierPropMap, CERTIFIER_OPT_OPTION.CERTIFIER_OPTION_MEASURE_PERFORMANCE)
        
        if measure_performance:
            start_memory_used = psutil.Process().memory_info().rss
            start_cpu_times = os.times()
            start_user_cpu_time = start_cpu_times.user
            start_system_cpu_time = start_cpu_times.system
            
            start_wall_time = time.perf_counter()
            start_cpu_time = time.process_time()

        force_registration = property_is_option_set(certifier.CertifierPropMap, CERTIFIER_OPT_OPTION.CERTIFIER_OPTION_FORCE_REGISTRATION)
                
        log(f"p12 filename is: {p12_filename}", "INFO")
                    
        if (path.exists(p12_filename)):
            if (force_registration):
                renamed_p12_filename = str(os.getcwd()) + "/" + (str(p12_filename)) + ".bk"
                            
                if (path.exists(renamed_p12_filename)):
                    try:
                        os.remove(renamed_p12_filename)
                    except Exception as e:
                        set_last_error(certifier, 10, gen_application_error_msg(f"Failed to delete pre-existing renamed PKCS12 file: {e}"))
                        assert False
                
                try:
                    original_p12_filename = str(os.getcwd()) + "/" + (str(p12_filename))
                    os.rename(original_p12_filename, renamed_p12_filename)                    
                except Exception as e:
                    set_last_error(certifier, 11, gen_application_error_msg(f"Failed to rename existing PKCS12 file: {e}"))
                    assert False

                log(f"Renamed file: {p12_filename} to {renamed_p12_filename}", "INFO")            
            else:
                log("\nCertificate already exists. Returning. Use '-f' flag if overwrite is necessary. \n", "INFO")
                certifier_register_cleanup(certifier, p12_filename, renamed_p12_filename, measure_performance, start_wall_time, start_user_cpu_time, start_system_cpu_time, start_cpu_time, start_memory_used)
                
                return
        if (_certifier_get_privkey(certifier) == None or certifier.tmp_map.der_public_key == None or certifier.tmp_map.base64_public_key == None):
                set_last_error(certifier, 12, gen_application_error_msg("Failed to retrieve private key or public key setup failed."))
                assert False
            
        log("\nCreating Certificate Signing Request...\n", "INFO")
            
        csr = generate_certificate_signing_request(certifier, certifier.tmp_map.private_ec_key)
        
        assert not isinstance(csr, CertifierError)
        
        if csr and len(csr):
            log("\nGot a valid Certificate Signing Request.", "DEBUG")
            log(f"\nCertificate Signing Request: {csr}\n", "DEBUG")
        
        log("\nRegistering Client...", "INFO")
        x509_certs = request_x509_certificate(certifier, csr, certifier.tmp_map.node_address, None)
                    
        if isinstance(x509_certs, CertifierError):
            log("\n<<< Failed to Request X509 Certificate! >>>\n", "ERROR")
            certifier_register_cleanup(certifier, p12_filename, renamed_p12_filename, measure_performance, start_wall_time, start_user_cpu_time, start_system_cpu_time, start_cpu_time, start_memory_used)
            assert False
        else:
            log("\nObtained x509 Certificate Successfully!\n", "INFO")
            
        assert save_x509_certs_to_filesystem(certifier, x509_certs, force_registration, p12_filename, password) == None

        if renamed_p12_filename and path.exists(renamed_p12_filename):
            try:
                os.remove(renamed_p12_filename)
            except Exception as e:
                set_last_error(certifier, 10, gen_application_error_msg("Failed to delete pre-existing renamed PKCS12 file."))
                assert False

        certifier_register_cleanup(certifier, p12_filename, renamed_p12_filename, measure_performance, start_wall_time, start_user_cpu_time, start_system_cpu_time, start_cpu_time, start_memory_used)
    except AssertionError:
        return get_last_error(certifier)

def certifier_register_cleanup(certifier, p12_filename, renamed_p12_filename, measure_performance, start_wall_time, start_user_cpu_time, start_system_cpu_time, start_cpu_time, start_memory_used):    
    '''
    Function to handle cleanup behavior needed for certifier_register(), i.e. calculating end times for measuring performance metrics, etc.
    
    Returns None on success
    
    Returns CertifierError() on failure
    '''
    try:
        force_registration = property_is_option_set(certifier.CertifierPropMap, CERTIFIER_OPT_OPTION.CERTIFIER_OPTION_FORCE_REGISTRATION)

        if force_registration and renamed_p12_filename and path.exists(renamed_p12_filename) and not path.exists(p12_filename):
            try:
                os.rename(renamed_p12_filename, p12_filename)
                log(f"Renamed file: {renamed_p12_filename} to {p12_filename}", "INFO")
            except Exception as e:
                set_last_error(certifier, 5, gen_application_error_msg("Failed to delete pre-existing renamed PKCS12 file."))
                assert False
        
        if measure_performance:
            end_memory_used = psutil.Process().memory_info().rss
            end_cpu_times = os.times()
            end_user_cpu_time = end_cpu_times.user
            end_system_cpu_time = end_cpu_times.system
            
            end_wall_time = time.perf_counter()
            end_cpu_time = time.process_time()
            elapsed_time = round(end_wall_time - start_wall_time, 4)
            cpu_time_used = round(end_cpu_time - start_cpu_time, 4)
            cpu_utilization = round(((cpu_time_used / elapsed_time) * 100 if elapsed_time > 0 else 0), 0)

            log(f"certifier_register[performance] - Elapsed Time {elapsed_time}, CPU Time {cpu_time_used}, CPU Ut {cpu_utilization}", "DEBUG")
            
            if ((start_memory_used > 0) and (end_memory_used > 0)):
                log("certifier_register[performance] start_memory_used: " + str(start_memory_used), "DEBUG")
                log("certifier_register[performance] end_memory_used: " + str(end_memory_used), "DEBUG")

            if ((start_user_cpu_time > 0) and (end_user_cpu_time > 0)):
                log("certifier_register[performance] start_user_cpu_time: " + str(start_user_cpu_time), "DEBUG")
                log("certifier_register[performance] end_user_cpu_time: " + str(end_user_cpu_time), "DEBUG")

            if ((start_system_cpu_time > 0) and (end_system_cpu_time > 0)):
                log("certifier_register[performance] start_system_cpu_time: " + str(start_system_cpu_time), "DEBUG")
                log("certifier_register[performance] end_system_cpu_time: " + str(end_system_cpu_time), "DEBUG")
    except AssertionError:
        return get_last_error(certifier)

def generate_certificate_signing_request(certifier: Certifier, eckey: ec.EllipticCurvePrivateKey):
    '''
    Generates CSR and adds extensions based on values present in config file.
    
    Returns CSR on success
    
    Returns CertifierError() on failure
    '''
    try:
        der_csr = None
    
        csr_builder = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([]))
        
        usage_values = property_get(certifier.CertifierPropMap, CERTIFIER_OPT.CERTIFIER_OPT_EXT_KEY_USAGE)
        log(f"Ext Key Usage is: {usage_values}", "DEBUG")
        
        if usage_values != None:
            usage_values = usage_values.split(',')
        
            toggle_critical = 'critical' in usage_values
            
            try:    
                if 'clientAuth' in usage_values and 'serverAuth' in usage_values:
                    csr_builder = csr_builder.add_extension(x509.ExtendedKeyUsage([x509.ExtendedKeyUsageOID.CLIENT_AUTH, x509.ExtendedKeyUsageOID.SERVER_AUTH]), critical=toggle_critical)
                elif 'serverAuth' in usage_values:
                    csr_builder = csr_builder.add_extension(x509.ExtendedKeyUsage([x509.ExtendedKeyUsageOID.SERVER_AUTH]), critical=toggle_critical)
                elif 'clientAuth' in usage_values:
                    csr_builder = csr_builder.add_extension(x509.ExtendedKeyUsageOID([x509.ExtendedKeyUsageOID.CLIENT_AUTH]), critical=toggle_critical)
            except (ValueError, TypeError) as e:
                set_last_error(certifier, 13, gen_application_error_msg(f"Error adding extensions to CSR: {str(e)}", None))  
                assert False
            
        try:
            csr = csr_builder.sign(eckey, hashes.SHA256())
        except (ValueError, TypeError) as e:
            set_last_error(certifier, 14, gen_application_error_msg(f"Error signing CSR: {str(e)}", None))
            assert False
        
        try:
            der_csr = csr.public_bytes(serialization.Encoding.DER)
        except (ValueError, TypeError) as e:
            set_last_error(certifier, 15, gen_application_error_msg(f"Serializing CSR to DER format failed: {str(e)}", None))
            assert False

        return base64.b64encode(der_csr).decode('utf-8')
    except AssertionError:
        return get_last_error(certifier)