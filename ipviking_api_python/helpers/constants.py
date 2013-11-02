"""Project constants. Can be used to configure API."""
import time
#run settings
DROP_ARGS = True                #drops invalid or unrecognized argments when true
DEBUG = False                   #Enables debugPrint method

#Default and debug proxy/key configurations
PROXIES = { 'UNIVERSAL':'api.ipviking.com',
            'NORTHAMERICA':'us.api.ipviking.com',
            'EUROPE':'eu.api.ipviking.com',
            'ASIAPACIFIC':'as.api.ipviking.com',
            'SOUTHAMERICA':'la.api.ipviking.com',
            'SANDBOX':'beta.ipviking.com'}

SANDBOX_APIKEY = '8292777557e8eb8bc169c2af29e87ac07d0f1ac4857048044402dbee06ba5cea'

DEFAULT_CONFIG = {'apikey':SANDBOX_APIKEY, 'proxy':PROXIES['SANDBOX']}


#Request parameters
REQUIREDS = {'submission':['apikey', 'category','protocol','ip'],               #Required parameters by method
             'geofilter':['apikey', 'geofilterxml'],
             'riskfactor':['apikey', 'settingsxml'],
             'ipq':['apikey', 'ip'],
             'risk':['apikey', 'ip'],
             'ipview':['apikey','ip']}

DEFAULTS = {'apikey':SANDBOX_APIKEY,                                            #Reasonable defaults for parameters, when we have defaults
            'proxy':PROXIES['SANDBOX'],
            'timestamp':str(int(time.time())),
            'method':'ipq',
            'output':'application/json'
            }

CATEGORIES = ['1','2','3','4','5','6','7', '8','9','10','11','12','13','14','15','16', '17','18','19','20','21', '22','31', '41','51','61', '71']                   #A map of categories to validate riskfactor args

PROTOCOLS = ['17','7','19','30','31','32','33','40','50','51','60','70','80','90','100','110','111','112','52','120','53','54','55','130','140','141','150','151','152','41','34']     #a map of protocols to validate riskfactor args

#Options for different requests. Note: some may be deprecated or not implemented.
OPTIONS = ['noresolve',
           'url_details',
           'suppress',
           'compress',
           'haversine']

#Request methods
METHODS = ['submission',
           'ipq',
           'risk',
           'riskfactor',
           'geofilter',
           'ipview']



#Response constants
RESPONSE_TAGS = {'method':'The IPViking API request method called',                 #A map of help texts to help decipher different API responses.
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

HTTP_RESPONSES = {  "200":"OK:Request accepted and data is returned (only for seal method)",                #A map of HTTP responses for error debugging.
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