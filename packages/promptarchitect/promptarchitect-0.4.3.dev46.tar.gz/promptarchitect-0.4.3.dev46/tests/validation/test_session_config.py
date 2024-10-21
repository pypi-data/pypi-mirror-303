import pytest
from promptarchitect.validation import SessionConfiguration
from pydantic import ValidationError


@pytest.fixture
def valid_config():
    return {
        "prompt_path": "/path/to/prompts",
        "output_path": "/path/to/output",
        "template_path": "/path/to/templates",
        "report_path": "/path/to/report",
        "report_format": "html",
        "report_theme": "blue",
    }


@pytest.fixture
def invalid_config_missing_path():
    return {
        "output_path": "/path/to/output",
        "template_path": "/path/to/templates",
        "report_path": "/path/to/report",
        "report_format": "html",
    }


@pytest.fixture
def invalid_config_wrong_report_type():
    return {
        "prompt_path": "/path/to/prompts",
        "output_path": "/path/to/output",
        "template_path": "/path/to/templates",
        "report_path": "/path/to/report",
        "report_format": "xml",
    }


def test_valid_configuration(valid_config):
    config = SessionConfiguration(**valid_config)

    assert config.template_path is not None
    assert config.output_path is not None
    assert config.report_path is not None
    assert config.prompt_path is not None


def test_invalid_configuration_missing_path(invalid_config_missing_path):
    with pytest.raises(ValidationError):
        SessionConfiguration(**invalid_config_missing_path)


def test_invalid_configuration_wrong_report_type(invalid_config_wrong_report_type):
    with pytest.raises(ValidationError):
        SessionConfiguration(**invalid_config_wrong_report_type)


def test_none_paths():
    with pytest.raises(ValidationError):
        SessionConfiguration(
            prompt_path=None,
            output_path=None,
            template_path=None,
            report_path=None,
            report_type="html",
        )


def test_invalid_path_type():
    with pytest.raises(ValidationError):
        SessionConfiguration(
            prompt_path=123,
            output_path=123,
            template_path=123,
            report_path=123,
            report_type="html",
        )
