"""contains a library of tests for this API"""
from wrapper import IPViking
from pprint import pprint

def test_with_sandbox():
    """should function just like the sandbox curl listed on the dev page"""
    params = {'method':'ipq', 'apikey':'8292777557e8eb8bc169c2af29e87ac07d0f1ac4857048044402dbee06ba5cea', 'ip':'208.74.76.5'}
    ip = IPViking(args=params)
    success = ip.execute()
    print success
    pprint(ip.get_dict())

if __name__=='__main__':
    test_with_sandbox()