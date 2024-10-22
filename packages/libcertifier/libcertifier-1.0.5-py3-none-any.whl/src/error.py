
from src.log import log, log_destroy

import sys, json
from inspect import getframeinfo, currentframe

class CertifierError:
    def __init__(self, app_error_code = 0, lib_error_code = 0, app_error_msg = None, lib_error_msg = None, output = None):
        self.application_error_code = app_error_code
        self.library_error_code = lib_error_code
        self.application_error_msg = app_error_msg
        self.library_error_msg = lib_error_msg
        self.output = output
        
    def clear(self):
        self.application_error_code = 0
        self.library_error_code = 0
        self.application_error_msg = None
        self.library_error_msg = None
        self.output = None

def gen_application_error_msg(error_message: str, resp):
    '''
    Formats application error message to additionally include info about method, file, and line # where error occurred. Also includes HTTP response if passed
    '''
    application_error_msg = {
        "method": str(getframeinfo(currentframe().f_back.f_back).function) ,
        "error_message": error_message,
        "file": str(getframeinfo(currentframe().f_back.f_back).filename),
        "line": str(getframeinfo(currentframe().f_back.f_back).lineno),
    }

    if resp != None:        
        replacements = [('"', ''), (':', ': '), (',', ', ')]
        
        body = resp.text
        
        for old, new in replacements:
            body = body.replace(old, new)
        
        application_error_msg.update({"http_response": body})
    
    return application_error_msg

def certifier_create_info(last_error: CertifierError, return_code: int, output: str):
    '''
    Final output for any command. Provides end return code and relevant error codes and messages from application and libraries
    '''
    
    root_object = {
        "return_code": return_code,
        "application_error_code": last_error.application_error_code,
        "application_error_message": last_error.application_error_msg,
        "library_error_code": last_error.library_error_code,
        "library_error_message": last_error.library_error_msg
        }
    
    if output:
        root_object.update({"output": output})

    serialized_string = json.dumps(root_object, indent=4)

    log(f"\nInfo: {serialized_string}", "INFO")

    log_destroy()
    sys.exit()