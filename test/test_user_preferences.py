# coding: utf-8

"""
    user-service

    User Management Service

    The version of the OpenAPI document: 0.03
    Contact: overparser@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.user_preferences import UserPreferences  # noqa: E501

class TestUserPreferences(unittest.TestCase):
    """UserPreferences unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserPreferences:
        """Test UserPreferences
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserPreferences`
        """
        model = UserPreferences()  # noqa: E501
        if include_optional:
            return UserPreferences(
                language = ''
            )
        else:
            return UserPreferences(
        )
        """

    def testUserPreferences(self):
        """Test UserPreferences"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
