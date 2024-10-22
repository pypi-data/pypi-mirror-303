import pytest
from pydantic import ValidationError
from promptarchitect.specification import LanguageTestSpecification


def test_language_test_specification_type():
    spec = LanguageTestSpecification(lang_code="en")
    assert spec.type == "language"


def test_language_test_specification_lang_required():
    with pytest.raises(ValidationError):
        LanguageTestSpecification()


def test_language_test_specification_lang_value():
    lang_code = "en"
    spec = LanguageTestSpecification(lang_code=lang_code)
    assert spec.lang_code == lang_code
