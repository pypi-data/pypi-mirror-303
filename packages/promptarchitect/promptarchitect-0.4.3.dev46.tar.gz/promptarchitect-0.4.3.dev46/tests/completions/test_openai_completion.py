import pytest
from dotenv import load_dotenv
from promptarchitect.completions.openai import OpenAICompletion

load_dotenv()


@pytest.mark.llm
def test_completion():
    completion = OpenAICompletion("You're a friendly assistant.")
    prompt = "What is the capital of France?"

    response = completion.completion(prompt)

    assert response is not None


@pytest.mark.llm
def test_completion_json_format():
    prompt = "You're a friendly assistant. Put the answer in a JSON object."

    completion = OpenAICompletion(
        prompt,
        "gpt-4o-mini",
        parameters={"output_format": "json"},
    )

    prompt = "What is the capital of France?"

    response = completion.completion(prompt)

    assert response is not None
    assert completion.is_json
    assert not completion.is_markdown


@pytest.mark.llm
def test_completion_markdown_format():
    prompt = "You're a friendly assistant. Put the answer in a markdown block."

    completion = OpenAICompletion(
        prompt,
        "gpt-4o-mini",
        parameters={"output_format": "markdown"},
    )

    prompt = "What is the capital of France?"

    response = completion.completion(prompt)

    assert response is not None
    assert not completion.is_json
    assert completion.is_markdown


@pytest.mark.llm
def test_assign_parameters():
    parameters = {"temperature": 0.7, "top_p": 0.9}
    completion = OpenAICompletion("You're a friendly assistant.", parameters=parameters)

    assert completion.parameters == parameters


@pytest.mark.llm
def test_run_with_parameters():
    parameters = {"temperature": 0.1, "top_p": 0.1, "max_tokens": 10}
    completion = OpenAICompletion("You're a friendly assistant.", parameters=parameters)

    response = completion.completion("What is the capital of France?")

    assert completion.parameters == parameters
    assert response is not None
    assert "Paris" in response


@pytest.mark.llm
def test_cost_and_latency():
    completion = OpenAICompletion("You're a friendly assistant.")
    prompt = "What is the capital of France?"

    completion.completion(prompt)

    assert completion.cost is not None
    assert completion.duration is not None


@pytest.mark.llm
def test_model_unknown_alias():
    expected_message = (
        "Model gpt-1.0 not supported. Check the provider file openai.json."
    )

    with pytest.raises(ValueError, match=expected_message):
        OpenAICompletion("You're a friendly assistant.", model="gpt-1.0")
