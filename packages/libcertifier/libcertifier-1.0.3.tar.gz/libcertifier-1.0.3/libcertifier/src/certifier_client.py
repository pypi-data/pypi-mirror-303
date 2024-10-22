from .certifier import gen_application_error_msg, get_last_error, set_last_error, assign_last_error, CertifierError, CertifierPropMap
from .constants import *
from .property import property_get, property_is_option_set
from .log import log

from requests_toolbelt.utils import dump
import requests
import threading
import json

lock = threading.Lock()   

@staticmethod
def check_certificate_status(_certifier, digest, as_helper: bool):
    '''
    Queries API for status of a certificate. 
    
    Returns None on success)
    
    Returns CertifierError() on failure
    '''
    
    if digest == None: 
        error_msg = gen_application_error_msg("Digest cannot be None", None)
        set_last_error(_certifier, 9, error_msg)
        return get_last_error(_certifier)

    certifier_url = property_get(_certifier.CertifierPropMap, CERTIFIER_OPT.CERTIFIER_OPT_CERTIFIER_URL)
    certifier_status_url = f"{certifier_url}/certificate/status/{digest}"

    mtls_pair, http_timeouts, ca_bundle = set_curl_options(_certifier.CertifierPropMap)
 
    try:
        is_trace_http_enabled = property_is_option_set(_certifier.CertifierPropMap, CERTIFIER_OPT_OPTION.CERTIFIER_OPTION_TRACE_HTTP)

        resp = requests.get(certifier_status_url, cert=mtls_pair, timeout=http_timeouts, verify=ca_bundle)
        resp.raise_for_status()

        certificate_status = resp.json()['status']

        if not as_helper:
            log("CURL Returned: \n" + str(resp.json()) + "\n", "DEBUG")
            log(f"Certificate Status={certificate_status}" + "\n", "DEBUG")

        if certificate_status == "GOOD":
            assign_last_error(_certifier, CertifierError(output=CERTIFIER_ERR_GET_CERT_STATUS_GOOD))
        elif certificate_status == "UNKNOWN":
            if as_helper: 
                set_last_error(_certifier, 10, gen_application_error_msg("Cannot perform this action on unknown (non-xPKI) certificate. Verify status with 'get-cert-status' command.", None))
            else:                
                assign_last_error(_certifier, CertifierError(output=CERTIFIER_ERR_GET_CERT_STATUS_UNKNOWN))
        elif certificate_status == "REVOKED":
            if as_helper:                 
                set_last_error(_certifier, 11, gen_application_error_msg("Cannot perform this action on certificate that was revoked (already). Verify status with 'get-cert-status' command.", None))
            else:                
                assign_last_error(_certifier, CertifierError(output=CERTIFIER_ERR_GET_CERT_STATUS_REVOKED))
        else:
            if as_helper:                
                set_last_error(_certifier, 10, gen_application_error_msg("Cannot perform this action on unknown (non-xPKI) certificate. Verify status with 'get-cert-status' command.", None))
            else:                
                assign_last_error(_certifier, CertifierError(output=CERTIFIER_ERR_GET_CERT_STATUS_UNKNOWN))
                
        if is_trace_http_enabled:
            data = dump.dump_all(resp, "Request: ".encode(), "Response: ".encode())
            log(data.decode('utf-8'), "DEBUG")
    except Exception as e:
        log("HTTP Request failed: " + str(e), "ERROR")
        
        if not as_helper:
            rc = CertifierError(app_error_code=10, 
                                        app_error_msg=gen_application_error_msg(f"Status Code: {resp.status_code}. Reason: {resp.reason}", resp))
        else:
            rc = CertifierError(app_error_code=14, 
                                        app_error_msg=gen_application_error_msg(f"Status Code: {resp.status_code}. Reason: {resp.reason}", resp))
     
        set_last_error(_certifier, rc.application_error_code, rc.application_error_msg)
        return get_last_error(_certifier)        
        
