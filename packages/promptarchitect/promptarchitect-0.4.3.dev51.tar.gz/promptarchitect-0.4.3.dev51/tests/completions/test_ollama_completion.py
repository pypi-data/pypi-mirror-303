import pytest
from dotenv import load_dotenv
from promptarchitect.completions.ollama import OllamaCompletion

load_dotenv()


@pytest.mark.llm
def test_completion():
    parameters = {"temperature": 0.7, "top_p": 0.2}
    completion = OllamaCompletion(
        "You're a friendly assistant.",
        model="gemma2",
        parameters=parameters,
    )

    prompt = "What is the capital of France?"

    response = completion.completion(prompt)

    assert response is not None
    assert "Paris" in response
    assert completion.parameters == parameters
    assert completion.cost is not None
    assert completion.duration is not None


@pytest.mark.llm
def test_completion_json_format():
    parameters = {"temperature": 0.7, "top_p": 0.2, "response_format": "json"}
    completion = OllamaCompletion(
        "You're a friendly assistant.",
        model="gemma2",
        parameters=parameters,
    )

    prompt = "What is the capital of France?"

    completion.completion(prompt)

    assert completion.is_json
    assert not completion.is_markdown


@pytest.mark.llm
def test_completion_markdown_format():
    parameters = {"temperature": 0.7, "top_p": 0.2, "response_format": "markdown"}

    completion = OllamaCompletion(
        "You're a friendly assistant.",
        model="gemma2",
        parameters=parameters,
    )

    prompt = "What is the capital of France?"

    completion.completion(prompt)

    assert not completion.is_json
    assert completion.is_markdown
