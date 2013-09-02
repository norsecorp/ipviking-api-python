"""Contains unit tests for all our helper functions"""
from requests import geofilterhelper, riskfactorhelper
from inputs import RISKFACTORXML, GEOFILTERXML, RISKFACTORLIST, GEOFILTERLIST

def test_rfhelper():
    assert riskfactorhelper(RISKFACTORLIST) == RISKFACTORXML, "rfhelper did not produce expected output. rfhelper output: %s\n\nExpected:%s" % (riskfactorhelper(RISKFACTORLIST), RISKFACTORXML)
    
def test_geohelper():
    assert geofilterhelper(GEOFILTERLIST) == GEOFILTERXML, "geohelper did not produce expected output. geohelper output: %s\n\nExpected:%s" % (geofilterhelper(GEOFILTERLIST), GEOFILTERXML)

if __name__ == '__main__':
    test_rfhelper()
    test_geohelper()
