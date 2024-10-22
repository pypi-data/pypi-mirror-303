"""Provides a set of factories for tests to generate fake objects and fixtures."""

from unittest.mock import MagicMock

from promptarchitect.prompting import EngineeredPrompt


def create_prompt_with_response(response: str) -> EngineeredPrompt:
    """
    Create a fake engineered prompt with a fixed response.

    Parameters
    ----------
    response : str
        The response that the prompt should return.

    Returns
    -------
    EngineeredPrompt
        The engineered prompt with the fixed response.
    """
    prompt = MagicMock()
    prompt.run = MagicMock()
    prompt.run.return_value = response
    prompt.specification = MagicMock()
    prompt.specification.filename = "test01.prompt"

    return prompt  # noqa
