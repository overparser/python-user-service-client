# coding: utf-8

"""
    user-service

    User Management Service

    The version of the OpenAPI document: 0.03
    Contact: derror.dd@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.post_user_request import PostUserRequest  # noqa: E501

class TestPostUserRequest(unittest.TestCase):
    """PostUserRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostUserRequest:
        """Test PostUserRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostUserRequest`
        """
        model = PostUserRequest()  # noqa: E501
        if include_optional:
            return PostUserRequest(
                user_id = '',
                telegram_login = '',
                telegram_id = 56,
                registration_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                username = '',
                status = 'active',
                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                default_repeats = [
                    '300 seconds'
                    ],
                preferences = openapi_client.models.user_preferences.User_preferences(
                    language = '', ),
                last_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return PostUserRequest(
                telegram_id = 56,
        )
        """

    def testPostUserRequest(self):
        """Test PostUserRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
