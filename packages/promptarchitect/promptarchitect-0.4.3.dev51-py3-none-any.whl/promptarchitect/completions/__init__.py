"""Completions for engineered prompts.

This module contains the logic for creating completions based on engineered prompts.
Completions integrate the concept of an engineered prompt with the LLM provides that
we support.

We currently support the following LLM providers:

- Ollama
- OpenAI
- Claude
- Azure OpenAI

The `create_completion` function creates a completion based on the specified provider
and model. It's used by `EngineeredPrompt` when you call `execute` on an
engineered prompt.
"""

from promptarchitect.completions.core import Completion
from promptarchitect.specification import EngineeredPromptMetadata


def create_completion(
    provider: str,
    model: str,
    metadata: EngineeredPromptMetadata,
    system_role: str,
) -> Completion:
    """Create a completion based on the specified provider and model.

    Arguments
    ---------
    provider : str
        The provider to use for the completion.
    model : str
        The model to use for the completion.
    metadata : EngineeredPromptMetadata
        The metadata of the engineered prompt.
    system_role : str
        The system role in the communication with the LLM provider.
    """
    from promptarchitect.completions.anthropic import AnthropicCompletion
    from promptarchitect.completions.ollama import OllamaCompletion
    from promptarchitect.completions.openai import OpenAICompletion
    from promptarchitect.completions.azure_openai import AzureOpenAICompletion

    parameters = _get_model_parameters(metadata)

    if provider == "ollama":
        return OllamaCompletion(system_role, model, parameters)
    if provider == "openai":
        return OpenAICompletion(system_role, model, parameters)
    if provider == "anthropic":
        return AnthropicCompletion(system_role, model, parameters)
    if provider == "azure_openai":
        return AzureOpenAICompletion(system_role, model, parameters)

    error_message = f"Provider {provider} is not supported."
    raise ValueError(error_message)


def _get_model_parameters(metadata: EngineeredPromptMetadata) -> dict:
    return {
        "temperature": metadata.temperature,
        "max_tokens": metadata.max_tokens,
        "frequency_penalty": metadata.frequency_penalty,
        "presence_penalty": metadata.presence_penalty,
        "output_format": metadata.output_format,
    }
