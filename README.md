ipviking-api-python
===================

IPViking API for Python

This API is designed to allow one to import IPViking data directly into Python as dicts. It requires no external
libraries, though it does reference several internals such as httplib.

Usage is simple, and examples can be seen in tests.tests. The request parameters are in tests.inputs, though.


Here's the structural breakdown:
	
	wrapper.py: This module contains the IPViking class, which is used to manage calls to the service. The method to
		use is request(args), with args being a dict of parameters for this specific request.
	requests.py: This module validates and prepares the arguments for the request to our server.
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
		
And that's about the shape of it! Enjoy.