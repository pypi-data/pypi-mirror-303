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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class BalanceSheet(BaseModel):
    """
    BalanceSheet
    """ # noqa: E501
    ticker: Optional[StrictStr] = Field(default=None, description="The ticker symbol.")
    calendar_date: Optional[date] = Field(default=None, description="The date of the balance sheet.")
    report_period: Optional[date] = Field(default=None, description="The reporting period of the balance sheet.")
    period: Optional[StrictStr] = Field(default=None, description="The time period of the balance sheet.")
    total_assets: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total assets of the company.")
    current_assets: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The current assets of the company.")
    cash_and_equivalents: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The cash and equivalents of the company.")
    inventory: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The inventory of the company.")
    current_investments: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The current investments of the company.")
    trade_and_non_trade_receivables: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The trade and non-trade receivables of the company.")
    non_current_assets: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The non-current assets of the company.")
    property_plant_and_equipment: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The property, plant, and equipment of the company.")
    goodwill_and_intangible_assets: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The goodwill and intangible assets of the company.")
    investments: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The investments of the company.")
    non_current_investments: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The non-current investments of the company.")
    tax_assets: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The tax assets of the company.")
    total_liabilities: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total liabilities of the company.")
    current_liabilities: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The current liabilities of the company.")
    current_debt: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The current debt of the company.")
    trade_and_non_trade_payables: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The trade and non-trade payables of the company.")
    deferred_revenue: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The deferred revenue of the company.")
    deposit_liabilities: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The deposit liabilities of the company.")
    non_current_liabilities: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The non-current liabilities of the company.")
    non_current_debt: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The non-current debt of the company.")
    tax_liabilities: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The tax liabilities of the company.")
    shareholders_equity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The shareholders' equity of the company.")
    retained_earnings: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The retained earnings of the company.")
    accumulated_other_comprehensive_income: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The accumulated other comprehensive income of the company.")
    total_debt: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total debt of the company.")
    __properties: ClassVar[List[str]] = ["ticker", "calendar_date", "report_period", "period", "total_assets", "current_assets", "cash_and_equivalents", "inventory", "current_investments", "trade_and_non_trade_receivables", "non_current_assets", "property_plant_and_equipment", "goodwill_and_intangible_assets", "investments", "non_current_investments", "tax_assets", "total_liabilities", "current_liabilities", "current_debt", "trade_and_non_trade_payables", "deferred_revenue", "deposit_liabilities", "non_current_liabilities", "non_current_debt", "tax_liabilities", "shareholders_equity", "retained_earnings", "accumulated_other_comprehensive_income", "total_debt"]

    @field_validator('period')
    def period_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['quarterly', 'ttm', 'annual']):
            raise ValueError("must be one of enum values ('quarterly', 'ttm', 'annual')")
        return value

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
        """Create an instance of BalanceSheet from a JSON string"""
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
        """Create an instance of BalanceSheet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ticker": obj.get("ticker"),
            "calendar_date": obj.get("calendar_date"),
            "report_period": obj.get("report_period"),
            "period": obj.get("period"),
            "total_assets": obj.get("total_assets"),
            "current_assets": obj.get("current_assets"),
            "cash_and_equivalents": obj.get("cash_and_equivalents"),
            "inventory": obj.get("inventory"),
            "current_investments": obj.get("current_investments"),
            "trade_and_non_trade_receivables": obj.get("trade_and_non_trade_receivables"),
            "non_current_assets": obj.get("non_current_assets"),
            "property_plant_and_equipment": obj.get("property_plant_and_equipment"),
            "goodwill_and_intangible_assets": obj.get("goodwill_and_intangible_assets"),
            "investments": obj.get("investments"),
            "non_current_investments": obj.get("non_current_investments"),
            "tax_assets": obj.get("tax_assets"),
            "total_liabilities": obj.get("total_liabilities"),
            "current_liabilities": obj.get("current_liabilities"),
            "current_debt": obj.get("current_debt"),
            "trade_and_non_trade_payables": obj.get("trade_and_non_trade_payables"),
            "deferred_revenue": obj.get("deferred_revenue"),
            "deposit_liabilities": obj.get("deposit_liabilities"),
            "non_current_liabilities": obj.get("non_current_liabilities"),
            "non_current_debt": obj.get("non_current_debt"),
            "tax_liabilities": obj.get("tax_liabilities"),
            "shareholders_equity": obj.get("shareholders_equity"),
            "retained_earnings": obj.get("retained_earnings"),
            "accumulated_other_comprehensive_income": obj.get("accumulated_other_comprehensive_income"),
            "total_debt": obj.get("total_debt")
        })
        return _obj