def renew_x509_certificate(_certifier, digest):
    '''
    Queries API to renew a certificate. 
    
    Returns Certificate Chain from parsed JSON on success
    
    Returns CertifierError() on failure
    '''
    
    serialized_string = None
    certificate_chain = None
    resp = None
    tracking_id = property_get(_certifier.CertifierPropMap, CERTIFIER_OPT.CERTIFIER_OPT_TRACKING_ID)
    bearer_token = property_get(_certifier.CertifierPropMap, CERTIFIER_OPT.CERTIFIER_OPT_CRT)
    source = property_get(_certifier.CertifierPropMap, CERTIFIER_OPT.CERTIFIER_OPT_SOURCE)
    certifier_url = property_get(_certifier.CertifierPropMap, CERTIFIER_OPT.CERTIFIER_OPT_CERTIFIER_URL)
    
    log(str("Tracking ID is: " + tracking_id), "DEBUG")
    
    certifier_renew_url = certifier_url + "/renew"
    
    mtls_pair, http_timeouts, ca_bundle = set_curl_options(_certifier.CertifierPropMap)

    headers = {"Accept": "application/json", 
               "Content-Type": "application/json", 
              }
        
    headers.update({"Authorization": f"Bearer {bearer_token}"[:VERY_LARGE_STRING_SIZE * 4]})
    headers.update({"x-xpki-tracking-id": tracking_id[:SMALL_STRING_SIZE]})
    headers.update({"x-xpki-source": source[:SMALL_STRING_SIZE]})

    body = {"certificateID": ''.join(digest)}
    serialized_string = json.dumps(body, indent=4)
    
    log(f"\nCertificate Renew Request:\n{serialized_string}\n", "INFO")
    
    with lock:
        try:  
            is_trace_http_enabled = property_is_option_set(_certifier.CertifierPropMap, CERTIFIER_OPT_OPTION.CERTIFIER_OPTION_TRACE_HTTP)

            resp = requests.post(certifier_renew_url, headers=headers, json=digest, cert=mtls_pair, timeout=http_timeouts, verify=ca_bundle)
            resp.raise_for_status()
            
            if is_trace_http_enabled:
                data = dump.dump_all(resp, "Request: ".encode(), "Response: ".encode())
                log(data.decode('utf-8'), "DEBUG")
        except requests.RequestException as e:
            log(f"Renew certificate post request failed with following exception: {e}", "ERROR")
            rc = CertifierError(app_error_code=15, 
                                            app_error_msg=gen_application_error_msg(f"Status Code: {resp.status_code}. Reason: {resp.reason}", resp))
            set_last_error(_certifier, rc.application_error_code, rc.application_error_msg)
            return get_last_error(_certifier)  
        
    log(f"HTTP Response: \n{resp.text}\n", "INFO")
    
    try:
        parsed_json = resp.json()
        certificate_chain = parsed_json.get("certificateChain")
        assert certificate_chain != None
    except Exception as e:
        log(f"Could not parse JSON from post request response. Got error: {e}", "ERROR")
        rc = CertifierError(app_error_code=16, 
                                            app_error_msg=gen_application_error_msg(f"Could not parse JSON from post request response", resp))
        set_last_error(_certifier, rc.application_error_code, rc.application_error_msg)
        return get_last_error(_certifier)          
    
    log(f"Certificate Chain: {certificate_chain}", "INFO")

    return certificate_chain

