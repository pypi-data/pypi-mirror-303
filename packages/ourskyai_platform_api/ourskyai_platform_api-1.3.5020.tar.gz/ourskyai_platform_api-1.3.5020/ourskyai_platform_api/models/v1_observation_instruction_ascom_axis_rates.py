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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt

class V1ObservationInstructionAscomAxisRates(BaseModel):
    """
    ASCOM mount properties for rate tracking based on previous diagnostics  # noqa: E501
    """
    max_primary_speed: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="maxPrimarySpeed")
    max_secondary_speed: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="maxSecondarySpeed")
    primary_sign_west: Optional[StrictInt] = Field(None, alias="primarySignWest")
    primary_sign_east: Optional[StrictInt] = Field(None, alias="primarySignEast")
    secondary_sign_west: Optional[StrictInt] = Field(None, alias="secondarySignWest")
    secondary_sign_east: Optional[StrictInt] = Field(None, alias="secondarySignEast")
    primary_reversed: Optional[StrictBool] = Field(None, alias="primaryReversed")
    secondary_reversed: Optional[StrictBool] = Field(None, alias="secondaryReversed")
    __properties = ["maxPrimarySpeed", "maxSecondarySpeed", "primarySignWest", "primarySignEast", "secondarySignWest", "secondarySignEast", "primaryReversed", "secondaryReversed"]

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
    def from_json(cls, json_str: str) -> V1ObservationInstructionAscomAxisRates:
        """Create an instance of V1ObservationInstructionAscomAxisRates from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ObservationInstructionAscomAxisRates:
        """Create an instance of V1ObservationInstructionAscomAxisRates from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ObservationInstructionAscomAxisRates.parse_obj(obj)

        _obj = V1ObservationInstructionAscomAxisRates.parse_obj({
            "max_primary_speed": obj.get("maxPrimarySpeed"),
            "max_secondary_speed": obj.get("maxSecondarySpeed"),
            "primary_sign_west": obj.get("primarySignWest"),
            "primary_sign_east": obj.get("primarySignEast"),
            "secondary_sign_west": obj.get("secondarySignWest"),
            "secondary_sign_east": obj.get("secondarySignEast"),
            "primary_reversed": obj.get("primaryReversed"),
            "secondary_reversed": obj.get("secondaryReversed")
        })
        return _obj


