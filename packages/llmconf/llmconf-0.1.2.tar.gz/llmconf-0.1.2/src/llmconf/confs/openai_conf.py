import os

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class OpenAIConf:
    # Defined at: openai._clinet.OpenAI.__init__
    # Link: https://github.com/openai/openai-python/blob/main/src/openai/_client.py

    api_key: str | None = field(default_factory=lambda: os.getenv("OPENAI_API_KEY", None))
    organization: str | None = field(default_factory=lambda: os.getenv("OPENAI_API_KEY", None))
    project: str | None = field(default_factory=lambda: os.getenv("OPENAI_API_KEY", None))
    base_url: str | None = field(default_factory=lambda: os.getenv("OPENAI_API_KEY", None))
    timeout: float | None = None
    max_retries: int | None = None

    # Defined at: openai.resources.chat.completions.Completions.create
    # Link: https://github.com/openai/openai-python/blob/main/src/openai/resources/chat/completions.py

    messages: list[dict[str, str]] | None = None
    model: str | None = None
    frequency_penalty: float | None = None
    logit_bias: dict[str, int] | None = None
    logprobs: bool | None = None
    max_completion_tokens: int | None = None
    max_tokens: int | None = None
    n: int | None = None
    presence_penalty: float | None = None
    seed: int | None = None
    temperature: float | None = None
    top_logprobs: int | None = None
    top_p: float | None = None
    user: str | None = None
