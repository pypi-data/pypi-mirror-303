from src.cli import cli_setup
from src.log import log_setup, log_destroy, Namespace
from src.xpki_client import *
from src.certifier import Certifier, certifier_get_property, certifier_create_info, get_last_error, certifier_get_node_address
from src.constants import CERTIFIER_OPT

import sys

def main():
    try:
        arg_parser = cli_setup()
        args = arg_parser.parse_args(sys.argv[1:] or ['--help'])
    
        log_setup(args)
        
        xpki_perform(args)
    finally:
        log_destroy()

def process(certifier: Certifier, args: Namespace, params: get_cert_param_t | get_cert_status_param_t | get_cert_validity_param_t | renew_cert_param_t): 
    if (isinstance(params, get_cert_param_t)):
        xc_get_default_cert_param(certifier, params)
                        
        if (args.input_p12_path):
            params.p12_path = args.input_p12_path
        if (args.input_p12_password):
            params.p12_password = args.input_p12_password
        if (args.auth_type):
            params.auth_type = map_to_xpki_auth_type(args.auth_type)
        if (args.auth_token):
            params.auth_token = args.auth_token
        if (args.crt):
            params.crt = args.crt
        if (args.overwrite_p12):
            params.overwrite_p12 = args.overwrite_p12
        if (args.profile_name):
            params.profile_name = args.profile_name
        if (args.output_p12_path):
            params.output_p12_path = args.output_p12_path
        if (args.output_p12_password):
            params.output_p12_password = args.output_p12_password
        if (args.validity_days):
            params.validity_days = args.validity_days
        if (args.product_id):
            params.product_id = args.product_id
        if (args.node_id):
            params.node_id = args.node_id
        if (args.fabric_id):
            params.fabric_id = args.fabric_id
        if (args.case_auth_tag):
            params.case_auth_tag = args.case_auth_tag
               
    elif (isinstance(params, get_cert_validity_param_t) or isinstance(params, print_cert_param_t) or isinstance(params, revoke_cert_param_t)):
        xc_get_default_cert_validity_param(certifier, params)
        
        if (args.input_p12_path):
            params.input_p12_path = args.input_p12_path
        if (args.input_p12_password):
            params.input_p12_password = args.input_p12_password
    elif (isinstance(params, renew_cert_param_t)):
        xc_get_default_renew_cert_param(certifier, params)

        if (args.input_p12_path):
            params.input_p12_path = args.input_p12_path
        if (args.input_p12_password):
            params.input_p12_password = args.input_p12_password 
        if hasattr(args, "auth_type") and args.auth_type != None:
            params.auth_type = map_to_xpki_auth_type(args.auth_type)
        else:
            params.auth_type = map_to_xpki_auth_type(certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_AUTH_TYPE))        
        if hasattr(args, "auth_token") and args.auth_token != None:
            params.auth_token = args.auth_token  
        else:
            params.auth_token = certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_AUTH_TOKEN)
    elif (isinstance(params, get_cert_status_param_t)):
        xc_get_default_cert_status_param(certifier, params)

        if (args.input_p12_path):
            params.input_p12_path = args.input_p12_path
        if (args.input_p12_password):
            params.input_p12_password = args.input_p12_password
               
def xpki_perform(args):
    certifier = get_certifier_instance(args)

    if (args.command == 'get-cert'):
        params = get_cert_param_t()
        process(certifier, args, params)

        xc_get_cert(certifier, params)
        last_error = get_last_error(certifier)
        return_code = last_error.application_error_code + last_error.library_error_code
        
        certifier_create_info(last_error, return_code, str(certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_CERT_X509_OUT)))        

    if (args.command == 'get-crt-token'):
        params = renew_cert_param_t()
        process(certifier, args, params)
                                
        xc_create_crt(certifier, params.auth_type, params)

        last_error = get_last_error(certifier)
        return_code = last_error.application_error_code + last_error.library_error_code
        
        certifier_create_info(last_error, return_code, certifier_get_property(certifier, CERTIFIER_OPT.CERTIFIER_OPT_CRT))
        
    if (args.command == 'get-cert-status'):
        params = get_cert_status_param_t()
        process(certifier, args, params)
        status: XPKI_CLIENT_CERT_STATUS = None

        status = xc_get_cert_status(certifier, params)
        last_error = get_last_error(certifier)
        return_code = last_error.application_error_code + last_error.library_error_code

        certifier_create_info(last_error, return_code, XPKI_CLIENT_CERT_STATUS(status).name)

    if (args.command == 'get-cert-validity'):
        params = get_cert_validity_param_t()
        process(certifier, args, params)
        validity: XPKI_CLIENT_CERT_STATUS = None
        
        validity = xc_get_cert_validity(certifier, params)
        last_error = get_last_error(certifier)
        return_code = last_error.application_error_code + last_error.library_error_code

        certifier_create_info(last_error, return_code, XPKI_CLIENT_CERT_STATUS(validity).name)

    if (args.command == 'renew-cert'):
        params = renew_cert_param_t()
        process(certifier, args, params)
        
        xc_renew_cert(certifier, params)
        last_error = get_last_error(certifier)
        return_code = last_error.application_error_code + last_error.library_error_code

        certifier_id = certifier_get_node_address(certifier)
        
        certifier_create_info(last_error, return_code, certifier_id)
        
    if (args.command == 'print-cert'):
        params = print_cert_param_t()
        process(certifier, args, params)
        
        b64_der_cert = xc_print_cert(certifier, params)
        last_error = get_last_error(certifier)
        return_code = last_error.application_error_code + last_error.library_error_code

        certifier_create_info(last_error, return_code, b64_der_cert) 
               
    if (args.command == 'revoke'):
        params = revoke_cert_param_t()
        process(certifier, args, params)
                
        xc_revoke_cert(certifier, params)
        last_error = get_last_error(certifier)
        return_code = last_error.application_error_code + last_error.library_error_code

        certifier_id = certifier_get_node_address(certifier)
        
        certifier_create_info(last_error, return_code, certifier_id)
        
if __name__ == '__main__':
    main()