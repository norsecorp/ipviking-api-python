"""Contains utility functions"""
from ipviking_api_python.helpers.constants import METHODS, OPTIONS, PROXIES, PROTOCOLS, CATEGORIES, DEFAULT_CONFIG, DROP_ARGS
from collections import OrderedDict
from ipviking_api_python.helpers.xmltodict import parse
from ast import literal_eval
from ipviking_api_python.helpers.errors import InvalidArgument, InvalidConfig

def ip_check(ip):
    """Simple helper method to check whether or not an IP is in expected 0-255.0-255.0-255.0-255 format."""
    if not ip:            
        return False
    if not len(ip.split('.')) == 4 or False in [(x.isdigit() and 0<=int(x)<256) for x in ip.split('.')]:
        return False
    return True

def configParse(conf):
    """Parses config args from string filename, dict, or list"""
    if not conf:
        configs = DEFAULT_CONFIG
    elif isinstance(conf, str):
        confs = []
        with open(conf, 'r') as fh:
            for line in fh:
                confs.append(line.split(' = ', 1).strip())
        configs = dict(filter(lambda line: len(line)==2, confs))
    elif isinstance(conf, dict):
        configs = conf
    elif isinstance(conf, list):
        configs = dict(filter(lambda line: len(line)==2, confs))
    else:
        raise InvalidConfig(type(conf))
    
    # Check our config values
    for key, arg in configs.items():
        if not (isinstance(key, str) and isinstance(arg,str) and PARAMCHECKS[key](arg)):
            if not DROP_ARGS:
                raise InvalidArgument()
    return configs
            
def break_out_dict(d):
    """removes unnecessary layers from a nested dict"""
    if not (isinstance(d, list) or isinstance(d, dict) or isinstance(d, OrderedDict)):
        return d
    layered = True
    while layered:
        layered, d = BREAKERS[type(d)](d)
    return d

#Parsing functions for different response body types
PARSERS = {'application/xml':lambda content: break_out_dict(parse(content)),
           'application/json':lambda content: break_out_dict(literal_eval(content))}

#Breakout-functions for lists, dicts, and ordered dicts.
BREAKERS = {type([]):lambda d: (True, d[0]) if len(d) == 1 else (False, d),
            type({}):lambda d: (True, d.values()[0]) if len(d) == 1 else (False, d),
            type(OrderedDict()): lambda d: (True, d.values()[0]) if len(d) == 1 else (False, d)}

#Basic validation checks for each request argument
PARAMCHECKS = {'apikey':lambda arg: len(arg)==64,
               'output':lambda arg: arg in ['application/xml', 'application/json'],
               'proxy':lambda arg: arg in PROXIES.values(),
               'method': lambda arg: arg in METHODS,
               'verb': lambda arg: arg in ['GET', 'POST', 'PUT', 'DELETE'],
               'ip': ip_check,
               'protocol': lambda arg: arg in PROTOCOLS,
               'category': lambda arg: arg in CATEGORIES,
               'timestamp': lambda arg: arg.isdigit() and len(arg) == 10,
               'categories':lambda arg: set(arg).issubset(CATEGORIES),
               'options':lambda arg:set(arg.split('|')).issubset(OPTIONS),
               'geofilterxml':lambda arg: True,
               'settingsxml':lambda arg: True}
