from dotenv import load_dotenv
load_dotenv(override=True)
from pathlib import Path
from datetime import datetime
from unittest import TestCase, mock, TestSuite, makeSuite, TextTestRunner
import get_all
import store
import update
import delete

class TestMeasureUnitsCases(TestCase):

    def setUp(self) -> None:
        return super().setUp()
    
    def test_get_all(self, *_, **__):
        self.event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/path/to/resource",
            "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
            "cookies": [
                "cookie1",
                "cookie2"
            ],
            "headers": {
                "Header1": "value1",
                "Header2": "value1,value2"
            },
            "queryStringParameters": {
                "parameter1": "value1,value2",
                "parameter2": "value"
            },
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "api-id",
                "authentication": {
                "clientCert": {
                    "clientCertPem": "CERT_CONTENT",
                    "subjectDN": "www.example.com",
                    "issuerDN": "Example issuer",
                    "serialNumber": "a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1",
                    "validity": {
                    "notBefore": "May 28 12:30:02 2019 GMT",
                    "notAfter": "Aug  5 09:36:04 2021 GMT"
                    }
                }
                },
                "authorizer": {
                "jwt": {
                    "claims": {
                    "claim1": "value1",
                    "claim2": "value2"
                    },
                    "scopes": [
                    "scope1",
                    "scope2"
                    ]
                }
                },
                "domainName": "id.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "id",
                "http": {
                "method": "POST",
                "path": "/path/to/resource",
                "protocol": "HTTP/1.1",
                "sourceIp": "192.168.0.1/32",
                "userAgent": "agent"
                },
                "requestId": "id",
                "routeKey": "$default",
                "stage": "$default",
                "time": "12/Mar/2020:19:03:58 +0000",
                "timeEpoch": 1583348638390
            },
            "body": "{\"name\": \"gramos\",\"symbol\": \"g\"}",
            "pathParameters": {
                "parameter1": "value1"
            },
            "isBase64Encoded": False
        }
        output = get_all.lambda_handler(self.event, None)
        print(output)

    def test_store(self, *_, **__):
        self.event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/path/to/resource",
            "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
            "cookies": [
                "cookie1",
                "cookie2"
            ],
            "headers": {
                "Header1": "value1",
                "Header2": "value1,value2"
            },
            "queryStringParameters": {
                "parameter1": "value1,value2",
                "parameter2": "value"
            },
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "api-id",
                "authentication": {
                "clientCert": {
                    "clientCertPem": "CERT_CONTENT",
                    "subjectDN": "www.example.com",
                    "issuerDN": "Example issuer",
                    "serialNumber": "a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1",
                    "validity": {
                    "notBefore": "May 28 12:30:02 2019 GMT",
                    "notAfter": "Aug  5 09:36:04 2021 GMT"
                    }
                }
                },
                "authorizer": {
                "jwt": {
                    "claims": {
                    "claim1": "value1",
                    "claim2": "value2"
                    },
                    "scopes": [
                    "scope1",
                    "scope2"
                    ]
                }
                },
                "domainName": "id.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "id",
                "http": {
                "method": "POST",
                "path": "/path/to/resource",
                "protocol": "HTTP/1.1",
                "sourceIp": "192.168.0.1/32",
                "userAgent": "agent"
                },
                "requestId": "id",
                "routeKey": "$default",
                "stage": "$default",
                "time": "12/Mar/2020:19:03:58 +0000",
                "timeEpoch": 1583348638390
            },
            "body": "{\"name\": \"gramos\",\"symbol\": \"g\"}",
            "pathParameters": {
                "parameter1": "value1"
            },
            "isBase64Encoded": False
        }
        output = store.lambda_handler(self.event, {})
        print(output)
    
    def test_update(self, *_, **__):
        self.event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/path/to/resource",
            "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
            "cookies": [
                "cookie1",
                "cookie2"
            ],
            "headers": {
                "Header1": "value1",
                "Header2": "value1,value2"
            },
            "queryStringParameters": None,
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "api-id",
                "authentication": {
                "clientCert": {
                    "clientCertPem": "CERT_CONTENT",
                    "subjectDN": "www.example.com",
                    "issuerDN": "Example issuer",
                    "serialNumber": "a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1",
                    "validity": {
                    "notBefore": "May 28 12:30:02 2019 GMT",
                    "notAfter": "Aug  5 09:36:04 2021 GMT"
                    }
                }
                },
                "authorizer": {
                "jwt": {
                    "claims": {
                    "claim1": "value1",
                    "claim2": "value2"
                    },
                    "scopes": [
                    "scope1",
                    "scope2"
                    ]
                }
                },
                "domainName": "id.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "id",
                "http": {
                "method": "POST",
                "path": "/path/to/resource",
                "protocol": "HTTP/1.1",
                "sourceIp": "192.168.0.1/32",
                "userAgent": "agent"
                },
                "requestId": "id",
                "routeKey": "$default",
                "stage": "$default",
                "time": "12/Mar/2020:19:03:58 +0000",
                "timeEpoch": 1583348638390
            },
            "body": "{\"symbol\": \"gr\"}",
            "pathParameters": {
                "id": 23
            },
            "isBase64Encoded": False
        }
        output = update.lambda_handler(self.event, {})
        print(output)
    
    def test_delete(self, *_, **__):
        self.event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/path/to/resource",
            "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
            "cookies": [
                "cookie1",
                "cookie2"
            ],
            "headers": {
                "Header1": "value1",
                "Header2": "value1,value2"
            },
            "queryStringParameters": None,
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "api-id",
                "authentication": {
                "clientCert": {
                    "clientCertPem": "CERT_CONTENT",
                    "subjectDN": "www.example.com",
                    "issuerDN": "Example issuer",
                    "serialNumber": "a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1",
                    "validity": {
                    "notBefore": "May 28 12:30:02 2019 GMT",
                    "notAfter": "Aug  5 09:36:04 2021 GMT"
                    }
                }
                },
                "authorizer": {
                "jwt": {
                    "claims": {
                    "claim1": "value1",
                    "claim2": "value2"
                    },
                    "scopes": [
                    "scope1",
                    "scope2"
                    ]
                }
                },
                "domainName": "id.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "id",
                "http": {
                "method": "POST",
                "path": "/path/to/resource",
                "protocol": "HTTP/1.1",
                "sourceIp": "192.168.0.1/32",
                "userAgent": "agent"
                },
                "requestId": "id",
                "routeKey": "$default",
                "stage": "$default",
                "time": "12/Mar/2020:19:03:58 +0000",
                "timeEpoch": 1583348638390
            },
            "body": None,
            "pathParameters": {
                "id": 24
            },
            "isBase64Encoded": False
        }
        output = delete.lambda_handler(self.event, {})
        print(output)


test_suites = TestSuite()
#test_suites.addTest(makeSuite(TestMeasureUnitsCases))
test = TestMeasureUnitsCases()
test.setUp()
test_suites.addTest(test.test_store)

runner = TextTestRunner()
runner.run(test_suites)

