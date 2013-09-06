from ipviking_api_python.wrapper import IPViking
from ipviking_api_python.helpers.constants import SANDBOX_APIKEY, PROXIES
            
class IPV_Response(object):
    """Base class for an IPViking Authentication response.
    -level is an integer value used to map the strength of this response relative to others.
    -state_message is a message to be passed along to the template to provide context to a blocked user.
        -An example might be, "We'll need you to login. Your IP address has been flagged, due to %s.",
            which will be completed with the reason passed on in self.respond.
    -response context contains other context values, such as a form, to be rendered in the template."""
    def __init__(self, state, template, response_context):
        self.state = state
        self.template = template
        self.response_context = response_context
    
    def respond(self, warning):
        respctxt = self.response_context
        respctxt.update({'state':self.state % warning, 'template':self.template})
        return respctxt
    
class IPV_Rule(object):
    """Base class for an IPViking Authentication rule. 
    -fields is a list of string keys to the IPViking Query data dict (see example in examples.py)
    -check is a function that results in a boolean when performed on the IPViking data field determined by fields. 
    -warning is a string, the warning message to pass along on failure of the check. 
    -response is an IPV_Response to be activated on failure of the check."""
    def __init__(self, fields, check , warning, response):
        self.check = check
        self.fields = fields
        self.warning = warning
        self.response = response
        
    def validate(self, ipv_data):
        """Method to check whether or not an IP address passes your rule, based on their IPViking data"""
        field_data = ipv_data
        field_idx = 0
        while not isinstance(field_data, (str, int, float)) and field_idx < len(self.fields):
            field_data = field_data.get(self.fields[field_idx])
            field_idx += 1
        if not isinstance(field_data, (str, int, float)):
            raise Exception("Could not find field. Check IPV Rule.")
        check = self.check(field_data)
        return check, self.warning, self.response

class ipvAuthorizer(object):
    apikey = SANDBOX_APIKEY
    proxy = PROXIES['SANDBOX']
    rules = []
    responses = {}
    ipv = IPViking(config = {'apikey':SANDBOX_APIKEY, 'proxy':PROXIES['SANDBOX']})
    authview = None
    validview = None
    
    def configure(self, authview = None, validview = None, apikey = None, proxy = None, rules = None, responses = None):
        """This is the method called externally. Pass it any or all of the following args and it will set them:
        authview, validview, apikey, proxy, rules, and responses"""
        if validview:
            self.validview = validview
        if authview:
            self.authview = authview
        if apikey:
            self.apikey = apikey
        if proxy:
            self.proxy = proxy
        if rules:
            self.rules = rules
        if responses:
            self.responses = responses
            
    def setRule(self, index, fields, check, warning, response):
        """Takes an index to insert the new rule at, and the arguments necessary to initialize an IPV_Rule object.
        Check the IPV_Rule docstring in rules_and_responses"""
        self.rules.insert(index, IPV_Rule(fields, check, warning, response))
        
    def setResponse(self, level, state_message, template, response_context):
        """Sets a new response to the ipvAuth object using the level it maps to and the initialization arguments
        for an IPV_Response object. Check the IPV_Response docstring in rules_and_responses"""
        self.responses[level]=IPV_Response(state_message, template, response_context)
        
    def validate_request(self, request, ip):
        """This is method that validates a request using the IPViking API."""
        if not self.ipv:                                                    #make sure we have an IPViking object
            self.configure()
        success, data = self.ipv.request({'method':'ipq', 'ip':ip})         #make the request
        if not success:
            raise Exception("IPViking request failed. Check your API key and proxy.")
            return (True, request, None, {})                                #if something goes wrong, warn and return ValidResponse
        
        levels = []
        warnings = []
        for rule in self.rules:                                             #validate the client using self.rules
            failed, warning, level = rule.validate(data)
            if failed:
                levels.append(level)
                warnings.append(warning)
                
        if len(levels) == 0:                                                #if we didn't get anything, let them in!
            return (True, request, 0, {})                                   
        level = max(levels)                                                 #pick the highest level and warning
        warning = warnings[levels.index(level)]
        context = self.responses[level].respond(warning)                    #generate the context from self.responses
        return (False, request, level, context)                                    #return the request and the context
        