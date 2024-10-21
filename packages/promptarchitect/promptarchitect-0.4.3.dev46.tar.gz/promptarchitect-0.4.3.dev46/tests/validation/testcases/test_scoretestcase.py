from unittest.mock import MagicMock

import pytest
from promptarchitect.specification import ScoreTestSpecification
from promptarchitect.validation.testcases import ScoreTestCase, TestCaseStatus


@pytest.fixture
def score_test_specification():
    return ScoreTestSpecification(
        type="score",
        prompt="How good is the explanation of the terms in the article?",
        min=0,
        max=100,
        threshold=50,
    )


@pytest.mark.llm
def test_score_test_case_passed(input_sample, score_test_specification):
    engineered_prompt = MagicMock()
    engineered_prompt.run = MagicMock()
    engineered_prompt.run.return_value = '{"score": 75, "response": "Good job!"}'
    engineered_prompt.specification = MagicMock()
    engineered_prompt.specification.filename = "test.prompt"

    test_case = ScoreTestCase(
        "test_id", engineered_prompt, input_sample, score_test_specification
    )

    outcome = test_case.run()

    assert outcome.status == TestCaseStatus.PASSED


@pytest.mark.llm
def test_score_test_case_failed(input_sample, score_test_specification):
    engineered_prompt = MagicMock()
    engineered_prompt.run = MagicMock()
    engineered_prompt.run.return_value = '{"score": 49, "response": "Good job!"}'
    engineered_prompt.specification = MagicMock()
    engineered_prompt.specification.filename = "test.prompt"

    test_case = ScoreTestCase(
        "test_id", engineered_prompt, input_sample, score_test_specification
    )

    outcome = test_case.run()

    assert outcome.status == TestCaseStatus.FAILED
    assert len(outcome.messages) == 1
