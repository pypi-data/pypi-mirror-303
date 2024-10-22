
from .error import CertifierError, gen_application_error_msg, certifier_create_info
from .log import log, verbose_log_check, cfg
from .constants import *

from dataclasses import dataclass
import json
import secrets
import importlib.resources as pkg_resources

ca_path_order_list = [DEFAULT_CA_PATH, DEFAULT_USER_CA_PATH, DEFAULT_GLOBAL_CA_PATH, DEFAULT_CURDIR_CA_PATH]

def get_default_cfg_filename():
    '''
    Function to find config file to use by default if not provided on command line
    
    Returns default config filename to use on success
    
    Program exits and reports an error with property-related code mapping on failure
    '''
    path = None

    with pkg_resources.path('src.resources', 'libcertifier.cfg') as cfg_path:
        path = str(cfg_path)

    if (path is None):
        log("Could not resolve default config filename", "ERROR")
        error_message = gen_application_error_msg("Could not resolve default configuration filename", None)
        rc = CertifierError(9, 0, error_message, None)
        certifier_create_info(rc, property_error + 9, None)
    
    return path

def get_default_ca_info():
    '''
    Function to find CA info to use by default
    
    Returns default CA info to use on success
    
    Program exits and reports an error with property-related code mapping on failure
    '''
    path = None

    with pkg_resources.path('src.resources', 'libcertifier-cert.crt') as ca_info_path:
        path = str(ca_info_path)

    if (path is None):
        log("Could not resolve default CA info", "ERROR")
        error_message = gen_application_error_msg("Could not resolve default CA info", None)
        rc = CertifierError(10, 0, error_message, None)
        certifier_create_info(rc, property_error + 10, None)

    return path

def get_default_ca_path():
    '''
    Function to find CA path to use by default if not provided on command line
    
    Returns default CA path to use on success
    
    Program exits and reports an error with property-related code mapping on failure
    '''
    ca_path = None
    
    for opt in ca_path_order_list:
        if (os.path.exists(opt)):
            ca_path = opt
            break

    if (ca_path is None):
        log("Could not resolve default CA path", "ERROR")
        error_message = gen_application_error_msg("Could not resolve default CA path", None)
        rc = CertifierError(11, 0, error_message, None)
        certifier_create_info(rc, property_error + 11, None)

    return ca_path

def print_warning(property_name: str):
    '''
    Print warning that given property shouldn't be used in production.
    '''
    log("WARNING! Property key: " + str(property_name) + " should not be used in PRODUCTION. It could cause security-related issues.", "WARN")

@dataclass
class CertifierPropMap():
    log_level: int = None
    log_max_size: int = None
    http_connect_timeout: int = None
    http_timeout: int = None
    options: int = 0
    cert_min_time_left_s: int = None
    validity_days: int = None
    autorenew_interval: int = None
    log_file: str = None
    ca_info: str = None
    ca_path: str = None
    certifier_url: str = None
    cfg_filename: str = None
    auth_type: str = None
    p12_filename: str = None
    output_p12_filename: str = None
    password: str = None
    password_out: str = None
    certifier_id: str = None
    system_id: str = None
    fabric_id: str = None
    node_id: str = None
    product_id: str = None
    auth_tag_1: str = None
    mac_address: str = None
    dns_san: str = None
    ip_san: str = None
    email_san: str = None
    crt: str = None
    profile_name: str = None
    source: str = None
    cn_prefix: str = None
    domain: str = None
    ext_key_usage_value: str = None
    tracking_id: str = None
    ecc_curve_id: str = None
    simulated_cert_expiration_date_after: str = None
    simulated_cert_expiration_date_before: str = None
    auth_token: str = None 
    output_node: str = None
    target_node: str = None
    action: str = None
    input_node: str = None
    autorenew_certs_path_list: str = None
    cert_x509_out = None
    mtls_filename: str = None
    mtls_p12_filename: str = None

def property_new():
    '''
    Constructs CertifierPropMap for certifier instance
    
    Returns CertifierPropMap on success
    
    Program exits and reports an error with certifier-related code mapping on failure
    '''
    prop_map = CertifierPropMap()

    if (prop_map == None):
        log("CertifierPropMap was None after attempted initialization", "ERROR")
        rc = CertifierError(1, 0, gen_application_error_msg("CertifierPropMap was None after attempted initialization", None), None, None)
        certifier_create_info(rc, certifier_error + 1, None)

    property_set_defaults(prop_map)
    
    return prop_map

