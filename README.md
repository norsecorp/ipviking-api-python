ipviking-api-python
===================

IPViking API for Python

This API is designed to allow one to import IPViking data directly into Python as dicts. It does require the requests
library, which is available via pip and easy_install, as well as from docs.python-requests.org.

File breakdown:

constants.py
-contains running constants for this module. 
 -Can be used as a config file. 
 -Shows the parameters for a request with descriptions as comments nearby. 
 -Contains the DROP_INVALID toggle, which when true drops unrecognized parameters instead of throwing an exception.

errors.py
-just contains exception classes. Nothing to see here.

response_parser.py
-parses the returned content into a dict, and throws an exception on bad responses.

tests.py
-tests for evaluating performance of this module

wrapper.py
-Here's the meat of it. This contains the IPViking class, which ingests parameters, sends the request, parses the
response, and allows you to call a dict of the response information.
  -IPViking object
    -initialized with 
      -config: contains parameters. can be .ini, dict, or list of 2-tuples. Defaults to sandbox.
      -args: args are parameters for an individual request. Overwrites values from config.
      -if args contains all necessary data for a request, initialization will send a single request and return the results of execute
    -.execute(args):
      -takes args (parameters for a single request, overwrites config values)
      -Sends the request and processes the data coming back.
      -appends the parsed response data to IPViking.data
      -returns success boolean and dict parsed from response
      
    
NOTES:
functionality tested for ipq, risk, riskfactor, and submission. geofilter returns 'null'