# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .node_item_param import NodeItemParam

__all__ = ["WorkflowConfigParam"]


class WorkflowConfigParam(TypedDict, total=False):
    workflow: Required[Iterable[NodeItemParam]]

    id: str

    account_id: str

    application_variant_id: str

    base_url: str

    concurrency_default: bool

    datasets: Iterable[object]

    egp_api_key_override: str

    egp_ui_evaluation: object

    evaluations: Iterable[NodeItemParam]

    final_output_nodes: List[str]

    nodes_to_log: Union[str, List[str]]

    num_workers: int

    streaming_nodes: List[str]

    type: Literal["workflow", "plan", "state_machine"]
    """An enumeration."""
