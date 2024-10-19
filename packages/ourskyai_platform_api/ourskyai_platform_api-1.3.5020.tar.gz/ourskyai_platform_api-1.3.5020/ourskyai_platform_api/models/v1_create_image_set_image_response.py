# coding: utf-8

"""
    OurSky Platform

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.3.5020
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr

class V1CreateImageSetImageResponse(BaseModel):
    """
    V1CreateImageSetImageResponse
    """
    id: StrictStr = Field(...)
    upload_url: StrictStr = Field(..., alias="uploadUrl")
    __properties = ["id", "uploadUrl"]

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
    def from_json(cls, json_str: str) -> V1CreateImageSetImageResponse:
        """Create an instance of V1CreateImageSetImageResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1CreateImageSetImageResponse:
        """Create an instance of V1CreateImageSetImageResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1CreateImageSetImageResponse.parse_obj(obj)

        _obj = V1CreateImageSetImageResponse.parse_obj({
            "id": obj.get("id"),
            "upload_url": obj.get("uploadUrl")
        })
        return _obj


