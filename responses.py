"""contains functions to parse responses"""
from helpers.util import PARSERS, break_out_dict

def parseResponse(response):
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