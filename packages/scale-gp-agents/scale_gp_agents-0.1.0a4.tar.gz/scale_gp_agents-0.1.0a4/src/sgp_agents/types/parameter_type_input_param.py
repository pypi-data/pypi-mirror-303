# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["ParameterTypeInputParam", "AdditionalProperties", "AnyOf", "Items"]

AdditionalProperties: TypeAlias = Union[
    Literal["object", "array"], Literal["string", "number", "integer", "boolean", "null"], "ParameterTypeInputParam"
]

AnyOf: TypeAlias = Union[
    Literal["object", "array"], Literal["string", "number", "integer", "boolean", "null"], "ParameterTypeInputParam"
]

Items: TypeAlias = Union[
    Literal["object", "array"], Literal["string", "number", "integer", "boolean", "null"], "ParameterTypeInputParam"
]


class ParameterTypeInputParam(TypedDict, total=False):
    additional_properties: Annotated[Optional[AdditionalProperties], PropertyInfo(alias="additionalProperties")]

    any_of: Annotated[Optional[Iterable[AnyOf]], PropertyInfo(alias="anyOf")]

    description: Optional[str]

    items: Optional[Items]

    property_names: Annotated[
        Union[
            Literal["string", "number", "integer", "boolean", "null"],
            List[Literal["string", "number", "integer", "boolean", "null"]],
            None,
        ],
        PropertyInfo(alias="propertyNames"),
    ]

    type: Union[
        Literal["object", "array"],
        Literal["string", "number", "integer", "boolean", "null"],
        List[Literal["object", "array", "string", "number", "integer", "boolean", "null"]],
        None,
    ]