def revoke_x509_certificate(_certifier, digest):
    '''
    Queries API to revoke a certificate. 
    
    Returns None on success
    
    Returns CertifierError() on failure
    '''
    
    source = property_get(_certifier.CertifierPropMap, CERTIFIER_OPT.CERTIFIER_OPT_SOURCE)
    tracking_id = property_get(_certifier.CertifierPropMap, CERTIFIER_OPT.CERTIFIER_OPT_TRACKING_ID)
    bearer_token = property_get(_certifier.CertifierPropMap, CERTIFIER_OPT.CERTIFIER_OPT_CRT)
    certifier_revoke_url = property_get(_certifier.CertifierPropMap, CERTIFIER_OPT.CERTIFIER_OPT_CERTIFIER_URL) + "/revoke"

    log(str("Tracking ID is: " + tracking_id), "DEBUG")

    mtls_pair, http_timeouts, ca_bundle = set_curl_options(_certifier.CertifierPropMap)

    headers = { 
               "Accept": "application/json", 
                "Content-Type": "application/json",
                "Authorization": f"Bearer {bearer_token}"[:VERY_LARGE_STRING_SIZE * 4],
                "x-xpki-tracking-id": tracking_id[:SMALL_STRING_SIZE],
                "x-xpki-source": source[:SMALL_STRING_SIZE]
              }
    
    body = {
        "certificateId": ''.join(digest), 
        "revokeReason": "UNSPECIFIED"
        }
    
    serialized_string = json.dumps(body, indent=4)
    
    log(f"\nCertificate Revoke Request:\n{serialized_string}\n", "INFO")
        
    with lock:
        try:  
            is_trace_http_enabled = property_is_option_set(_certifier.CertifierPropMap, CERTIFIER_OPT_OPTION.CERTIFIER_OPTION_TRACE_HTTP)

            resp = requests.post(certifier_revoke_url, headers=headers, json=body, cert=mtls_pair, timeout=http_timeouts, verify=ca_bundle)
            resp.raise_for_status()

            if is_trace_http_enabled:
                data = dump.dump_all(resp, "Request: ".encode(), "Response: ".encode())
                log(data.decode('utf-8'), "DEBUG")
            
            log("HTTP Revoke certificate request succeeded.", "INFO")
        except Exception as e:
            log(f"Revoke certificate post request failed with following exception: {e}", "ERROR")
        
            rc = CertifierError(app_error_code=15, 
                                      app_error_msg=gen_application_error_msg(f"Status Code: {resp.status_code}. Reason: {resp.reason}", resp))
            set_last_error(_certifier, rc.application_error_code, rc.application_error_msg)
            return get_last_error(_certifier)        

