from unittest.mock import MagicMock

import pytest
from promptarchitect.specification import QuestionTestSpecification
from promptarchitect.validation.testcases import (
    QuestionTestCase,
    TestCaseStatus,
)


@pytest.fixture
def question_test_specification():
    return QuestionTestSpecification(
        prompt="Are all titles related to machine learning?",
    )


@pytest.fixture
def dutch_question_test_specification():
    return QuestionTestSpecification(
        prompt="Zijn alle titels gerelateerd aan machine learning?",
    )


@pytest.mark.llm
def test_question_test_case_run_yes_response(
    engineered_prompt,
    input_sample,
    question_test_specification,
):
    engineered_prompt.run = MagicMock()
    engineered_prompt.run.return_value = (
        "* Machine learning for professionals\n* ML today\n* The machine learners\n* "
        "Exploring machine learning with Willem and Joop\n* The machine learning "
        "podcast\n"
    )

    engineered_prompt.completion = MagicMock()
    engineered_prompt.completion.input_tokens = 10
    engineered_prompt.completion.output_tokens = 10

    test_case = QuestionTestCase(
        "test_id",
        engineered_prompt,
        input_sample,
        question_test_specification,
    )

    outcome = test_case.run()

    assert outcome.status == TestCaseStatus.PASSED


@pytest.mark.llm
def test_question_test_case_run_dutch_response(
    engineered_prompt,
    input_sample,
    question_test_specification,
):
    engineered_prompt.run = MagicMock()
    engineered_prompt.run.return_value = (
        "* Machine learning voor professionals\n* AI today\n* De machine learning "
        "experts\n* Leer machine learning met Willem and Joop\n* De machine learning "
        "podcast\n"
    )

    engineered_prompt.completion = MagicMock()
    engineered_prompt.completion.input_tokens = 10
    engineered_prompt.completion.output_tokens = 10

    test_case = QuestionTestCase(
        "test_id",
        engineered_prompt,
        input_sample,
        question_test_specification,
    )

    outcome = test_case.run()

    assert outcome.status == TestCaseStatus.PASSED
    assert outcome.error_message is None
