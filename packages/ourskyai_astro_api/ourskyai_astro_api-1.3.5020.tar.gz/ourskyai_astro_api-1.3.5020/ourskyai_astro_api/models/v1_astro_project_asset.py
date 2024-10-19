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

from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from ourskyai_astro_api.models.asset_file_type import AssetFileType
from ourskyai_astro_api.models.asset_type import AssetType
from ourskyai_astro_api.models.filter_type import FilterType
from ourskyai_astro_api.models.v1_astro_project_asset_metadata import V1AstroProjectAssetMetadata

class V1AstroProjectAsset(BaseModel):
    """
    Astro Project Asset  # noqa: E501
    """
    id: StrictStr = Field(...)
    asset_type: AssetType = Field(..., alias="assetType")
    filter_type: Optional[conlist(FilterType)] = Field(None, alias="filterType")
    metadata: Optional[V1AstroProjectAssetMetadata] = None
    url: StrictStr = Field(...)
    file_size_mb: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="fileSizeMb")
    file_type: Optional[AssetFileType] = Field(None, alias="fileType")
    created_at: datetime = Field(..., alias="createdAt")
    created_by: StrictStr = Field(..., alias="createdBy")
    number_of_combined_images: Optional[StrictInt] = Field(None, alias="numberOfCombinedImages")
    combined_exposure_seconds: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="combinedExposureSeconds")
    __properties = ["id", "assetType", "filterType", "metadata", "url", "fileSizeMb", "fileType", "createdAt", "createdBy", "numberOfCombinedImages", "combinedExposureSeconds"]

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
    def from_json(cls, json_str: str) -> V1AstroProjectAsset:
        """Create an instance of V1AstroProjectAsset from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1AstroProjectAsset:
        """Create an instance of V1AstroProjectAsset from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1AstroProjectAsset.parse_obj(obj)

        _obj = V1AstroProjectAsset.parse_obj({
            "id": obj.get("id"),
            "asset_type": obj.get("assetType"),
            "filter_type": obj.get("filterType"),
            "metadata": V1AstroProjectAssetMetadata.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "url": obj.get("url"),
            "file_size_mb": obj.get("fileSizeMb"),
            "file_type": obj.get("fileType"),
            "created_at": obj.get("createdAt"),
            "created_by": obj.get("createdBy"),
            "number_of_combined_images": obj.get("numberOfCombinedImages"),
            "combined_exposure_seconds": obj.get("combinedExposureSeconds")
        })
        return _obj


