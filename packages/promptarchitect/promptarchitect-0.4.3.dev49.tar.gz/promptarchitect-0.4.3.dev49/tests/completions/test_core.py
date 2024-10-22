from pathlib import Path

import pytest
from promptarchitect.completions.ollama import OllamaCompletion
from promptarchitect.exceptions import PromptConfigurationError


def create_invalid_completion():
    return OllamaCompletion(
        "You're a friendly assistant",
        "invalid_model",
        {"provider": "ollama", "model": "invalid_model"},
    )


def create_completion():
    return OllamaCompletion("You're a friendly assistant", "gemma2", {})


@pytest.mark.llm
def test_json_in_fenced_block():
    completion = create_completion()
    sample_response = '```json\n{"key": "value"}\n```'

    response = completion._extract_json(sample_response)

    assert response == '{"key": "value"}'


@pytest.mark.llm
def test_json_in_unmarked_fenced_block():
    completion = create_completion()
    sample_response = '```\n{"key": "value"}\n```'

    response = completion._extract_json(sample_response)

    assert response == '{"key": "value"}'


@pytest.mark.llm
def test_json_in_unmarked_fenced_block_with_list():
    completion = create_completion()
    sample_response = '```\n[{"key": "value"}]\n```'

    response = completion._extract_json(sample_response)

    assert response == '[{"key": "value"}]'


@pytest.mark.llm
def test_json_fenced_with_yapping():
    completion = create_completion()
    sample_response = (
        'Hello, here\'s your json\n```json\n{"key": "value"}\n``` More yapping!'
    )

    response = completion._extract_json(sample_response)

    assert response == '{"key": "value"}'


@pytest.mark.llm
def test_json_list():
    completion = create_completion()
    sample_response = '[{"key": "value"}]'
    response = completion._extract_json(sample_response)

    assert response == '[{"key": "value"}]'


@pytest.mark.llm
def test_json_string():
    completion = create_completion()
    sample_response = '{"key": "value"}'

    response = completion._extract_json(sample_response)

    assert response == '{"key": "value"}'


@pytest.mark.llm
def test_json_object():
    completion = create_completion()
    sample_response = '{"key": "value"}'

    response = completion._extract_json(sample_response)

    assert response == '{"key": "value"}'


@pytest.mark.llm
def test_markdown_fenced():
    completion = create_completion()
    sample_response = "```markdown\n# This is awesome markdown\n```"
    expected_response = "# This is awesome markdown"

    response = completion._extract_markdown(sample_response)

    assert expected_response == response


@pytest.mark.llm
def test_markdown_fenced_code_full():
    completion = create_completion()
    sample_file = Path(__file__).parent / "markdown" / "fenced_code_full.md"
    sample_response = sample_file.read_text()

    expected_response = "# Hello world"

    response = completion._extract_markdown(sample_response)

    assert expected_response == response


@pytest.mark.llm
def test_markdown_fenced_code_prefix():
    completion = create_completion()
    sample_file = Path(__file__).parent / "markdown" / "fenced_code_prefix.md"
    sample_response = sample_file.read_text()

    expected_response = "# Hello world"

    response = completion._extract_markdown(sample_response)

    assert expected_response == response


@pytest.mark.llm
def test_unfenced_markdown():
    completion = create_completion()
    sample_file = Path(__file__).parent / "markdown" / "regular.md"
    sample_response = sample_file.read_text()

    response = completion._extract_markdown(sample_response)

    assert sample_response == response


def test_completion_init_with_invalid_model():
    with pytest.raises(PromptConfigurationError):
        create_invalid_completion()


# def test_completion_init_with_default_model():
#     system_role = "assistant"
#     model = None
#     parameters = {"temperature": 0.7}
#     provider_file = "provider_config.json"

#     completion = Completion(system_role, model, parameters, provider_file)

#     assert completion.system_role == system_role
#     assert completion.model is not None
#     assert completion.parameters == parameters
#     assert completion.provider_file is not None