def property_get(prop_map: CertifierPropMap, name: CERTIFIER_OPT):
    '''
    Function to retrieve a given property from certifier instance's CertifierPropMap based on name passed in.
    
    Returns value associated with property name on success
    
    Program exits and reports an error with property-related code mapping on failure
    '''
    return_value = None

    if (name <= 0):
        log("invalid property [" + str(name) + "]", "ERROR")
        rc = CertifierError(3, None, gen_application_error_msg("Property name was <= 0", None))
        certifier_create_info(rc, property_error + 3, None)
    elif (name > max(CERTIFIER_OPT, key = lambda e: e.value)):
        log("invalid property [" + str(name) + "]", "ERROR")
        rc = CertifierError(4, None, gen_application_error_msg("Property name was > than max in CERTIFIER_OPT enum.", None))
        certifier_create_info(rc, property_error + 4, None)
    
    match(name):
        case CERTIFIER_OPT.CERTIFIER_OPT_CFG_FILENAME:
            return_value = prop_map.cfg_filename
        case CERTIFIER_OPT.CERTIFIER_OPT_CERT_X509_OUT:
            return_value = prop_map.cert_x509_out
        case CERTIFIER_OPT.CERTIFIER_OPT_AUTH_TYPE:
            return_value = prop_map.auth_type
        case CERTIFIER_OPT.CERTIFIER_OPT_CERTIFIER_URL:
            return_value = prop_map.certifier_url
        case CERTIFIER_OPT.CERTIFIER_OPT_HTTP_TIMEOUT:
            return_value = prop_map.http_timeout
        case CERTIFIER_OPT.CERTIFIER_OPT_HTTP_CONNECT_TIMEOUT:
            return_value = prop_map.http_connect_timeout
        case CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PATH:
            return_value = prop_map.p12_filename
        case CERTIFIER_OPT.CERTIFIER_OPT_OUTPUT_P12_PATH:
            return_value = prop_map.output_p12_filename
        case CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PASSWORD:
            return_value = prop_map.password
        case CERTIFIER_OPT.CERTIFIER_OPT_OUTPUT_P12_PASSWORD:
            return_value = prop_map.password_out
        case CERTIFIER_OPT.CERTIFIER_OPT_CA_INFO:
            return_value = prop_map.ca_info
        case CERTIFIER_OPT.CERTIFIER_OPT_CA_PATH:
            return_value = prop_map.ca_path
        case CERTIFIER_OPT.CERTIFIER_OPT_CRT:
            return_value = prop_map.crt
        case CERTIFIER_OPT.CERTIFIER_OPT_PROFILE_NAME:
            return_value = prop_map.profile_name
        case CERTIFIER_OPT.CERTIFIER_OPT_ECC_CURVE_ID:
            return_value = prop_map.ecc_curve_id
        case CERTIFIER_OPT.CERTIFIER_OPT_OPTIONS:
            return_value = prop_map.options
        case CERTIFIER_OPT.CERTIFIER_OPT_SYSTEM_ID:
            return_value = prop_map.system_id
        case CERTIFIER_OPT.CERTIFIER_OPT_FABRIC_ID:
            return_value = prop_map.fabric_id
        case CERTIFIER_OPT.CERTIFIER_OPT_NODE_ID:
            return_value = prop_map.node_id
        case CERTIFIER_OPT.CERTIFIER_OPT_PRODUCT_ID:
            return_value = prop_map.product_id
        case CERTIFIER_OPT.CERTIFIER_OPT_AUTH_TAG_1:
            return_value = prop_map.auth_tag_1
        case CERTIFIER_OPT.CERTIFIER_OPT_MAC_ADDRESS:
            return_value = prop_map.mac_address
        case CERTIFIER_OPT.CERTIFIER_OPT_DNS_SAN:
            return_value = prop_map.dns_san
        case CERTIFIER_OPT.CERTIFIER_OPT_IP_SAN:
            return_value = prop_map.ip_san
        case CERTIFIER_OPT.CERTIFIER_OPT_EMAIL_SAN:
            return_value = prop_map.email_san
        case CERTIFIER_OPT.CERTIFIER_OPT_SIMULATION_CERT_EXP_DATE_BEFORE:
            return_value = prop_map.simulated_cert_expiration_date_before
        case CERTIFIER_OPT.CERTIFIER_OPT_SIMULATION_CERT_EXP_DATE_AFTER:
            return_value = prop_map.simulated_cert_expiration_date_after
        case CERTIFIER_OPT.CERTIFIER_OPT_LOG_LEVEL:
            return_value = prop_map.log_level
        case CERTIFIER_OPT.CERTIFIER_OPT_LOG_MAX_SIZE:
            return_value = prop_map.log_max_size
        case CERTIFIER_OPT.CERTIFIER_OPT_LOG_FILENAME:
            return_value = prop_map.log_file
        case CERTIFIER_OPT.CERTIFIER_OPT_AUTH_TOKEN:
            return_value = prop_map.auth_token
        case CERTIFIER_OPT.CERTIFIER_OPT_OUTPUT_NODE:
            return_value = prop_map.output_node
        case CERTIFIER_OPT.CERTIFIER_OPT_TARGET_NODE:
            return_value = prop_map.target_node
        case CERTIFIER_OPT.CERTIFIER_OPT_ACTION:
            return_value = prop_map.action
        case CERTIFIER_OPT.CERTIFIER_OPT_INPUT_NODE:
            return_value = prop_map.input_node
        case CERTIFIER_OPT.CERTIFIER_OPT_TRACKING_ID:
            return_value = prop_map.tracking_id
        case CERTIFIER_OPT.CERTIFIER_OPT_SOURCE:
            return_value = prop_map.source
        case CERTIFIER_OPT.CERTIFIER_OPT_CN_PREFIX:
            return_value = prop_map.cn_prefix
        case CERTIFIER_OPT.CERTIFIER_OPT_DOMAIN:
            return_value = prop_map.domain
        case CERTIFIER_OPT.CERTIFIER_OPT_VALIDITY_DAYS:
            return_value = prop_map.validity_days
        case CERTIFIER_OPT.CERTIFIER_OPT_AUTORENEW_INTERVAL:
            return_value = prop_map.autorenew_interval
        case CERTIFIER_OPT.CERTIFIER_OPT_CERT_MIN_TIME_LEFT_S:
            return_value = prop_map.cert_min_time_left_s
        case CERTIFIER_OPT.CERTIFIER_OPT_EXT_KEY_USAGE:
            return_value = prop_map.ext_key_usage_value
        case CERTIFIER_OPT.CERTIFIER_OPT_AUTORENEW_CERTS_PATH_LIST:
            return_value = prop_map.autorenew_certs_path_list
        case CERTIFIER_OPT.CERTIFIER__OPT_LOG_FUNCTION:
            # Write-only value
            return_value = None
        case CERTIFIER_OPT.CERTIFIER_OPT_MTLS_P12_PATH:
            return_value = prop_map.mtls_filename
        case CERTIFIER_OPT.CERTIFIER_OPT_MTLS_P12_PASSWORD:
            return_value = prop_map.mtls_p12_filename
        case CERTIFIER_OPT.CERTIFIER_OPT_DEBUG_HTTP | CERTIFIER_OPT.CERTIFIER_OPT_TRACE_HTTP | CERTIFIER_OPT.CERTIFIER_OPT_FORCE_REGISTRATION | CERTIFIER_OPT.CERTIFIER_OPT_MEASURE_PERFORMANCE | CERTIFIER_OPT.CERTIFIER_OPT_CERTIFICATE_LITE: 
            bit = name - CERTIFIER_OPT.CERTIFIER_OPT_BOOL_FIRST
            option: CERTIFIER_OPT_OPTION = 1 << bit
            
            return_value = property_is_option_set(prop_map, option)            
        case CERTIFIER_OPT.CERTIFIER_OPT_USE_SCOPES:
            bit = name - CERTIFIER_OPT.CERTIFIER_OPT_BOOL_FIRST
            option: CERTIFIER_OPT_OPTION = 1 << bit
            
            return_value = property_is_option_set(prop_map, option)            
        case _:
            log("property_get: unrecognized property [" + str(name) + "]", "WARN")
            rc = certifier.CertifierError(8, None, certifier.gen_application_error_msg("Attempted to set unrecognized property in property_get()", None))
            certifier.certifier_create_info(rc, property_error + 8, None)

    return return_value

