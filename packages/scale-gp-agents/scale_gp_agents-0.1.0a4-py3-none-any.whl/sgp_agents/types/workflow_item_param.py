# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WorkflowItemParam"]


class WorkflowItemParam(TypedDict, total=False):
    workflow_name: Required[str]

    request_user_input: Literal["never", "maybe", "always"]
    """
    If always: available the first time: request missing the first time: request
    available the next time: continue missing the next time: request (treat like
    need_based) If need_based: available the first time: continue missing the first
    time: request available the next time: continue missing the next time: request
    (treat like the first time) If never: available the first time: continue missing
    the first time: raise Exception available the next time: continue missing the
    next time: raise Exception
    """

    workflow_alias: Optional[str]

    workflow_inputs: Optional[Dict[str, Union[str, Dict[str, Union[str, object]]]]]

    workflow_save_outputs: Optional[Dict[str, str]]
