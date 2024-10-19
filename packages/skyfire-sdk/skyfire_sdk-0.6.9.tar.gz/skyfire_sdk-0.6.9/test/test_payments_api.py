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

from skyfire_sdk.api.payments_api import PaymentsApi


class TestPaymentsApi(unittest.TestCase):
    """PaymentsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PaymentsApi()

    def tearDown(self) -> None:
        pass

    def test_make_payment_standalone(self) -> None:
        """Test case for make_payment_standalone

        """
        pass

    def test_validate_payment(self) -> None:
        """Test case for validate_payment

        """
        pass


if __name__ == '__main__':
    unittest.main()