def request_x509_certificate(_certifier, csr, node_address, certifier_id):    
    '''
    Queries API to request a certificate. 
    
    Returns Certificate Chain from parsed JSON on success
    
    Returns CertifierError() on failure
    '''    
        
    certifier_get_url = property_get(_certifier.CertifierPropMap, CERTIFIER_OPT.CERTIFIER_OPT_CERTIFIER_URL) + "/certificate"
    tracking_id = property_get(_certifier.CertifierPropMap, CERTIFIER_OPT.CERTIFIER_OPT_TRACKING_ID)
    bearer_token = property_get(_certifier.CertifierPropMap, CERTIFIER_OPT.CERTIFIER_OPT_CRT)
    source = property_get(_certifier.CertifierPropMap, CERTIFIER_OPT.CERTIFIER_OPT_SOURCE)
    
    log(f"Tracking ID is: {tracking_id}", "DEBUG")
    log(f"Source ID is: {source}", "DEBUG")
    
    headers = {"Accept": "application/json", 
               "Content-Type": "application/json; charset=utf-8"}
        
    if bearer_token != None:
        headers.update({"Authorization": f"Bearer {bearer_token}"[:VERY_LARGE_STRING_SIZE * 4]})
            
    headers.update({"x-xpki-tracking-id": tracking_id[:SMALL_STRING_SIZE]})
    headers.update({"x-xpki-source": source[:SMALL_STRING_SIZE]})
    
    json_body = create_csr_post_data(_certifier.CertifierPropMap, csr, node_address, certifier_id)
    
    mtls_pair, http_timeouts, ca_bundle = set_curl_options(_certifier.CertifierPropMap)
    
    with lock:
        try:  
            is_trace_http_enabled = property_is_option_set(_certifier.CertifierPropMap, CERTIFIER_OPT_OPTION.CERTIFIER_OPTION_TRACE_HTTP)
            resp = requests.post(certifier_get_url, headers=headers, json=json_body, cert=mtls_pair, timeout=http_timeouts, verify=ca_bundle)
            resp.raise_for_status()

            if is_trace_http_enabled:
                data = dump.dump_all(resp, "Request: ".encode(), "Response: ".encode())
                log(data.decode('utf-8'), "DEBUG")
        except Exception as e:  
            log(f"Get certificate post request failed with following exception: {e}", "ERROR")
            
            rc = CertifierError(app_error_code=16, 
                                      app_error_msg=gen_application_error_msg(f"Status Code: {resp.status_code}. Reason: {resp.reason}", resp))
            set_last_error(_certifier, rc.application_error_code, rc.application_error_msg)
            return get_last_error(_certifier)        
    
    log(f"HTTP Response: \n{resp.text}\n", "INFO")
    
    try:
        parsed_json = resp.json()
        certificate_chain = parsed_json.get("certificateChain")
        assert certificate_chain != None
    except Exception as e:
        log(f"Could not parse JSON from post request response. Got error: {e}", "ERROR")
        rc = CertifierError(app_error_code=17, 
                                      app_error_msg=gen_application_error_msg("Could not parse JSON from post request response", resp))
        set_last_error(_certifier, rc.application_error_code, rc.application_error_msg)
        return get_last_error(_certifier)

    log(f"Certificate Chain: {certificate_chain}", "INFO")

    return certificate_chain

def create_csr_post_data(props: CertifierPropMap, csr, node_address, certifier_id):
    '''
    Creates CSR in JSON format to include in request for new certificate. 
    
    Returns CSR on success
    
    Will exit program with property-related error code on failure
    '''    
    
    serialized_string  = None

    node_id             = property_get(props, CERTIFIER_OPT.CERTIFIER_OPT_NODE_ID)
    system_id           = property_get(props, CERTIFIER_OPT.CERTIFIER_OPT_SYSTEM_ID)
    fabric_id           = property_get(props, CERTIFIER_OPT.CERTIFIER_OPT_FABRIC_ID)
    mac_address         = property_get(props, CERTIFIER_OPT.CERTIFIER_OPT_MAC_ADDRESS)
    dns_san             = property_get(props, CERTIFIER_OPT.CERTIFIER_OPT_DNS_SAN)
    ip_san              = property_get(props, CERTIFIER_OPT.CERTIFIER_OPT_IP_SAN)
    email_san           = property_get(props, CERTIFIER_OPT.CERTIFIER_OPT_EMAIL_SAN)
    domain              = property_get(props, CERTIFIER_OPT.CERTIFIER_OPT_DOMAIN)
    profile_name        = property_get(props, CERTIFIER_OPT.CERTIFIER_OPT_PROFILE_NAME)
    product_id          = property_get(props, CERTIFIER_OPT.CERTIFIER_OPT_PRODUCT_ID)
    authenticated_tag_1 = property_get(props, CERTIFIER_OPT.CERTIFIER_OPT_AUTH_TAG_1)
    num_days            = property_get(props, CERTIFIER_OPT.CERTIFIER_OPT_VALIDITY_DAYS)
    use_scopes          = property_is_option_set(props, CERTIFIER_OPT_OPTION.CERTIFIER_OPTION_USE_SCOPES)
    is_certificate_lite = property_is_option_set(props, CERTIFIER_OPT_OPTION.CERTIFIER_OPTION_CERTIFICATE_LITE)

    body = {"csr": csr}
    
    if node_address:
        body.update({"nodeAddress": node_address})
        
    if domain:
        log(f"\ndomain Id :\n{domain}\n", "DEBUG")
        body.update({"domain": domain})
    
    if node_id:
        body.update({"nodeId": node_id})

    body.update({"profileName": profile_name})
    body.update({"productId": product_id})
    
    if authenticated_tag_1:
        body.update({"authenticatedTag1": authenticated_tag_1})
        
    if is_certificate_lite and fabric_id:
        log(f"\nfabric Id :\n{fabric_id}\n", "DEBUG")
        body.update({"fabricId": fabric_id})        
    elif system_id:
        log(f"\nsystem Id :\n{system_id}\n", "DEBUG")
        body.update({"systemId": system_id})
        
    if certifier_id:
        log(f"\nCertifier Id :\n{certifier_id}\n", "DEBUG")
        body.update({"ledgerId": certifier_id})
        
    if mac_address:
        log(f"\nmacAddress Id :\n{mac_address}\n", "DEBUG")
        body.update({"macAddress": mac_address})
    
    if dns_san:
        log(f"\ndnsNames Id :\n{dns_san}\n", "DEBUG")
        body.update({"dnsNames": dns_san})
        
    if ip_san:
        log(f"\nipAddress Id :\n{ip_san}\n", "DEBUG")
        body.update({"ipAddresses": ip_san})
    
    if email_san:
        log(f"\nemails Id :\n{email_san}\n", "DEBUG")
        body.update({"emails": email_san})
        
    if num_days > 0:
        log(f"\nvalidityDays :\n{num_days}\n", "DEBUG")
        body.update({"validityDays": num_days})
    
    if is_certificate_lite:
        log("CertificateLite=1", "DEBUG")
        body.update({"certificateLite": "true"})
        
    if use_scopes:
        log("UseScopes=1", "DEBUG")
        body.update({"useScopes": "true"})
        
    serialized_string = json.dumps(body, indent=4)
    
    log(f"\nCertificate Request POST Data:\n{serialized_string}\n", "DEBUG")
    
    return body

