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
from ourskyai_platform_api.models.v1_observation_metrics import V1ObservationMetrics

class V2CompleteObservationRequest(BaseModel):
    """
    V2CompleteObservationRequest
    """
    image_set_id: StrictStr = Field(..., alias="imageSetId")
    expected_image_count: StrictInt = Field(..., alias="expectedImageCount")
    metrics: Optional[V1ObservationMetrics] = None
    __properties = ["imageSetId", "expectedImageCount", "metrics"]

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
    def from_json(cls, json_str: str) -> V2CompleteObservationRequest:
        """Create an instance of V2CompleteObservationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of metrics
        if self.metrics:
            _dict['metrics'] = self.metrics.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V2CompleteObservationRequest:
        """Create an instance of V2CompleteObservationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V2CompleteObservationRequest.parse_obj(obj)

        _obj = V2CompleteObservationRequest.parse_obj({
            "image_set_id": obj.get("imageSetId"),
            "expected_image_count": obj.get("expectedImageCount"),
            "metrics": V1ObservationMetrics.from_dict(obj.get("metrics")) if obj.get("metrics") is not None else None
        })
        return _obj


