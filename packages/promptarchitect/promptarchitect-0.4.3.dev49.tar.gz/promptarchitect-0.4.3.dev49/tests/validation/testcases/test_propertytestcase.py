import pytest
from promptarchitect.prompting import EngineeredPrompt
from promptarchitect.specification import (
    EngineeredPromptMetadata,
    EngineeredPromptSpecification,
    Limits,
    PropertyTestSpecification,
)
from promptarchitect.validation.testcases import (
    PropertyTestCase,
    TestCaseStatus,
)

from tests.validation.objectfactory import create_prompt_with_response


def test_property_test_case_initialization(input_sample):
    prompt = create_prompt_with_response("Hello world!")
    specification = PropertyTestSpecification(unit="words", equals=5)
    test_case = PropertyTestCase("test_id", prompt, input_sample, specification)
    assert test_case.test_id == "test_id"
    assert test_case.prompt == prompt
    assert test_case.input_sample == input_sample
    assert test_case.specification == specification


def test_property_test_case_words_run_equals(input_sample):
    prompt = create_prompt_with_response("hello world")
    specification = PropertyTestSpecification(unit="words", equals=2)
    test_case = PropertyTestCase("test_id", prompt, input_sample, specification)
    outcome = test_case.run()
    assert outcome.status == TestCaseStatus.PASSED
    assert outcome.error_message is None


def test_property_test_case_sentences_run_equals(input_sample):
    prompt = create_prompt_with_response("hello world. everything is fine.")
    specification = PropertyTestSpecification(unit="sentences", equals=2)
    test_case = PropertyTestCase("test_id", prompt, input_sample, specification)
    outcome = test_case.run()
    assert outcome.status == TestCaseStatus.PASSED
    assert outcome.error_message is None


def test_property_test_case_lines_run_equals(input_sample):
    prompt = create_prompt_with_response(
        "hello world.\nEverything is fine.\nAnother line",
    )
    specification = PropertyTestSpecification(unit="lines", equals=3)
    test_case = PropertyTestCase("test_id", prompt, input_sample, specification)
    outcome = test_case.run()
    assert outcome.status == TestCaseStatus.PASSED
    assert outcome.error_message is None


def test_property_test_case_characters_run_equals(input_sample):
    prompt = create_prompt_with_response("hello world.")
    specification = PropertyTestSpecification(unit="characters", equals=12)
    test_case = PropertyTestCase("test_id", prompt, input_sample, specification)
    outcome = test_case.run()
    assert outcome.status == TestCaseStatus.PASSED
    assert outcome.error_message is None


def test_property_test_case_paragraphs_run_equals(input_sample):
    prompt = create_prompt_with_response(
        "hello world.\n\nhello world.\n\nhello world.\n\nhello world.\n\n",
    )

    specification = PropertyTestSpecification(unit="paragraphs", equals=4)
    test_case = PropertyTestCase("test_id", prompt, input_sample, specification)
    outcome = test_case.run()
    assert outcome.status == TestCaseStatus.PASSED
    assert outcome.error_message is None


def test_property_test_case_words_run_limit(input_sample):
    prompt = create_prompt_with_response("hello world")
    specification = PropertyTestSpecification(unit="words", limit=Limits(max=2))
    test_case = PropertyTestCase("test_id", prompt, input_sample, specification)
    outcome = test_case.run()
    assert outcome.status == TestCaseStatus.PASSED
    assert outcome.error_message is None


def test_property_test_case_sentences_run_limit(input_sample):
    prompt = create_prompt_with_response("hello world. everything is fine.")
    specification = PropertyTestSpecification(unit="sentences", limit=Limits(max=2))
    test_case = PropertyTestCase("test_id", prompt, input_sample, specification)
    outcome = test_case.run()
    assert outcome.status == TestCaseStatus.PASSED
    assert outcome.error_message is None


def test_property_test_case_lines_run_limit(input_sample):
    prompt = create_prompt_with_response(
        "hello world.\nEverything is fine.\nAnother line",
    )
    specification = PropertyTestSpecification(unit="lines", limit=Limits(max=3))
    test_case = PropertyTestCase("test_id", prompt, input_sample, specification)
    outcome = test_case.run()
    assert outcome.status == TestCaseStatus.PASSED
    assert outcome.error_message is None


def test_property_test_case_characters_run_limit(input_sample):
    prompt = create_prompt_with_response("hello world.")
    specification = PropertyTestSpecification(unit="characters", limit=Limits(max=12))
    test_case = PropertyTestCase("test_id", prompt, input_sample, specification)
    outcome = test_case.run()
    assert outcome.status == TestCaseStatus.PASSED
    assert outcome.error_message is None


def test_property_test_case_paragraphs_run_limit(input_sample):
    prompt = create_prompt_with_response(
        "hello world.\n\nhello world.\n\nhello world.\n\nhello world.\n\n",
    )

    specification = PropertyTestSpecification(unit="paragraphs", limit=Limits(max=4))
    test_case = PropertyTestCase("test_id", prompt, input_sample, specification)
    outcome = test_case.run()
    assert outcome.status == TestCaseStatus.PASSED
    assert outcome.error_message is None


@pytest.mark.llm
def test_property_test_case_caching(input_sample):
    prompt_spec = EngineeredPromptSpecification(
        metadata=EngineeredPromptMetadata(
            provider="ollama",
            model="gemma2",
        ),
        filename="test.prompt",
        prompt="Give me a poem about prompt engineering please",
    )

    prompt = EngineeredPrompt(specification=prompt_spec)

    test_specification = PropertyTestSpecification(unit="words", limit=Limits(min=10))
    test_case = PropertyTestCase("test_id", prompt, input_sample, test_specification)

    test_case.run()
    original_prompt_duration = test_case.prompt.completion.duration

    test_case.run()
    new_prompt_duration = test_case.prompt.completion.duration

    # This must be equal, because the LLM response is cached.
    # If we called the LLM a second time, the duration would be different.
    assert original_prompt_duration == new_prompt_duration
