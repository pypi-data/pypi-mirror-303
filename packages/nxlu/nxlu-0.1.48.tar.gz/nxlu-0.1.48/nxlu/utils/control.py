import logging
import sys
import warnings
from typing import Any

import psutil

from nxlu.config import AnthropicModel, Framework, LocalModel, NxluConfig, OpenAIModel

warnings.filterwarnings("ignore")

sys.set_int_max_str_digits(0)


logger = logging.getLogger("nxlu")

__all__ = ["ResourceManager", "init_llm_model"]


class ResourceManager:
    def __init__(self, max_time: float | None = None, max_space: float | None = None):
        """Manage resource limits such as time and space for graph-related operations.

        If the maximum time (`max_time`) or space (`max_space`) are not provided,
        they are dynamically determined based on system resources (CPU and memory).

        Parameters
        ----------
        max_time : float, optional
            Maximum allowable time cost in seconds. If None, dynamically calculated
            based on CPU resources.
        max_space : float, optional
            Maximum allowable space cost in bytes. If None, dynamically calculated as a
            fraction of available memory.

        Attributes
        ----------
        max_time : float
            The maximum allowed time, either provided or dynamically determined.
        max_space : float
            The maximum allowed space in bytes, either provided or dynamically
            determined.

        Methods
        -------
        is_within_limits(estimated_time, estimated_space)
            Check if the provided time and space estimates are within the allowed
            limits.
        update_limits(new_time, new_space)
            Update the maximum allowed time and space.
        get_limits()
            Retrieve the current time and space limits.
        """
        if max_time is not None and max_time < 0:
            raise ValueError("max_time must be non-negative.")
        if max_space is not None and max_space < 0:
            raise ValueError("max_space must be non-negative.")

        if max_time is None:
            self.max_time = self._determine_max_time()
            logger.info(
                f"max_time not provided. Dynamically set to {self.max_time:.2f} time "
                f"units based on CPU resources."
            )
        else:
            self.max_time = max_time
            logger.info(f"max_time explicitly set to {self.max_time} time units.")

        if max_space is None:
            self.max_space = self._determine_max_space()
            logger.info(
                f"max_space not provided. Dynamically set to "
                f"{self.max_space / (1024**3):.2f} GB based on available memory."
            )
        else:
            self.max_space = max_space
            logger.info(
                f"max_space explicitly set to {self.max_space / (1024**3):.2f} GB."
            )

    def _determine_max_time(self, max_allowed_time=3600) -> float:
        """Determine a reasonable default maximum time based on CPU resources.

        The method considers the number of CPU cores and their frequency to dynamically
        calculate a time limit, capped at `max_allowed_time` seconds.

        Parameters
        ----------
        max_allowed_time : float, optional
            The maximum allowable time to be used if calculated time exceeds this
            value. Default is 3600 seconds.

        Returns
        -------
        float
            The dynamically calculated maximum time limit in seconds.
        """
        cpu_count = psutil.cpu_count(logical=True) or 1
        cpu_freq_info = psutil.cpu_freq()
        cpu_freq = (
            cpu_freq_info.current if cpu_freq_info else 2.5
        )  # default to 2.5 GHz if unavailable

        # reduce the base scaling factor to make sure the total time is within
        # reasonable bounds.
        base_time_per_core = 30

        # calculate max_time as a function of CPU count and frequency, with a
        # cap.
        max_time = min(
            cpu_count * base_time_per_core * (cpu_freq / 2.5), max_allowed_time
        )

        logger.info(
            f"Determined max_time based on CPU: {max_time:.2f} seconds (CPU cores: "
            f"{cpu_count}, Frequency: {cpu_freq:.2f} GHz)"
        )

        return max_time

    def _determine_max_space(self, percent_of_available=0.9) -> float:
        """Determine a reasonable default maximum space based on available memory.

        Parameters
        ----------
        percent_of_available : float, optional
            The percentage of available system memory to use for the maximum space
            calculation. Default is 90%.

        Returns
        -------
        float
            The dynamically calculated maximum space in bytes.
        """
        virtual_mem = psutil.virtual_memory()
        available_memory = virtual_mem.available  # in bytes

        max_space = available_memory * percent_of_available

        return max_space

    def is_within_limits(self, estimated_time: Any, estimated_space: Any) -> bool:
        """Check if estimated time and space costs are within predefined limits."""
        try:
            estimated_time_float = float(estimated_time)
        except (OverflowError, ValueError, TypeError):
            logger.warning("Estimated time is not a valid number.")
            return False

        try:
            estimated_space_float = float(estimated_space)
        except (OverflowError, ValueError, TypeError):
            logger.warning("Estimated space is not a valid number.")
            return False

        if self.max_time >= 0:
            time_within = estimated_time_float <= self.max_time
        else:
            time_within = estimated_time_float >= self.max_time

        if self.max_space >= 0:
            space_within = estimated_space_float <= self.max_space
        else:
            space_within = estimated_space_float >= self.max_space

        if not time_within:
            if self.max_time >= 0:
                logger.warning(
                    f"Estimated time {estimated_time_float} exceeds max_time "
                    f"{self.max_time}."
                )
            else:
                logger.warning(
                    f"Estimated time {estimated_time_float} is below min_time "
                    f"{self.max_time}."
                )

        if not space_within:
            if self.max_space >= 0:
                logger.warning(
                    f"Estimated space {estimated_space_float / (1024**3):.2f} GB "
                    f"exceeds max_space {self.max_space / (1024**3):.2f} GB."
                )
            else:
                logger.warning(
                    f"Estimated space {estimated_space_float / (1024**3):.2f} GB is "
                    f"below min_space {self.max_space / (1024**3):.2f} GB."
                )

        return time_within and space_within

    def update_limits(self, new_time: float, new_space: float):
        """Update the maximum time and space limits.

        Parameters
        ----------
        new_time : float
            The new maximum allowed time in seconds.
        new_space : float
            The new maximum allowed space in bytes.
        """
        self.max_time = new_time
        self.max_space = new_space
        logger.info(
            f"Updated max_time to {self.max_time:e} time units and max_space to "
            f"{self.max_space / (1024**3):e} GB."
        )

    def get_limits(self) -> dict[str, float]:
        """Get the current time and space limits.

        Returns
        -------
        dict
            A dictionary containing the keys 'max_time' and 'max_space' with the
            corresponding values in seconds and bytes, respectively.
        """
        return {"max_time": self.max_time, "max_space": self.max_space}


