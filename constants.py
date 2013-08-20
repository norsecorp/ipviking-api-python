"""Project constants. Can be used to configure API."""
from sys import stdout
#run settings
DROP_ARGS = True
DEBUG = True

def debugPrint(message):
    if DEBUG:
        stdout.write(message)

#for requests
PROXY_UNIVERSAL    = 'http://api.ipviking.com/api/'
PROXY_NORTHAMERICA = 'http://us.api.ipviking.com/api/'
PROXY_EUROPE       = 'http://eu.api.ipviking.com/api/'
PROXY_ASIAPACIFIC  = 'http://as.api.ipviking.com/api/'
PROXY_SOUTHAMERICA = 'http://la.api.ipviking.com/api/'
PROXY_SANDBOX      = 'http://beta.ipviking.com/api/'

SANDBOX_APIKEY = '8292777557e8eb8bc169c2af29e87ac07d0f1ac4857048044402dbee06ba5cea'

REQUIRED_CONFIG = ['apikey',
                   'proxy']

REQUIRED_PARAMS = ['ip']

ALL_PARAMS = ['ip', #Required. IP address.
              'apikey', #Required. API Key provided by Norse. Overwrite for apikey provided in config.
              'method', #Required. Defaults to ipq.
              'verb', #Required. Defaults to POST except if method is submission; then default is PUT
              'transID', #Optional. User-supplied transaction ID for client-side processing.
              'clientID', #Optional. User-supplied client ID for client-side processing.
              'customID', #Optional. User-supplied custom ID for client-side processing.
              'address', #Optional. Street address for GeoMatch feature.
              'city', #Optional. City for GeoMatch feature.
              'zip', #Optional. ZIP for GeoMatch feature.
              'state', #Optional. State for GeoMatch feature.
              'country', #Optional. Country for GeoMatch feature.
              'categories', #Optional. Comma-separated list of categories to filter by. Defaults to pull all entries.
              'options', #Optional. Pipe-separated ("|") list of options for API behavior. 
              'protocol', #Optional. For PUT requests.
              'category', #Optional.  For PUT requests.
              'timestamp'] #Optional. Unix timestamp for PUT requests.

CATEGORIES = {  '1':'Explicit Content',
                '2':'Bogon Unadv',
                '3':'Bogon Unass',
                '4':'Proxy',
                '5':'Botnet',
                '6':'Financial',
                '7':'CyberTerrorism',
                '8':'Identity',
                '9':'BruteForce',
                '10':'Cyber Stalking',
                '11':'Arms',
                '12':'Drugs',
                '13':'Espionage',
                '14':'Music Piracy',
                '15':'Games piracy',
                '16':'Movie piracy',
                '17':'Publishing piracy',
                '18':'StockMarket',
                '19':'Hacked',
                '20':'Information piracy',
                '21':'High risk',
                '22':'HTTP',
                '31':'Malicious Site',
                '41':'Friendly Scanning',
                '51':'Web Attacks',
                '61':'DATA Harvesting',
                '71':'Global Whitelist'   }

OPTIONS = ['noresolve',
           'url_details',
           'suppress',
           'compress',
           'haversine']

METHODS = ['submission',
           'ipq',
           'risk',
           'blacklist',
           'riskfactor',
           'geofilter',
           'geomatch']


#response stuff

RESPONSE_TAGS = {'method':'The IPViking API request method called',
                'ip':'The IP being analyzed',
                'host':'The host name for the IP',
                'clientID':'The clientID value, if one was supplied in the request',
                'transID':'The transID value, if one was supplied in the request',
                'customID':'The customID value, if one was supplied in the request',
                'risk_factor':'The IPQ Score',
                'risk_color':'A color associated with a IPViking-defined scale of risk. Possible values are green, yellow, orange, red',
                'risk_name':'The IPViking-defined general category of risk. Possible values are Low, Medium, High',
                'risk_desc':'The IPViking-defined general category of risk. Possible values are Low, Medium, High',
                'timestamp':'The UNIX timestamp of the request',
                'ip_info':'The nameserver and autonomous system information.',
                'geoloc':'The country, region, city, latitude, longitude, and ISP of the provided IP.',
                'organization':'The organization associated with the provided IP',
                'entries':'A set of information for each category of behavior associated with the provided IP.',
                'factoring':'The weight of a common set of risk factors that was used in evaluating the IP risk. See the Risk Factor table below for possible values.'}

HTTP_RESPONSES = {  "200":"OK:Request accepted and data is returned (only for seal method)",
                    "201":"Created:Submission accepted and processed",
                    "202":"Accepted:Submission accepted and in processing queue",
                    "204":"No Content:Request successful but no data exists for the given IP",
                    "302":"Found:Request successful and IP data was returned",
                    "400":"Bad Request:NOT an IPViking API KEY",
                    "401":"Unauthorized:Invalid IPViking API key",
                    "402":"Payment Required:Subscription has expired. Go to your Account and update payment information.",
                    "405":"Method Not Allowed:Not a supported HTTP method",
                    "409":"Conflict:Record already exists",
                    "415":"Unsupported media Type:Unsupported MIME/Media type",
                    "417":"Expectation Failed:Invalid supplied IP value",
                    "418":"Wrong Action:Invalid action was provided",
                    "419":"Wrong category:Invalid category was supplied",
                    "420":"GeoFilter Country error:Invalid or missing country filter",
                    "421":"GeoFilter Region error:Invalid or missing Region filter",
                    "422":"GeoFilter City error:Invalid or missing City filter",
                    "423":"GeoFilter ZIP error:Invalid or missing ZIP filter",
                    "424":"XML Command error:Missing or wrong command supplied in XML string",
                    "426":"Upgrade required:Subscription upgrade needed to use the request method",
                    "500":"Internal Server Error:Database or Server Error",
                    "501":"Not Implemented:Request method not implemented or supported",
                    "503":"Service unavailable:Service is currently down for unscheduled maintenance",
                    "509":"Bandwidth Limited Exceeded:This is for TEST API KEY only and the 24 hour limit of 200 requests is reached"}