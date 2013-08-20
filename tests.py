"""contains a library of tests for this API"""
from wrapper import IPViking
from constants import PROXY_SANDBOX
from pprint import pprint
import timeit


def test_with_sandbox():
    """should function just like the sandbox curl listed on the dev page"""
    config = {'apikey':'bac03485550e8fa1f2c1aca58d4947cac7942326d81265d9e0dcbf41c04787a9', 'proxy':PROXY_SANDBOX}
    params = {'method':'ipq', 'apikey':'bac03485550e8fa1f2c1aca58d4947cac7942326d81265d9e0dcbf41c04787a9', 'ip':'208.74.76.5'}

    ip = IPViking(config=config)
    success, response = ip.execute(params)
    if success:
        print type(response.data)
        pprint(response.data)
    else:
        print type(response)
        
def time_test():
    t=timeit.Timer("ip.execute(args={'method':'ipq', 'apikey':'bac03485550e8fa1f2c1aca58d4947cac7942326d81265d9e0dcbf41c04787a9', 'ip':'208.74.76.5'})", "from wrapper import IPViking\nip=IPViking(config={'apikey':'bac03485550e8fa1f2c1aca58d4947cac7942326d81265d9e0dcbf41c04787a9', 'proxy':'http://beta.ipviking.com/api/'})\n")
    print t.repeat(10,10)
    
if __name__=='__main__':
    time_test()
    

