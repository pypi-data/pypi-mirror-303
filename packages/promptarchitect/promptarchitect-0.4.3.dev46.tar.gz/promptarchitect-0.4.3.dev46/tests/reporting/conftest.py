from datetime import datetime

import pytest
from promptarchitect.reporting.core import (
    PromptFileTestReport,
    TestSessionReport,
    TestSpecificationReport,
)
from promptarchitect.specification import (
    EngineeredPromptMetadata,
    EngineeredPromptSpecification,
    FormatTestSpecification,
    PromptInput,
    PromptOutputFormat,
    QuestionTestSpecification,
)
from promptarchitect.validation.testcases import (
    TestCaseOutcome,
    TestCaseStatus,
)


@pytest.fixture
def valid_prompt_specification():
    return EngineeredPromptSpecification(
        filename="test01.prompt",
        metadata=EngineeredPromptMetadata(
            provider="openai",
            model="gpt-4o-mini",
            tests={
                "test01": {
                    "type": "question",
                    "prompt": (
                        "Are all 5 titles written in normal casing? Answer with YES or"
                        " NO. Explain why."
                    ),
                },
            },
        ),
        prompt=(
            "Please give me 5 titles for a podcast about machine learning. Write each "
            "title in a separate bullet point. Use normal casing for the titles."
        ),
    )


@pytest.fixture
def prompt_specification_without_tests():
    return EngineeredPromptSpecification(
        filename="test02.prompt",
        metadata=EngineeredPromptMetadata(
            provider="openai",
            model="gpt-4o-mini",
            tests={},
        ),
        prompt=(
            "Please give me 5 titles for a podcast about machine learning. Write each "
            "title in a separate bullet point. Use normal casing for the titles."
        ),
    )


@pytest.fixture
def prompt_specification_with_multiple_tests():
    return EngineeredPromptSpecification(
        filename="test02.prompt",
        metadata=EngineeredPromptMetadata(
            provider="openai",
            model="gpt-4o-mini",
            tests={
                "test01": QuestionTestSpecification(prompt="Basic example prompt"),
                "test02": FormatTestSpecification(format=PromptOutputFormat.JSON),
            },
        ),
        prompt=(
            "Please give me 5 titles for a podcast about machine learning. Write each "
            "title in a separate bullet point. Use normal casing for the titles."
        ),
    )


@pytest.fixture
def test_outcomes(prompt_specification_with_multiple_tests):
    return [
        TestCaseOutcome(
            prompt_file=prompt_specification_with_multiple_tests.filename,
            test_id="test01",
            status=TestCaseStatus.PASSED,
            duration=0.5,
            input_sample=PromptInput(id="input-1", input="Sample input"),
            messages=[],
            prompt_duration=0,
            prompt_costs=0,
            test_duration=0,
            test_costs=0,
        ),
        TestCaseOutcome(
            prompt_file=prompt_specification_with_multiple_tests.filename,
            test_id="test02",
            status=TestCaseStatus.PASSED,
            duration=0.5,
            input_sample=PromptInput(id="input-2", input="Sample input"),
            messages=[],
            prompt_duration=0,
            prompt_costs=0,
            test_duration=0,
            test_costs=0,
        ),
    ]


@pytest.fixture
def input_sample():
    return PromptInput(
        id="input-1",
        input="Sample input",
    )


@pytest.fixture
def test_case_outcome_passed(input_sample):
    return TestCaseOutcome(
        test_id="test1",
        status=TestCaseStatus.PASSED,
        prompt_file="file1",
        input_sample=input_sample,
        messages=[],
        prompt_duration=0,
        prompt_costs=0,
        test_duration=0,
        test_costs=0,
    )


@pytest.fixture
def test_case_outcome_failed(input_sample):
    return TestCaseOutcome(
        test_id="test2",
        status=TestCaseStatus.FAILED,
        prompt_file="file1",
        input_sample=input_sample,
        messages=[],
        prompt_duration=0,
        prompt_costs=0,
        test_duration=0,
        test_costs=0,
    )


@pytest.fixture
def test_session_report(prompt_file_test_report):
    return TestSessionReport(
        files=[prompt_file_test_report],
        messages=[],
    )


@pytest.fixture
def test_session_report_without_tests(prompt_file_test_report_without_tests):
    return TestSessionReport(
        files=[prompt_file_test_report_without_tests],
        messages=[],
    )


@pytest.fixture
def test_specification():
    return QuestionTestSpecification(prompt="test prompt")


@pytest.fixture
def test_specification_report(
    test_case_outcome_passed,
    test_case_outcome_failed,
    test_specification,
):
    return TestSpecificationReport(
        test_id="test1",
        specification=test_specification,
        outcomes=[test_case_outcome_passed, test_case_outcome_failed],
    )


@pytest.fixture
def prompt_file_test_report(valid_prompt_specification, test_specification_report):
    return PromptFileTestReport(
        date_created=datetime.now(),  # noqa DTZ005
        specification=valid_prompt_specification,
        tests=[test_specification_report],
    )


@pytest.fixture
def prompt_file_test_report_without_tests(prompt_specification_without_tests):
    prompt_specification_without_tests.metadata.tests = {}

    return PromptFileTestReport(
        date_created=datetime.now(),  # noqa DTZ005
        specification=prompt_specification_without_tests,
        tests=[],
    )
