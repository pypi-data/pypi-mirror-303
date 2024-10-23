# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._compat import PYDANTIC_V2
from .._models import BaseModel
from .jinja_node_template import JinjaNodeTemplate

__all__ = [
    "NodeItemOutput",
    "Config",
    "ConfigNodeConfigOutput",
    "ConfigJinjaNodeConfigOutput",
    "ConfigChunkEvaluationNodeConfigOutput",
    "ConfigRerankerNodeConfigOutput",
    "ConfigRetrieverNodeConfigOutput",
    "ConfigCitationNodeConfigOutput",
    "ConfigCitationNodeConfigOutputCitationContext",
    "ConfigSearchCitationNodeConfigOutput",
    "ConfigDataTransformNodeConfigOutput",
    "ConfigCreateMessagesNodeConfigOutput",
    "ConfigCreateMessagesNodeConfigOutputMessageConfig",
    "ConfigCreateMessagesNodeConfigOutputMessageConfigAlternatingRoleMessages",
    "ConfigCreateMessagesNodeConfigOutputMessageConfigSingleRoleMessages",
    "ConfigInsertMessagesConfigOutput",
    "ConfigRemoveMessageConfigOutput",
    "ConfigGetMessageConfigOutput",
    "ConfigTokenizerChatTemplateConfigOutput",
    "ConfigLlmEngineNodeConfigOutput",
    "ConfigLlmEngineNodeConfigOutputBatchSysKwargs",
    "ConfigResponseParserNodeConfigOutput",
    "ConfigProcessingNodeConfigOutput",
    "ConfigProcessingNodeConfigOutputFunctionSpecs",
    "ConfigSqlExecutorNodeConfigOutput",
    "ConfigStaticNodeConfigOutput",
    "ConfigGenerationNodeConfigOutput",
    "ConfigGenerationNodeConfigOutputRetryConfig",
    "ConfigRegexMatchNodeConfigOutput",
    "ConfigCodeExecutionConfigOutput",
    "ConfigChatGenerationNodeConfigOutput",
    "ConfigChatGenerationNodeConfigOutputRetryConfig",
]


class ConfigNodeConfigOutput(BaseModel):
    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None


class ConfigJinjaNodeConfigOutput(BaseModel):
    context_chunks_key: Optional[str] = None

    data_transformations: Optional[Dict[str, JinjaNodeTemplate]] = None

    llm_model: Optional[str] = None

    log_output: Optional[bool] = None

    log_prefix: Optional[str] = None

    max_tokens: Optional[int] = None

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    output_template: Optional[JinjaNodeTemplate] = None
    """
    Base model for a Jinja template. Guaranteed to store a string that can be read
    in to Template().
    """

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None

    verbose: Optional[bool] = None


class ConfigChunkEvaluationNodeConfigOutput(BaseModel):
    top_k_thresholds: List[int]

    fuzzy_match_threshold: Optional[float] = None

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    require_all: Optional[bool] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None


class ConfigRerankerNodeConfigOutput(BaseModel):
    num_to_return: int

    scorers: List[object]

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    score_threshold: Optional[float] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None


class ConfigRetrieverNodeConfigOutput(BaseModel):
    num_to_return: int

    exact_knn_search: Optional[bool] = None

    knowledge_base_id: Optional[str] = None

    knowledge_base_name: Optional[str] = None

    metadata: Optional[Dict[str, Optional[str]]] = None

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None


class ConfigCitationNodeConfigOutputCitationContext(BaseModel):
    generate_with_llm: Optional[bool] = None

    metric: Optional[str] = None

    min_similarity: Optional[float] = None

    score: Optional[Literal["precision", "recall", "fmeasure"]] = None


class ConfigCitationNodeConfigOutput(BaseModel):
    citation_type: Literal["rouge", "model_defined"]

    citation_context: Optional[ConfigCitationNodeConfigOutputCitationContext] = None

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    s3_path_override: Optional[str] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None


class ConfigSearchCitationNodeConfigOutput(BaseModel):
    end_search_regex: str

    search_regex: str

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None


