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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, conlist
from ourskyai_astro_api.models.v1_gain_curve_point import V1GainCurvePoint
from ourskyai_astro_api.models.v1_read_noise_point import V1ReadNoisePoint

class V1GainCurve(BaseModel):
    """
    Gain Curve  # noqa: E501
    """
    gain_mode: StrictInt = Field(..., alias="gainMode")
    gain_curve: conlist(V1GainCurvePoint) = Field(..., alias="gainCurve")
    readout_noise_curve: Optional[conlist(V1ReadNoisePoint)] = Field(None, alias="readoutNoiseCurve")
    __properties = ["gainMode", "gainCurve", "readoutNoiseCurve"]

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
    def from_json(cls, json_str: str) -> V1GainCurve:
        """Create an instance of V1GainCurve from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in gain_curve (list)
        _items = []
        if self.gain_curve:
            for _item in self.gain_curve:
                if _item:
                    _items.append(_item.to_dict())
            _dict['gainCurve'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in readout_noise_curve (list)
        _items = []
        if self.readout_noise_curve:
            for _item in self.readout_noise_curve:
                if _item:
                    _items.append(_item.to_dict())
            _dict['readoutNoiseCurve'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1GainCurve:
        """Create an instance of V1GainCurve from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1GainCurve.parse_obj(obj)

        _obj = V1GainCurve.parse_obj({
            "gain_mode": obj.get("gainMode"),
            "gain_curve": [V1GainCurvePoint.from_dict(_item) for _item in obj.get("gainCurve")] if obj.get("gainCurve") is not None else None,
            "readout_noise_curve": [V1ReadNoisePoint.from_dict(_item) for _item in obj.get("readoutNoiseCurve")] if obj.get("readoutNoiseCurve") is not None else None
        })
        return _obj


