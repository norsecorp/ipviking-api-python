"""This is a library of classes used by this API"""
from urlparse import urlparse
import requests
from sys import stdout
from errors import InvalidProxy, InvalidApikey, MissingArgument, UnrecognizedArgument, InvalidArgument
from response_parser import ResponseData
from constants import (SANDBOX_APIKEY, 
                       PROXY_SANDBOX,
                       REQUIRED_CONFIG, 
                       ALL_PARAMS, 
                       DROP_ARGS,
                       DEBUG,
                       METHODS,
                       OPTIONS)

REQUEST_TYPES = {'GET':requests.get,
                 'POST':requests.post,
                 'PUT':requests.put,
                 'DELETE':requests.delete}
def ip_check(args):
    if args.get('method') not in ['riskfactor', 'geofilter']:
        ip = args.get('ip')
        if not ip:            
            return (False, MissingArgument('ip'))
        if not len(ip.split('.')) == 4 or False in [lambda x: x.is_digit() and 0<=int(x)<256 for x in ip.split('.')]:
            return (False, InvalidArgument('ip'))
    return (True, None)

ARG_CHECKS = {'method':lambda args: (True, None) if args.get('method') in METHODS else (False, InvalidArgument('method')),
              'options':lambda args: (True, None) if args.get('options') in OPTIONS else (False, InvalidArgument('options')), 
              'ip':ip_check}

def debugPrint(message):
    if DEBUG:
        stdout.write(message)

class IPViking(object):
    """class for outgoing API calls to IPViking"""
    def __init__(self, config = None, args = {}):
        self.args = {}
        self.config = self.parse_config(config)
        self.responses = []
        if 'ip' in self.args.keys():
            return True, self.execute(args)
    
    def parse_config(self, config):
        """parses config"""
        configs = {}
        
        if not config:
            #use the sandbox apikey and proxy
            configs = {'proxy':PROXY_SANDBOX, 'apikey':SANDBOX_APIKEY}
        elif isinstance(config, str):
            with open(config, 'r') as fh:
                for line in fh:
                    if " = " in line:
                        configs[line.split(' = ', 1)[0].lower()] = line.split(' = ', 1)[1]
        elif isinstance(config, list):
            for arg, value in config:
                configs[arg.lower()] = value
        elif isinstance(config, dict):
            for arg, value in config.items():
                configs[arg.lower()] = value
        else:
            raise Exception("Invalid Config Type. Valid: none, filepath, array, dict")

        for arg in REQUIRED_CONFIG:
            if not arg in configs.keys():
                raise MissingArgument(arg)

        for key, value in configs.items():
            self.args[key] = value
    
    def validate_config(self):
        """validates config options"""
        #validate proxy
        scheme, netloc = urlparse(self.args['proxy'])[:2]
        if len(scheme) == 0 or len(netloc) == 0:
            raise InvalidProxy()
        if not self.args.get('apikey') or len(self.args['apikey']) != 64:
            raise InvalidApikey()
    
    def validate_args(self, args):
        """validates and cleans args"""
        cleaned_args = {}
        success = True
        errors = []

        #check args and move to cleaned
        for arg, val in args.items():
            if arg in ALL_PARAMS:
                if not ARG_CHECKS.get(arg):
                    cleaned_args[arg] = val                
                elif ARG_CHECKS[arg](args)[0]:
                    cleaned_args[arg] = val
                elif not ARG_CHECKS[arg](args)[0]:
                    success = False
                    errors.append(ARG_CHECKS[arg](args)[1])
            else:
                if not DROP_ARGS:
                    success = False 
                    errors.append(UnrecognizedArgument(arg))
                
        #add needed arguments
        if not 'method' in cleaned_args:
            cleaned_args['method'] = 'ipq'
        if not 'verb' in cleaned_args:
            if cleaned_args['method'].lower() == 'submission':
                self.args['verb'] = 'PUT'
            else:
                self.args['verb'] = 'POST'
        if not 'output' in cleaned_args:
            self.args['output'] = 'application/json'

        if not success:
            return (False, ';    '.join(str(error) for error in errors))
        
        else:
            return (True, cleaned_args)
        
    def execute(self, args = {}):
        """makes the request"""
        #validate config... just in case
        self.validate_config()
        
        #clean args, make sure we've got everything we need
        success, cleaned_args = self.validate_args(args)
        if not success:
            return False, cleaned_args
        
        #make the request
        response = REQUEST_TYPES[self.args['verb']](self.args['proxy'], 
                                                    data=cleaned_args, 
                                                    headers = {'Accept':self.args['output']})
        
        #create ResponseData object (parses at initialization)
        response = ResponseData(response)
        
        #append the response to our IPViking object
        self.responses.append(response)
        
        return True, response
    
               
               
