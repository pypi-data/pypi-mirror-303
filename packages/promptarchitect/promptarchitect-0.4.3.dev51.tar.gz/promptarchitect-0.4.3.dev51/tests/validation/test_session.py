from unittest.mock import MagicMock, patch

import pytest
from promptarchitect.prompting import EngineeredPrompt
from promptarchitect.specification import (
    EngineeredPromptMetadata,
    EngineeredPromptSpecification,
    PromptInput,
)
from promptarchitect.validation import SessionConfiguration, TestSession
from promptarchitect.validation.testcases import (
    TestCase,
    TestCaseOutcome,
    TestCaseStatus,
)


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
def valid_spec():
    return EngineeredPromptSpecification(
        metadata=EngineeredPromptMetadata(
            provider="openai",
            model="gpt-4o-mini",
            test_path="/path/to/tests",
            tests={},
        ),
        prompt="Placeholder prompt.",
        filename="test_prompt.prompt",
    )


@pytest.fixture
def success_test_case(valid_spec):
    test_case = MagicMock(spec=TestCase)
    test_case.prompt = EngineeredPrompt(valid_spec)
    test_case.test_id = "test01"
    test_case.run = MagicMock()
    test_case.run.return_value = TestCaseOutcome(
        test_id="test01",
        status=TestCaseStatus.PASSED,
        prompt_file="test01.prompt",
        input_sample=PromptInput(id="input-1", input="Sample input"),
        messages=[],
        prompt_duration=0,
        prompt_costs=0,
        test_duration=0,
        test_costs=0,
    )

    return test_case


@pytest.fixture
def failing_test_case(valid_spec):
    test_case = MagicMock(spec=TestCase)
    test_case.prompt = EngineeredPrompt(valid_spec)
    test_case.run = MagicMock()
    test_case.test_id = "test01"
    test_case.run.return_value = TestCaseOutcome(
        test_id="test01",
        status=TestCaseStatus.FAILED,
        prompt_file="test01.prompt",
        input_sample=PromptInput(id="input-1", input="Sample input"),
        messages=[],
        prompt_duration=0,
        prompt_costs=0,
        test_duration=0,
        test_costs=0,
    )

    return test_case


def test_test_session_initialization(valid_config):
    config = SessionConfiguration(**valid_config)
    session = TestSession(config)

    assert session.config == config


@patch("promptarchitect.validation.discover_test_cases")
@patch("promptarchitect.validation.create_test_reporter")
def test_start_session(
    create_test_reporter,
    mock_discover_test_cases,
    valid_config,
    success_test_case,
    valid_spec,
):
    mock_test_reporter = MagicMock()

    create_test_reporter.return_value = mock_test_reporter

    mock_discover_test_cases.return_value = ([valid_spec], [success_test_case])

    config = SessionConfiguration.model_validate(valid_config)
    session = TestSession(config)

    result = session.start()

    mock_discover_test_cases.assert_called_once()
    mock_test_reporter.generate_report.assert_called_once()

    assert len(session.test_cases) == 1
    assert len(session.prompts) == 1
    assert len(session.test_outcomes) == 1

    assert result


@patch("promptarchitect.validation.discover_test_cases")
@patch("promptarchitect.validation.create_test_reporter")
def test_start_session_with_failing_tests(
    create_test_reporter,
    mock_discover_test_cases,
    valid_config,
    failing_test_case,
    valid_spec,
):
    mock_test_reporter = MagicMock()

    create_test_reporter.return_value = mock_test_reporter

    mock_discover_test_cases.return_value = ([valid_spec], [failing_test_case])

    config = SessionConfiguration.model_validate(valid_config)
    session = TestSession(config)

    result = session.start()

    mock_discover_test_cases.assert_called_once()
    mock_test_reporter.generate_report.assert_called_once()

    assert len(session.test_cases) == 1
    assert len(session.prompts) == 1
    assert len(session.test_outcomes) == 1

    assert not result
