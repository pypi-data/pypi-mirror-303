# coding: utf-8

"""
    Guardrails API

    Guardrails CRUD API

    The version of the OpenAPI document: 0.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from guardrails_api_client.models.llm_response import LLMResponse
from guardrails_api_client.models.outputs_parsed_output import OutputsParsedOutput
from guardrails_api_client.models.outputs_validation_response import OutputsValidationResponse
from guardrails_api_client.models.reask import Reask
from guardrails_api_client.models.validator_log import ValidatorLog
from typing import Set
from typing_extensions import Self

class Outputs(BaseModel):
    """
    Outputs
    """ # noqa: E501
    llm_response_info: Optional[LLMResponse] = Field(default=None, alias="llmResponseInfo")
    raw_output: Optional[str] = Field(default=None, description="The string content from the LLM response.", alias="rawOutput")
    parsed_output: Optional[OutputsParsedOutput] = Field(default=None, alias="parsedOutput")
    validation_response: Optional[OutputsValidationResponse] = Field(default=None, alias="validationResponse")
    guarded_output: Optional[OutputsParsedOutput] = Field(default=None, alias="guardedOutput")
    reasks: Optional[List[Reask]] = None
    validator_logs: Optional[List[ValidatorLog]] = Field(default=None, alias="validatorLogs")
    error: Optional[str] = Field(default=None, description="The error message from any exception which interrupted the Guard execution process.")
    __properties: ClassVar[List[str]] = ["llmResponseInfo", "rawOutput", "parsedOutput", "validationResponse", "guardedOutput", "reasks", "validatorLogs", "error"]

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
        """Create an instance of Outputs from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of llm_response_info
        if self.llm_response_info:
            _dict['llmResponseInfo'] = self.llm_response_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parsed_output
        if self.parsed_output:
            _dict['parsedOutput'] = self.parsed_output.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validation_response
        if self.validation_response:
            _dict['validationResponse'] = self.validation_response.to_dict()
        # override the default output from pydantic by calling `to_dict()` of guarded_output
        if self.guarded_output:
            _dict['guardedOutput'] = self.guarded_output.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in reasks (list)
        _items = []
        if self.reasks:
            for _item in self.reasks:
                if _item:
                    _items.append(_item.to_dict() if hasattr(_item, "to_dict") and callable(_item.to_dict) else _item)
            _dict['reasks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in validator_logs (list)
        _items = []
        if self.validator_logs:
            for _item in self.validator_logs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['validatorLogs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Outputs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "llmResponseInfo": LLMResponse.from_dict(obj["llmResponseInfo"]) if obj.get("llmResponseInfo") is not None else None,
            "rawOutput": obj.get("rawOutput"),
            "parsedOutput": OutputsParsedOutput.from_dict(obj["parsedOutput"]) if obj.get("parsedOutput") is not None else None,
            "validationResponse": OutputsValidationResponse.from_dict(obj["validationResponse"]) if obj.get("validationResponse") is not None else None,
            "guardedOutput": OutputsParsedOutput.from_dict(obj["guardedOutput"]) if obj.get("guardedOutput") is not None else None,
            "reasks": [Reask.from_dict(_item) for _item in obj["reasks"]] if obj.get("reasks") is not None else None,
            "validatorLogs": [ValidatorLog.from_dict(_item) for _item in obj["validatorLogs"]] if obj.get("validatorLogs") is not None else None,
            "error": obj.get("error")
        })
        return _obj


