"""Contains the classes built from a response"""
from xmltodict import parse
from ast import literal_eval
from collections import OrderedDict
from errors import UnrecognizedResponse, HttpReturned

class ResponseData(object):
    """Data structure built from IPQ response. Attributes assigned directly from response."""
    
    def __init__(self, response):
        self.headers = response.headers
        self.content = response.content
        self.data = self.assign_data(self.pick_and_parse())
        
    def pick_and_parse(self):
        """picks the parser type to use"""
        if '<?xml' in self.content:
            return parse(self.content)
        elif self.content[0]=='{':
            return literal_eval(self.content)
        elif self.content[:14]=="<!DOCTYPE HTML":
            httpcode = self.response.split("<title>",1)[1].rsplit("/title")[0]
            return HttpReturned(httpcode)
        else:
            return UnrecognizedResponse(self.response)
    
    def assign_data(self, parsed):
        """assigns IPQ_Data attributes from flattened dict"""
        discard_tags, broken = break_out_dict(parsed)
        data = {'discarded':discard_tags}

        #handle empty response case
        if not broken:
            data['data'] = None
            return data
        
        #assign keys and values
        for key, val in broken.items():
            data[key] = val
            
        return data
 
def break_out_dict(d):
    """removes unnecessary layers from a nested dict"""
    if not (isinstance(d, list) or isinstance(d, dict) or isinstance(d, OrderedDict)):
        return [], d
    layered = True
    layer_keys = []
    while layered:
        if isinstance(d, list):
            d = filter(lambda x: x!=None, d)
            if len(d) == 1:
                #layer is unnecesary
                layer_keys.append('list')
                d=d[0]
            else:
                layered = False
        elif isinstance(d, dict):
            if len(d.keys()) == 1:
                # this layer is unnecessary
                layer_keys.append(d.keys()[0])
                d=d.values()[0]
            else:
                layered = False
        elif isinstance(d, OrderedDict):
            if len(d.keys()) == 1:
                # this layer is unnecessary
                layer_keys.append(d.keys()[0])
                d=d.values()[0]
            else:
                layered = False
        else:
            layered = False
    return layer_keys, d

def flatten_dict(d):
    """flattens dict, working around any lists"""
    def items():
        for key, value in d.items():
            if value.isinstance(list):
                if len(value)>1:
                    value = OrderedDict(zip(range(len(value)),value))
                else:
                    value = value[0]
            if 'dict' in type(value).__repr__().lower():
                for subkey, subvalue in flatten_dict(value).items():
                    yield key + "." + subkey, subvalue
            else:
                yield key, value

    return OrderedDict(items())

def unflatten_dict(d):
    """like flatten, but backwards?"""
    out = OrderedDict()
    for key, value in d.items():
        current = out
        layers = key.split('.')
        for layer in layers:
            if not layer in current.keys():
                current[layer] = value
            else:
                current = current[layer]
    return out
            
    
