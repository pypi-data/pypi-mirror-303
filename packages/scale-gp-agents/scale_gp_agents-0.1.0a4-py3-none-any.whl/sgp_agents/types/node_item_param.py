# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "NodeItemParam",
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


class ConfigNodeConfig(TypedDict, total=False):
    node_metadata: List[str]

    num_workers: int


class ConfigJinjaNodeConfigDataTransformations(TypedDict, total=False):
    jinja_helper_functions: List[Union[str, object]]

    jinja_template_path: str

    jinja_template_str: str
    """Raw template to apply to the data.

    This should be a Jinja2 template string. Please note, the data will be mapped as
    'value' in the template. Default None corresponds to {{value}}. Should access
    property `jinja_template_str` or field `jinja_template_str_loaded` for the
    loaded template data
    """

    jinja_template_str_loaded: str
    """
    The original jinja_template_str field from the config might not contain the
    needed template, and we may need to load S3 data specified with
    `jinja_template_path`. This field caches the loaded template content, it is also
    accessed through property `jinja_template_str`.
    """


class ConfigJinjaNodeConfigOutputTemplate(TypedDict, total=False):
    jinja_helper_functions: List[Union[str, object]]

    jinja_template_path: str

    jinja_template_str: str
    """Raw template to apply to the data.

    This should be a Jinja2 template string. Please note, the data will be mapped as
    'value' in the template. Default None corresponds to {{value}}. Should access
    property `jinja_template_str` or field `jinja_template_str_loaded` for the
    loaded template data
    """

    jinja_template_str_loaded: str
    """
    The original jinja_template_str field from the config might not contain the
    needed template, and we may need to load S3 data specified with
    `jinja_template_path`. This field caches the loaded template content, it is also
    accessed through property `jinja_template_str`.
    """


class ConfigJinjaNodeConfig(TypedDict, total=False):
    context_chunks_key: str

    data_transformations: Dict[str, ConfigJinjaNodeConfigDataTransformations]

    llm_model: str

    log_output: bool

    log_prefix: str

    max_tokens: int

    node_metadata: List[str]

    num_workers: int

    output_template: ConfigJinjaNodeConfigOutputTemplate
    """
    Base model for a Jinja template. Guaranteed to store a string that can be read
    in to Template().
    """

    verbose: bool


class ConfigChunkEvaluationNodeConfig(TypedDict, total=False):
    top_k_thresholds: Required[Iterable[int]]

    fuzzy_match_threshold: float

    node_metadata: List[str]

    num_workers: int

    require_all: bool


class ConfigRerankerNodeConfig(TypedDict, total=False):
    num_to_return: Required[int]

    scorers: Required[Iterable[object]]

    node_metadata: List[str]

    num_workers: int

    score_threshold: float


class ConfigRetrieverNodeConfig(TypedDict, total=False):
    num_to_return: Required[int]

    exact_knn_search: bool

    knowledge_base_id: str

    knowledge_base_name: str

    metadata: Dict[str, str]

    node_metadata: List[str]

    num_workers: int


class ConfigCitationNodeConfigCitationContext(TypedDict, total=False):
    generate_with_llm: bool

    metric: str

    min_similarity: float

    score: Literal["precision", "recall", "fmeasure"]


class ConfigCitationNodeConfig(TypedDict, total=False):
    citation_type: Required[Literal["rouge", "model_defined"]]

    citation_context: ConfigCitationNodeConfigCitationContext

    node_metadata: List[str]

    num_workers: int

    s3_path_override: str


class ConfigSearchCitationNodeConfig(TypedDict, total=False):
    end_search_regex: Required[str]

    search_regex: Required[str]

    node_metadata: List[str]

    num_workers: int


class ConfigDataTransformNodeConfig(TypedDict, total=False):
    action: Required[str]

    additional_inputs: object

    apply_to_dictlist_leaves: bool

    node_metadata: List[str]

    num_workers: int


class ConfigCreateMessagesNodeConfigMessageConfigAlternatingRoleMessages(TypedDict, total=False):
    role_value_pairs: Required[Iterable[Dict[str, str]]]


class ConfigCreateMessagesNodeConfigMessageConfigSingleRoleMessages(TypedDict, total=False):
    content: Required[str]

    role: Required[str]


ConfigCreateMessagesNodeConfigMessageConfig: TypeAlias = Union[
    ConfigCreateMessagesNodeConfigMessageConfigAlternatingRoleMessages,
    ConfigCreateMessagesNodeConfigMessageConfigSingleRoleMessages,
]


class ConfigCreateMessagesNodeConfig(TypedDict, total=False):
    message_configs: Required[Iterable[ConfigCreateMessagesNodeConfigMessageConfig]]

    node_metadata: List[str]

    num_workers: int


class ConfigInsertMessagesConfig(TypedDict, total=False):
    index: Required[int]

    node_metadata: List[str]

    num_workers: int


class ConfigRemoveMessageConfig(TypedDict, total=False):
    index: Required[int]

    node_metadata: List[str]

    num_workers: int


class ConfigTokenizerChatTemplateConfig(TypedDict, total=False):
    llm_model: Required[str]

    add_generation_prompt: bool

    kwargs: object

    max_length: int

    node_metadata: List[str]

    num_workers: int

    padding: bool

    truncation: bool


class ConfigLlmEngineNodeConfigBatchSysKwargs(TypedDict, total=False):
    checkpoint_path: str

    labels: Dict[str, str]

    num_shards: int

    seed: int


class ConfigLlmEngineNodeConfig(TypedDict, total=False):
    llm_model: Required[str]

    batch_run_mode: Literal["sync", "async"]

    batch_sys_kwargs: ConfigLlmEngineNodeConfigBatchSysKwargs

    frequency_penalty: float

    guided_choice: List[str]

    guided_json: object

    guided_regex: str

    include_stop_str_in_output: bool

    max_tokens: int

    node_metadata: List[str]

    num_workers: int

    presence_penalty: float

    stop_sequences: List[str]

    temperature: float

    timeout: int

    top_k: int

    top_p: float


class ConfigResponseParserNodeConfig(TypedDict, total=False):
    action: Required[str]

    node_metadata: List[str]

    num_workers: int

    reference_value: object


class ConfigProcessingNodeConfigFunctionSpecs(TypedDict, total=False):
    kwargs: Required[object]

    path: Required[str]


class ConfigProcessingNodeConfig(TypedDict, total=False):
    function_specs: Required[Dict[str, ConfigProcessingNodeConfigFunctionSpecs]]

    return_key: Required[str]

    node_metadata: List[str]

    num_workers: int


class ConfigSqlExecutorNodeConfig(TypedDict, total=False):
    connector_kwargs: Required[Dict[str, str]]

    connector_type: Literal["snowflake"]

    log_queries: bool

    node_metadata: List[str]

    num_workers: int

    return_type: Literal["df", "dicts", "markdown", "json", "str"]

    schema_remapping_file: str

    secrets: List[str]


class ConfigStaticNodeConfig(TypedDict, total=False):
    from_file: Union[Iterable[object], str, object]

    node_metadata: List[str]

    num_workers: int

    value: object


class ConfigGenerationNodeConfig(TypedDict, total=False):
    llm_model: str

    llm_model_deployment: str

    llm_model_instance: str

    max_tokens: int

    node_metadata: List[str]

    num_workers: int

    stop_sequences: List[str]

    strip_whitespace: bool

    temperature: float

    tool_name: str


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


class NodeItemParam(TypedDict, total=False):
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

    save_to_memory_as: str