def property_set(prop_map: CertifierPropMap, name: CERTIFIER_OPT, value):
    '''
    Function attempts to set certifier instance's CertifierPropMap property of type [name] with [value].
    
    Returns None on success
    
    Program exits and reports an error with property-related code mapping on failure
    '''
    rc = CertifierError()

    match(name):
        case CERTIFIER_OPT.CERTIFIER_OPT_HTTP_TIMEOUT:
            None
        case CERTIFIER_OPT.CERTIFIER_OPT_HTTP_CONNECT_TIMEOUT:
            None
        case CERTIFIER_OPT.CERTIFIER_OPT_OPTIONS:
            None
        case CERTIFIER_OPT.CERTIFIER_OPT_LOG_LEVEL:
            None
        case CERTIFIER_OPT.CERTIFIER__OPT_LOG_FUNCTION:
            None
        case CERTIFIER_OPT.CERTIFIER_OPT_CERT_MIN_TIME_LEFT_S:
            None
        case CERTIFIER_OPT.CERTIFIER_OPT_VALIDITY_DAYS:
            None
        case CERTIFIER_OPT.CERTIFIER_OPT_AUTORENEW_INTERVAL:
            None
        case _:
            # Checking if non-boolean option (string option) is None
            if not (name >= CERTIFIER_OPT.CERTIFIER_OPT_BOOL_FIRST) and (value is None):
                rc = CertifierError(6, None, gen_application_error_msg(f"Attempted to set {CERTIFIER_OPT(name).name} with property value None", None))
                certifier_create_info(rc, property_error + 6, None)
                
    match(name):
        case CERTIFIER_OPT.CERTIFIER_OPT_CERT_X509_OUT:
            prop_map.cert_x509_out = value
        case CERTIFIER_OPT.CERTIFIER_OPT_CFG_FILENAME:
            prop_map.cfg_filename = value
        case CERTIFIER_OPT.CERTIFIER_OPT_AUTH_TYPE:
            prop_map.auth_type = value
        case CERTIFIER_OPT.CERTIFIER_OPT_CERTIFIER_URL:
            if str(value).startswith("https://"):
                prop_map.certifier_url = value
            else:
                rc = CertifierError(7, None, gen_application_error_msg("Attempted to set URL property with value not starting with https://", None))
                certifier_create_info(rc, property_error + 7, None)
        case CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PATH:
            prop_map.p12_filename = value
        case CERTIFIER_OPT.CERTIFIER_OPT_OUTPUT_P12_PATH:
            prop_map.output_p12_filename = value
        case CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PASSWORD:
            prop_map.password = value
        case CERTIFIER_OPT.CERTIFIER_OPT_OUTPUT_P12_PASSWORD:
            prop_map.password_out = value
        case CERTIFIER_OPT.CERTIFIER_OPT_CA_INFO:
            prop_map.ca_info = value
        case CERTIFIER_OPT.CERTIFIER_OPT_CA_PATH:
            prop_map.ca_path = value
        case CERTIFIER_OPT.CERTIFIER_OPT_CRT:
            prop_map.crt = value
        case CERTIFIER_OPT.CERTIFIER_OPT_PROFILE_NAME:
            prop_map.profile_name = value
        case CERTIFIER_OPT.CERTIFIER_OPT_ECC_CURVE_ID:
            prop_map.ecc_curve_id = value
        case CERTIFIER_OPT.CERTIFIER_OPT_SYSTEM_ID:
            prop_map.system_id = value
        case CERTIFIER_OPT.CERTIFIER_OPT_FABRIC_ID:
            prop_map.fabric_id = value
        case CERTIFIER_OPT.CERTIFIER_OPT_NODE_ID:
            prop_map.node_id = value
        case CERTIFIER_OPT.CERTIFIER_OPT_PRODUCT_ID:
            prop_map.product_id = value
        case CERTIFIER_OPT.CERTIFIER_OPT_AUTH_TAG_1:
            prop_map.auth_tag_1 = value
        case CERTIFIER_OPT.CERTIFIER_OPT_MAC_ADDRESS:
            prop_map.mac_address = value
        case CERTIFIER_OPT.CERTIFIER_OPT_DNS_SAN:
            prop_map.dns_san = value
        case CERTIFIER_OPT.CERTIFIER_OPT_IP_SAN:
            prop_map.ip_san = value
        case CERTIFIER_OPT.CERTIFIER_OPT_EMAIL_SAN:
            prop_map.email_san = value
        case CERTIFIER_OPT.CERTIFIER_OPT_SIMULATION_CERT_EXP_DATE_BEFORE:
            prop_map.simulated_cert_expiration_date_before = value
        case CERTIFIER_OPT.CERTIFIER_OPT_SIMULATION_CERT_EXP_DATE_AFTER:
            prop_map.simulated_cert_expiration_date_after = value

        # integer options            
        case CERTIFIER_OPT.CERTIFIER_OPT_HTTP_TIMEOUT:
            property_set_int(prop_map, name, int(value))
        case CERTIFIER_OPT.CERTIFIER_OPT_HTTP_CONNECT_TIMEOUT:
            property_set_int(prop_map, name, int(value))
        case CERTIFIER_OPT.CERTIFIER_OPT_LOG_LEVEL:
            property_set_int(prop_map, name, int(value))
        case CERTIFIER_OPT.CERTIFIER_OPT_LOG_MAX_SIZE:
            property_set_int(prop_map, name, int(value))
        case CERTIFIER_OPT.CERTIFIER_OPT_CERT_MIN_TIME_LEFT_S:
            property_set_int(prop_map, name, int(value))
        case CERTIFIER_OPT.CERTIFIER_OPT_VALIDITY_DAYS:
            property_set_int(prop_map, name, int(value))
        case CERTIFIER_OPT.CERTIFIER_OPT_AUTORENEW_INTERVAL:
            property_set_int(prop_map, name, int(value))
        case CERTIFIER_OPT.CERTIFIER_OPT_LOG_FILENAME:
            prop_map.log_file = value
            cfg.file_name = value
        case CERTIFIER_OPT.CERTIFIER_OPT_AUTH_TOKEN:
            prop_map.auth_token = value
        case CERTIFIER_OPT.CERTIFIER_OPT_OUTPUT_NODE:
            prop_map.output_node = value
        case CERTIFIER_OPT.CERTIFIER_OPT_TARGET_NODE:
            prop_map.target_node = value
        case CERTIFIER_OPT.CERTIFIER_OPT_ACTION:
            prop_map.action = value
        case CERTIFIER_OPT.CERTIFIER_OPT_INPUT_NODE:
            prop_map.input_node = value
        case CERTIFIER_OPT.CERTIFIER_OPT_SOURCE:
            prop_map.source = value
        case CERTIFIER_OPT.CERTIFIER_OPT_CN_PREFIX:
            prop_map.cn_prefix = value
        case CERTIFIER_OPT.CERTIFIER_OPT_DOMAIN:
            prop_map.domain = value
        case CERTIFIER_OPT.CERTIFIER_OPT_TRACKING_ID:
            prop_map.tracking_id = value
        case CERTIFIER_OPT.CERTIFIER_OPT_EXT_KEY_USAGE:
            prop_map.ext_key_usage_value = value
        case CERTIFIER_OPT.CERTIFIER_OPT_AUTORENEW_CERTS_PATH_LIST:
            prop_map.autorenew_certs_path_list = value
        case CERTIFIER_OPT.CERTIFIER__OPT_LOG_FUNCTION:
            # This is handled by certifier_set_property
            None
        case CERTIFIER_OPT.CERTIFIER_OPT_OPTIONS:
            # readonly value 
            log("Property [" + str(name) + "] is read-only", lvl = "WARN")
        case CERTIFIER_OPT.CERTIFIER_OPT_MTLS_P12_PATH:
            prop_map.mtls_filename = value
        case CERTIFIER_OPT.CERTIFIER_OPT_MTLS_P12_PASSWORD:
            prop_map.mtls_p12_filename = value
        case CERTIFIER_OPT.CERTIFIER_OPT_DEBUG_HTTP | CERTIFIER_OPT.CERTIFIER_OPT_TRACE_HTTP | CERTIFIER_OPT.CERTIFIER_OPT_FORCE_REGISTRATION | CERTIFIER_OPT.CERTIFIER_OPT_MEASURE_PERFORMANCE | CERTIFIER_OPT.CERTIFIER_OPT_CERTIFICATE_LITE:            
            bit = name - CERTIFIER_OPT.CERTIFIER_OPT_BOOL_FIRST

            option = 1 << bit

            property_set_option(prop_map, option, value != 0)
        case CERTIFIER_OPT.CERTIFIER_OPT_USE_SCOPES:
            bit = name - CERTIFIER_OPT.CERTIFIER_OPT_BOOL_FIRST
            
            option  = 1 << bit

            property_set_option(prop_map, option, value != 0)            
        case _:
            # some unknown property type
            log("property_set: unrecognized property [" + str(name) + "]", "WARN")
            rc = certifier.CertifierError(8, None, certifier.gen_application_error_msg("Attempted to set unrecognized property in property_set()", None))
            certifier.certifier_create_info(rc, property_error + 8, None)
    
