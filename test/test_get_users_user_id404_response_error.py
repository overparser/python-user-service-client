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

from openapi_client.models.get_users_user_id404_response_error import GetUsersUserId404ResponseError  # noqa: E501

class TestGetUsersUserId404ResponseError(unittest.TestCase):
    """GetUsersUserId404ResponseError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetUsersUserId404ResponseError:
        """Test GetUsersUserId404ResponseError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetUsersUserId404ResponseError`
        """
        model = GetUsersUserId404ResponseError()  # noqa: E501
        if include_optional:
            return GetUsersUserId404ResponseError(
                code = 56,
                message = '',
                details = ''
            )
        else:
            return GetUsersUserId404ResponseError(
        )
        """

    def testGetUsersUserId404ResponseError(self):
        """Test GetUsersUserId404ResponseError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
