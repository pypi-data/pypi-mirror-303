# coding: utf-8

"""
    OurSky Astro

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.3.5020
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class CalibrationMasterType(str, Enum):
    """
    CalibrationMasterType
    """

    """
    allowed enum values
    """
    FLAT = 'FLAT'
    DARK = 'DARK'
    BIAS = 'BIAS'

    @classmethod
    def from_json(cls, json_str: str) -> CalibrationMasterType:
        """Create an instance of CalibrationMasterType from a JSON string"""
        return CalibrationMasterType(json.loads(json_str))


