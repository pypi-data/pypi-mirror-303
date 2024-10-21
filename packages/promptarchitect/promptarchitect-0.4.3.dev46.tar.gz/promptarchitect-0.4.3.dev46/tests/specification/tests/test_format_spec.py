import pytest
from pydantic import ValidationError
from promptarchitect.specification import FormatTestSpecification


def test_format_test_specification_type():
    spec = FormatTestSpecification(format="html")
    assert spec.type == "format"


def test_format_test_specification_format_html():
    spec = FormatTestSpecification(format="html")
    assert spec.format == "html"


def test_format_test_specification_format_json():
    spec = FormatTestSpecification(format="json")
    assert spec.format == "json"


def test_format_test_specification_format_markdown():
    spec = FormatTestSpecification(format="markdown")
    assert spec.format == "markdown"


def test_format_test_specification_invalid_format():
    with pytest.raises(ValidationError):
        FormatTestSpecification(format="xml")


def test_format_test_specification_format_required():
    with pytest.raises(ValidationError):
        FormatTestSpecification()
