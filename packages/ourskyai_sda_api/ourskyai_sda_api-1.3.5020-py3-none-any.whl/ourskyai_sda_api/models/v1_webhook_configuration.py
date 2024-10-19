# coding: utf-8

"""
    OurSky SDA

    The basic flow for a new organization is as follows: 1. View the available satellite targets with the [satellite targets](https://api.prod.oursky.ai/docs/sda#tag/satellite-targets/get/v1/satellite-targets) endpoint. Copy the id of the target you want to observe. 2. Create an organization target with the [organization target](https://api.prod.oursky.ai/docs/sda#tag/organization-targets/get/v1/organization-targets) endpoint. Use the id copied from above. 3. Create a webhook with the [webhook](https://api.prod.oursky.ai/docs/sda#tag/webhooks/post/v1/communications/webhook) endpoint to receive TDMs automatically (preferred) or use the [tdms](https://api.prod.oursky.ai/docs/sda#tag/tdms/get/v1/tdms) endpoint to poll for TDMs.  Check out our [examples](https://github.com/ourskyai/oursky-examples) repository to see usage in each language.

    The version of the OpenAPI document: 1.3.5020
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from ourskyai_sda_api.models.webhook_event import WebhookEvent

class V1WebhookConfiguration(BaseModel):
    """
    V1WebhookConfiguration
    """
    id: StrictStr = Field(...)
    url: StrictStr = Field(...)
    failure_count: StrictInt = Field(..., alias="failureCount")
    last_failure_at: Optional[datetime] = Field(None, alias="lastFailureAt")
    disabled_at: Optional[datetime] = Field(None, alias="disabledAt")
    events: conlist(WebhookEvent) = Field(...)
    created_by: StrictStr = Field(..., alias="createdBy")
    created_at: datetime = Field(..., alias="createdAt")
    __properties = ["id", "url", "failureCount", "lastFailureAt", "disabledAt", "events", "createdBy", "createdAt"]

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
    def from_json(cls, json_str: str) -> V1WebhookConfiguration:
        """Create an instance of V1WebhookConfiguration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1WebhookConfiguration:
        """Create an instance of V1WebhookConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1WebhookConfiguration.parse_obj(obj)

        _obj = V1WebhookConfiguration.parse_obj({
            "id": obj.get("id"),
            "url": obj.get("url"),
            "failure_count": obj.get("failureCount"),
            "last_failure_at": obj.get("lastFailureAt"),
            "disabled_at": obj.get("disabledAt"),
            "events": obj.get("events"),
            "created_by": obj.get("createdBy"),
            "created_at": obj.get("createdAt")
        })
        return _obj


