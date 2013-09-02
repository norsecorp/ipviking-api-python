"""Contains example inputs for API calls"""
import time

GEOFILTERLIST = [{'command':'add',
                  'clientID':'123456',
                  'action':'Allow',
                  'category':'Master'},
                 {'command':'add',
                  'clientID':'123456',
                  'action':'Deny',
                  'category':'zip',
                  'country':'US',
                  'zip':'13601'}]

GEOFILTERXML = """\
<?xml version=1.0?>
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

RISKFACTORLIST = [{'command':'add',
                   'risk_id':'1',
                   'risk_good_value':'99',
                   'risk_bad_value':'99'},
                  {'command':'delete',
                   'risk_id':'2',
                   'risk_good_value':'99',
                   'risk_bad_value':'99'},
                  {'command':'add',
                   'risk_id':'3',
                   'risk_good_value':'-5',
                   'risk_bad_value':'12'}
                  ]

RISKFACTORXML = """\
<?xml version=1.0?>
<ipviking>
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
          "risk":{'method':'risk', 'ip':'208.74.76.5'},
          "submission":{'method':'submission','apikey':'bac03485550e8fa1f2c1aca58d4947cac7942326d81265d9e0dcbf41c04787a9', 'ip':'208.74.76.5','category':'7','protocol':'51','timestamp':str(int(time.time())), 'proxy':'labs.ipviking.com'},
          "riskfactor":{'method':'riskfactor', 'settingsxml':RISKFACTORXML},
          "geofilter":{'method':'geofilter', 'geofilterxml':GEOFILTERXML}
          }