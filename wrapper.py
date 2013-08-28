"""This is a library of classes used by this API"""
import httplib
from errors import MissingArgument, UnrecognizedArgument, InvalidArgument
from util import PARAMCHECKS, PARSERS, configParse, break_out_dict
from constants import (REQUIREDS, 
                                     DROP_ARGS,
                                     DEFAULTS)


class IPViking(object):
    """class for outgoing API calls to IPViking"""
    def __init__(self, config = None, args = {}):
        self.config = configParse(config) #config is general settings for the object, not request parameters
        self.responses = []
        self.httpc = httplib.HTTPConnection(self.config['proxy'])   #prepare proxy and build HTTPConnection

    
    def execute(self, args = {}):
        """makes the request"""
        #clean args, make sure we've got everything we need
        reqargs, args = self.validate_args(args)
        
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
        
        success, data  = self.parseResponse(response)
        
        #break out any unneeded dicts
        if isinstance(data, dict):
            data_broken = {}
            for key, item in data.items():
                data_broken[key] = break_out_dict(item)
        
        return success, data
    
    def validate_args(self, args):
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
                argy = self.config.get(arg) # failing that, go for configs
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
    
    def parseResponse(self,response):
        """Parses data from HTTPResponse"""
        content = response.read()
        contenttype = response.getheader('content-type')
        if contenttype == '':
            contenttype = 'text/html'
        if contenttype == 'text/html':
            if response.status in [200,201,202,204,302]:
                #good response code
                return (True, content)
            else:
                return (False, content)
        elif content in ['', 'null']:
            if response.status in [200,201,202,204,302]:
                #good response code
                return (True, content)
            else:
                return (False, content)
        elif contenttype in PARSERS:
            data=PARSERS[contenttype](content)
            return (True, data)            
        else:
            return (False, content)
        
    
               
               
