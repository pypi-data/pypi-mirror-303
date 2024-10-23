# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "NodeItem",
    "Config",
    "ConfigNodeConfig",
    "ConfigJinjaNodeConfig",
    "ConfigJinjaNodeConfigDataTransformations",
    "ConfigJinjaNodeConfigOutputTemplate",
    "ConfigChunkEvaluationNodeConfig",
    "ConfigRerankerNodeConfig",
    "ConfigRetrieverNodeConfig",
    "ConfigCitationNodeConfig",
    "ConfigCitationNodeConfigCitationContext",
    "ConfigSearchCitationNodeConfig",
    "ConfigDataTransformNodeConfig",
    "ConfigCreateMessagesNodeConfig",
    "ConfigCreateMessagesNodeConfigMessageConfig",
    "ConfigCreateMessagesNodeConfigMessageConfigAlternatingRoleMessages",
    "ConfigCreateMessagesNodeConfigMessageConfigSingleRoleMessages",
    "ConfigInsertMessagesConfig",
    "ConfigRemoveMessageConfig",
    "ConfigTokenizerChatTemplateConfig",
    "ConfigLlmEngineNodeConfig",
    "ConfigLlmEngineNodeConfigBatchSysKwargs",
    "ConfigResponseParserNodeConfig",
    "ConfigProcessingNodeConfig",
    "ConfigProcessingNodeConfigFunctionSpecs",
    "ConfigSqlExecutorNodeConfig",
    "ConfigStaticNodeConfig",
    "ConfigGenerationNodeConfig",
]


class ConfigNodeConfig(BaseModel):
    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None


class ConfigJinjaNodeConfigDataTransformations(BaseModel):
    jinja_helper_functions: Optional[List[Union[str, object]]] = None

    jinja_template_path: Optional[str] = None

    jinja_template_str: Optional[str] = None
    """Raw template to apply to the data.

    This should be a Jinja2 template string. Please note, the data will be mapped as
    'value' in the template. Default None corresponds to {{value}}. Should access
    property `jinja_template_str` or field `jinja_template_str_loaded` for the
    loaded template data
    """

    jinja_template_str_loaded: Optional[str] = None
    """
    The original jinja_template_str field from the config might not contain the
    needed template, and we may need to load S3 data specified with
    `jinja_template_path`. This field caches the loaded template content, it is also
    accessed through property `jinja_template_str`.
    """


class ConfigJinjaNodeConfigOutputTemplate(BaseModel):
    jinja_helper_functions: Optional[List[Union[str, object]]] = None

    jinja_template_path: Optional[str] = None

    jinja_template_str: Optional[str] = None
    """Raw template to apply to the data.

    This should be a Jinja2 template string. Please note, the data will be mapped as
    'value' in the template. Default None corresponds to {{value}}. Should access
    property `jinja_template_str` or field `jinja_template_str_loaded` for the
    loaded template data
    """

    jinja_template_str_loaded: Optional[str] = None
    """
    The original jinja_template_str field from the config might not contain the
    needed template, and we may need to load S3 data specified with
    `jinja_template_path`. This field caches the loaded template content, it is also
    accessed through property `jinja_template_str`.
    """


class ConfigJinjaNodeConfig(BaseModel):
    context_chunks_key: Optional[str] = None

    data_transformations: Optional[Dict[str, ConfigJinjaNodeConfigDataTransformations]] = None

    llm_model: Optional[str] = None

    log_output: Optional[bool] = None

    log_prefix: Optional[str] = None

    max_tokens: Optional[int] = None

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    output_template: Optional[ConfigJinjaNodeConfigOutputTemplate] = None
    """
    Base model for a Jinja template. Guaranteed to store a string that can be read
    in to Template().
    """

    verbose: Optional[bool] = None


class ConfigChunkEvaluationNodeConfig(BaseModel):
    top_k_thresholds: List[int]

    fuzzy_match_threshold: Optional[float] = None

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    require_all: Optional[bool] = None


class ConfigRerankerNodeConfig(BaseModel):
    num_to_return: int

    scorers: List[object]

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    score_threshold: Optional[float] = None


class ConfigRetrieverNodeConfig(BaseModel):
    num_to_return: int

    exact_knn_search: Optional[bool] = None

    knowledge_base_id: Optional[str] = None

    knowledge_base_name: Optional[str] = None

    metadata: Optional[Dict[str, str]] = None

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None


class ConfigCitationNodeConfigCitationContext(BaseModel):
    generate_with_llm: Optional[bool] = None

    metric: Optional[str] = None

    min_similarity: Optional[float] = None

    score: Optional[Literal["precision", "recall", "fmeasure"]] = None


