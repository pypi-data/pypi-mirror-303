import pytest
from promptarchitect.specification import (
    QuestionTestSpecification,
)
from pydantic import ValidationError


def test_question_test_specification_type():
    spec = QuestionTestSpecification(prompt="Is this a test?")
    assert spec.type == "question"


def test_question_test_specification_prompt_required():
    with pytest.raises(ValidationError):
        QuestionTestSpecification()


def test_question_test_specification_prompt_value():
    prompt_text = "Is this a test?"
    spec = QuestionTestSpecification(prompt=prompt_text)
    assert spec.prompt == prompt_text
