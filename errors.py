"""Contains custom error classes."""
from constants import CATEGORIES

class InvalidProxy(Exception):
    def __init__(self, arg='suppled.'): self.arg=arg
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
                
class InvalidKeyLength(Exception):        
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
    def __str__(self):
        return repr("Unable to recognize response as XML or JSON.")