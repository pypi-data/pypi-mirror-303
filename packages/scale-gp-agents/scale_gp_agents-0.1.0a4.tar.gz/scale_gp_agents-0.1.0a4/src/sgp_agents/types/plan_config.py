# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .node_item import NodeItem

__all__ = [
    "PlanConfig",
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


class PlanWorkflowItem(BaseModel):
    workflow_name: str

    request_user_input: Optional[Literal["never", "maybe", "always"]] = None
    """
    If always: available the first time: request missing the first time: request
    available the next time: continue missing the next time: request (treat like
    need_based) If need_based: available the first time: continue missing the first
    time: request available the next time: continue missing the next time: request
    (treat like the first time) If never: available the first time: continue missing
    the first time: raise Exception available the next time: continue missing the
    next time: raise Exception
    """

    workflow_alias: Optional[str] = None

    workflow_inputs: Optional[Dict[str, Union[str, Dict[str, Union[str, object]]]]] = None

    workflow_save_outputs: Optional[Dict[str, str]] = None


class PlanBranchConfigConditionalWorkflowConditionTreeConditionUnaryCondition(BaseModel):
    condition_input_var: str

    operator: str

    reference_var: Optional[object] = None


class PlanBranchConfigConditionalWorkflowConditionTreeConditionCompoundConditionConditionUnaryCondition(BaseModel):
    condition_input_var: str

    operator: str

    reference_var: Optional[object] = None


PlanBranchConfigConditionalWorkflowConditionTreeConditionCompoundConditionCondition: TypeAlias = Union[
    PlanBranchConfigConditionalWorkflowConditionTreeConditionCompoundConditionConditionUnaryCondition, object
]


class PlanBranchConfigConditionalWorkflowConditionTreeConditionCompoundCondition(BaseModel):
    conditions: Optional[List[PlanBranchConfigConditionalWorkflowConditionTreeConditionCompoundConditionCondition]] = (
        None
    )

    input_names: Optional[List[str]] = None

    logical_operator: Optional[Literal["ALL", "ANY", "NOT"]] = None


PlanBranchConfigConditionalWorkflowConditionTreeCondition: TypeAlias = Union[
    PlanBranchConfigConditionalWorkflowConditionTreeConditionUnaryCondition,
    PlanBranchConfigConditionalWorkflowConditionTreeConditionCompoundCondition,
]


class PlanBranchConfigConditionalWorkflowConditionTree(BaseModel):
    conditions: Optional[List[PlanBranchConfigConditionalWorkflowConditionTreeCondition]] = None

    input_names: Optional[List[str]] = None

    logical_operator: Optional[Literal["ALL", "ANY", "NOT"]] = None


class PlanBranchConfigConditionalWorkflow(BaseModel):
    condition: Literal["if", "elif", "else"]

    workflow_name: str

    condition_input_var: Optional[str] = None

    condition_tree: Optional[PlanBranchConfigConditionalWorkflowConditionTree] = None
    """Representation of a compound boolean statement, i.e.

    a negation, conjunction, or disjunction of UnaryConditions
    """

    operator: Optional[str] = None

    reference_var: Optional[str] = None

    request_user_input: Optional[Literal["never", "maybe", "always"]] = None
    """
    If always: available the first time: request missing the first time: request
    available the next time: continue missing the next time: request (treat like
    need_based) If need_based: available the first time: continue missing the first
    time: request available the next time: continue missing the next time: request
    (treat like the first time) If never: available the first time: continue missing
    the first time: raise Exception available the next time: continue missing the
    next time: raise Exception
    """

    workflow_alias: Optional[str] = None

    workflow_inputs: Optional[Dict[str, Union[str, Dict[str, Union[str, object]]]]] = None

    workflow_nodes: Optional[List[str]] = None

    workflow_save_outputs: Optional[Dict[str, str]] = None


class PlanBranchConfig(BaseModel):
    branch: str

    conditional_workflows: List[PlanBranchConfigConditionalWorkflow]

    merge_outputs: Optional[Dict[str, List[str]]] = None

    request_user_input: Optional[Literal["never", "maybe", "always"]] = None
    """
    If always: available the first time: request missing the first time: request
    available the next time: continue missing the next time: request (treat like
    need_based) If need_based: available the first time: continue missing the first
    time: request available the next time: continue missing the next time: request
    (treat like the first time) If never: available the first time: continue missing
    the first time: raise Exception available the next time: continue missing the
    next time: raise Exception
    """

    save_merge_to_memory: Optional[Dict[str, str]] = None


class PlanLoopConfigConditionConditionUnaryCondition(BaseModel):
    condition_input_var: str

    operator: str

    reference_var: Optional[object] = None


class PlanLoopConfigConditionConditionCompoundConditionConditionUnaryCondition(BaseModel):
    condition_input_var: str

    operator: str

    reference_var: Optional[object] = None


PlanLoopConfigConditionConditionCompoundConditionCondition: TypeAlias = Union[
    PlanLoopConfigConditionConditionCompoundConditionConditionUnaryCondition, object
]


class PlanLoopConfigConditionConditionCompoundCondition(BaseModel):
    conditions: Optional[List[PlanLoopConfigConditionConditionCompoundConditionCondition]] = None

    input_names: Optional[List[str]] = None

    logical_operator: Optional[Literal["ALL", "ANY", "NOT"]] = None


PlanLoopConfigConditionCondition: TypeAlias = Union[
    PlanLoopConfigConditionConditionUnaryCondition, PlanLoopConfigConditionConditionCompoundCondition
]


class PlanLoopConfigCondition(BaseModel):
    conditions: Optional[List[PlanLoopConfigConditionCondition]] = None

    input_names: Optional[List[str]] = None

    logical_operator: Optional[Literal["ALL", "ANY", "NOT"]] = None


class PlanLoopConfigWorkflow(BaseModel):
    workflow_name: str

    request_user_input: Optional[Literal["never", "maybe", "always"]] = None
    """
    If always: available the first time: request missing the first time: request
    available the next time: continue missing the next time: request (treat like
    need_based) If need_based: available the first time: continue missing the first
    time: request available the next time: continue missing the next time: request
    (treat like the first time) If never: available the first time: continue missing
    the first time: raise Exception available the next time: continue missing the
    next time: raise Exception
    """

    workflow_alias: Optional[str] = None

    workflow_inputs: Optional[Dict[str, Union[str, Dict[str, Union[str, object]]]]] = None

    workflow_save_outputs: Optional[Dict[str, str]] = None


class PlanLoopConfigLoopInputsSelfEdge(BaseModel):
    node_name: str

    default_source: Optional[str] = None

    default_value: Optional[object] = None


PlanLoopConfigLoopInputs: TypeAlias = Union[str, PlanLoopConfigLoopInputsSelfEdge]


class PlanLoopConfig(BaseModel):
    condition: PlanLoopConfigCondition
    """Representation of a compound boolean statement, i.e.

    a negation, conjunction, or disjunction of UnaryConditions
    """

    max_iter: int

    name: str

    workflow: PlanLoopConfigWorkflow
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

    loop_inputs: Optional[Dict[str, PlanLoopConfigLoopInputs]] = None

    merge_outputs: Optional[Dict[str, str]] = None

    request_user_input: Optional[Literal["never", "maybe", "always"]] = None
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


class WorkflowsWorkflow(BaseModel):
    name: str

    nodes: List[NodeItem]


Workflows: TypeAlias = Union[WorkflowsWorkflow, str, List[NodeItem]]


class PlanConfig(BaseModel):
    plan: List[Plan]

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

    workflows: Optional[Dict[str, Workflows]] = None
