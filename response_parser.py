"""Contains the classes built from an ipq response"""
import xmltodict
import json
from collections import OrderedDict
from constants import RESPONSE_TAGS
from errors import UnrecognizedResponse

def prep_response(response):
    """preps response for Response_Data creation"""

class Response_Data():
    """Data structure built from IPQ response. Attributes assigned directly from response."""
    response = None #string: raw response
    resp_dict = None #dict: response processed into layered dict
    fields = None #list: field names populated from response
    unrecognized = None #dict: unrecognized tags
    
    def __init__(self, response):
        self.response = response
        self.fields = []
        self.pick_and_parse()
        self.assign_data()
        
    def __repr__(self):
        return str(self.__dict__)
        
        
    def pick_and_parse(self):
        """picks the parser type to use"""
        if '<?xml' in self.response:
            self.resp_dict = xmltodict.parse(self.response)
        elif self.response[0]=='{':
            self.resp_dict = json.loads(self.response)
        else:
            raise UnrecognizedResponse()
    
    def assign_data(self):
        """assigns IPQ_Data attributes from flattened dict"""
        discard_tags, broken = break_out_dict(self.resp_dict)
        
        #assign attributes
        for tag in RESPONSE_TAGS:
            if tag in broken.keys():
                self.__dict__[tag] = broken.pop(tag)
                self.fields.append(tag)
        
        self.unrecognized = broken
        self.discarded_tags = discard_tags
    
        
    
    
        
        
        
def break_out_dict(d):
    """removes unnecessary layers from a nested dict"""
    layered = True
    layer_keys = []
    while layered:
        if len(d) == 1:
            # this layer is unnecessary
            if isinstance(d, list):
                #break out the list first
                d = d[0]
                continue
            key = d.keys()[0]
            layer_keys.append(key)
            d = d[key]
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
            
    