def init_llm_model(config: NxluConfig) -> Any:
    """Initialize the appropriate LLM based on the current configuration and framework.

    Parameters
    ----------
    config : NxluConfig
        The configuration object containing model settings.

    Returns
    -------
    Any
        An instance of the initialized LLM.

    Raises
    ------
    ValueError
        If the specified model or framework is not supported.
    """
    model_name = config.get_model_name()
    temperature = config.get_temperature()
    max_tokens = config.get_max_tokens()
    num_gpu = config.get_num_gpu()
    anthropic_api_key = config.get_anthropic_api_key()
    framework = config.get_llm_framework()

    if framework == Framework.LANGCHAIN:
        from langchain_community.chat_models import (
            ChatAnthropic as LangChainChatAnthropic,
        )
        from langchain_community.chat_models import ChatOpenAI as LangChainChatOpenAI
        from langchain_community.llms import Ollama as LangChainOllama

        if model_name in [model.value for model in OpenAIModel]:
            return LangChainChatOpenAI(
                temperature=temperature,
                openai_api_key=config.get_openai_api_key(),
                model_name=model_name,
                max_tokens=max_tokens,
            )
        if model_name in [model.value for model in LocalModel]:
            return LangChainOllama(
                model=model_name,
                num_gpu=num_gpu,
                temperature=temperature,
            )
        if model_name in [model.value for model in AnthropicModel]:
            return LangChainChatAnthropic(
                model=model_name,
                temperature=temperature,
                max_tokens_to_sample=max_tokens,
                anthropic_api_key=anthropic_api_key,
            )
        raise ValueError(f"Model {model_name} is not supported in LangChain framework.")

    if framework == Framework.LLAMAINDEX:
        from llama_index.llms.anthropic import Anthropic as LlamaAnthropic
        from llama_index.llms.ollama import Ollama as LlamaOllama
        from llama_index.llms.openai import OpenAI as LlamaOpenAI

        if model_name in [model.value for model in OpenAIModel]:
            return LlamaOpenAI(
                temperature=temperature,
                openai_api_key=config.get_openai_api_key(),
                model_name=model_name,
                max_tokens=max_tokens,
            )
        if model_name in [model.value for model in LocalModel]:
            return LlamaOllama(
                model=model_name,
                num_gpu=num_gpu,
                temperature=temperature,
            )
        if model_name in [model.value for model in AnthropicModel]:
            return LlamaAnthropic(
                model=model_name,
                temperature=temperature,
                max_tokens_to_sample=max_tokens,
                anthropic_api_key=anthropic_api_key,
            )
        raise ValueError(
            f"Model {model_name} is not supported in LlamaIndex framework."
        )
    raise ValueError(f"Framework {framework} is not supported.")
