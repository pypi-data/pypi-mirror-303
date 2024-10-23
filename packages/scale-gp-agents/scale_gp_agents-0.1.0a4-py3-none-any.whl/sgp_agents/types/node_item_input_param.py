# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .jinja_node_template_param import JinjaNodeTemplateParam
from .parameter_type_input_param import ParameterTypeInputParam

__all__ = [
    "NodeItemInputParam",
    "Config",
    "ConfigNodeConfigInput",
    "ConfigJinjaNodeConfigInput",
    "ConfigChunkEvaluationNodeConfigInput",
    "ConfigRerankerNodeConfigInput",
    "ConfigRetrieverNodeConfigInput",
    "ConfigCitationNodeConfigInput",
    "ConfigCitationNodeConfigInputCitationContext",
    "ConfigSearchCitationNodeConfigInput",
    "ConfigDataTransformNodeConfigInput",
    "ConfigCreateMessagesNodeConfigInput",
    "ConfigCreateMessagesNodeConfigInputMessageConfig",
    "ConfigCreateMessagesNodeConfigInputMessageConfigAlternatingRoleMessages",
    "ConfigCreateMessagesNodeConfigInputMessageConfigSingleRoleMessages",
    "ConfigInsertMessagesConfigInput",
    "ConfigRemoveMessageConfigInput",
    "ConfigGetMessageConfigInput",
    "ConfigTokenizerChatTemplateConfigInput",
    "ConfigLlmEngineNodeConfigInput",
    "ConfigLlmEngineNodeConfigInputBatchSysKwargs",
    "ConfigResponseParserNodeConfigInput",
    "ConfigProcessingNodeConfigInput",
    "ConfigProcessingNodeConfigInputFunctionSpecs",
    "ConfigSqlExecutorNodeConfigInput",
    "ConfigStaticNodeConfigInput",
    "ConfigGenerationNodeConfigInput",
    "ConfigGenerationNodeConfigInputRetryConfig",
    "ConfigRegexMatchNodeConfigInput",
    "ConfigCodeExecutionConfigInput",
    "ConfigChatGenerationNodeConfigInput",
    "ConfigChatGenerationNodeConfigInputRetryConfig",
]


class ConfigNodeConfigInput(TypedDict, total=False):
    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]


class ConfigJinjaNodeConfigInput(TypedDict, total=False):
    context_chunks_key: Optional[str]

    data_transformations: Dict[str, JinjaNodeTemplateParam]

    llm_model: Optional[str]

    log_output: bool

    log_prefix: str

    max_tokens: Optional[int]

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    output_template: JinjaNodeTemplateParam
    """
    Base model for a Jinja template. Guaranteed to store a string that can be read
    in to Template().
    """

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]

    verbose: bool


class ConfigChunkEvaluationNodeConfigInput(TypedDict, total=False):
    top_k_thresholds: Required[Iterable[int]]

    fuzzy_match_threshold: float

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    require_all: bool

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]


class ConfigRerankerNodeConfigInput(TypedDict, total=False):
    num_to_return: Required[int]

    scorers: Required[Iterable[object]]

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    score_threshold: Optional[float]

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]


class ConfigRetrieverNodeConfigInput(TypedDict, total=False):
    num_to_return: Required[int]

    exact_knn_search: Optional[bool]

    knowledge_base_id: Optional[str]

    knowledge_base_name: Optional[str]

    metadata: Optional[Dict[str, Optional[str]]]

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]


class ConfigCitationNodeConfigInputCitationContext(TypedDict, total=False):
    generate_with_llm: bool

    metric: Optional[str]

    min_similarity: Optional[float]

    score: Optional[Literal["precision", "recall", "fmeasure"]]


class ConfigCitationNodeConfigInput(TypedDict, total=False):
    citation_type: Required[Literal["rouge", "model_defined"]]

    citation_context: ConfigCitationNodeConfigInputCitationContext

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    s3_path_override: Optional[str]

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]


class ConfigSearchCitationNodeConfigInput(TypedDict, total=False):
    end_search_regex: Required[str]

    search_regex: Required[str]

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]


class ConfigDataTransformNodeConfigInput(TypedDict, total=False):
    action: Required[str]

    additional_inputs: object

    apply_to_dictlist_leaves: bool

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]


class ConfigCreateMessagesNodeConfigInputMessageConfigAlternatingRoleMessages(TypedDict, total=False):
    role_value_pairs: Required[Iterable[Dict[str, str]]]


class ConfigCreateMessagesNodeConfigInputMessageConfigSingleRoleMessages(TypedDict, total=False):
    content: Required[str]

    role: Required[str]


ConfigCreateMessagesNodeConfigInputMessageConfig: TypeAlias = Union[
    ConfigCreateMessagesNodeConfigInputMessageConfigAlternatingRoleMessages,
    ConfigCreateMessagesNodeConfigInputMessageConfigSingleRoleMessages,
]


class ConfigCreateMessagesNodeConfigInput(TypedDict, total=False):
    message_configs: Required[Iterable[ConfigCreateMessagesNodeConfigInputMessageConfig]]

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]


class ConfigInsertMessagesConfigInput(TypedDict, total=False):
    index: Required[int]

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]


class ConfigRemoveMessageConfigInput(TypedDict, total=False):
    index: Required[int]

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]


class ConfigGetMessageConfigInput(TypedDict, total=False):
    index: Required[int]

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]


class ConfigTokenizerChatTemplateConfigInput(TypedDict, total=False):
    llm_model: Required[str]

    add_generation_prompt: bool

    kwargs: object

    max_length: Optional[int]

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    padding: bool

    truncation: bool

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]


