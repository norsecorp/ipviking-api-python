"""contains a library of tests for this API"""
from wrapper import IPViking
from constants import PROXY_SANDBOX
from pprint import pprint
from cStringIO import StringIO
import timeit
import time

GEOFILTERXML = StringIO("""<?xml version=1.0?>
<ipviking>
        <geofilter>
                <filters>
                        <command>add</command>
                        <clientID>123456</clientID>
                        <action>Allow</action>
                        <category>Master</category>
                        <country></country>
                        <region></region>
                        <city></city>
                        <zip></zip>
                </filters>
                <filters>
                        <command>add</command>
                        <clientID>123456</clientID>
                        <action>Deny</action>
                        <category>zip</category>
                        <country>US</country>
                        <region></region>
                        <city></city>
                        <zip>13601</zip>
                </filters>
        </geofilter>
</ipviking>""")

RISKFACTORXML = """<ipviking>
        <settings>
                <riskfactors>
                        <command>add</command>
            <risk_id>1</risk_id>
            <risk_good_value>99</risk_good_value>
            <risk_bad_value>99</risk_bad_value>
                </riskfactors>
        <riskfactors>
                        <command>delete</command>
            <risk_id>2</risk_id>
            <risk_good_value>99</risk_good_value>
            <risk_bad_value>99</risk_bad_value>
                </riskfactors>
                <riskfactors>
                        <command>add</command>
            <risk_id>3</risk_id>
            <risk_good_value>-5</risk_good_value>
            <risk_bad_value>12</risk_bad_value>
                </riskfactors>
        </settings>
</ipviking>"""

PARAMS = {"ipq":{'method':'ipq', 'apikey':'bac03485550e8fa1f2c1aca58d4947cac7942326d81265d9e0dcbf41c04787a9', 'ip':'208.74.76.5'},
          "risk":{'method':'risk', 'apikey':'bac03485550e8fa1f2c1aca58d4947cac7942326d81265d9e0dcbf41c04787a9', 'ip':'208.74.76.5'},
          "submission":{'method':'submission','apikey':'bac03485550e8fa1f2c1aca58d4947cac7942326d81265d9e0dcbf41c04787a9','ip':'67.13.46.123','category':'7','protocol':'51','timestamp':str(int(time.time()))},
          "riskfactor":{'method':'riskfactor', 'apikey':'bac03485550e8fa1f2c1aca58d4947cac7942326d81265d9e0dcbf41c04787a9', 'settingsxml':RISKFACTORXML},
          "geofilter":{'method':'geofilter', 'apikey':'bac03485550e8fa1f2c1aca58d4947cac7942326d81265d9e0dcbf41c04787a9', 'geofilterxml':GEOFILTERXML}
          }

def testmethod(method):
    config = {'apikey':'bac03485550e8fa1f2c1aca58d4947cac7942326d81265d9e0dcbf41c04787a9', 'proxy':'http://labs.ipviking.com/api/'}
    params = PARAMS.get(method)

    ip = IPViking(config=config)
    success, response = ip.execute(params)
    if success:
        pprint(response.data)
    else:
        print type(response)
        
def time_test():
    t=timeit.Timer("ip.execute(args={'method':'ipq', 'apikey':'bac03485550e8fa1f2c1aca58d4947cac7942326d81265d9e0dcbf41c04787a9', 'ip':'208.74.76.5'})", "from wrapper import IPViking\nip=IPViking(config={'apikey':'bac03485550e8fa1f2c1aca58d4947cac7942326d81265d9e0dcbf41c04787a9', 'proxy':'http://beta.ipviking.com/api/'})\n")
    print t.repeat(10,10)
    
if __name__=='__main__':
    testmethod("geofilter")
    

