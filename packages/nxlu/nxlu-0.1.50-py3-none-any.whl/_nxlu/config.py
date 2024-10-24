import os
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from networkx.utils.configs import Config

from _nxlu.enums import AnthropicModel, Framework, LocalModel, OpenAIModel
from _nxlu.logging import LoggerConfig, LoggingConfig, LoggingHandlerConfig

__all__ = ["_config", "NxluConfig"]


@dataclass
class NxluConfig(Config):
    """Configuration for NetworkX that controls behaviors such as how to use backends
    and logging.
    """

    active: bool = False
    simple: int = False
    cache_converted_graphs: bool = True
    llm_framework: Framework | str = "langchain"
    openai_api_key: str | None = None
    anthropic_api_key: str | None = None
    model_name: OpenAIModel | AnthropicModel | LocalModel | str = "gpt-4o-mini"
    temperature: float = 0.1
    max_tokens: int = 5000
    num_thread: int = 8
    num_gpu: int = 0
    backend_name: str = "nxlu"
    backend_params: dict = field(default_factory=dict)

    logging_config: LoggingConfig = field(default_factory=LoggingConfig)

    include_algorithms: list[str] | None = field(default_factory=list)
    exclude_algorithms: list[str] | None = field(default_factory=list)
    enable_classification: bool = True
    enable_resource_constraints: bool = True
    enable_subgraph_retrieval: bool = True
    embedding_model_name: str = "all-MiniLM-L6-v2"

    _LLM_FRAMEWORK = "LLM_FRAMEWORK"
    _OPENAI_API_KEY = "OPENAI_API_KEY"
    _ANTHROPIC_API_KEY = "ANTHROPIC_API_KEY"
    _MODEL_NAME = "MODEL_NAME"
    _TEMPERATURE = "TEMPERATURE"
    _MAX_TOKENS = "MAX_TOKENS"
    _NUM_THREAD = "NUM_THREAD"
    _NUM_GPU = "NUM_GPU"
    _BACKEND_NAME = "BACKEND_NAME"

    _observers: list[Callable[[str, Any], None]] = field(
        default_factory=list, init=False, repr=False
    )

    def __post_init__(self):
        """Set environment variables based on initialized fields."""
        if self.llm_framework:
            self.set_llm_framework(self.llm_framework)
        if self.openai_api_key:
            self.set_openai_api_key(self.openai_api_key)
        if self.anthropic_api_key:
            self.set_anthropic_api_key(self.anthropic_api_key)
        if self.model_name:
            self.set_model_name(self.model_name)
        self.set_temperature(self.temperature)
        self.set_max_tokens(self.max_tokens)
        self.set_num_thread(self.num_thread)
        self.set_num_gpu(self.num_gpu)
        self.set_include_algorithms(self.include_algorithms)
        self.set_exclude_algorithms(self.exclude_algorithms)
        self.set_enable_classification(self.enable_classification)
        self.set_enable_resource_constraints(self.enable_resource_constraints)
        self.set_enable_subgraph_retrieval(self.enable_subgraph_retrieval)
        self.set_backend_name(self.backend_name)
        self.set_embedding_model_name(self.embedding_model_name)

    def register_observer(self, callback: Callable[[str, Any], None]) -> None:
        """Register an observer callback to be notified on configuration changes.

        Parameters
        ----------
        callback : Callable[[str, any], None]
            A function that accepts two arguments: the name of the configuration
            parameter
            that changed and its new value.
        """
        self._observers.append(callback)

    def notify_observers(self, name: str, value: Any) -> None:
        """Notify all registered observers about a configuration change.

        Parameters
        ----------
        name : str
            The name of the configuration parameter that changed.
        value : Any
            The new value of the configuration parameter.
        """
        for callback in self._observers:
            callback(name, value)

    def set_llm_framework(self, llm_framework: Framework | str) -> None:
        """Set the LLM framework, supporting both enum and string."""
        if isinstance(llm_framework, Framework):
            llm_framework_value = llm_framework.value
        else:
            llm_framework_value = llm_framework
        os.environ[self._LLM_FRAMEWORK] = llm_framework_value
        self.llm_framework = llm_framework_value
        self.notify_observers("llm_framework", llm_framework_value)

    def get_llm_framework(self) -> str | None:
        """Get the LLM framework."""
        return self.llm_framework

    def set_openai_api_key(self, key: str) -> None:
        """Set the OpenAI API key."""
        os.environ[self._OPENAI_API_KEY] = key

    def get_openai_api_key(self) -> str | None:
        """Get the OpenAI API key."""
        return os.environ.get(self._OPENAI_API_KEY)

    def set_anthropic_api_key(self, key: str) -> None:
        """Set the Anthropic API key."""
        os.environ[self._ANTHROPIC_API_KEY] = key

    def get_anthropic_api_key(self) -> str | None:
        """Get the Anthropic API key."""
        return os.environ.get(self._ANTHROPIC_API_KEY)

    def set_model_name(
        self, model: OpenAIModel | AnthropicModel | LocalModel | str
    ) -> None:
        """Set the model name, supporting both enum and string."""
        if isinstance(model, (OpenAIModel, AnthropicModel, LocalModel)):
            model_value = model.value
        else:
            model_value = model
        os.environ[self._MODEL_NAME] = model_value
        self.model_name = model_value
        self.notify_observers("model_name", model_value)

    def get_model_name(self) -> str:
        """Get the model name."""
        return self.model_name

    def set_temperature(self, temp: float) -> None:
        """Set the temperature."""
        os.environ[self._TEMPERATURE] = str(temp)
        self.temperature = temp
        self.notify_observers("temperature", temp)

    def get_temperature(self) -> float:
        """Get the temperature."""
        return self.temperature

    def set_max_tokens(self, tokens: int) -> None:
        """Set the maximum number of tokens."""
        os.environ[self._MAX_TOKENS] = str(tokens)
        self.max_tokens = tokens
        self.notify_observers("max_tokens", tokens)

    def get_max_tokens(self) -> int:
        """Get the maximum number of tokens."""
        return self.max_tokens

    def set_num_thread(self, threads: int) -> None:
        """Set the number of threads."""
        os.environ[self._NUM_THREAD] = str(threads)
        self.num_thread = threads
        self.notify_observers("num_thread", threads)

    def get_num_thread(self) -> int:
        """Get the number of threads."""
        return self.num_thread

    def set_num_gpu(self, gpus: int) -> None:
        """Set the number of GPUs."""
        os.environ[self._NUM_GPU] = str(gpus)
        self.num_gpu = gpus
        self.notify_observers("num_gpu", gpus)

    def get_num_gpu(self) -> int:
        """Get the number of GPUs."""
        return self.num_gpu

    def set_backend_name(self, name: str) -> None:
        """Set the backend name."""
        os.environ[self._BACKEND_NAME] = name
        self.backend_name = name
        self.notify_observers("backend_name", name)

    def get_backend_name(self) -> str:
        """Get the backend name."""
        return self.backend_name

    def set_verbosity_level(self, level: int) -> None:
        """Set the verbosity level (0-2). 2=DEBUG, 1=INFO, 0=NO logging."""
        if level not in [0, 1, 2]:
            raise ValueError("Verbosity level must be 0, 1, or 2")

        level_map = {0: None, 1: "INFO", 2: "DEBUG"}
        log_level = level_map[level]

        nxlu_logger_cfg = next(
            (logger for logger in self.logging_config.loggers if logger.name == "nxlu"),
            None,
        )

        if level == 0:
            if nxlu_logger_cfg:
                self.logging_config.loggers.remove(nxlu_logger_cfg)
                self.notify_observers("remove_logger", "nxlu")
        elif nxlu_logger_cfg:
            nxlu_logger_cfg.level = log_level
            for handler in nxlu_logger_cfg.handlers:
                handler.level = log_level
            self.notify_observers("update_logger", "nxlu")
        else:
            new_logger = LoggerConfig(
                name="nxlu",
                level=log_level,
                handlers=[
                    LoggingHandlerConfig(
                        handler_type="console",
                        level=log_level,
                        formatter="%(asctime)s - %(name)s - %(levelname)s - % "
                        "(message)s",
                    )
                ],
            )
            self.logging_config.loggers.append(new_logger)
            self.notify_observers("add_logger", "nxlu")

        self.notify_observers("verbosity_level", level)

    def set_include_algorithms(self, algorithms: list[str]) -> None:
        """Specify algorithms to include explicitly."""
        self.include_algorithms = algorithms
        self.notify_observers("include_algorithms", algorithms)

    def set_exclude_algorithms(self, algorithms: list[str]) -> None:
        """Specify algorithms to exclude explicitly."""
        self.exclude_algorithms = algorithms
        self.notify_observers("exclude_algorithms", algorithms)

    def set_enable_classification(self, enable: bool) -> None:
        """Enable or disable automatic algorithm classification."""
        self.enable_classification = enable
        self.notify_observers("enable_classification", enable)

    def set_enable_resource_constraints(self, enable: bool) -> None:
        """Enable or disable algorithm filtering based on compute resource
        availability.
        """
        self.enable_resource_constraints = enable
        self.notify_observers("enable_resource_constraints", enable)

    def set_enable_subgraph_retrieval(self, enable: bool) -> None:
        """Enable or disable subgraph selection based on semantic similarity."""
        self.enable_subgraph_retrieval = enable
        self.notify_observers("enable_subgraph_retrieval", enable)

    def set_embedding_model_name(self, embedding_model_name: str) -> None:
        """Set the embedding model name."""
        self.embedding_model_name = embedding_model_name
        self.notify_observers("embedding_model_name", embedding_model_name)

    def get_embedding_model_name(self) -> int:
        """Get the embedding model name."""
        return self.embedding_model_name


_config = NxluConfig()
