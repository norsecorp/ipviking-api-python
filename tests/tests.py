"""contains a library of tests for this API"""
from wrapper import IPViking
from inputs import PARAMS
from outputs import RESPONSES
from pprint import pprint

PRINT_OUTPUT = True
def printOut(success, data):
    """Alternate to debugPrint for whole-method testing"""
    if PRINT_OUTPUT:
        pprint(success)
        pprint(data)


TEST_CONFIG = {'apikey':'8292777557e8eb8bc169c2af29e87ac07d0f1ac4857048044402dbee06ba5cea', 'proxy':'beta.ipviking.com'}

def testmethod(method):
    """Tests a specific method, or all methods, using the parameters from tests.inputs and asserts that we receive the expected response from tests.outputs"""
    ip = IPViking(config=TEST_CONFIG)
    
    if method == 'all':
        for method, param in PARAMS.items():
            success, data = ip.request(param)
            print "Method %s: %s!"% (method, str(success))
            assert cmp(data, RESPONSES[method]) or str(RESPONSES[method]) == str(data), "Failed to deliver same result for method %s.\n\nExpected: %s\nGot:      %s" % (method, str(RESPONSES[method]), str(data))

    else:
        param = PARAMS.get(method)
        if not param:
            raise Exception("Invalid method. Check the documentation for implemented methods.")
        success, data = ip.request(param)
        printOut(success, data)

if __name__ == '__main__':
    testmethod('all')
    

