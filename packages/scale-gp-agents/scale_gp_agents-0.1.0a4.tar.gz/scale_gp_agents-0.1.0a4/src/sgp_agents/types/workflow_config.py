# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .node_item import NodeItem

__all__ = ["WorkflowConfig"]


class WorkflowConfig(BaseModel):
    workflow: List[NodeItem]

    id: Optional[str] = None

    account_id: Optional[str] = None

    application_variant_id: Optional[str] = None

    base_url: Optional[str] = None

    concurrency_default: Optional[bool] = None

    datasets: Optional[List[object]] = None

    egp_api_key_override: Optional[str] = None

    egp_ui_evaluation: Optional[object] = None

    evaluations: Optional[List[NodeItem]] = None

    final_output_nodes: Optional[List[str]] = None

    nodes_to_log: Union[str, List[str], None] = None

    num_workers: Optional[int] = None

    streaming_nodes: Optional[List[str]] = None

    type: Optional[Literal["workflow", "plan", "state_machine"]] = None
    """An enumeration."""
