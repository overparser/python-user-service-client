# coding: utf-8

"""
    user-service

    User Management Service

    The version of the OpenAPI document: 0.03
    Contact: derror.dd@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr

class GetUsersUserId404ResponseError(BaseModel):
    """
    GetUsersUserId404ResponseError
    """
    code: Optional[StrictInt] = None
    message: Optional[StrictStr] = None
    details: Optional[StrictStr] = None
    __properties = ["code", "message", "details"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GetUsersUserId404ResponseError:
        """Create an instance of GetUsersUserId404ResponseError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetUsersUserId404ResponseError:
        """Create an instance of GetUsersUserId404ResponseError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetUsersUserId404ResponseError.parse_obj(obj)

        _obj = GetUsersUserId404ResponseError.parse_obj({
            "code": obj.get("code"),
            "message": obj.get("message"),
            "details": obj.get("details")
        })
        return _obj

