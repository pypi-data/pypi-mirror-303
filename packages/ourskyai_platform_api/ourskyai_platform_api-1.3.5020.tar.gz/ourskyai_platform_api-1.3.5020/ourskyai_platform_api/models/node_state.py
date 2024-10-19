# coding: utf-8

"""
    OurSky Platform

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.3.5020
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class NodeState(str, Enum):
    """
    NodeState
    """

    """
    allowed enum values
    """
    READY = 'READY'
    PENDING = 'PENDING'
    OFFLINE = 'OFFLINE'
    UNAVAILABLE = 'UNAVAILABLE'
    UNKNOWN = 'UNKNOWN'
    SUPERSEDED = 'SUPERSEDED'
    DECOMMISSIONED = 'DECOMMISSIONED'

    @classmethod
    def from_json(cls, json_str: str) -> NodeState:
        """Create an instance of NodeState from a JSON string"""
        return NodeState(json.loads(json_str))