class ConfigDataTransformNodeConfigOutput(BaseModel):
    action: str

    additional_inputs: Optional[object] = None

    apply_to_dictlist_leaves: Optional[bool] = None

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None


class ConfigCreateMessagesNodeConfigOutputMessageConfigAlternatingRoleMessages(BaseModel):
    role_value_pairs: List[Dict[str, str]]


class ConfigCreateMessagesNodeConfigOutputMessageConfigSingleRoleMessages(BaseModel):
    content: str

    role: str


ConfigCreateMessagesNodeConfigOutputMessageConfig: TypeAlias = Union[
    ConfigCreateMessagesNodeConfigOutputMessageConfigAlternatingRoleMessages,
    ConfigCreateMessagesNodeConfigOutputMessageConfigSingleRoleMessages,
]


class ConfigCreateMessagesNodeConfigOutput(BaseModel):
    message_configs: List[ConfigCreateMessagesNodeConfigOutputMessageConfig]

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None


class ConfigInsertMessagesConfigOutput(BaseModel):
    index: int

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None


class ConfigRemoveMessageConfigOutput(BaseModel):
    index: int

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None


class ConfigGetMessageConfigOutput(BaseModel):
    index: int

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None


class ConfigTokenizerChatTemplateConfigOutput(BaseModel):
    llm_model: str

    add_generation_prompt: Optional[bool] = None

    kwargs: Optional[object] = None

    max_length: Optional[int] = None

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    padding: Optional[bool] = None

    truncation: Optional[bool] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None


class ConfigLlmEngineNodeConfigOutputBatchSysKwargs(BaseModel):
    checkpoint_path: Optional[str] = None

    labels: Optional[Dict[str, str]] = None

    num_shards: Optional[int] = None

    seed: Optional[int] = None


class ConfigLlmEngineNodeConfigOutput(BaseModel):
    llm_model: str

    batch_run_mode: Optional[Literal["sync", "async"]] = None

    batch_sys_kwargs: Optional[ConfigLlmEngineNodeConfigOutputBatchSysKwargs] = None

    frequency_penalty: Optional[float] = None

    guided_choice: Optional[List[str]] = None

    guided_json: Optional[object] = None

    guided_regex: Optional[str] = None

    include_stop_str_in_output: Optional[bool] = None

    max_tokens: Optional[int] = None

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    presence_penalty: Optional[float] = None

    stop_sequences: Optional[List[str]] = None

    temperature: Optional[float] = None

    timeout: Optional[int] = None

    top_k: Optional[int] = None

    top_p: Optional[float] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None


class ConfigResponseParserNodeConfigOutput(BaseModel):
    action: str

    reference_value: object

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None


class ConfigProcessingNodeConfigOutputFunctionSpecs(BaseModel):
    kwargs: object

    path: str


class ConfigProcessingNodeConfigOutput(BaseModel):
    function_specs: Dict[str, ConfigProcessingNodeConfigOutputFunctionSpecs]

    return_key: str

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None


class ConfigSqlExecutorNodeConfigOutput(BaseModel):
    connector_kwargs: Dict[str, str]

    connector_type: Optional[Literal["snowflake"]] = None

    log_queries: Optional[bool] = None

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    return_type: Optional[Literal["df", "dicts", "markdown", "json", "str"]] = None

    schema_remapping_file: Optional[str] = None

    secrets: Optional[List[str]] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None


class ConfigStaticNodeConfigOutput(BaseModel):
    from_file: Union[List[object], str, object, None] = None

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None

    value: Optional[object] = None


class ConfigGenerationNodeConfigOutputRetryConfig(BaseModel):
    backoff: Optional[int] = None

    delay: Optional[int] = None

    exceptions: Optional[
        List[Literal["SGPClientError", "APITimeoutError", "InternalServerError", "RateLimitError", "Exception"]]
    ] = None

    tries: Optional[int] = None


class ConfigGenerationNodeConfigOutput(BaseModel):
    llm_model: Optional[str] = None

    llm_model_deployment: Optional[str] = None

    llm_model_instance: Optional[str] = None

    max_tokens: Optional[int] = None

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    retry_config: Optional[ConfigGenerationNodeConfigOutputRetryConfig] = None

    stop_sequences: Optional[List[str]] = None

    strip_whitespace: Optional[bool] = None

    temperature: Optional[float] = None

    tool_name: Optional[str] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None


