# coding: utf-8

"""
    Skyfire API

    The Skyfire API is designed to allow agents to interact with the Skyfire platform to enable autonomous payments.

    The version of the OpenAPI document: 1.0.0
    Contact: support@skyfire.xyz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from skyfire_sdk.models.api_ninja_dns_record import APINinjaDNSRecord

class TestAPINinjaDNSRecord(unittest.TestCase):
    """APINinjaDNSRecord unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> APINinjaDNSRecord:
        """Test APINinjaDNSRecord
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `APINinjaDNSRecord`
        """
        model = APINinjaDNSRecord()
        if include_optional:
            return APINinjaDNSRecord(
                record_type = 'NS',
                value = '',
                priority = 1.337,
                mname = '',
                rname = '',
                serial = 1.337,
                refresh = 1.337,
                retry = 1.337,
                expire = 1.337,
                ttl = 1.337
            )
        else:
            return APINinjaDNSRecord(
                record_type = 'NS',
        )
        """

    def testAPINinjaDNSRecord(self):
        """Test APINinjaDNSRecord"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
