"""This module contains the ipvAuth class, which handles authentications"""
import ipviking_api_python.helpers.constants as ipv_consts
from ipviking_api_python.auth.objects import ipvAuthorizer

APIKEY = ipv_consts.SANDBOX_APIKEY
PROXY = ipv_consts.PROXIES['SANDBOX']    
IPV_AUTH = ipvAuthorizer().configure({'apikey':APIKEY, 'proxy':PROXY})

def configure(self, authview = None, validview = None, apikey = None, proxy = None, rules = None, responses = None):
    try:
        IPV_AUTH.configure(apikey = apikey, proxy = proxy, rules = rules, responses = responses, authview = authview, validview = validview)
    except:
        global IPV_AUTH
        IPV_AUTH = ipvAuthorizer()
        IPV_AUTH.configure(apikey = apikey, proxy = proxy, rules = rules, responses = responses, authview = authview, validview = validview)

def validate(request):
    """Runs the IPV_AUTH's validator"""
    #django style check for necessity
    if request.session['ipviking']:
        #it's already been checked
        response = IPV_AUTH.validview(request, request.session['ipviking'], request.path, {})
        return response
    
    #django-style ip getting, trimming port off the end
    ip = request.get_host().split(':')[0]
    
    #localhost is invalid, so we'll use the sandbox-suggested host in that case
    if ip == '127.0.0.1':
        ip = '208.74.76.5'
    
    valid, request, level, context = IPV_AUTH.validate_request(request, ip)
    
    if valid:
        #if it's valid, we'll set the flag and return the valid view
        request.session['ipviking'] = level
        response = IPV_AUTH.validview(request, level, request.path, {})
    else:
        #We've got something to do here. Call the authview function
        response = IPV_AUTH.authview(request, level, request.path, context)
    return response
    
    