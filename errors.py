"""Contains custom error classes."""

class RequestFailed(Exception):
    def __str__(self):
        return repr("IPViking request failed. Check your settings.")

class MissingArgument(Exception):        
    def __init__(self, arg): self.arg = arg 
    def __str__(self):
        return repr("Missing required argument %s." % self.arg)

class UnrecognizedArgument(Exception):
    def __init__(self, arg): self.arg = arg 
    def __str__(self):
        return repr("Unrecognized argument %s. Check documentation for valid arguments." % self.arg)
                
class InvalidArgument(Exception):        
    def __init__(self, arg, val): 
        self.arg = arg
        self.val = val
    def __str__(self):
        return repr("Invalid argument %s: %s" % (self.arg, self.val))

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

class InvalidConfig(Exception):
    def __init__(self, conftype):
        self.conftype = str(conftype)
    def __str__(self):
        return repr("You provided an invalid config %. Please provide one of: .ini-style config file, dict, list of 2-tuples, or None for defaults." % self.conftype)
    