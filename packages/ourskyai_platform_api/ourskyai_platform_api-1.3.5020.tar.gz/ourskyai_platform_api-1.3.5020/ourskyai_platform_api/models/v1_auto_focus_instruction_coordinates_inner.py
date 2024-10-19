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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class V1AutoFocusInstructionCoordinatesInner(BaseModel):
    """
    Coordinates in degrees in epoch J2000  # noqa: E501
    """
    right_ascension: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="rightAscension")
    declination: Optional[Union[StrictFloat, StrictInt]] = None
    __properties = ["rightAscension", "declination"]

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
    def from_json(cls, json_str: str) -> V1AutoFocusInstructionCoordinatesInner:
        """Create an instance of V1AutoFocusInstructionCoordinatesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1AutoFocusInstructionCoordinatesInner:
        """Create an instance of V1AutoFocusInstructionCoordinatesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1AutoFocusInstructionCoordinatesInner.parse_obj(obj)

        _obj = V1AutoFocusInstructionCoordinatesInner.parse_obj({
            "right_ascension": obj.get("rightAscension"),
            "declination": obj.get("declination")
        })
        return _obj


