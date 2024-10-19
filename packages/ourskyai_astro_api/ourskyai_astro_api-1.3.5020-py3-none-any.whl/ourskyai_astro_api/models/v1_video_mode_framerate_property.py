# coding: utf-8

"""
    OurSky Astro

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.3.5020
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class V1VideoModeFramerateProperty(BaseModel):
    """
    V1VideoModeFramerateProperty
    """
    roi_x_pixels: StrictInt = Field(..., alias="roiXPixels")
    roi_y_pixels: StrictInt = Field(..., alias="roiYPixels")
    adc_bit_depth: StrictInt = Field(..., alias="adcBitDepth")
    fps: Union[StrictFloat, StrictInt] = Field(...)
    binning: StrictInt = Field(...)
    __properties = ["roiXPixels", "roiYPixels", "adcBitDepth", "fps", "binning"]

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
    def from_json(cls, json_str: str) -> V1VideoModeFramerateProperty:
        """Create an instance of V1VideoModeFramerateProperty from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1VideoModeFramerateProperty:
        """Create an instance of V1VideoModeFramerateProperty from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1VideoModeFramerateProperty.parse_obj(obj)

        _obj = V1VideoModeFramerateProperty.parse_obj({
            "roi_x_pixels": obj.get("roiXPixels"),
            "roi_y_pixels": obj.get("roiYPixels"),
            "adc_bit_depth": obj.get("adcBitDepth"),
            "fps": obj.get("fps"),
            "binning": obj.get("binning")
        })
        return _obj


