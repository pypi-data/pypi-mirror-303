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

from skyfire_sdk.models.gift_card_order_request import GiftCardOrderRequest

class TestGiftCardOrderRequest(unittest.TestCase):
    """GiftCardOrderRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GiftCardOrderRequest:
        """Test GiftCardOrderRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GiftCardOrderRequest`
        """
        model = GiftCardOrderRequest()
        if include_optional:
            return GiftCardOrderRequest(
                recipient_email = '',
                note = ''
            )
        else:
            return GiftCardOrderRequest(
                recipient_email = '',
        )
        """

    def testGiftCardOrderRequest(self):
        """Test GiftCardOrderRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
