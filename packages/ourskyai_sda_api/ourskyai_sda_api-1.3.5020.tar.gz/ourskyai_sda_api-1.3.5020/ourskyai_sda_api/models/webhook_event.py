# coding: utf-8

"""
    OurSky SDA

    The basic flow for a new organization is as follows: 1. View the available satellite targets with the [satellite targets](https://api.prod.oursky.ai/docs/sda#tag/satellite-targets/get/v1/satellite-targets) endpoint. Copy the id of the target you want to observe. 2. Create an organization target with the [organization target](https://api.prod.oursky.ai/docs/sda#tag/organization-targets/get/v1/organization-targets) endpoint. Use the id copied from above. 3. Create a webhook with the [webhook](https://api.prod.oursky.ai/docs/sda#tag/webhooks/post/v1/communications/webhook) endpoint to receive TDMs automatically (preferred) or use the [tdms](https://api.prod.oursky.ai/docs/sda#tag/tdms/get/v1/tdms) endpoint to poll for TDMs.  Check out our [examples](https://github.com/ourskyai/oursky-examples) repository to see usage in each language.

    The version of the OpenAPI document: 1.3.5020
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class WebhookEvent(str, Enum):
    """
    Webhook events that can be subscribed to. For `EO_OBSERVATION` events, please refer to the Unified Data Library for the full schema.
    """

    """
    allowed enum values
    """
    V1_TDM_CREATED = 'V1_TDM_CREATED'
    V1_OBSERVATION_SEQUENCE_RESULT_CREATED = 'V1_OBSERVATION_SEQUENCE_RESULT_CREATED'
    V1_OBSERVATION_CREATED = 'V1_OBSERVATION_CREATED'
    V1_IMAGE_CREATED = 'V1_IMAGE_CREATED'
    V1_STREAK_CREATED = 'V1_STREAK_CREATED'
    V1_SATELLITE_TARGET_TRACKING_DEACTIVATED = 'V1_SATELLITE_TARGET_TRACKING_DEACTIVATED'
    V1_EO_OBSERVATION_CREATED = 'V1_EO_OBSERVATION_CREATED'
    V1_OBSERVATION_STATUS_UPDATED = 'V1_OBSERVATION_STATUS_UPDATED'
    V1_EO_CALIBRATION_OBSERVATION_CREATED = 'V1_EO_CALIBRATION_OBSERVATION_CREATED'
    V1_NODE_CALIBRATION_DATA_CREATED = 'V1_NODE_CALIBRATION_DATA_CREATED'

    @classmethod
    def from_json(cls, json_str: str) -> WebhookEvent:
        """Create an instance of WebhookEvent from a JSON string"""
        return WebhookEvent(json.loads(json_str))