class ConfigRegexMatchNodeConfigOutput(BaseModel):
    pattern: str

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None


class ConfigCodeExecutionConfigOutput(BaseModel):
    files: Dict[str, str]

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None


class ConfigChatGenerationNodeConfigOutputRetryConfig(BaseModel):
    backoff: Optional[int] = None

    delay: Optional[int] = None

    exceptions: Optional[
        List[Literal["SGPClientError", "APITimeoutError", "InternalServerError", "RateLimitError", "Exception"]]
    ] = None

    tries: Optional[int] = None


class ConfigChatGenerationNodeConfigOutput(BaseModel):
    memory_strategy: object

    llm_model: Optional[str] = None

    llm_model_deployment: Optional[str] = None

    llm_model_instance: Optional[str] = None

    max_tokens: Optional[int] = None

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    retry_config: Optional[ConfigChatGenerationNodeConfigOutputRetryConfig] = None

    stop_sequences: Optional[List[str]] = None

    strip_whitespace: Optional[bool] = None

    temperature: Optional[float] = None

    tool_name: Optional[str] = None

    type_hints: Optional[Dict[str, "ParameterTypeOutput"]] = None


Config: TypeAlias = Union[
    ConfigNodeConfigOutput,
    ConfigJinjaNodeConfigOutput,
    ConfigChunkEvaluationNodeConfigOutput,
    ConfigRerankerNodeConfigOutput,
    ConfigRetrieverNodeConfigOutput,
    ConfigCitationNodeConfigOutput,
    ConfigSearchCitationNodeConfigOutput,
    ConfigDataTransformNodeConfigOutput,
    ConfigCreateMessagesNodeConfigOutput,
    ConfigInsertMessagesConfigOutput,
    ConfigRemoveMessageConfigOutput,
    ConfigGetMessageConfigOutput,
    ConfigTokenizerChatTemplateConfigOutput,
    ConfigLlmEngineNodeConfigOutput,
    ConfigResponseParserNodeConfigOutput,
    ConfigProcessingNodeConfigOutput,
    ConfigSqlExecutorNodeConfigOutput,
    ConfigStaticNodeConfigOutput,
    ConfigGenerationNodeConfigOutput,
    ConfigRegexMatchNodeConfigOutput,
    ConfigCodeExecutionConfigOutput,
    ConfigChatGenerationNodeConfigOutput,
]


class NodeItemOutput(BaseModel):
    config: Config
    """A data model describing parameters for back-citation using ROUGE similarity.

    metric is the ROUGE metric to use (e.g. rouge1, rouge2, rougeLsum) score is one
    of "precision", "recall", "fmeasure"

    NOTE (john): copied directly from generation.py in order to subclass from
    NodeConfig.
    """

    name: str

    type: str

    inputs: Optional[Dict[str, Union[str, Dict[str, Union[str, object]]]]] = None

    save_to_memory_as: Optional[str] = None


from .parameter_type_output import ParameterTypeOutput

