ipviking-api-python
===================

IPViking API for Python

This API is designed to allow one to import IPViking data directly into Python as dicts.

File breakdown:

constants.py
-contains running constants for this module. 
 -Can be used as a config file. 
 -Shows the parameters for a request with descriptions as comments nearby. 
 -Contains the DROP_INVALID toggle, which when true drops unrecognized parameters instead of throwing an exception.

errors.py
-just contains exception classes. Nothing to see here.

request_validator.py
-contains rules for validating options handed to a request. see wrapper.py

response_parser.py
-parses the returned content into a dict

tests.py
-tests for evaluating performance of this module

wrapper.py
-Here's the meat of it. This contains the IPViking class, which ingests parameters, sends the request, parses the response, and returns the response header and a ResponseData object.
  -IPViking object
    -initialized with 
      -config: contains parameters. can be .ini, dict, or list of 2-tuples. Defaults to sandbox.
      -verb: String. HTTP verb. GET, POST, PUT, and DELETE are supported.
      -args: Dict. Keys should be from the parameters list in constants.
    -IPViking.execute():
      -Sends the request and processes the data coming back.
      -returns response header and a dict of the information from the response.
	-for more data, look at the ResponseData object- it includes unrecognized information.