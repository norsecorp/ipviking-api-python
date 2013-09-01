"""contains functions to parse requests"""
from helpers.constants import DROP_ARGS, DEFAULTS, REQUIREDS
from helpers.util import PARAMCHECKS
from helpers.errors import InvalidArgument, UnrecognizedArgument, MissingArgument


def validate_args(args, config):
    """validates and cleans args"""
    cleaned_args = {}

    #check args and move to cleaned
    if DROP_ARGS:
        for arg, val in args.items():
            if not PARAMCHECKS.get(arg) or not PARAMCHECKS.get(arg)(val):
                continue
            cleaned_args[arg]=val
    else:
        for arg, val in args.items():
            try:
                if not PARAMCHECKS[arg](val):
                    raise InvalidArgument(arg,val)
                cleaned_args[arg]=val
            except KeyError:
                raise UnrecognizedArgument(arg, val)
    
    #make sure we have method, output, proxy
    reqargs = {}
    for arg in ['method', 'output','proxy', 'apikey']:
        try:
            argy=cleaned_args.pop(arg) # try to get it from the request arguments first
        except KeyError:
            argy=None
        if not argy:
            argy = config.get(arg) # failing that, go for configs
        if not argy:
            argy=DEFAULTS[arg] # finally, go for the defaults
        reqargs[arg]=argy
    
    #pop out method and apikey from required args
    method=reqargs.pop('method')
    cleaned_args['method']=method
    cleaned_args['apikey']=reqargs['apikey']
    
    #use method to determine required arguments
    for arg in REQUIREDS[method]:
        if not cleaned_args.get(arg):
            raise MissingArgument(arg)

    #set verb
    reqargs['verb'] = 'PUT' if method=='submission' else 'POST'
    
    #return it!
    return reqargs, cleaned_args