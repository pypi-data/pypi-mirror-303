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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from guardrails_api_client.models.validation_type import ValidationType
from typing import Set
from typing_extensions import Self

class Validation(BaseModel):
    """
    Validation
    """ # noqa: E501
    multiple_of: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="multipleOf")
    maximum: Optional[Union[StrictFloat, StrictInt]] = None
    exclusive_maximum: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="exclusiveMaximum")
    minimum: Optional[Union[StrictFloat, StrictInt]] = None
    exclusive_minimum: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="exclusiveMinimum")
    max_length: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="maxLength")
    min_length: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="minLength")
    pattern: Optional[str] = None
    max_items: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="maxItems")
    min_items: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="minItems")
    unique_items: Optional[bool] = Field(default=False, alias="uniqueItems")
    max_contains: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="maxContains")
    min_contains: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="minContains")
    max_properties: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="maxProperties")
    min_properties: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="minProperties")
    required: Optional[List[str]] = None
    dependent_required: Optional[Dict[str, List[str]]] = Field(default=None, alias="dependentRequired")
    const: Optional[Any] = None
    enum: Optional[List[Any]] = None
    type: Optional[ValidationType] = None
    __properties: ClassVar[List[str]] = ["multipleOf", "maximum", "exclusiveMaximum", "minimum", "exclusiveMinimum", "maxLength", "minLength", "pattern", "maxItems", "minItems", "uniqueItems", "maxContains", "minContains", "maxProperties", "minProperties", "required", "dependentRequired", "const", "enum", "type"]

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
        """Create an instance of Validation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        # set to None if const (nullable) is None
        # and model_fields_set contains the field
        if self.const is None and "const" in self.model_fields_set:
            _dict['const'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Validation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "multipleOf": obj.get("multipleOf"),
            "maximum": obj.get("maximum"),
            "exclusiveMaximum": obj.get("exclusiveMaximum"),
            "minimum": obj.get("minimum"),
            "exclusiveMinimum": obj.get("exclusiveMinimum"),
            "maxLength": obj.get("maxLength"),
            "minLength": obj.get("minLength"),
            "pattern": obj.get("pattern"),
            "maxItems": obj.get("maxItems"),
            "minItems": obj.get("minItems"),
            "uniqueItems": obj.get("uniqueItems") if obj.get("uniqueItems") is not None else False,
            "maxContains": obj.get("maxContains"),
            "minContains": obj.get("minContains"),
            "maxProperties": obj.get("maxProperties"),
            "minProperties": obj.get("minProperties"),
            "required": obj.get("required"),
            "const": obj.get("const"),
            "enum": obj.get("enum"),
            "type": ValidationType.from_dict(obj["type"]) if obj.get("type") is not None else None
        })
        return _obj


