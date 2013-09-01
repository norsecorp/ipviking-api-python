"""This modules contains a library of expected responses to the parameters in inputs"""

RESPONSES = {'geofilter' : { 0: {'action': 'Allow',
                                 'category': 'City',
                                 'city': 'PONG',
                                 'clientID': '0',
                                 'country': 'TW',
                                 'filter_id': '443',
                                 'hits': '0',
                                 'region': '04',
                                 'zip': '-'},
                             1: {'action': 'Allow',
                                 'category': 'Country',
                                 'city': '-',
                                 'clientID': '0',
                                 'country': 'US',
                                 'filter_id': '423',
                                 'hits': '4268',
                                 'region': '-',
                                 'zip': '-'},
                             2: {'action': 'Deny',
                                 'category': 'Master',
                                 'city': '-',
                                 'clientID': '0',
                                 'country': '-',
                                 'filter_id': '433',
                                 'hits': '0',
                                 'region': '-',
                                 'zip': '-'},
                             3: {'action': 'Allow',
                                 'category': 'Master',
                                 'city': '-',
                                 'clientID': '0',
                                 'country': '-',
                                 'filter_id': '1031',
                                 'hits': '0',
                                 'region': '-',
                                 'zip': '-'}},
         
             'ipq':{'clientID': 0,
                    'customID': 0,
                    'entries':[{'category_factor': '5',
                                'category_id': '1',
                                'category_name': 'Explicit Content',
                                'last_active': '2009-08-04T21:53:21-04:00',
                                'overall_protocol': 'eDonkey',
                                'protocol_id': '7',
                                'protocol_name': 'eDonkey User'},
                               {'category_factor': '5',
                                'category_id': '1',
                                'category_name': 'Explicit Content',
                                'last_active': '2010-02-14T04:30:05-05:00',
                                'overall_protocol': 'Ares',
                                'protocol_id': '17',
                                'protocol_name': 'Ares User'}],
                    'factor_entries': 13,
                    'factoring' : {'asn_record_factor': '-2',
                                   'asn_threat_factor': 2,
                                   'bgp_delegation_factor': '-2',
                                   'country_risk_factor': '4.1',
                                   'data_age_factor': '1',
                                   'geomatch_distance': 0,
                                   'geomatch_factor': 0,
                                   'iana_allocation_factor': '-2',
                                   'ip_resolve_factor': '-5',
                                   'ipviking_category_factor': 2,
                                   'ipviking_geofilter_factor': 0,
                                   'ipviking_geofilter_rule': 0,
                                   'ipviking_personal_factor': '-1',
                                   'region_risk_factor': '5',
                                   'search_volume_factor': '0'},
                     'geoloc': {'city': 'Los Angeles',
                                'country': 'United States',
                                'country_code': 'US',
                                'internet_service_provider': 'U.s. Colo, LLC',
                                'latitude': '34.053',
                                'longtitude': '-118.264',
                                'organization': 'CIS',
                                'region': 'CALIFORNIA',
                                'region_code': 'CA'},
                     'host': '208.74.76.5.uscolo.com',
                     'ip': '208.74.76.5',
                     'ip_info': {'autonomous_system_name': 'USCOLO-ASN - U.S. COLO, LLC',
                                 'autonomous_system_number': '32743'},
                     'method': 'ipq',
                     'risk_color': 'green',
                     'risk_desc': 'Low risk involved',
                     'risk_factor': 2.1,
                     'risk_name': 'Low',
                     'timestamp': '2013-08-31T19:26:05-04:00',
                     'transID': 0},
             'riskfactor':{  0: {'risk_attribute': 'Country Risk Factor',
                                 'risk_bad_value': '99',
                                 'risk_good_value': '99',
                                 'risk_id': '1'},
                             1: {'risk_attribute': 'Region Risk Factor',
                                 'risk_bad_value': '99',
                                 'risk_good_value': '99',
                                 'risk_id': '2'},
                             2: {'risk_attribute': 'IP resolve Factor',
                                 'risk_bad_value': '12',
                                 'risk_good_value': '-5',
                                 'risk_id': '3'},
                             3: {'risk_attribute': 'ASN Risk Factor',
                                 'risk_bad_value': '10',
                                 'risk_good_value': '-2',
                                 'risk_id': '4'},
                             4: {'risk_attribute': 'BGP Status Risk Factor',
                                 'risk_bad_value': '20',
                                 'risk_good_value': '-2',
                                 'risk_id': '5'},
                             5: {'risk_attribute': 'IANA status Risk factor',
                                 'risk_bad_value': '10',
                                 'risk_good_value': '-2',
                                 'risk_id': '6'},
                             6: {'risk_attribute': 'ByteWolf Risk factor',
                                 'risk_bad_value': '50',
                                 'risk_good_value': '-1',
                                 'risk_id': '7'},
                             7: {'risk_attribute': 'Category Risk Factor',
                                 'risk_bad_value': '99',
                                 'risk_good_value': '99',
                                 'risk_id': '8'},
                             8: {'risk_attribute': 'Freshness Risk Factor',
                                 'risk_bad_value': '20',
                                 'risk_good_value': '-15',
                                 'risk_id': '9'},
                             9: {'risk_attribute': 'Search Volume',
                                 'risk_bad_value': '20',
                                 'risk_good_value': '0',
                                 'risk_id': '10'},
                             10: {'risk_attribute': 'GeoFilter Factor',
                                  'risk_bad_value': '99',
                                  'risk_good_value': '-50',
                                  'risk_id': '11'}},
             'risk':{'clientID': 0,
                     'customID': 0,
                     'details': {'asn_record_factor': '10',
                                 'asn_threat_factor': 5,
                                 'bgp_delegation_factor': '-2',
                                 'country_risk_factor': '4.1',
                                 'data_age_factor': '3',
                                 'geomatch_distance': 0,
                                 'geomatch_factor': 0,
                                 'iana_allocation_factor': '-2',
                                 'ip_resolve_factor': '-5',
                                 'ipviking_category_factor': -103,
                                 'ipviking_geofilter_factor': 0,
                                 'ipviking_geofilter_rule': 0,
                                 'ipviking_personal_factor': '-1',
                                 'region_risk_factor': '5',
                                 'search_volume_factor': '0'},
                     'factor_entries': 13,
                     'geoloc': {'city': 'San Francisco',
                                'country': 'United States',
                                'country_code': 'US',
                                'internet_service_provider': 'Fastmetrics',
                                'latitude': '37.7749',
                                'longtitude': '-122.419',
                                'organization': 'PS Print',
                                'region': 'CALIFORNIA',
                                'region_code': 'CA'},
                     'host': 'mail.rpaarch.com',
                     'ip': '216.38.154.18',
                     'ip_info': {'autonomous_system_name': 'n\\/a',
                                 'autonomous_system_number': 'n\\/a'},
                     'method': 'risk',
                     'risk_color': 'green',
                     'risk_desc': 'Low risk involved',
                     'risk_factor': 0,
                     'risk_name': 'Low',
                     'timestamp': '2013-08-31T16:33:38-07:00',
                     'transID': 0},
             'submission':'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">   \n                    <html>   \n                        <head>   \n                            <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">   \n                            <title>201 Created</title>   \n                        </head>   \n                        <body>   \n                            <h1>Created</h1>   \n                            <p></p>   \n                            <hr />   \n                            <address>labs.ipviking.com</address>   \n                        </body>   \n                    </html>'
             }