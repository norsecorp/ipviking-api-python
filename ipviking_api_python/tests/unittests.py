"""Contains unit tests for all our helper functions"""
from ipviking_api_python.requests import geofilterhelper, riskfactorhelper
from ipviking_api_python.tests.inputs import RISKFACTORXML, GEOFILTERXML, RISKFACTORLIST, GEOFILTERLIST

def test_rfhelper():
    """Tests riskfactorhelper xml-builder function"""
    assert riskfactorhelper(RISKFACTORLIST) == RISKFACTORXML, "rfhelper did not produce expected output. rfhelper output: %s\n\nExpected:%s" % (riskfactorhelper(RISKFACTORLIST), RISKFACTORXML)
    
def test_geohelper():
    """Tests geofilterhelper xml-builder function"""
    assert geofilterhelper(GEOFILTERLIST) == GEOFILTERXML, "geohelper did not produce expected output. geohelper output: %s\n\nExpected:%s" % (geofilterhelper(GEOFILTERLIST), GEOFILTERXML)

if __name__ == '__main__':
    test_rfhelper()
    test_geohelper()