if PYDANTIC_V2:
    NodeItemOutput.model_rebuild()
    ConfigNodeConfigOutput.model_rebuild()
    ConfigJinjaNodeConfigOutput.model_rebuild()
    ConfigChunkEvaluationNodeConfigOutput.model_rebuild()
    ConfigRerankerNodeConfigOutput.model_rebuild()
    ConfigRetrieverNodeConfigOutput.model_rebuild()
    ConfigCitationNodeConfigOutput.model_rebuild()
    ConfigCitationNodeConfigOutputCitationContext.model_rebuild()
    ConfigSearchCitationNodeConfigOutput.model_rebuild()
    ConfigDataTransformNodeConfigOutput.model_rebuild()
    ConfigCreateMessagesNodeConfigOutput.model_rebuild()
    ConfigCreateMessagesNodeConfigOutputMessageConfigAlternatingRoleMessages.model_rebuild()
    ConfigCreateMessagesNodeConfigOutputMessageConfigSingleRoleMessages.model_rebuild()
    ConfigInsertMessagesConfigOutput.model_rebuild()
    ConfigRemoveMessageConfigOutput.model_rebuild()
    ConfigGetMessageConfigOutput.model_rebuild()
    ConfigTokenizerChatTemplateConfigOutput.model_rebuild()
    ConfigLlmEngineNodeConfigOutput.model_rebuild()
    ConfigLlmEngineNodeConfigOutputBatchSysKwargs.model_rebuild()
    ConfigResponseParserNodeConfigOutput.model_rebuild()
    ConfigProcessingNodeConfigOutput.model_rebuild()
    ConfigProcessingNodeConfigOutputFunctionSpecs.model_rebuild()
    ConfigSqlExecutorNodeConfigOutput.model_rebuild()
    ConfigStaticNodeConfigOutput.model_rebuild()
    ConfigGenerationNodeConfigOutput.model_rebuild()
    ConfigGenerationNodeConfigOutputRetryConfig.model_rebuild()
    ConfigRegexMatchNodeConfigOutput.model_rebuild()
    ConfigCodeExecutionConfigOutput.model_rebuild()
    ConfigChatGenerationNodeConfigOutput.model_rebuild()
    ConfigChatGenerationNodeConfigOutputRetryConfig.model_rebuild()
else:
    NodeItemOutput.update_forward_refs()  # type: ignore
    ConfigNodeConfigOutput.update_forward_refs()  # type: ignore
    ConfigJinjaNodeConfigOutput.update_forward_refs()  # type: ignore
    ConfigChunkEvaluationNodeConfigOutput.update_forward_refs()  # type: ignore
    ConfigRerankerNodeConfigOutput.update_forward_refs()  # type: ignore
    ConfigRetrieverNodeConfigOutput.update_forward_refs()  # type: ignore
    ConfigCitationNodeConfigOutput.update_forward_refs()  # type: ignore
    ConfigCitationNodeConfigOutputCitationContext.update_forward_refs()  # type: ignore
    ConfigSearchCitationNodeConfigOutput.update_forward_refs()  # type: ignore
    ConfigDataTransformNodeConfigOutput.update_forward_refs()  # type: ignore
    ConfigCreateMessagesNodeConfigOutput.update_forward_refs()  # type: ignore
    ConfigCreateMessagesNodeConfigOutputMessageConfigAlternatingRoleMessages.update_forward_refs()  # type: ignore
    ConfigCreateMessagesNodeConfigOutputMessageConfigSingleRoleMessages.update_forward_refs()  # type: ignore
    ConfigInsertMessagesConfigOutput.update_forward_refs()  # type: ignore
    ConfigRemoveMessageConfigOutput.update_forward_refs()  # type: ignore
    ConfigGetMessageConfigOutput.update_forward_refs()  # type: ignore
    ConfigTokenizerChatTemplateConfigOutput.update_forward_refs()  # type: ignore
    ConfigLlmEngineNodeConfigOutput.update_forward_refs()  # type: ignore
    ConfigLlmEngineNodeConfigOutputBatchSysKwargs.update_forward_refs()  # type: ignore
    ConfigResponseParserNodeConfigOutput.update_forward_refs()  # type: ignore
    ConfigProcessingNodeConfigOutput.update_forward_refs()  # type: ignore
    ConfigProcessingNodeConfigOutputFunctionSpecs.update_forward_refs()  # type: ignore
    ConfigSqlExecutorNodeConfigOutput.update_forward_refs()  # type: ignore
    ConfigStaticNodeConfigOutput.update_forward_refs()  # type: ignore
    ConfigGenerationNodeConfigOutput.update_forward_refs()  # type: ignore
    ConfigGenerationNodeConfigOutputRetryConfig.update_forward_refs()  # type: ignore
    ConfigRegexMatchNodeConfigOutput.update_forward_refs()  # type: ignore
    ConfigCodeExecutionConfigOutput.update_forward_refs()  # type: ignore
    ConfigChatGenerationNodeConfigOutput.update_forward_refs()  # type: ignore
    ConfigChatGenerationNodeConfigOutputRetryConfig.update_forward_refs()  # type: ignore
