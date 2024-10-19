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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from guardrails_api_client.models.validation_type import ValidationType
from typing import Set
from typing_extensions import Self

class ModelSchema(BaseModel):
    """
    ModelSchema
    """ # noqa: E501
    definitions: Optional[Dict[str, Any]] = None
    dependencies: Optional[Dict[str, Any]] = None
    anchor: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="$anchor")
    ref: Optional[str] = Field(default=None, alias="$ref")
    dynamic_ref: Optional[str] = Field(default=None, alias="$dynamicRef")
    dynamic_anchor: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="$dynamicAnchor")
    vocabulary: Optional[Dict[str, Any]] = Field(default=None, alias="$vocabulary")
    comment: Optional[str] = Field(default=None, alias="$comment")
    defs: Optional[Dict[str, Any]] = Field(default=None, alias="$defs")
    prefix_items: Optional[Annotated[List[Any], Field(min_length=1)]] = Field(default=None, alias="prefixItems")
    items: Optional[Any] = None
    contains: Optional[Any] = None
    additional_properties: Optional[Any] = Field(default=None, alias="additionalProperties")
    properties: Optional[Dict[str, Any]] = None
    pattern_properties: Optional[Dict[str, Any]] = Field(default=None, alias="patternProperties")
    dependent_schemas: Optional[Dict[str, Any]] = Field(default=None, alias="dependentSchemas")
    property_names: Optional[Any] = Field(default=None, alias="propertyNames")
    var_if: Optional[Any] = Field(default=None, alias="if")
    then: Optional[Any] = None
    var_else: Optional[Any] = Field(default=None, alias="else")
    all_of: Optional[Annotated[List[Any], Field(min_length=1)]] = Field(default=None, alias="allOf")
    any_of: Optional[Annotated[List[Any], Field(min_length=1)]] = Field(default=None, alias="anyOf")
    one_of: Optional[Annotated[List[Any], Field(min_length=1)]] = Field(default=None, alias="oneOf")
    var_not: Optional[Any] = Field(default=None, alias="not")
    unevaluated_items: Optional[Any] = Field(default=None, alias="unevaluatedItems")
    unevaluated_properties: Optional[Any] = Field(default=None, alias="unevaluatedProperties")
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
    unique_items: Optional[bool] = Field(default=None, alias="uniqueItems")
    max_contains: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="maxContains")
    min_contains: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="minContains")
    max_properties: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="maxProperties")
    min_properties: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="minProperties")
    required: Optional[List[Any]] = None
    dependent_required: Optional[Dict[str, List[str]]] = Field(default=None, alias="dependentRequired")
    const: Optional[Any] = None
    enum: Optional[List[Any]] = None
    type: Optional[ValidationType] = None
    title: Optional[str] = None
    description: Optional[str] = None
    default: Optional[Any] = None
    deprecated: Optional[bool] = None
    read_only: Optional[bool] = Field(default=None, alias="readOnly")
    write_only: Optional[bool] = Field(default=None, alias="writeOnly")
    examples: Optional[List[Any]] = None
    format: Optional[str] = None
    content_media_type: Optional[str] = Field(default=None, alias="contentMediaType")
    content_encoding: Optional[str] = Field(default=None, alias="contentEncoding")
    content_schema: Optional[Any] = Field(default=None, alias="contentSchema")
    __properties: ClassVar[List[str]] = ["$anchor", "$ref", "$dynamicRef", "$dynamicAnchor", "$vocabulary", "$comment", "$defs", "prefixItems", "items", "contains", "additionalProperties", "properties", "patternProperties", "dependentSchemas", "propertyNames", "if", "then", "else", "allOf", "anyOf", "oneOf", "not", "unevaluatedItems", "unevaluatedProperties", "multipleOf", "maximum", "exclusiveMaximum", "minimum", "exclusiveMinimum", "maxLength", "minLength", "pattern", "maxItems", "minItems", "uniqueItems", "maxContains", "minContains", "maxProperties", "minProperties", "required", "dependentRequired", "const", "enum", "type", "title", "description", "default", "deprecated", "readOnly", "writeOnly", "examples", "format", "contentMediaType", "contentEncoding", "contentSchema"]

    @field_validator('anchor')
    def anchor_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[A-Za-z_][-A-Za-z0-9._]*$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z_][-A-Za-z0-9._]*$/")
        return value

    @field_validator('dynamic_anchor')
    def dynamic_anchor_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[A-Za-z_][-A-Za-z0-9._]*$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z_][-A-Za-z0-9._]*$/")
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
        """Create an instance of ModelSchema from a JSON string"""
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
        # set to None if items (nullable) is None
        # and model_fields_set contains the field
        if self.items is None and "items" in self.model_fields_set:
            _dict['items'] = None

        # set to None if contains (nullable) is None
        # and model_fields_set contains the field
        if self.contains is None and "contains" in self.model_fields_set:
            _dict['contains'] = None

        # set to None if additional_properties (nullable) is None
        # and model_fields_set contains the field
        if self.additional_properties is None and "additional_properties" in self.model_fields_set:
            _dict['additionalProperties'] = None

        # set to None if property_names (nullable) is None
        # and model_fields_set contains the field
        if self.property_names is None and "property_names" in self.model_fields_set:
            _dict['propertyNames'] = None

        # set to None if var_if (nullable) is None
        # and model_fields_set contains the field
        if self.var_if is None and "var_if" in self.model_fields_set:
            _dict['if'] = None

        # set to None if then (nullable) is None
        # and model_fields_set contains the field
        if self.then is None and "then" in self.model_fields_set:
            _dict['then'] = None

        # set to None if var_else (nullable) is None
        # and model_fields_set contains the field
        if self.var_else is None and "var_else" in self.model_fields_set:
            _dict['else'] = None

        # set to None if var_not (nullable) is None
        # and model_fields_set contains the field
        if self.var_not is None and "var_not" in self.model_fields_set:
            _dict['not'] = None

        # set to None if unevaluated_items (nullable) is None
        # and model_fields_set contains the field
        if self.unevaluated_items is None and "unevaluated_items" in self.model_fields_set:
            _dict['unevaluatedItems'] = None

        # set to None if unevaluated_properties (nullable) is None
        # and model_fields_set contains the field
        if self.unevaluated_properties is None and "unevaluated_properties" in self.model_fields_set:
            _dict['unevaluatedProperties'] = None

        # set to None if const (nullable) is None
        # and model_fields_set contains the field
        if self.const is None and "const" in self.model_fields_set:
            _dict['const'] = None

        # set to None if default (nullable) is None
        # and model_fields_set contains the field
        if self.default is None and "default" in self.model_fields_set:
            _dict['default'] = None

        # set to None if content_schema (nullable) is None
        # and model_fields_set contains the field
        if self.content_schema is None and "content_schema" in self.model_fields_set:
            _dict['contentSchema'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModelSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
			**obj,
            "$anchor": obj.get("$anchor"),
            "$ref": obj.get("$ref"),
            "$dynamicRef": obj.get("$dynamicRef"),
            "$dynamicAnchor": obj.get("$dynamicAnchor"),
            "$comment": obj.get("$comment"),
            "prefixItems": obj.get("prefixItems"),
            "items": obj.get("items"),
            "contains": obj.get("contains"),
            "additionalProperties": obj.get("additionalProperties"),
            "propertyNames": obj.get("propertyNames"),
            "if": obj.get("if"),
            "then": obj.get("then"),
            "else": obj.get("else"),
            "allOf": obj.get("allOf"),
            "anyOf": obj.get("anyOf"),
            "oneOf": obj.get("oneOf"),
            "not": obj.get("not"),
            "unevaluatedItems": obj.get("unevaluatedItems"),
            "unevaluatedProperties": obj.get("unevaluatedProperties"),
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
            "uniqueItems": obj.get("uniqueItems"),
            "maxContains": obj.get("maxContains"),
            "minContains": obj.get("minContains"),
            "maxProperties": obj.get("maxProperties"),
            "minProperties": obj.get("minProperties"),
            "required": obj.get("required"),
            "const": obj.get("const"),
            "enum": obj.get("enum"),
            "type": ValidationType.from_dict(obj["type"]) if obj.get("type") is not None else None,
            "title": obj.get("title"),
            "description": obj.get("description"),
            "default": obj.get("default"),
            "deprecated": obj.get("deprecated"),
            "readOnly": obj.get("readOnly"),
            "writeOnly": obj.get("writeOnly"),
            "examples": obj.get("examples"),
            "format": obj.get("format"),
            "contentMediaType": obj.get("contentMediaType"),
            "contentEncoding": obj.get("contentEncoding"),
            "contentSchema": obj.get("contentSchema")
        })
        return _obj


