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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from ourskyai_platform_api.models.optical_tube_type import OpticalTubeType

class V1CreateOpticalTubeRequest(BaseModel):
    """
    V1CreateOpticalTubeRequest
    """
    model: StrictStr = Field(...)
    focal_length_mm: StrictInt = Field(..., alias="focalLengthMm")
    aperture_mm: StrictInt = Field(..., alias="apertureMm")
    type: Optional[OpticalTubeType] = None
    __properties = ["model", "focalLengthMm", "apertureMm", "type"]

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
    def from_json(cls, json_str: str) -> V1CreateOpticalTubeRequest:
        """Create an instance of V1CreateOpticalTubeRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1CreateOpticalTubeRequest:
        """Create an instance of V1CreateOpticalTubeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1CreateOpticalTubeRequest.parse_obj(obj)

        _obj = V1CreateOpticalTubeRequest.parse_obj({
            "model": obj.get("model"),
            "focal_length_mm": obj.get("focalLengthMm"),
            "aperture_mm": obj.get("apertureMm"),
            "type": obj.get("type")
        })
        return _obj


