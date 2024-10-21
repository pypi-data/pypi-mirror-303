import pytest
from promptarchitect.specification import ScoreTestSpecification
from pydantic import ValidationError


def test_score_test_specification_initialization():
    score_test_spec = ScoreTestSpecification(
        type="score",
        prompt="Please provide a score for the following text.",
        min=0,
        max=100,
        threshold=50,
    )
    assert score_test_spec.type == "score"
    assert score_test_spec.prompt == "Please provide a score for the following text."
    assert score_test_spec.min == 0
    assert score_test_spec.max == 100
    assert score_test_spec.threshold == 50


def test_score_test_specification_missing_fields():
    with pytest.raises(ValidationError):
        ScoreTestSpecification(
            type="score",
            prompt="Please provide a score for the following text.",
            min=0,
            max=100,
            # Missing threshold
        )


def test_score_test_specification_invalid_limits():
    with pytest.raises(ValidationError):
        ScoreTestSpecification(
            type="score",
            prompt="Please provide a score for the following text.",
            min=100,
            max=0,
            threshold=50,
        )


def test_score_test_specification_threshold_out_of_bounds():
    with pytest.raises(ValidationError):
        ScoreTestSpecification(
            type="score",
            prompt="Please provide a score for the following text.",
            min=0,
            max=100,
            threshold=150,
        )
