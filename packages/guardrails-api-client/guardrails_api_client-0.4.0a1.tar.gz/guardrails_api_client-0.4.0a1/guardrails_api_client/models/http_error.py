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
from typing import Set
from typing_extensions import Self

class HttpError(BaseModel):
    """
    HttpError
    """ # noqa: E501
    status: int = Field(description="A valid http status code")
    message: str = Field(description="A message explaining the status")
    cause: Optional[str] = Field(default=None, description="Used to describe the origin of an error if that original error has meaning to the client.  This field should add specificity to 'message'.")
    fields: Optional[Dict[str, List[str]]] = Field(default=None, description="Used to identify specific fields in a JSON body that caused the error.  Typically only used for 4xx type responses.  The key should be the json path to the invalid property and the value should be a list of error messages specific to that property.")
    context: Optional[str] = Field(default=None, description="Used to identify what part of the request caused the error for non-JSON payloads.")
    __properties: ClassVar[List[str]] = ["status", "message", "cause", "fields", "context"]

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
        """Create an instance of HttpError from a JSON string"""
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
        """Create an instance of HttpError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "message": obj.get("message"),
            "cause": obj.get("cause"),
            "context": obj.get("context")
        })
        return _obj


