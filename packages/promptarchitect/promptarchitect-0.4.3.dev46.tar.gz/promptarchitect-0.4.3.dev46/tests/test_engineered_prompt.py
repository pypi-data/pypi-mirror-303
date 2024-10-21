import logging

import pytest
from dotenv import load_dotenv
from promptarchitect.prompting import EngineeredPrompt
from promptarchitect.specification import (
    EngineeredPromptMetadata,
    EngineeredPromptSpecification,
)

load_dotenv()

LOGGER = logging.getLogger(__name__)

valid_prompt_content = """
---
provider: openai
model: gpt-4o
input: input.txt
output: output.txt
author: John Doe
date_created: 2023/10/01
description: This is a test description.
---
This is a test prompt.
"""

templated_prompt_content = """
---
provider: ollama
model: gemma2
author: Jane Smith
date_created: 2023/09/15
description: This is a templated prompt.
---
This is a {{text}} prompt, with a {{variable}}.
{{variable}}

{{input}}
"""


@pytest.fixture
def templated_prompt_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "template.txt"
    p.write_text(templated_prompt_content)
    return p


# Define fixtures to use in your tests
@pytest.fixture
def valid_prompt_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "prompt.txt"
    p.write_text(valid_prompt_content)
    return p


@pytest.fixture
def valid_specification():
    return EngineeredPromptSpecification(
        metadata=EngineeredPromptMetadata(
            provider="openai",
            model="gpt-4o-mini",
            input="input.txt",
            author="John Doe",
            date_created="2023/10/01",
            description="This is a test description.",
        ),
        filename="test_prompt.prompt",
        prompt="Give a list of 5 blog post titles for a post about {{input}}",
    )


def test_initialize_specification(valid_specification):
    engineered_prompt = EngineeredPrompt(specification=valid_specification)

    # The specification contains also the optional fields, so we
    # have to compare the fields that are set in the specification
    assert engineered_prompt.specification.metadata.provider == "openai"
    assert engineered_prompt.specification.metadata.model == "gpt-4o-mini"
    assert engineered_prompt.specification.metadata.input == "input.txt"
    assert engineered_prompt.specification.metadata.author == "John Doe"
    assert engineered_prompt.specification.metadata.date_created == "2023/10/01"
    assert (
        engineered_prompt.specification.metadata.description
        == "This is a test description."
    )
    assert (
        engineered_prompt.specification.prompt
        == "Give a list of 5 blog post titles for a post about {{input}}"
    )


def test_initialize__from_file(valid_prompt_file):
    engineered_prompt = EngineeredPrompt(prompt_file=str(valid_prompt_file))

    assert engineered_prompt.specification.metadata.provider == "openai"
    assert engineered_prompt.specification.metadata.model == "gpt-4o"
    assert engineered_prompt.specification.metadata.author == "John Doe"
    assert engineered_prompt.specification.metadata.date_created == "2023/10/01"
    assert (
        engineered_prompt.specification.metadata.description
        == "This is a test description."
    )


def test_initialize__from_file_to_specification(valid_prompt_file):
    engineered_prompt = EngineeredPrompt(
        EngineeredPromptSpecification.from_file(str(valid_prompt_file)),
    )

    assert engineered_prompt.specification.metadata.provider == "openai"
    assert engineered_prompt.specification.metadata.model == "gpt-4o"
    assert engineered_prompt.specification.metadata.author == "John Doe"
    assert engineered_prompt.specification.metadata.date_created == "2023/10/01"
    assert (
        engineered_prompt.specification.metadata.description
        == "This is a test description."
    )


def test_initialize_without_options():
    expected_error_message = "Either specification or prompt_file must be provided."
    with pytest.raises(ValueError, match=expected_error_message):
        EngineeredPrompt()


def test_initialize_with_too_many_options(valid_prompt_file):
    expected_error_message = "Only one of specification or prompt_file can be provided."

    with pytest.raises(ValueError, match=expected_error_message):
        EngineeredPrompt(
            specification=EngineeredPromptSpecification.from_file(
                str(valid_prompt_file),
            ),
            prompt_file=str(valid_prompt_file),
        )


@pytest.mark.llm
def test_run(valid_specification):
    engineered_prompt = EngineeredPrompt(specification=valid_specification)
    result = engineered_prompt.run("Prompt testing")

    assert result is not None


@pytest.mark.llm
def test_run_errors(valid_prompt_file):
    engineered_prompt = EngineeredPrompt(prompt_file=valid_prompt_file)
    expected_error_message = "Only one of input_text or input_file can be provided."

    with pytest.raises(ValueError, match=expected_error_message):
        engineered_prompt.run(input_text="Prompt testing", input_file="input.txt")


@pytest.mark.llm
def test_run_template(templated_prompt_file):
    engineered_prompt = EngineeredPrompt(prompt_file=templated_prompt_file)
    result = engineered_prompt.run(properties={"text": "test", "variable": "variable"})

    assert result is not None


@pytest.mark.llm
def test_run_template_some_properties(templated_prompt_file, caplog):
    engineered_prompt = EngineeredPrompt(prompt_file=templated_prompt_file)
    with caplog.at_level(logging.WARNING):
        _ = engineered_prompt.run(properties={"variable": "variable"})

    # The number of mustaches in the prompt is not equal to the number of properties
    # This should raise a warning

    assert "Mustaches mismatch:" in caplog.text


@pytest.mark.llm
def test_run_template_unknown_properties(templated_prompt_file):
    engineered_prompt = EngineeredPrompt(prompt_file=templated_prompt_file)
    result = engineered_prompt.run(
        properties={"text": "test", "variable": "variable", "unknown": "unknown"},
    )

    assert result is not None


@pytest.mark.llm
def test_number_of_mustache_variables(templated_prompt_file):
    engineered_prompt = EngineeredPrompt(prompt_file=templated_prompt_file)
    mustaches = engineered_prompt._number_of_mustaches_in_prompt()

    assert mustaches == 2


def test_id_in_dictionary_for_serialization():
    specification = EngineeredPromptSpecification(
        metadata=EngineeredPromptMetadata(
            provider="openai",
            model="gpt-4o-mini",
            input="input.txt",
            author="John Doe",
            date_created="2023/10/01",
            description="This is a test description.",
        ),
        filename="test_prompt.prompt",
        prompt="Give a list of 5 blog post titles for a post about {{input}}",
    )

    engineered_prompt = EngineeredPrompt(specification=specification)

    assert "id" in engineered_prompt.to_dict()
