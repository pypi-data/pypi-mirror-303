import pytest
from promptarchitect.specification import (
    EngineeredPromptMetadata,
    FormatTestSpecification,
    Limits,
    MetricTestSpecification,
    PreciseLimits,
    PropertyTestSpecification,
    QuestionTestSpecification,
)
from pydantic import ValidationError


def test_engineered_prompt_metadata_required_fields():
    metadata = EngineeredPromptMetadata(provider="openai", model="gpt-4o-mini")
    assert metadata.provider == "openai"
    assert metadata.model == "gpt-4o-mini"
    assert metadata.test_path is None
    assert metadata.tests == {}


def test_engineered_prompt_metadata_optional_fields():
    metadata = EngineeredPromptMetadata(
        provider="openai",
        model="gpt-4o-mini",
        test_path="/path/to/tests",
        tests={
            "test1": MetricTestSpecification(
                metric="accuracy",
                input={"text": "sample"},
                limit=PreciseLimits(min=0.5, max=1.0),
            ),
        },
    )
    assert metadata.provider == "openai"
    assert metadata.model == "gpt-4o-mini"
    assert metadata.test_path == "/path/to/tests"
    assert "test1" in metadata.tests
    assert metadata.tests["test1"].type == "metric"


def test_engineered_prompt_metadata_missing_required_fields():
    with pytest.raises(ValidationError) as excinfo:
        EngineeredPromptMetadata(model="gpt-3")
    assert "Field required" in str(excinfo.value)


def test_engineered_prompt_metadata_invalid_tests():
    with pytest.raises(ValidationError) as excinfo:
        EngineeredPromptMetadata(
            provider="openai",
            model="gpt-4o-mini",
            tests={
                "test1": {
                    "type": "invalid",
                    "metric": "accuracy",
                    "input": {"text": "sample"},
                    "limit": PreciseLimits(min=0.5, max=1.0),
                },
            },
        )
    assert "Input tag 'invalid' found" in str(excinfo.value)


def test_engineered_prompt_metadata_valid_property_test():
    metadata = EngineeredPromptMetadata(
        provider="openai",
        model="gpt-4o-mini",
        tests={
            "test1": PropertyTestSpecification(
                type="property",
                unit="words",
                limit=Limits(min=10, max=100),
            ),
        },
    )
    assert metadata.tests["test1"].type == "property"
    assert metadata.tests["test1"].unit == "words"
    assert metadata.tests["test1"].limit.min == 10
    assert metadata.tests["test1"].limit.max == 100


def test_engineered_prompt_metadata_valid_format_test():
    metadata = EngineeredPromptMetadata(
        provider="openai",
        model="gpt-4o-mini",
        tests={"test1": FormatTestSpecification(type="format", format="json")},
    )
    assert metadata.tests["test1"].type == "format"
    assert metadata.tests["test1"].format == "json"


def test_engineered_prompt_metadata_valid_question_test():
    metadata = EngineeredPromptMetadata(
        provider="openai",
        model="gpt-4o-mini",
        tests={
            "test1": QuestionTestSpecification(type="question", prompt="What is AI?"),
        },
    )
    assert metadata.tests["test1"].type == "question"
    assert metadata.tests["test1"].prompt == "What is AI?"
