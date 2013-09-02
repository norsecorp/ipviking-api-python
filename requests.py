"""contains functions to parse requests"""
from helpers.constants import DROP_ARGS, DEFAULTS, REQUIREDS
from helpers.util import PARAMCHECKS
from helpers.errors import InvalidArgument, UnrecognizedArgument, MissingArgument

def geofilterhelper(filters):
    """This field constructs a valid, IPViking-readable xml string from a list of dictionary filters.
    For guidance on necessary fields, please look at the IPViking Developer's docs. Required fields:
    command, action, category"""
    outputs = []
    for filt in filters:
        fields = ['                <filters>',
                  "<command>%s</command>" % filt.get('command', default = "add"),
                  "<clientID>%s</clientID>" % filt.get('clientID', default = '0'),
                  "<action>%s</action>" % filt.get('action'),
                  "<category>%s</category>" % filt.get('category'),
                  "<country>%s</country>" % filt.get('country', default = ''),
                  "<region>%s</region>" % filt.get('region', default = ''),
                  "<city>%s</city>" % filt.get('city', default = ''),
                  "<zip>%s</zip>" % filt.get('zip', default = '')]
        
         
        
        output ='\n                        '.join(fields)+'                </filters>\n'
        outputs.append(output)
    geoxml = "<?xml version=1.0?>\n<ipviking>\n        <geofilter>\n"+''.join(outputs)+'        </geofilter>\n</ipviking>'
    return geoxml

def riskfactorhelper(factors):
    """This field constructs a valid, IPViking-readable xml string from a list of dictionary factors.
    For guidance on necessary fields, please look at the IPViking Developer's docs. Required fields:
    command, action, category"""
    outputs = []
    for fact in factors:
        fields = ['                <riskfactors>',
                  "<command>%s</command>" % fact.get('command'),
                  "<risk_id>%s</risk_id>" % fact.get('risk_id'),
                  "<risk_good_value>%s</risk_good_value>" % fact.get('risk_good_value'),
                  "<risk_bad_value>%s</risk_bad_value>" % fact.get('risk_bad_value')]
        
         
        
        output ='\n                        '.join(fields)+'                </riskfactors>\n'
        outputs.append(output)
    riskxml = "<?xml version=1.0?>\n<ipviking>\n        <settings>\n"+''.join(outputs)+'        </settings>\n</ipviking>'
    return riskxml    

def validate_args(args, config):
    """validates and cleans args"""
    cleaned_args = {}

    #check args and move to cleaned
    if DROP_ARGS:
        for arg, val in args.items():
            if not PARAMCHECKS.get(arg) or not PARAMCHECKS.get(arg)(val):
                continue
            cleaned_args[arg]=val
    else:
        for arg, val in args.items():
            try:
                if not PARAMCHECKS[arg](val):
                    raise InvalidArgument(arg,val)
                cleaned_args[arg]=val
            except KeyError:
                raise UnrecognizedArgument(arg, val)
    
    #make sure we have method, output, proxy
    reqargs = {}
    for arg in ['method', 'output','proxy', 'apikey']:
        try:
            argy=cleaned_args.pop(arg) # try to get it from the request arguments first
        except KeyError:
            argy=None
        if not argy:
            argy = config.get(arg) # failing that, go for configs
        if not argy:
            argy=DEFAULTS[arg] # finally, go for the defaults
        reqargs[arg]=argy
    
    #pop out method and apikey from required args
    method=reqargs.pop('method')
    cleaned_args['method']=method
    cleaned_args['apikey']=reqargs['apikey']
    
    #convert lists to xml strings for geofilter/xml if that input style is used
    if method == 'geofilter' and isinstance(cleaned_args['geofilterxml'], list):
        cleaned_args['geofilterxml'] = geofilterhelper(cleaned_args['geofilterxml'])
    if method == 'riskfactor' and isinstance(cleaned_args['settingsxml'], list):
        cleaned_args['settingsxml'] = riskfactorhelper(cleaned_args['settingsxml'])


    
    #use method to determine required arguments
    for arg in REQUIREDS[method]:
        if not cleaned_args.get(arg):
            raise MissingArgument(arg)

    #set verb
    reqargs['verb'] = 'PUT' if method=='submission' else 'POST'
    
    #return it!
    return reqargs, cleaned_args