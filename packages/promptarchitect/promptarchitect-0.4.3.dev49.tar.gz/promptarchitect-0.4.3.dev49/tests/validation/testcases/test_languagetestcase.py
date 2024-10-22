from unittest.mock import MagicMock

import pytest
from promptarchitect.specification import LanguageTestSpecification
from promptarchitect.validation.testcases import LanguageTestCase, TestCaseStatus
from pydantic import ValidationError


@pytest.fixture
def language_test_specification_en():
    return LanguageTestSpecification(type="language", lang_code="en")


@pytest.fixture
def language_test_specification_nl():
    return LanguageTestSpecification(type="language", lang_code="nl")


def test_question_test_case_passed(
    engineered_prompt,
    input_sample,
    language_test_specification_en,
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

    test_case = LanguageTestCase(
        "test_id",
        engineered_prompt,
        input_sample,
        language_test_specification_en,
    )

    outcome = test_case.run()

    assert outcome.status == TestCaseStatus.PASSED


def test_question_test_case_passed_nl(
    engineered_prompt,
    input_sample,
    language_test_specification_nl,
):
    engineered_prompt.run = MagicMock()
    engineered_prompt.run.return_value = (
        "Een podcast over Machine Learning met Willem en Joop\n"
    )
    engineered_prompt.completion = MagicMock()
    engineered_prompt.completion.input_tokens = 10
    engineered_prompt.completion.output_tokens = 10

    test_case = LanguageTestCase(
        "test_id",
        engineered_prompt,
        input_sample,
        language_test_specification_nl,
    )

    outcome = test_case.run()

    assert outcome.status == TestCaseStatus.PASSED


def test_question_test_case_failed(
    engineered_prompt,
    input_sample,
    language_test_specification_nl,
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

    test_case = LanguageTestCase(
        "test_id",
        engineered_prompt,
        input_sample,
        language_test_specification_nl,
    )

    outcome = test_case.run()

    assert outcome.status == TestCaseStatus.FAILED


def test_question_test_case_wrong_lang_code(
    engineered_prompt,
    input_sample,
):
    engineered_prompt.run = MagicMock()

    engineered_prompt.run.return_value = (
        "* Machine learning for professionals\n* ML today\n* The machine learners\n* "
        "Exploring machine learning with Willem and Joop\n* The machine learning "
        "podcast\n"
    )

    with pytest.raises(ValidationError):
        _ = LanguageTestCase(
            "test_id",
            engineered_prompt,
            input_sample,
            LanguageTestSpecification(type="language", lang_code="xxx"),
        )

    with pytest.raises(ValidationError):
        _ = LanguageTestCase(
            "test_id",
            engineered_prompt,
            input_sample,
            LanguageTestSpecification(type="language", lang_code="NL"),
        )


def test_question_test_case_length_of_response(
    engineered_prompt,
    input_sample,
    language_test_specification_en,
):
    engineered_prompt.run = MagicMock()
    engineered_prompt.run.return_value = "* Machine learning for professionals"

    engineered_prompt.completion = MagicMock()
    engineered_prompt.completion.input_tokens = 10
    engineered_prompt.completion.output_tokens = 10

    test_case = LanguageTestCase(
        "test_id",
        engineered_prompt,
        input_sample,
        language_test_specification_en,
    )

    outcome = test_case.run()

    assert outcome.status == TestCaseStatus.PASSED