def property_set_option(prop_map: CertifierPropMap, option: CERTIFIER_OPT.CERTIFIER_OPT_OPTIONS, enable: bool):
    '''
    If enable boolean is True, sets option by bitwise OR operation on CertifierPropMap's options field.
    
    If enable boolean is False, disables option by bitwise AND operation on CertifierPropMap's options field.
    
    Returns None
    '''
    if (enable):
        prop_map.options |= option
    else:
        prop_map.options &= ~option

def property_is_option_set(prop_map: CertifierPropMap, option: CERTIFIER_OPT_OPTION):
    '''
    Function checks if option is set by comparing the bitwise AND operation between CertifierPropMap's options field and a given option
    
    Returns boolean
    '''
    return (prop_map.options & option) != 0
    
def property_set_int(prop_map: CertifierPropMap, name: CERTIFIER_OPT, value: int):
    rc = CertifierError()
    
    if (value < 0):
        rc.application_error_code = CERTIFIER_ERR_PROPERTY_SET_3
        rc.application_error_msg = gen_application_error_msg("Property integer value was < 0", None)
        certifier_create_info(rc, CERTIFIER_ERR_PROPERTY_SET + CERTIFIER_ERR_PROPERTY_SET_3, None)

    match (name):
        case CERTIFIER_OPT.CERTIFIER_OPT_HTTP_TIMEOUT:
            prop_map.http_timeout = value
        case CERTIFIER_OPT.CERTIFIER_OPT_HTTP_CONNECT_TIMEOUT:
            prop_map.http_connect_timeout = value
        case CERTIFIER_OPT.CERTIFIER_OPT_LOG_LEVEL:
            prop_map.log_level = value
            cfg.level = prop_map.log_level
        case CERTIFIER_OPT.CERTIFIER_OPT_LOG_MAX_SIZE:
            prop_map.log_max_size = value
            cfg.max_size = prop_map.log_max_size
        case CERTIFIER_OPT.CERTIFIER_OPT_CERT_MIN_TIME_LEFT_S:
            prop_map.cert_min_time_left_s = value
        case CERTIFIER_OPT.CERTIFIER_OPT_VALIDITY_DAYS:
            prop_map.validity_days = value
        case CERTIFIER_OPT.CERTIFIER_OPT_AUTORENEW_INTERVAL:
            prop_map.autorenew_interval = value
        case _:
            log("property_set_int: unrecognized property [" + str(name) + "]", "WARN")
            rc = CertifierError(CERTIFIER_ERR_PROPERTY_SET_5, None, gen_application_error_msg("Attempted to set unrecognized property in property_set_int()", None))
            certifier_create_info(rc, CERTIFIER_ERR_PROPERTY_SET + CERTIFIER_ERR_PROPERTY_SET_5, None)
    
