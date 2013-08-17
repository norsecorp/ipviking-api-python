"""This is a library of classes used by this API"""
from urlparse import urlparse
from request_validator import validateRequest
import requests
from errors import InvalidProxy, InvalidVerb
from constants import SANDBOX_APIKEY, PROXY_SANDBOX
from response_parser import Response_Data
    
REQUEST_TYPES = {"GET":requests.get,
                 "POST":requests.post,
                 "PUT":requests.put,
                 "DELETE":requests.delete
                 }
                    
class IPViking():
    """class for outgoing API calls to IPViking"""
    def __init__(self, config = None, verb = 'POST', args = {}):
        self.config = config
        self.args = args
        self.parse_config()
        self.verb = verb
        self.validate_config()

        
    def parse_config(self):
        """parses config"""
        configs = {}

        if not self.config:
            self.apikey = SANDBOX_APIKEY
            self.proxy = PROXY_SANDBOX

        elif isinstance(self.config, str):
            with open(self.config, 'r') as fh:
                for line in fh:
                    if " = " in line:
                        configs[line.split(' = ', 1)[0].lower()] = line.split(' = ', 1)[1]
 
        elif isinstance(self.config, list):
            for arg, value in self.config:
                configs[arg.lower()] = value
        
        elif isinstance(self.config, dict):
            for arg, value in self.config.items():
                configs[arg.lower()] = value
        
        else:
            raise Exception("Invalid Config Type. Valid: default, filepath, array, dict")
        
        self.proxy = PROXY_SANDBOX if not 'proxy' in configs.keys() else configs.pop('proxy')
        for key, value in configs.items():
            self.args[key] = value
    
    def validate_config(self):
        """validates config options"""
        #validate proxy
        scheme, netloc = urlparse(self.proxy)[:2]
        if len(scheme) == 0 or len(netloc) == 0:
            raise InvalidProxy()
        #validate method
        if self.verb not in ["GET", "POST", "PUT", "DELETE"]:
            raise InvalidVerb()
    
    def validate_args(self):
        """validates and cleans args"""
        succ, errors, args = validateRequest(self.args,self.verb)
        if succ:
            return args
        else:
            raise Exception(''.join([str(error) for error in errors], ';   '))
        
    def execute(self):
        """makes the request"""
        self.validate_config()
        cleaned_args = self.validate_args()
        response = REQUEST_TYPES[self.verb](self.proxy, data=cleaned_args)
        headers = response.headers
        content = response.content
        data = Response_Data(content)
        self.responsedata = data
        self.responseheader = headers
        self.responsecontent = content
        return True
    
    def get_dict(self):
        return self.responsedata.to_dict()
        
