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

from skyfire_sdk.models.reloadly_gift_card_response_product import ReloadlyGiftCardResponseProduct

class TestReloadlyGiftCardResponseProduct(unittest.TestCase):
    """ReloadlyGiftCardResponseProduct unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReloadlyGiftCardResponseProduct:
        """Test ReloadlyGiftCardResponseProduct
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReloadlyGiftCardResponseProduct`
        """
        model = ReloadlyGiftCardResponseProduct()
        if include_optional:
            return ReloadlyGiftCardResponseProduct(
                brand = skyfire_sdk.models.reloadly_gift_card_response_product_brand.ReloadlyGiftCardResponse_product_brand(
                    brand_name = '', 
                    brand_id = 1.337, ),
                currency_code = '',
                total_price = 1.337,
                unit_price = 1.337,
                quantity = 1.337,
                country_code = '',
                product_name = '',
                product_id = 1.337
            )
        else:
            return ReloadlyGiftCardResponseProduct(
                brand = skyfire_sdk.models.reloadly_gift_card_response_product_brand.ReloadlyGiftCardResponse_product_brand(
                    brand_name = '', 
                    brand_id = 1.337, ),
                currency_code = '',
                total_price = 1.337,
                unit_price = 1.337,
                quantity = 1.337,
                country_code = '',
                product_name = '',
                product_id = 1.337,
        )
        """

    def testReloadlyGiftCardResponseProduct(self):
        """Test ReloadlyGiftCardResponseProduct"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
