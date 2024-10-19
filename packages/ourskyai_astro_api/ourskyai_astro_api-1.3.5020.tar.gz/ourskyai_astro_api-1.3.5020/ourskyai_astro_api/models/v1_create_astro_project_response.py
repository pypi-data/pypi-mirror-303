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



from pydantic import BaseModel, Field, StrictStr

class V1CreateAstroProjectResponse(BaseModel):
    """
    Create Astro Response  # noqa: E501
    """
    id: StrictStr = Field(...)
    image_set_id: StrictStr = Field(..., alias="imageSetId")
    __properties = ["id", "imageSetId"]

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
    def from_json(cls, json_str: str) -> V1CreateAstroProjectResponse:
        """Create an instance of V1CreateAstroProjectResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1CreateAstroProjectResponse:
        """Create an instance of V1CreateAstroProjectResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1CreateAstroProjectResponse.parse_obj(obj)

        _obj = V1CreateAstroProjectResponse.parse_obj({
            "id": obj.get("id"),
            "image_set_id": obj.get("imageSetId")
        })
        return _obj


