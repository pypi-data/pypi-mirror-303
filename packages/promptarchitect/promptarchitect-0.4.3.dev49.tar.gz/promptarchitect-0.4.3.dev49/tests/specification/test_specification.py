import pytest
from promptarchitect.specification import (
    EngineeredPromptMetadata,
    EngineeredPromptSpecification,
    Limits,
    PropertyTestSpecification,
)
from pydantic import ValidationError


def test_engineered_prompt_specification_initialization():
    metadata = EngineeredPromptMetadata(
        provider="test_provider",
        model="test_model",
        test_path="test_path",
        tests={
            "test1": PropertyTestSpecification(
                type="property",
                unit="words",
                limit=Limits(min=1, max=10),
            ),
        },
    )

    prompt = "This is a test prompt."

    spec = EngineeredPromptSpecification(metadata=metadata, prompt=prompt)

    assert spec.metadata.provider == "test_provider"
    assert spec.metadata.model == "test_model"
    assert spec.metadata.test_path == "test_path"
    assert spec.metadata.tests["test1"].type == "property"
    assert spec.metadata.tests["test1"].unit == "words"
    assert spec.metadata.tests["test1"].limit.min == 1
    assert spec.metadata.tests["test1"].limit.max == 10
    assert spec.prompt == "This is a test prompt."


def test_engineered_prompt_specification_initialization_with_filename():
    metadata = EngineeredPromptMetadata(
        provider="test_provider",
        model="test_model",
        test_path="test_path",
        tests={
            "test1": PropertyTestSpecification(
                type="property",
                unit="words",
                limit=Limits(min=1, max=10),
            ),
        },
    )

    prompt = "This is a test prompt."

    spec = EngineeredPromptSpecification(
        metadata=metadata,
        prompt=prompt,
        filename="test.prompt",
    )

    assert spec.filename == "test.prompt"


def test_engineered_prompt_specification_from_file():
    spec = EngineeredPromptSpecification.from_file(
        "tests/test_data/test_prompts/valid_prompt.prompt",
    )

    assert spec.metadata.provider == "openai"
    assert spec.metadata.model == "gpt-4o-mini"
    assert spec.metadata.test_path == "inputs"
    assert spec.metadata.tests["test01"].type == "property"
    assert spec.metadata.tests["test01"].unit == "lines"
    assert spec.metadata.tests["test01"].limit.max == 5
    assert spec.prompt == "This is a sample prompt {{input}}."


def test_invalid_engineered_prompt_specification_from_file():
    with pytest.raises(ValidationError):
        EngineeredPromptSpecification.from_file(
            "tests/test_data/test_prompts/invalid_prompt.prompt",
        )
