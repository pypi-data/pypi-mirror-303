# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .node_item_param import NodeItemParam

__all__ = [
    "PlanConfigParam",
    "Plan",
    "PlanWorkflowItem",
    "PlanBranchConfig",
    "PlanBranchConfigConditionalWorkflow",
    "PlanBranchConfigConditionalWorkflowConditionTree",
    "PlanBranchConfigConditionalWorkflowConditionTreeCondition",
    "PlanBranchConfigConditionalWorkflowConditionTreeConditionUnaryCondition",
    "PlanBranchConfigConditionalWorkflowConditionTreeConditionCompoundCondition",
    "PlanBranchConfigConditionalWorkflowConditionTreeConditionCompoundConditionCondition",
    "PlanBranchConfigConditionalWorkflowConditionTreeConditionCompoundConditionConditionUnaryCondition",
    "PlanLoopConfig",
    "PlanLoopConfigCondition",
    "PlanLoopConfigConditionCondition",
    "PlanLoopConfigConditionConditionUnaryCondition",
    "PlanLoopConfigConditionConditionCompoundCondition",
    "PlanLoopConfigConditionConditionCompoundConditionCondition",
    "PlanLoopConfigConditionConditionCompoundConditionConditionUnaryCondition",
    "PlanLoopConfigWorkflow",
    "PlanLoopConfigLoopInputs",
    "PlanLoopConfigLoopInputsSelfEdge",
    "Workflows",
    "WorkflowsWorkflow",
]


class PlanWorkflowItem(TypedDict, total=False):
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

    workflow_alias: str

    workflow_inputs: Dict[str, Union[str, Dict[str, Union[str, object]]]]

    workflow_save_outputs: Dict[str, str]


class PlanBranchConfigConditionalWorkflowConditionTreeConditionUnaryCondition(TypedDict, total=False):
    condition_input_var: Required[str]

    operator: Required[str]

    reference_var: object


class PlanBranchConfigConditionalWorkflowConditionTreeConditionCompoundConditionConditionUnaryCondition(
    TypedDict, total=False
):
    condition_input_var: Required[str]

    operator: Required[str]

    reference_var: object


PlanBranchConfigConditionalWorkflowConditionTreeConditionCompoundConditionCondition: TypeAlias = Union[
    PlanBranchConfigConditionalWorkflowConditionTreeConditionCompoundConditionConditionUnaryCondition, object
]


class PlanBranchConfigConditionalWorkflowConditionTreeConditionCompoundCondition(TypedDict, total=False):
    conditions: Iterable[PlanBranchConfigConditionalWorkflowConditionTreeConditionCompoundConditionCondition]

    input_names: List[str]

    logical_operator: Literal["ALL", "ANY", "NOT"]


PlanBranchConfigConditionalWorkflowConditionTreeCondition: TypeAlias = Union[
    PlanBranchConfigConditionalWorkflowConditionTreeConditionUnaryCondition,
    PlanBranchConfigConditionalWorkflowConditionTreeConditionCompoundCondition,
]


class PlanBranchConfigConditionalWorkflowConditionTree(TypedDict, total=False):
    conditions: Iterable[PlanBranchConfigConditionalWorkflowConditionTreeCondition]

    input_names: List[str]

    logical_operator: Literal["ALL", "ANY", "NOT"]


class PlanBranchConfigConditionalWorkflow(TypedDict, total=False):
    condition: Required[Literal["if", "elif", "else"]]

    workflow_name: Required[str]

    condition_input_var: str

    condition_tree: PlanBranchConfigConditionalWorkflowConditionTree
    """Representation of a compound boolean statement, i.e.

    a negation, conjunction, or disjunction of UnaryConditions
    """

    operator: str

    reference_var: str

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

    workflow_alias: str

    workflow_inputs: Dict[str, Union[str, Dict[str, Union[str, object]]]]

    workflow_nodes: List[str]

    workflow_save_outputs: Dict[str, str]


class PlanBranchConfig(TypedDict, total=False):
    branch: Required[str]

    conditional_workflows: Required[Iterable[PlanBranchConfigConditionalWorkflow]]

    merge_outputs: Dict[str, List[str]]

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

    save_merge_to_memory: Dict[str, str]


