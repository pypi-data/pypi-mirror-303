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
from ourskyai_platform_api.models.location import Location

class V1CreateNodeRequest(BaseModel):
    """
    Create Node  # noqa: E501
    """
    name: StrictStr = Field(...)
    observatory_id: Optional[StrictStr] = Field(None, alias="observatoryId")
    camera_id: StrictStr = Field(..., alias="cameraId")
    optical_tube_id: StrictStr = Field(..., alias="opticalTubeId")
    mount_id: StrictStr = Field(..., alias="mountId")
    filter_wheel_id: Optional[StrictStr] = Field(None, alias="filterWheelId")
    max_altitude: StrictInt = Field(..., alias="maxAltitude")
    location: Location = Field(...)
    __properties = ["name", "observatoryId", "cameraId", "opticalTubeId", "mountId", "filterWheelId", "maxAltitude", "location"]

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
    def from_json(cls, json_str: str) -> V1CreateNodeRequest:
        """Create an instance of V1CreateNodeRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1CreateNodeRequest:
        """Create an instance of V1CreateNodeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1CreateNodeRequest.parse_obj(obj)

        _obj = V1CreateNodeRequest.parse_obj({
            "name": obj.get("name"),
            "observatory_id": obj.get("observatoryId"),
            "camera_id": obj.get("cameraId"),
            "optical_tube_id": obj.get("opticalTubeId"),
            "mount_id": obj.get("mountId"),
            "filter_wheel_id": obj.get("filterWheelId"),
            "max_altitude": obj.get("maxAltitude"),
            "location": Location.from_dict(obj.get("location")) if obj.get("location") is not None else None
        })
        return _obj


