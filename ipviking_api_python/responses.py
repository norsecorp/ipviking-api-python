"""contains functions to parse responses"""
from ipviking_api_python.helpers.util import PARSERS, break_out_dict

def parseResponse(response):
    """Parses data from HTTPResponse. First get the content type.
        -if text/html and status code indicates success, return True and the http response.
        -if text/html and status code indicates failure, return False and the http response.
        -if application/json, parse it into a dict.
        -if application/xml, parse it into a dict.
        -else: who knows what we're looking at; return False and the response.
    If the parsing returned anything besides a dict, we'll coerce it to a dict to make 
    downstream use easier. Then if there are any unneeded layers of wrappign around the dict,
    we'll get rid of those for the sake of easier calls later on. Return True and our parsed data."""
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

    else:
        return (False, content)
    
    #enumerate and coerce to dict
    if isinstance(data, list):
        data = {i:element for i, element in enumerate(data)}
        
    #break out any unneeded dicts
    data_broken = {}
    for key, item in data.items():
        data_broken[key] = break_out_dict(item)
    
    return (True, data_broken)