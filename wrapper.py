"""This is a library of classes used by this API"""
import httplib
from helpers.util import configParse
from requests import validate_args
from responses import parseResponse


class IPViking(object):
    """This is a wrapper class to make requests easier.
    
    The config attribute provides a fallback for missing request parameters, while the httpc(onnection)
    saves us the time and trouble of initializing one for each request. Ideally, this should save time
    making calls to our service. See the Django repo for an example of integration.
    """
    
    def __init__(self, config = None, args = {}):
        self.config = configParse(config)                           #config is general settings for the object, not request parameters
        self.httpc = httplib.HTTPConnection(self.config['proxy'])   #prepare proxy and build HTTPConnection

    
    def request(self, args = {}):
        """This is what you'll call for any request. First, we validate the arguments. Then, make the request.
        Then get and parse the response, and return a boolean success and the parsed data. That data will be
        either a string text/html response (usually if the request failed), or a parsed OrderedDict."""
        #clean args, make sure we've got everything we need
        reqargs, args = validate_args(args, self.config)
        
        #make the request
        try:
            self.httpc.request(method=reqargs['verb'], 
                               url='http://%s/api/' % reqargs['proxy'], 
                               body='&'.join(("%s=%s" % (str(key), str(val)) for key, val in args.items())), 
                               headers = {'Accept':reqargs['output'],
                                          'User-Agent':'python-requests/1.2.3 CPython/2.7.5 Windows/7',
                                          'Content-Type':'application/x-www-form-urlencoded',
                                          'Accept-Encoding':'gzip, deflate, compress'})
        
        #recreate httpconnection in case of failed request
        except httplib.CannotSendRequest:
            self.httpc = httplib.HTTPConnection(reqargs['proxy'])   #prepare proxy and build HTTPConnection
            self.httpc.request(method=reqargs['verb'], 
                              url='http://%s/api/' % reqargs['proxy'], 
                              body='&'.join(("%s=%s" % (str(key), str(val)) for key, val in args.items())), 
                              headers = {'Accept':reqargs['output'],
                                         'User-Agent':'python-requests/1.2.3 CPython/2.7.5 Windows/7',
                                         'Content-Type':'application/x-www-form-urlencoded',
                                         'Accept-Encoding':'gzip, deflate, compress'})
        #get and parse the response
        response=self.httpc.getresponse()
        success, data  = parseResponse(response)        
        
        return success, data
    

    

        
    
               
               