class PlanLoopConfigConditionConditionUnaryCondition(TypedDict, total=False):
    condition_input_var: Required[str]

    operator: Required[str]

    reference_var: object


class PlanLoopConfigConditionConditionCompoundConditionConditionUnaryCondition(TypedDict, total=False):
    condition_input_var: Required[str]

    operator: Required[str]

    reference_var: object


PlanLoopConfigConditionConditionCompoundConditionCondition: TypeAlias = Union[
    PlanLoopConfigConditionConditionCompoundConditionConditionUnaryCondition, object
]


class PlanLoopConfigConditionConditionCompoundCondition(TypedDict, total=False):
    conditions: Iterable[PlanLoopConfigConditionConditionCompoundConditionCondition]

    input_names: List[str]

    logical_operator: Literal["ALL", "ANY", "NOT"]


PlanLoopConfigConditionCondition: TypeAlias = Union[
    PlanLoopConfigConditionConditionUnaryCondition, PlanLoopConfigConditionConditionCompoundCondition
]


class PlanLoopConfigCondition(TypedDict, total=False):
    conditions: Iterable[PlanLoopConfigConditionCondition]

    input_names: List[str]

    logical_operator: Literal["ALL", "ANY", "NOT"]


class PlanLoopConfigWorkflow(TypedDict, total=False):
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

    workflow_alias: str

    workflow_inputs: Dict[str, Union[str, Dict[str, Union[str, object]]]]

    workflow_save_outputs: Dict[str, str]


class PlanLoopConfigLoopInputsSelfEdge(TypedDict, total=False):
    node_name: Required[str]

    default_source: str

    default_value: object


PlanLoopConfigLoopInputs: TypeAlias = Union[str, PlanLoopConfigLoopInputsSelfEdge]


class PlanLoopConfig(TypedDict, total=False):
    condition: Required[PlanLoopConfigCondition]
    """Representation of a compound boolean statement, i.e.

    a negation, conjunction, or disjunction of UnaryConditions
    """

    max_iter: Required[int]

    name: Required[str]

    workflow: Required[PlanLoopConfigWorkflow]
    """
    Representation of an instance of an abstract Workflow Attributes: workflow_name:
    Key in the map of workflows defined at the top of a plan config workflow_alias:
    Alias of the abstract workflow in the graph. If None, defaults to workflow_name.
    Use in order to re-use the same abstract workflow in multiple portions of the
    graph. workflow_inputs: Inputs to the workflow can be: 1) empty if this workflow
    does not receive input from another workflow, 2) a dictionary mapping another
    workflow's outputs or a branch's merged outputs to this workflows input keys For
    case 2, inputs can be a mapping from: a) str to str b) str to dict(str, str) c)
    str to dict(str, dict(str, str)) workflow_save_outputs: If the following
    parameter is set, the node output can ADDITIONALLY be stored under an alias in
    memory. request_user_input: request_user_input behaves as follows: - When set to
    NEVER, input of this step must be available in memory otherwise exception will
    be raised - When set to NEED_BASED, run will _only_ be interrupted when reaching
    this step in order to request required input fields in case they don't already
    exist in memory from previous node outputs or user inputs - When set to ALWAYS,
    run will _always_ be interrupted when reaching this step in order to request
    these input fields, whether they exist in memory or not
    """

    loop_inputs: Dict[str, PlanLoopConfigLoopInputs]

    merge_outputs: Dict[str, str]

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


Plan: TypeAlias = Union[PlanWorkflowItem, PlanBranchConfig, PlanLoopConfig]


class WorkflowsWorkflow(TypedDict, total=False):
    name: Required[str]

    nodes: Required[Iterable[NodeItemParam]]


Workflows: TypeAlias = Union[WorkflowsWorkflow, str, Iterable[NodeItemParam]]


class PlanConfigParam(TypedDict, total=False):
    plan: Required[Iterable[Plan]]

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

    workflows: Dict[str, Workflows]