def property_set_defaults(prop_map: CertifierPropMap):  
    '''
    Function to set defaults of a certifier instance's CertifierPropMap before a config file is applied.
    
    Returns None on success
    
    Program exits and reports an error with property-related code mapping on failure via calls to helpers
    '''  
    trace_id = ''.join(secrets.choice(ALLOWABLE_CHARACTERS) for i in range(16))

    if (trace_id):
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_TRACKING_ID, trace_id)
            
    if (prop_map.cfg_filename == None):
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_CFG_FILENAME, get_default_cfg_filename())
        
    if (prop_map.auth_type == None):
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_AUTH_TYPE, DEFAULT_AUTH_TYPE)

    if (prop_map.certifier_url == None):
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_CERTIFIER_URL, DEFAULT_CERTIFER_URL)
        
    if (prop_map.profile_name == None):
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_PROFILE_NAME, DEFAULT_PROFILE_NAME)

    if (prop_map.product_id == None):
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_PRODUCT_ID, DEFAULT_PRODUCT_ID)
        
    property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_HTTP_TIMEOUT, DEFAULT_HTTP_TIMEOUT)
    
    property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_HTTP_CONNECT_TIMEOUT, DEFAULT_HTTP_CONNECT_TIMEOUT)

    if (prop_map.ca_info == None):
        default_ca_info = get_default_ca_info()
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_CA_INFO, default_ca_info)

    if (prop_map.ca_path == None):
        default_ca_path = get_default_ca_path()
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_CA_PATH, default_ca_path)

    if (prop_map.ecc_curve_id == None):
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_ECC_CURVE_ID, DEFAULT_ECC_CURVE_ID)
        
    property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_LOG_LEVEL, DEFAULT_LOG_LEVEL)

    property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_LOG_MAX_SIZE, DEFAULT_LOG_MAX_SIZE)
    
    cfg.max_size = prop_map.log_max_size

    prop_map.cert_min_time_left_s = DEFAULT_CERT_MIN_TIME_LEFT_S

    property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_SOURCE, DEFAULT_OPT_SOURCE)

    if (prop_map.output_p12_filename == None):
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_OUTPUT_P12_PATH, DEFAULT_OUTPUT_P12_PATH)

    property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_AUTORENEW_INTERVAL, DEFAULT_AUTORENEW_INTERVAL)

    if (prop_map.autorenew_certs_path_list == None):
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_AUTORENEW_CERTS_PATH_LIST, DEFAULT_AUTORENEW_CERTS_PATH)
            
