import pytest
from pydantic import ValidationError
from promptarchitect.specification import KeywordTestSpecification


def test_keyword_test_specification_keyword_required():
    with pytest.raises(ValidationError):
        KeywordTestSpecification()


def test_keyword_test_specification_keyword_value():
    keyword = "test"
    spec = KeywordTestSpecification(keyword=keyword)
    assert spec.keyword == keyword
