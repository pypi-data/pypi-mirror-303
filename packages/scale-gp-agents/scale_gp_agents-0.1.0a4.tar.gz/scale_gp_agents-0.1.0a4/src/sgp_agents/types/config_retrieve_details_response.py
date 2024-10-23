# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ConfigRetrieveDetailsResponse", "Edge", "Input", "Node"]


class Edge(BaseModel):
    from_node: str

    to_node: str


class Input(BaseModel):
    name: str

    type: str


class Node(BaseModel):
    id: str

    config: object

    name: str

    type: str


class ConfigRetrieveDetailsResponse(BaseModel):
    edges: List[Edge]

    inputs: List[Input]

    nodes: List[Node]
