"""contains a library of tests for this API"""
from wrapper import IPViking
from pprint import pprint
import timeit
import time

GEOFILTERXML = """<?xml version=1.0?>
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
</ipviking>"""

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

PARAMS = {"ipq":{'method':'ipq', 'ip':'208.74.76.5'},
          "risk":{'method':'risk', 'apikey':'8292777557e8eb8bc169c2af29e87ac07d0f1ac4857048044402dbee06ba5cea', 'ip':'216.38.154.18'},
          "submission":{'method':'submission','apikey':'8292777557e8eb8bc169c2af29e87ac07d0f1ac4857048044402dbee06ba5cea','ip':'67.13.46.123','category':'7','protocol':'51','timestamp':str(int(time.time()))},
          "riskfactor":{'method':'riskfactor', 'apikey':'8292777557e8eb8bc169c2af29e87ac07d0f1ac4857048044402dbee06ba5cea', 'settingsxml':RISKFACTORXML},
          "geofilter":{'method':'geofilter', 'apikey':'8292777557e8eb8bc169c2af29e87ac07d0f1ac4857048044402dbee06ba5cea', 'geofilterxml':GEOFILTERXML}
          }

TEST_CONFIG = {'apikey':'8292777557e8eb8bc169c2af29e87ac07d0f1ac4857048044402dbee06ba5cea', 'proxy':'api.ipviking.com'}
LOCAL_CONFIG = {'apikey':'8292777557e8eb8bc169c2af29e87ac07d0f1ac4857048044402dbee06ba5cea', 'proxy':'localhost:15000'}

def testmethod(method):

    ip = IPViking(config=TEST_CONFIG)
    
    if method == 'all':
        for method, param in PARAMS.items():
            print "METHOD: "+method
            success, data = ip.execute(param)
            print str(success)
            pprint(data)

    else:
        param = PARAMS.get(method)
        success, data = ip.execute(param)
        print str(success)+': '+str(data)
        pprint(data)

        
def time_test(method):
    if method == 'all':
        for method, param in PARAMS.items():
            print "METHOD: %s\n" % method
            t=timeit.Timer("ip.execute(args=%s)" % str(param), "from wrapper import IPViking\nip=IPViking(config=%s)" % TEST_CONFIG)
            print t.repeat(10,10)
    else:
        t=timeit.Timer("ip.execute(args= %s)" % str(PARAMS.get(method)), "from wrapper import IPViking\nip=IPViking(config={'apikey':'bac03485550e8fa1f2c1aca58d4947cac7942326d81265d9e0dcbf41c04787a9', 'proxy':'http://beta.ipviking.com/api/'})\n")
        print t.repeat(10,10)
    
if __name__=='__main__':
    testmethod('all')
    

