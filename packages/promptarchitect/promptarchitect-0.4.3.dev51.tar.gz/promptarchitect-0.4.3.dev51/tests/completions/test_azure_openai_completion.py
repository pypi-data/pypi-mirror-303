import pytest
from dotenv import load_dotenv
from promptarchitect.completions.azure_openai import AzureOpenAICompletion

load_dotenv()


@pytest.mark.llm
def test_completion():
    completion = AzureOpenAICompletion("You're a friendly assistant.", model="gpt-4o")
    prompt = "What is the capital of France?"

    response = completion.completion(prompt)

    assert response is not None


@pytest.mark.llm
def test_completion_json_format():
    completion = AzureOpenAICompletion(
        "You're a friendly assistant.",
        parameters={"output_format": "json"},
        model="gpt-4o",
    )

    prompt = "What is the capital of France? Answer the question in a JSON object."

    response = completion.completion(prompt)

    assert response is not None
    assert completion.is_json
    assert not completion.is_markdown


@pytest.mark.llm
def test_completion_markdown_format():
    completion = AzureOpenAICompletion(
        "You're a friendly assistant.",
        parameters={"output_format": "markdown"},
    )

    prompt = "What is the capital of France? Put the answer in a markdown block."

    response = completion.completion(prompt)

    assert response is not None
    assert completion.is_json is False
    assert completion.is_markdown is True


@pytest.mark.llm
def test_assign_parameters():
    parameters = {"temperature": 0.7, "top_p": 0.9}
    completion = AzureOpenAICompletion(
        "You're a friendly assistant.", parameters=parameters, model="gpt-4o"
    )

    assert completion.parameters == parameters
    assert completion.model == "gpt-4o"


@pytest.mark.llm
def test_cost_and_duration():
    completion = AzureOpenAICompletion("You're a friendly assistant.")
    prompt = "What is the capital of France?"

    completion.completion(prompt)

    assert completion.cost is not None
    assert completion.duration is not None


@pytest.mark.llm
def test_run_with_parameters():
    parameters = {"temperature": 0.1, "top_p": 0.1, "max_tokens": 10}
    completion = AzureOpenAICompletion(
        "You're a friendly assistant.",
        parameters=parameters,
    )

    response = completion.completion("What is the capital of France?")

    assert completion.parameters == parameters
    assert response is not None
    assert "Paris" in response
    assert completion.input_tokens is not None
    assert completion.output_tokens is not None
    assert completion.cost is not None


@pytest.mark.llm
def test_run_with_parameters_containing_none_values():
    parameters = {"temperature": None, "top_p": None, "max_tokens": None}
    completion = AzureOpenAICompletion(
        "You're a friendly assistant.",
        parameters=parameters,
    )

    response = completion.completion("What is the capital of France?")

    assert completion.parameters == parameters
    assert response is not None
    assert "Paris" in response
    assert completion.input_tokens is not None
    assert completion.output_tokens is not None
    assert completion.cost is not None