def set_curl_options(props: CertifierPropMap):
    '''
    Called before every request to query certifier object for properties relevant for requests.
    
    Returns such fields to be passed into requests.get() and requests.post() respectively
    '''
    
    host_validation = 2
    peer_validation = 1
    is_debug_http_enabled = property_is_option_set(props, CERTIFIER_OPT_OPTION.CERTIFIER_OPTION_DEBUG_HTTP)
    is_trace_http_enabled = property_is_option_set(props, CERTIFIER_OPT_OPTION.CERTIFIER_OPTION_TRACE_HTTP)
    http_timeout         = property_get(props, CERTIFIER_OPT.CERTIFIER_OPT_HTTP_TIMEOUT)
    http_connect_timeout = property_get(props, CERTIFIER_OPT.CERTIFIER_OPT_HTTP_CONNECT_TIMEOUT)
    mtls_p12           = property_get(props, CERTIFIER_OPT.CERTIFIER_OPT_MTLS_P12_PATH)
    mtls_password      = property_get(props, CERTIFIER_OPT.CERTIFIER_OPT_MTLS_P12_PASSWORD)
    ca_path = property_get(props, CERTIFIER_OPT.CERTIFIER_OPT_CA_PATH)
    ca_info = property_get(props, CERTIFIER_OPT.CERTIFIER_OPT_CA_INFO)    
        
    log("[set_curl_options] - Host Validation=" + str(host_validation), "DEBUG")
    log("[set_curl_options] - Peer Validation=" + str(peer_validation), "DEBUG")
    log("[set_curl_options] - Debug HTTP Enabled=" + str(is_debug_http_enabled), "DEBUG")
    log("[set_curl_options] - Trace HTTP Enabled=" + str(is_trace_http_enabled), "DEBUG")
    
    verify_ca = ca_info if ca_info else ca_path
            
    return (mtls_p12, mtls_password), (http_connect_timeout, http_timeout), verify_ca