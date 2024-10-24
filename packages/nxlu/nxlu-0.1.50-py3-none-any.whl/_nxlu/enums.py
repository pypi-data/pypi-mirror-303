from enum import Enum

__all__ = ["Framework", "OpenAIModel", "AnthropicModel", "LocalModel"]


class Framework(str, Enum):
    LANGCHAIN = "langchain"
    LLAMAINDEX = "llamaindex"


class OpenAIModel(str, Enum):
    GPT_4_TURBO = "gpt-4-turbo"
    GPT_4 = "gpt-4"
    GPT_4O = "gpt-4o-2024-08-06"
    GPT_4O_MINI = "gpt-4o-mini"
    GPT_4O1_PREVIEW = "o1-preview"
    GPT_401_MINI = "o1-mini"


class AnthropicModel(str, Enum):
    CLAUDE_2 = "claude-2"
    CLAUDE_2_0 = "claude-2.0"
    CLAUDE_INSTANT = "claude-instant"
    CLAUDE_INSTANT_1 = "claude-instant-1"
    CLAUDE_INSTANT_1_1 = "claude-instant-1.1"
    CLAUDE_3_5_SONNET = "claude-3.5-sonnet"
    CLAUDE_3_SONNET = "claude-3-sonnet"


class LocalModel(str, Enum):
    LLAMA3_70B = "llama3:70b"
    LLAMA3_8B = "llama3:8b"
    GEMMA2_9B = "gemma2:9b"
    QWEN2_7B = "qwen2:7b"
