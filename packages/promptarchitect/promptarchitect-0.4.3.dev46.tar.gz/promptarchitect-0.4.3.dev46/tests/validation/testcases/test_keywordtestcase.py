from unittest.mock import MagicMock

import pytest
from promptarchitect.specification import KeywordTestSpecification
from promptarchitect.validation.testcases import KeywordTestCase, TestCaseStatus


@pytest.fixture
def keyword_test_specification():
    return KeywordTestSpecification(keyword="test")


def test_keyword_test_case_passed(
    engineered_prompt, input_sample, keyword_test_specification
):
    engineered_prompt.run = MagicMock()
    engineered_prompt.run.return_value = (
        "This is a test response containing the keyword test."
    )
    engineered_prompt.completion = MagicMock()
    engineered_prompt.completion.input_tokens = 10
    engineered_prompt.completion.output_tokens = 10
    engineered_prompt.completion.duration = 1.0
    engineered_prompt.completion.cost = 1.0

    test_case = KeywordTestCase(
        "test_id", engineered_prompt, input_sample, keyword_test_specification
    )
    outcome = test_case.run()

    assert outcome.status == TestCaseStatus.PASSED
    assert outcome.prompt_file == engineered_prompt.specification.filename
    assert outcome.prompt_duration == engineered_prompt.completion.duration
    assert outcome.test_duration == 0
    assert outcome.prompt_costs == engineered_prompt.completion.cost
    assert outcome.test_costs == 0
    assert outcome.input_sample == input_sample
    assert outcome.messages == test_case.messages
    assert outcome.response == "This is a test response containing the keyword test."


def test_keyword_test_case_failed(
    engineered_prompt, input_sample, keyword_test_specification
):
    engineered_prompt.run = MagicMock()
    engineered_prompt.run.return_value = "This response does not contain the keyword."
    engineered_prompt.completion = MagicMock()
    engineered_prompt.completion.input_tokens = 10
    engineered_prompt.completion.output_tokens = 10
    engineered_prompt.completion.duration = 1.0
    engineered_prompt.completion.cost = 1.0

    test_case = KeywordTestCase(
        "test_id", engineered_prompt, input_sample, keyword_test_specification
    )

    outcome = test_case.run()

    assert outcome.status == TestCaseStatus.FAILED
    assert outcome.prompt_file == engineered_prompt.specification.filename
    assert outcome.prompt_duration == engineered_prompt.completion.duration
    assert outcome.test_duration == 0
    assert outcome.prompt_costs == engineered_prompt.completion.cost
    assert outcome.test_costs == 0
    assert outcome.input_sample == input_sample
    assert outcome.messages == test_case.messages
    assert outcome.response == "This response does not contain the keyword."
