# coding: utf-8

# flake8: noqa
"""
    OurSky Astro

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.3.5020
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from ourskyai_astro_api.models.asset_file_type import AssetFileType
from ourskyai_astro_api.models.asset_type import AssetType
from ourskyai_astro_api.models.calibration_master_type import CalibrationMasterType
from ourskyai_astro_api.models.daily_weather_city import DailyWeatherCity
from ourskyai_astro_api.models.daily_weather_forecast_item import DailyWeatherForecastItem
from ourskyai_astro_api.models.daily_weather_forecast_item_temp import DailyWeatherForecastItemTemp
from ourskyai_astro_api.models.daily_weather_forecast_item_weather_inner import DailyWeatherForecastItemWeatherInner
from ourskyai_astro_api.models.daily_weather_forecast_list_response import DailyWeatherForecastListResponse
from ourskyai_astro_api.models.empty_success import EmptySuccess
from ourskyai_astro_api.models.filter_type import FilterType
from ourskyai_astro_api.models.fits_header import FitsHeader
from ourskyai_astro_api.models.location import Location
from ourskyai_astro_api.models.mount_type import MountType
from ourskyai_astro_api.models.node_state import NodeState
from ourskyai_astro_api.models.optical_tube_type import OpticalTubeType
from ourskyai_astro_api.models.shutter_type import ShutterType
from ourskyai_astro_api.models.successful_create import SuccessfulCreate
from ourskyai_astro_api.models.tracking_type import TrackingType
from ourskyai_astro_api.models.v1_astro_project import V1AstroProject
from ourskyai_astro_api.models.v1_astro_project_asset import V1AstroProjectAsset
from ourskyai_astro_api.models.v1_astro_project_asset_metadata import V1AstroProjectAssetMetadata
from ourskyai_astro_api.models.v1_astro_project_asset_metadata_color_combination import V1AstroProjectAssetMetadataColorCombination
from ourskyai_astro_api.models.v1_astro_target import V1AstroTarget
from ourskyai_astro_api.models.v1_calibration_master import V1CalibrationMaster
from ourskyai_astro_api.models.v1_camera import V1Camera
from ourskyai_astro_api.models.v1_create_astro_project_image_set_request import V1CreateAstroProjectImageSetRequest
from ourskyai_astro_api.models.v1_create_astro_project_request import V1CreateAstroProjectRequest
from ourskyai_astro_api.models.v1_create_astro_project_response import V1CreateAstroProjectResponse
from ourskyai_astro_api.models.v1_create_calibration_master_request import V1CreateCalibrationMasterRequest
from ourskyai_astro_api.models.v1_create_calibration_master_response import V1CreateCalibrationMasterResponse
from ourskyai_astro_api.models.v1_create_calibration_set_image_request import V1CreateCalibrationSetImageRequest
from ourskyai_astro_api.models.v1_create_calibration_set_image_response import V1CreateCalibrationSetImageResponse
from ourskyai_astro_api.models.v1_create_calibration_set_request import V1CreateCalibrationSetRequest
from ourskyai_astro_api.models.v1_create_calibration_set_response import V1CreateCalibrationSetResponse
from ourskyai_astro_api.models.v1_create_camera_request import V1CreateCameraRequest
from ourskyai_astro_api.models.v1_create_image_set_image_request import V1CreateImageSetImageRequest
from ourskyai_astro_api.models.v1_create_image_set_image_response import V1CreateImageSetImageResponse
from ourskyai_astro_api.models.v1_create_image_set_request import V1CreateImageSetRequest
from ourskyai_astro_api.models.v1_create_mount_request import V1CreateMountRequest
from ourskyai_astro_api.models.v1_create_node_request import V1CreateNodeRequest
from ourskyai_astro_api.models.v1_create_optical_tube_request import V1CreateOpticalTubeRequest
from ourskyai_astro_api.models.v1_elevation_mask_point import V1ElevationMaskPoint
from ourskyai_astro_api.models.v1_gain_curve import V1GainCurve
from ourskyai_astro_api.models.v1_gain_curve_point import V1GainCurvePoint
from ourskyai_astro_api.models.v1_get_astro_platform_credit_balance_response import V1GetAstroPlatformCreditBalanceResponse
from ourskyai_astro_api.models.v1_get_nodes import V1GetNodes
from ourskyai_astro_api.models.v1_get_or_create_camera_request import V1GetOrCreateCameraRequest
from ourskyai_astro_api.models.v1_get_or_create_mount_request import V1GetOrCreateMountRequest
from ourskyai_astro_api.models.v1_get_or_create_optical_tube_request import V1GetOrCreateOpticalTubeRequest
from ourskyai_astro_api.models.v1_image_set import V1ImageSet
from ourskyai_astro_api.models.v1_image_set_image import V1ImageSetImage
from ourskyai_astro_api.models.v1_job_kind import V1JobKind
from ourskyai_astro_api.models.v1_job_log import V1JobLog
from ourskyai_astro_api.models.v1_job_status import V1JobStatus
from ourskyai_astro_api.models.v1_mount import V1Mount
from ourskyai_astro_api.models.v1_node import V1Node
from ourskyai_astro_api.models.v1_node_with_location import V1NodeWithLocation
from ourskyai_astro_api.models.v1_optical_tube import V1OpticalTube
from ourskyai_astro_api.models.v1_platform_credit import V1PlatformCredit
from ourskyai_astro_api.models.v1_platform_credit_source import V1PlatformCreditSource
from ourskyai_astro_api.models.v1_platform_credit_type import V1PlatformCreditType
from ourskyai_astro_api.models.v1_platform_credit_unit import V1PlatformCreditUnit
from ourskyai_astro_api.models.v1_predicted_streak_location import V1PredictedStreakLocation
from ourskyai_astro_api.models.v1_put_stack_astro_project_request import V1PutStackAstroProjectRequest
from ourskyai_astro_api.models.v1_put_stack_astro_project_response import V1PutStackAstroProjectResponse
from ourskyai_astro_api.models.v1_read_noise_point import V1ReadNoisePoint
from ourskyai_astro_api.models.v1_setup_action import V1SetupAction
from ourskyai_astro_api.models.v1_slew_timing import V1SlewTiming
from ourskyai_astro_api.models.v1_slew_timing_interval import V1SlewTimingInterval
from ourskyai_astro_api.models.v1_update_node_request import V1UpdateNodeRequest
from ourskyai_astro_api.models.v1_video_mode_framerate_property import V1VideoModeFramerateProperty