class ConfigLlmEngineNodeConfigInputBatchSysKwargs(TypedDict, total=False):
    checkpoint_path: Optional[str]

    labels: Optional[Dict[str, str]]

    num_shards: Optional[int]

    seed: Optional[int]


class ConfigLlmEngineNodeConfigInput(TypedDict, total=False):
    llm_model: Required[str]

    batch_run_mode: Literal["sync", "async"]

    batch_sys_kwargs: ConfigLlmEngineNodeConfigInputBatchSysKwargs

    frequency_penalty: Optional[float]

    guided_choice: Optional[List[str]]

    guided_json: Optional[object]

    guided_regex: Optional[str]

    include_stop_str_in_output: Optional[bool]

    max_tokens: Optional[int]

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    presence_penalty: Optional[float]

    stop_sequences: Optional[List[str]]

    temperature: Optional[float]

    timeout: int

    top_k: Optional[int]

    top_p: Optional[float]

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]


class ConfigResponseParserNodeConfigInput(TypedDict, total=False):
    action: Required[str]

    reference_value: Required[object]

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]


class ConfigProcessingNodeConfigInputFunctionSpecs(TypedDict, total=False):
    kwargs: Required[object]

    path: Required[str]


class ConfigProcessingNodeConfigInput(TypedDict, total=False):
    function_specs: Required[Dict[str, ConfigProcessingNodeConfigInputFunctionSpecs]]

    return_key: Required[str]

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]


class ConfigSqlExecutorNodeConfigInput(TypedDict, total=False):
    connector_kwargs: Required[Dict[str, str]]

    connector_type: Literal["snowflake"]

    log_queries: bool

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    return_type: Literal["df", "dicts", "markdown", "json", "str"]

    schema_remapping_file: Optional[str]

    secrets: List[str]

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]


class ConfigStaticNodeConfigInput(TypedDict, total=False):
    from_file: Union[Iterable[object], str, object, None]

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]

    value: Optional[object]


class ConfigGenerationNodeConfigInputRetryConfig(TypedDict, total=False):
    backoff: int

    delay: int

    exceptions: List[Literal["SGPClientError", "APITimeoutError", "InternalServerError", "RateLimitError", "Exception"]]

    tries: int


class ConfigGenerationNodeConfigInput(TypedDict, total=False):
    llm_model: str

    llm_model_deployment: Optional[str]

    llm_model_instance: Optional[str]

    max_tokens: int

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    retry_config: ConfigGenerationNodeConfigInputRetryConfig

    stop_sequences: Optional[List[str]]

    strip_whitespace: bool

    temperature: float

    tool_name: Optional[str]

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]


class ConfigRegexMatchNodeConfigInput(TypedDict, total=False):
    pattern: Required[str]

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]


class ConfigCodeExecutionConfigInput(TypedDict, total=False):
    files: Required[Dict[str, str]]

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]


class ConfigChatGenerationNodeConfigInputRetryConfig(TypedDict, total=False):
    backoff: int

    delay: int

    exceptions: List[Literal["SGPClientError", "APITimeoutError", "InternalServerError", "RateLimitError", "Exception"]]

    tries: int


class ConfigChatGenerationNodeConfigInput(TypedDict, total=False):
    memory_strategy: Required[object]

    llm_model: str

    llm_model_deployment: Optional[str]

    llm_model_instance: Optional[str]

    max_tokens: int

    node_metadata: Optional[List[str]]

    num_workers: Optional[int]

    retry_config: ConfigChatGenerationNodeConfigInputRetryConfig

    stop_sequences: Optional[List[str]]

    strip_whitespace: bool

    temperature: float

    tool_name: Optional[str]

    type_hints: Optional[Dict[str, ParameterTypeInputParam]]


Config: TypeAlias = Union[
    ConfigNodeConfigInput,
    ConfigJinjaNodeConfigInput,
    ConfigChunkEvaluationNodeConfigInput,
    ConfigRerankerNodeConfigInput,
    ConfigRetrieverNodeConfigInput,
    ConfigCitationNodeConfigInput,
    ConfigSearchCitationNodeConfigInput,
    ConfigDataTransformNodeConfigInput,
    ConfigCreateMessagesNodeConfigInput,
    ConfigInsertMessagesConfigInput,
    ConfigRemoveMessageConfigInput,
    ConfigGetMessageConfigInput,
    ConfigTokenizerChatTemplateConfigInput,
    ConfigLlmEngineNodeConfigInput,
    ConfigResponseParserNodeConfigInput,
    ConfigProcessingNodeConfigInput,
    ConfigSqlExecutorNodeConfigInput,
    ConfigStaticNodeConfigInput,
    ConfigGenerationNodeConfigInput,
    ConfigRegexMatchNodeConfigInput,
    ConfigCodeExecutionConfigInput,
    ConfigChatGenerationNodeConfigInput,
]


class NodeItemInputParam(TypedDict, total=False):
    config: Required[Config]
    """A data model describing parameters for back-citation using ROUGE similarity.

    metric is the ROUGE metric to use (e.g. rouge1, rouge2, rougeLsum) score is one
    of "precision", "recall", "fmeasure"

    NOTE (john): copied directly from generation.py in order to subclass from
    NodeConfig.
    """

    name: Required[str]

    type: Required[str]

    inputs: Dict[str, Union[str, Dict[str, Union[str, object]]]]

    save_to_memory_as: Optional[str]
