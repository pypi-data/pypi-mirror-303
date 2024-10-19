# coding: utf-8

"""
    Skyfire API

    The Skyfire SDK is designed to allow agents to interact with the Skyfire platform to enable autonomous payments.

    The version of the OpenAPI document: 1.0.0
    Contact: support@skyfire.xyz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class APINinjaIPLookupResponse(BaseModel):
    """
    Represents the response from an IP Lookup request.
    """ # noqa: E501
    address: StrictStr = Field(description="The IP address of the query.")
    timezone: StrictStr = Field(description="The time zone related to the IP address.")
    region: StrictStr = Field(description="The region name where the IP address is located. In the United States, this is equivalent to the state.")
    region_code: StrictStr = Field(description="The region code of the IP address location. In the United States, this is equivalent to the 2-letter state abbreviation.")
    country: StrictStr = Field(description="The name of the country where the IP address is located.")
    country_code: StrictStr = Field(description="The 2-letter country code of the IP address location.")
    is_valid: StrictBool = Field(description="The validity status of the IP address.")
    __properties: ClassVar[List[str]] = ["address", "timezone", "region", "region_code", "country", "country_code", "is_valid"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of APINinjaIPLookupResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of APINinjaIPLookupResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "timezone": obj.get("timezone"),
            "region": obj.get("region"),
            "region_code": obj.get("region_code"),
            "country": obj.get("country"),
            "country_code": obj.get("country_code"),
            "is_valid": obj.get("is_valid")
        })
        return _obj


