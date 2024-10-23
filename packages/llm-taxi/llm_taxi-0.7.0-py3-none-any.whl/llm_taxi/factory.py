import os
from collections.abc import Mapping
from enum import Enum
from typing import Any

from llm_taxi.embeddings import GoogleEmbedding, MistralEmbedding, OpenAIEmbedding
from llm_taxi.llms import (
    Anthropic,
    BigModel,
    DashScope,
    DeepInfra,
    DeepSeek,
    Google,
    Groq,
    Mistral,
    OpenAI,
    OpenRouter,
    Perplexity,
    Together,
)


class Provider(Enum):
    OpenAI = "openai"
    Google = "google"
    Together = "together"
    Groq = "groq"
    Anthropic = "anthropic"
    Mistral = "mistral"
    Perplexity = "perplexity"
    DeepInfra = "deepinfra"
    DeepSeek = "deepseek"
    OpenRouter = "openrouter"
    DashScope = "dashscope"
    BigModel = "bigmodel"


MODEL_CLASSES: Mapping[
    Provider,
    type[OpenAI]
    | type[Google]
    | type[Together]
    | type[Groq]
    | type[Anthropic]
    | type[Mistral]
    | type[Perplexity]
    | type[DeepInfra]
    | type[DeepSeek]
    | type[OpenRouter]
    | type[DashScope]
    | type[BigModel],
] = {
    Provider.OpenAI: OpenAI,
    Provider.Google: Google,
    Provider.Together: Together,
    Provider.Groq: Groq,
    Provider.Anthropic: Anthropic,
    Provider.Mistral: Mistral,
    Provider.Perplexity: Perplexity,
    Provider.DeepInfra: DeepInfra,
    Provider.DeepSeek: DeepSeek,
    Provider.OpenRouter: OpenRouter,
    Provider.DashScope: DashScope,
    Provider.BigModel: BigModel,
}

EMBEDDING_CLASSES: Mapping[
    Provider,
    type[GoogleEmbedding] | type[OpenAIEmbedding] | type[MistralEmbedding],
] = {
    Provider.OpenAI: OpenAIEmbedding,
    Provider.Mistral: MistralEmbedding,
    Provider.Google: GoogleEmbedding,
}


def _get_env(key: str) -> str:
    if (value := os.getenv(key)) is None:
        msg = f"Required environment variable `{key}` not found"
        raise KeyError(msg)

    return value


def _get_class_name_and_class(
    model: str,
    class_dict: Mapping[Provider, type],
) -> tuple[str, type]:
    provider_name, model = model.split(":", 1)

    try:
        provider = Provider(provider_name)
    except ValueError as error:
        msg = f"Unknown LLM provider: {provider_name}"
        raise ValueError(msg) from error

    return model, class_dict[provider]


def _get_params(
    cls: (
        type[OpenAI]
        | type[Google]
        | type[Together]
        | type[Groq]
        | type[Anthropic]
        | type[Mistral]
        | type[Perplexity]
        | type[DeepInfra]
        | type[DeepSeek]
        | type[OpenRouter]
        | type[DashScope]
        | type[GoogleEmbedding]
        | type[OpenAIEmbedding]
        | type[MistralEmbedding]
    ),
    local_vars: dict[str, Any],
) -> dict[str, str]:
    env_var_values: dict[str, str] = {}
    for key, env_name in cls.env_vars.items():
        value = (
            params
            if (params := local_vars.get(key)) is not None
            else _get_env(env_name)
        )
        env_var_values[key] = value

    return env_var_values


def llm(
    model: str,
    api_key: str | None = None,
    base_url: str | None = None,
    call_options: dict[str, Any] | None = None,
    client_options: dict[str, Any] | None = None,
) -> (
    OpenAI
    | Google
    | Together
    | Groq
    | Anthropic
    | Mistral
    | Perplexity
    | DeepInfra
    | DeepSeek
    | OpenRouter
    | DashScope
    | BigModel
):
    """Initialize and return an instance of a specified LLM (Large Language Model) provider.

    Args:
        model (str): The model identifier in the format 'provider:model_name'.
        api_key (str | None, optional): The API key for authentication. Defaults to None.
        base_url (str | None, optional): The base URL for the API. Defaults to None.
        call_options (dict[str, Any] | None, optional): Additional keyword arguments for the API call. Defaults to None.
        client_options (dict[str, Any] | None, optional): Additional keyword arguments for the LLM client initialization.

    Returns:
        LLM: An instance of the specified LLM provider.

    Raises:
        ValueError: If the specified provider is unknown.
        KeyError: If a required environment variable is not found.
    """
    model, model_class = _get_class_name_and_class(model, MODEL_CLASSES)
    env_var_values = _get_params(model_class, locals())

    return model_class(
        model=model,
        **env_var_values,
        call_options=call_options,
        client_options=client_options,
    )


def embedding(
    model: str,
    api_key: str | None = None,
    base_url: str | None = None,
    call_options: dict[str, Any] | None = None,
    client_options: dict[str, Any] | None = None,
) -> GoogleEmbedding | OpenAIEmbedding | MistralEmbedding:
    """Initialize and return an instance of a specified embedding provider.

    Args:
        model (str): The model identifier in the format 'provider:model_name'.
        api_key (str | None, optional): The API key for authentication. Defaults to None.
        base_url (str | None, optional): The base URL for the API. Defaults to None.
        call_options (dict[str, Any] | None, optional): Additional keyword arguments for the API call. Defaults to None.
        client_options (dict[str, Any] | None, optional): Additional keyword arguments for the embedding client initialization.

    Returns:
        Embedding: An instance of the specified embedding provider.

    Raises:
        ValueError: If the specified provider is unknown.
        KeyError: If a required environment variable is not found.
    """
    model, embedding_class = _get_class_name_and_class(model, EMBEDDING_CLASSES)
    env_var_values = _get_params(embedding_class, locals())

    return embedding_class(
        model=model,
        **env_var_values,
        call_options=call_options,
        client_options=client_options,
    )
