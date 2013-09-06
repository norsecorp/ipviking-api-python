ipviking-api-python
===================

IPViking API for Python

This API is designed to allow one to import IPViking data directly into Python as dicts. It requires no external
libraries, though it does reference several internals such as httplib.

Usage is simple, and examples can be seen in tests.tests. The request parameters are in tests.inputs.


Here's the structural breakdown:
	
	wrapper.py: This module contains the IPViking class, which is used to manage calls to the service. The method to
		use is request(args), with args being a dict of parameters for this specific request.
	requests.py: This module validates and prepares the arguments for the request to our server. It also contains two helper 
		functions, geofilterhelper and riskfactorhelper, which convert lists of geofilter/riskfactor arguments to an appropriate
		xml-formatted string.
	responses.py: This module parses the responses from our server into a dict (leaves it a string, if it's an http document).
	
	helpers/
		-constants.py: This module contains various running constants referenced throughout the package.
		-errors.py: This module contains our error classes.
		-util.py: This module contains utilities to help check, repair, and parse the data.
		-xmltodict.py: This is a module by Martin Blech of https://github.com/martinblech/ used to reduce xml documents to dicts.
		
	tests/
		-inputs.py: This module contains test input values for the various API methods.
		-outputs.py: This module contains expected responses for the various API methods.
		-tests.py: This module contains functions to test the various API methods
		-unittests.py: UNDER CONSTRUCTION (will eventually contain tests for individual helper functions)
		
	auth/
		This module contains base objects and an example of use for using the API as part of web authentication. See the
		ipviking-django, ipviking-pyramid or other packages to see the full implementation.
		-objects.py: base objects for authentication.
			-IPV_Rule: a check to perform on IPViking IPQ data.
			-IPV_Response: response to failure to meet an IPV rule. Generates a response context dict.
			-ipvAuthorizer: one class to find them all, one class to bind them. This is what actually runs the rules and responses.
		-sample_authorizer.py: contains methods for authentication.
			-configure: configures the IPV_AUTH instance in this module, which is used by validate.
			-validate: gets the client's host address, feeds it to a configured ipvAuthorizer, and returns the responses in a fashion
				that works for whatever framework you're using. This one is geared towards Django.
		
And that's about the shape of it! Enjoy.