"""Contains custom error classes."""
from constants import CATEGORIES, HTTP_RESPONSES

class NoAddressSupplied():
    def __str__(self):
        return repr("No address supplied. Required arguments: apikey, ip address.")

class InvalidProxy(Exception):
    def __init__(self, arg='supplied.'): self.arg=arg
    def __str__(self):
        return repr("Invalid proxy location %s" % self.arg)
    
class InvalidVerb(Exception):
    def __init__(self, arg = ''): self.arg = ' '+arg if len(arg)>0 else arg
    def __str__(self):
        return repr("Invalid HTTP verb%s. GET, POST, PUT, and DELETE are supported." % self.arg)

class MissingArgument(Exception):        
    def __init__(self, arg): self.arg = arg 
    def __str__(self):
        return repr("Missing required argument %s." % self.arg)

class UnrecognizedArgument(Exception):
    def __init__(self, arg): self.arg = arg 
    def __str__(self):
        return repr("Unrecognized argument %s. Check documentation for valid arguments." % self.arg)
                
class InvalidApikey(Exception):        
    def __init__(self, arg): self.arg = arg 
    def __str__(self):
        return repr("Invalid API key. API keys are 64-character strings.")

class InvalidIP(Exception):        
    def __init__(self, arg): self.arg = arg 
    def __str__(self):
        return repr("Invalid IP address %s.")

class InvalidCategory(Exception):        
    def __init__(self, arg): self.arg = arg 
    def __str__(self):
        return repr("Invalid category number %s. Valid categories are %s." % (self.arg, ''.join(CATEGORIES)))

class InvalidOption(Exception):        
    def __init__(self, arg): self.arg = arg 
    def __str__(self):
        return repr("Invalid option.")

class InvalidMethod(Exception):        
    def __init__(self, arg): self.arg = arg 
    def __str__(self):
        return repr("Invalid method %s. Valid methods: ")

class PUTArgument(Exception):        
    def __init__(self, arg): self.arg = arg 
    def __str__(self):
        return repr("Option only valid for PUT requests.")

class UnrecognizedResponse(Exception):
    def __init__(self, response = ''):
        if len(response) > 0:
            self.response = response
        else:
            self.response = None
    def __str__(self):
        if self.response:
            return repr("Unable to recognize response as XML or JSON. Response: %s" % self.response)
        else:
            return repr("Unable to recognize response as XML or JSON.")

class RequestNotSent(Exception):
    def __str__(self):
        return repr("IPViking.responsedata field is not assigned yet. IPViking.execute() has not been called or was not successful.")

class HttpReturned(Exception):
    def __init__(self, code):
        self.code = code
    def __str__(self):
        return repr("Http response received instead of XML or JSON. HTTP code %s:%s." % (self.code, HTTP_RESPONSES[self.code]))