class ConfigCitationNodeConfig(BaseModel):
    citation_type: Literal["rouge", "model_defined"]

    citation_context: Optional[ConfigCitationNodeConfigCitationContext] = None

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    s3_path_override: Optional[str] = None


class ConfigSearchCitationNodeConfig(BaseModel):
    end_search_regex: str

    search_regex: str

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None


class ConfigDataTransformNodeConfig(BaseModel):
    action: str

    additional_inputs: Optional[object] = None

    apply_to_dictlist_leaves: Optional[bool] = None

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None


class ConfigCreateMessagesNodeConfigMessageConfigAlternatingRoleMessages(BaseModel):
    role_value_pairs: List[Dict[str, str]]


class ConfigCreateMessagesNodeConfigMessageConfigSingleRoleMessages(BaseModel):
    content: str

    role: str


ConfigCreateMessagesNodeConfigMessageConfig: TypeAlias = Union[
    ConfigCreateMessagesNodeConfigMessageConfigAlternatingRoleMessages,
    ConfigCreateMessagesNodeConfigMessageConfigSingleRoleMessages,
]


class ConfigCreateMessagesNodeConfig(BaseModel):
    message_configs: List[ConfigCreateMessagesNodeConfigMessageConfig]

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None


class ConfigInsertMessagesConfig(BaseModel):
    index: int

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None


class ConfigRemoveMessageConfig(BaseModel):
    index: int

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None


class ConfigTokenizerChatTemplateConfig(BaseModel):
    llm_model: str

    add_generation_prompt: Optional[bool] = None

    kwargs: Optional[object] = None

    max_length: Optional[int] = None

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    padding: Optional[bool] = None

    truncation: Optional[bool] = None


class ConfigLlmEngineNodeConfigBatchSysKwargs(BaseModel):
    checkpoint_path: Optional[str] = None

    labels: Optional[Dict[str, str]] = None

    num_shards: Optional[int] = None

    seed: Optional[int] = None


class ConfigLlmEngineNodeConfig(BaseModel):
    llm_model: str

    batch_run_mode: Optional[Literal["sync", "async"]] = None

    batch_sys_kwargs: Optional[ConfigLlmEngineNodeConfigBatchSysKwargs] = None

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


class ConfigResponseParserNodeConfig(BaseModel):
    action: str

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    reference_value: Optional[object] = None


class ConfigProcessingNodeConfigFunctionSpecs(BaseModel):
    kwargs: object

    path: str


class ConfigProcessingNodeConfig(BaseModel):
    function_specs: Dict[str, ConfigProcessingNodeConfigFunctionSpecs]

    return_key: str

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None


class ConfigSqlExecutorNodeConfig(BaseModel):
    connector_kwargs: Dict[str, str]

    connector_type: Optional[Literal["snowflake"]] = None

    log_queries: Optional[bool] = None

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    return_type: Optional[Literal["df", "dicts", "markdown", "json", "str"]] = None

    schema_remapping_file: Optional[str] = None

    secrets: Optional[List[str]] = None


class ConfigStaticNodeConfig(BaseModel):
    from_file: Union[List[object], str, object, None] = None

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    value: Optional[object] = None


class ConfigGenerationNodeConfig(BaseModel):
    llm_model: Optional[str] = None

    llm_model_deployment: Optional[str] = None

    llm_model_instance: Optional[str] = None

    max_tokens: Optional[int] = None

    node_metadata: Optional[List[str]] = None

    num_workers: Optional[int] = None

    stop_sequences: Optional[List[str]] = None

    strip_whitespace: Optional[bool] = None

    temperature: Optional[float] = None

    tool_name: Optional[str] = None


Config: TypeAlias = Union[
    ConfigNodeConfig,
    ConfigJinjaNodeConfig,
    ConfigChunkEvaluationNodeConfig,
    ConfigRerankerNodeConfig,
    ConfigRetrieverNodeConfig,
    ConfigCitationNodeConfig,
    ConfigSearchCitationNodeConfig,
    ConfigDataTransformNodeConfig,
    ConfigCreateMessagesNodeConfig,
    ConfigInsertMessagesConfig,
    ConfigRemoveMessageConfig,
    ConfigTokenizerChatTemplateConfig,
    ConfigLlmEngineNodeConfig,
    ConfigResponseParserNodeConfig,
    ConfigProcessingNodeConfig,
    ConfigSqlExecutorNodeConfig,
    ConfigStaticNodeConfig,
    ConfigGenerationNodeConfig,
]


class NodeItem(BaseModel):
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