def property_set_defaults_from_cfg_file(prop_map: CertifierPropMap, verbose: bool):
    '''
    Function to set defaults of certifier instance's CertifierPropMap from a config file (either from CLI or default file)
    
    Returns None on success
    
    Program exits and reports an error with property-related code mapping on failure via calls to helpers
    '''     
    verbose_log_check(verbose, "Loading cfg file: " + str(prop_map.cfg_filename), "INFO")

    with open(prop_map.cfg_filename, 'r') as file:
        data = json.load(file)
        
    if ('libcertifier.certifier.url' in data):
        verbose_log_check(verbose, "Loaded certifier url: " + str(data['libcertifier.certifier.url']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_CERTIFIER_URL, data['libcertifier.certifier.url'])

    if ('libcertifier.profile.name' in data):
        verbose_log_check(verbose, "Loaded profile name: " + str(data['libcertifier.profile.name']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_PROFILE_NAME, data['libcertifier.profile.name'])

    if ('libcertifier.auth.type' in data):
        verbose_log_check(verbose, "Loaded crt.type: " + str(data['libcertifier.auth.type']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_AUTH_TYPE, data['libcertifier.auth.type'])

    if ('libcertifier.input.p12.password' in data):
        if verbose:
            print_warning("input.p12.password")
            log("Loaded password from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PASSWORD, data['libcertifier.input.p12.password'])

    if ('libcertifier.system.id' in data):
        verbose_log_check(verbose, "Loaded system_id_value: " + str(data['libcertifier.system.id']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_SYSTEM_ID, data['libcertifier.system.id'])

    if ('libcertifier.fabric.id' in data):
        verbose_log_check(verbose, "Loaded fabric_id_value: " + str(data['libcertifier.fabric.id']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_FABRIC_ID, data['libcertifier.fabric.id'])

    if ('libcertifier.node.id' in data):
        verbose_log_check(verbose, "Loaded node_id_value: " + str(data['libcertifier.node.id']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_NODE_ID, data['libcertifier.node.id'])

    if ('libcertifier.product.id' in data):
        verbose_log_check(verbose, "Loaded product_id_value: " + str(data['libcertifier.product.id']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_PRODUCT_ID, data['libcertifier.product.id'])

    if ('libcertifier.authentication.tag.1' in data):
        verbose_log_check(verbose, "Loaded auth_tag_1_value: " + str(data['libcertifier.authentication.tag.1']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_AUTH_TAG_1, data['libcertifier.authentication.tag.1'])

    if ('libcertifier.http.timeout' in data and data['libcertifier.http.timeout'] >= 0):
        verbose_log_check(verbose, "Loaded http_timeout_value: " + str(data['libcertifier.http.timeout']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_HTTP_TIMEOUT, data['libcertifier.http.timeout'])

    if ('libcertifier.http.connect.timeout' in data and data['libcertifier.http.connect.timeout'] >= 0):
        verbose_log_check(verbose, "Loaded http_connect_timeout_value: " + str(data['libcertifier.http.connect.timeout']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_HTTP_CONNECT_TIMEOUT, data['libcertifier.http.connect.timeout'])

    if ('libcertifier.http.trace' in data and data['libcertifier.http.trace'] == 1):
        if verbose:
            log("Loaded http_trace_value: " + str(data['libcertifier.http.trace']) + " from config file.", "INFO")
            print_warning("http.trace")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_TRACE_HTTP, data['libcertifier.http.trace'])

        prop_map.options |= (CERTIFIER_OPT_OPTION.CERTIFIER_OPTION_TRACE_HTTP | CERTIFIER_OPT_OPTION.CERTIFIER_OPTION_DEBUG_HTTP)

    if ('libcertifier.measure.performance' in data and data['libcertifier.measure.performance'] == 1):
        verbose_log_check(verbose, "Loaded measure.performance: " + str(data['libcertifier.measure.performance']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_MEASURE_PERFORMANCE, data['libcertifier.measure.performance'])
        prop_map.options |= CERTIFIER_OPT_OPTION.CERTIFIER_OPTION_MEASURE_PERFORMANCE

    if ('libcertifier.autorenew.interval' in data and data['libcertifier.autorenew.interval'] == 1):
        verbose_log_check(verbose, "Loaded autorenew.interval: " + str(data['libcertifier.autorenew.interval']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_AUTORENEW_INTERVAL, data['libcertifier.autorenew.interval'])

    if ('libcertifier.input.p12.path' in data):
        verbose_log_check(verbose, "Loaded input_p12_path value: " + str(data['libcertifier.input.p12.path']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_INPUT_P12_PATH, data['libcertifier.input.p12.path'])

    if ('libcertifier.sat.token' in data):
        verbose_log_check(verbose, "Loaded sat_token_value: " + str(data['libcertifier.sat.token']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_AUTH_TOKEN, data['libcertifier.sat.token'])

    if ('libcertifier.ca.info' in data):
        verbose_log_check(verbose, "Loaded ca_info_value: " + str(data['libcertifier.ca.info']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_CA_INFO, data['libcertifier.ca.info'])

    if ('libcertifier.ca.path' in data):
        verbose_log_check(verbose, "Loaded ca_path_value: " + str(data['libcertifier.ca.path']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_CA_PATH, data['libcertifier.ca.path'])

    if ('libcertifier.validity.days' in data):
        verbose_log_check(verbose, "Loaded validity_days: " + str(data['libcertifier.validity.days']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_VALIDITY_DAYS, data['libcertifier.validity.days'])

    if ('libcertifier.ecc.curve.id' in data):
        verbose_log_check(verbose, "Loaded ecc_curve_id_value " + str(data['libcertifier.ecc.curve.id']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_ECC_CURVE_ID, data['libcertifier.ecc.curve.id'])

    if ('libcertifier.log.file' in data):
        verbose_log_check(verbose, "Loaded log_file_value: " + str(data['libcertifier.log.file']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_LOG_FILENAME, data['libcertifier.log.file'])

    if ('libcertifier.log.level' in data and data['libcertifier.log.level'] >= 0):
        verbose_log_check(verbose, "Loaded log_level_value: " + str(data['libcertifier.log.level']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_LOG_LEVEL, data['libcertifier.log.level'])

    if ('libcertifier.log.max.size' in data and data['libcertifier.log.max.size'] >= 0):
        verbose_log_check(verbose, "Loaded log_max_size_value: " + str(data['libcertifier.log.max.size']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_LOG_MAX_SIZE, data['libcertifier.log.max.size'])

    cfg.max_size = prop_map.log_max_size

    if ('libcertifier.source.id' in data):
        verbose_log_check(verbose, "Loaded source.id: " + str(data['libcertifier.source.id']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_SOURCE, data['libcertifier.source.id'])

    if ('libcertifier.certificate.lite' in data and data['libcertifier.certificate.lite'] == 1):
        if verbose:
            log("Loaded certificate.lite: " + str(data['libcertifier.certificate.lite']) + " from config file.", "INFO")
            print_warning("certificate.lite")
        prop_map.options |= (CERTIFIER_OPT_OPTION.CERTIFIER_OPTION_CERTIFICATE_LITE)
    if ('libcertifier.certificate.scopes' in data and data['libcertifier.certificate.scopes'] == 1):
        if verbose:
            log(f"Loaded certificate.scopes: {data['libcertifier.certificate.scopes']} from cfg file.", "INFO")
            print_warning("certificate.scopes")
        prop_map.options |= (CERTIFIER_OPT_OPTION.CERTIFIER_OPTION_USE_SCOPES)
    if ('libcertifier.cn.name' in data and data['libcertifier.cn.name'] != None):
        verbose_log_check(verbose, "Loaded common_name_value: " + str(data['libcertifier.cn.name']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_CN_PREFIX, data['libcertifier.cn.name'])

    if ('libcertifier.ext.key.usage' in data):
        verbose_log_check(verbose, "Loaded extended_key_usage_values: " + str(data['libcertifier.ext.key.usage']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_EXT_KEY_USAGE, data['libcertifier.ext.key.usage'])

    if ('libcertifier.autorenew.certs.path.list' in data):
        verbose_log_check(verbose, "Loaded autorenew_certs_path: " + str(data['libcertifier.autorenew.certs.path.list']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_AUTORENEW_CERTS_PATH_LIST, data['libcertifier.autorenew.certs.path.list'])

    if ('libcertifier.mtls.p12.path' in data):
        verbose_log_check(verbose, "Loaded mtls_p12_path_value: " + str(data['libcertifier.mtls.p12.path']) + " from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_MTLS_P12_PATH, data['libcertifier.mtls.p12.path'])
        
    if ('libcertifier.mtls.p12.password' in data):
        if verbose:
            print_warning("mtls.p12.password")
            log("Loaded mTLS password from config file.", "INFO")
        property_set(prop_map, CERTIFIER_OPT.CERTIFIER_OPT_MTLS_P12_PASSWORD, data['libcertifier.mtls.p12.password'])