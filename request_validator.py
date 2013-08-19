from constants import CATEGORIES, OPTIONS, METHODS, REQUIRED_PARAMS, DROP_INVALID
from errors import *

def validateIP(ip):
    """checks that a string is four 0-255 numbers joined with periods"""
    valid = True
    splitted = ip.split('.')
    if len(splitted)!=4:
        valid = False
    for num in splitted:
        try:
            if not 0<=int(num)<=255:
                valid = False
        except:
            valid = False
    return valid
        
PARAM_CHECKS = {'apikey':lambda val, verb: (True, None) if len(val)==64 else (False, InvalidKeyLength()),
                'method':lambda val, verb: (True, None) if val.lower() in METHODS else (False, InvalidMethod(val)),
                'ip':lambda val, verb: (True, None) if validateIP(val) else (False, InvalidIP(val)),
                'transID':lambda val, verb: (True, None),
                'clientID':lambda val, verb: (True, None),
                'customID':lambda val, verb: (True, None),
                'address':lambda val, verb: (True, None),
                'city':lambda val, verb: (True, None),
                'zip':lambda val, verb: (True, None),
                'state':lambda val, verb: (True, None),
                'country':lambda val, verb: (True, None),
                'categories':lambda val, verb: (True, None) if val in CATEGORIES.keys() else (False, InvalidCategory(val)),
                'options':lambda val, verb: (True, None) if val in OPTIONS else InvalidOption(val),
                'protocol':lambda val, verb: (True, None) if verb == "PUT" else (False, PUTArgument()),
                'category':lambda val, verb: (True, None) if verb == "PUT" else (False, PUTArgument()),
                'timestamp':lambda val, verb: (True, None) if verb == "PUT" else (False, PUTArgument())}

def validateRequest(args, verb):
    """checks and cleans arguments to be passed through this API"""
    success = True
    errors = []
    cleaned_args = {}

    #check that we have all required parameters
    for param in REQUIRED_PARAMS:
        if not param in args.keys():
            success = False
            errors.append(MissingArgument(param))
    
    #check parameters for validity
    for param, value in args.items():
        if param not in PARAM_CHECKS.keys() and DROP_INVALID == False:
            success = False
            errors.append(UnrecognizedArgument(param))
        else:
            succ, error = PARAM_CHECKS[param](value, verb)
            if not succ:
                success = False
                errors.append(error)
            else:
                cleaned_args[param]=value
    
    return success, errors, cleaned_args