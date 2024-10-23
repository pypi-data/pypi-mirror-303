# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["ParameterTypeOutput", "AdditionalProperties", "AnyOf", "Items"]

AdditionalProperties: TypeAlias = Union[
    Literal["object", "array"], Literal["string", "number", "integer", "boolean", "null"], "ParameterTypeOutput", None
]

AnyOf: TypeAlias = Union[
    Literal["object", "array"], Literal["string", "number", "integer", "boolean", "null"], "ParameterTypeOutput"
]

Items: TypeAlias = Union[
    Literal["object", "array"], Literal["string", "number", "integer", "boolean", "null"], "ParameterTypeOutput", None
]


class ParameterTypeOutput(BaseModel):
    additional_properties: Optional[AdditionalProperties] = FieldInfo(alias="additionalProperties", default=None)

    any_of: Optional[List[AnyOf]] = FieldInfo(alias="anyOf", default=None)

    description: Optional[str] = None

    items: Optional[Items] = None

    property_names: Union[
        Literal["string", "number", "integer", "boolean", "null"],
        List[Literal["string", "number", "integer", "boolean", "null"]],
        None,
    ] = FieldInfo(alias="propertyNames", default=None)

    type: Union[
        Literal["object", "array"],
        Literal["string", "number", "integer", "boolean", "null"],
        List[Literal["object", "array", "string", "number", "integer", "boolean", "null"]],
        None,
    ] = None


if PYDANTIC_V2:
    ParameterTypeOutput.model_rebuild()
else:
    ParameterTypeOutput.update_forward_refs()  # type: ignore
