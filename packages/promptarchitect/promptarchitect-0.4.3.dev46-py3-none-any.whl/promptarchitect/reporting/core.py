"""Core types for reporting test results."""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Literal

from pydantic import BaseModel, computed_field

from promptarchitect.specification import (
    EngineeredPromptSpecification,
    TestSpecificationTypes,
)
from promptarchitect.validation.core import (
    TestCaseOutcome,
    TestCaseStatus,
    TestRunMessage,
)


class TestSpecificationReport(BaseModel):
    """Defines the format for a test report for a single test specification.

    Attributes
    ----------
    test_id : str
        The ID of the test
    specification : TestSpecificationTypes
        The specification for the test
    outcomes : List[TestCaseOutcome]
        The outcomes of the test cases
    description: str
        The description of the test case
    messages: List[str]
        The messages recorded during the test case
    """

    test_id: str
    specification: TestSpecificationTypes
    outcomes: List[TestCaseOutcome]

    @computed_field
    @property
    def description(self) -> str:
        """The description of the test case."""
        return self.specification.description

    @computed_field
    @property
    def messages(self) -> List[TestRunMessage]:
        """The messages recorded during the test case."""
        return [message for outcome in self.outcomes for message in outcome.messages]


class PromptFileTestReport(BaseModel):
    """Defines the format for a test report for a single file.

    Attributes
    ----------
    file_path : str
        The path to the file
    specification : EngineeredPromptSpecification
        The specification for the file
    passed_tests : int
        The number of tests that passed
    failed_tests : int
        The number of tests that failed
    total_prompt_duration: float
        The total duration of the prompt under test
    total_test_duration: float
        The total duration of the test prompts
    total_prompt_costs: float
        The total cost of the prompts executed in the tests
    total_test_costs: float
        The total cost of the test prompts executed in the tests
    total_errors: int
        The total number of errors in the tests
    total_warnings: int
        The total number of warnings in the tests
    messages: List[str]
        The messages recorded during the test cases
    """

    date_created: datetime
    specification: EngineeredPromptSpecification
    tests: List[TestSpecificationReport]

    @computed_field
    @property
    def tests_passed(self) -> int:
        """The number of tests that passed."""
        return len(
            [
                outcome
                for test in self.tests
                for outcome in test.outcomes
                if outcome.status == TestCaseStatus.PASSED
            ],
        )

    @computed_field
    @property
    def tests_failed(self) -> int:
        """The number of tests that failed."""
        return len(
            [
                outcome
                for test in self.tests
                for outcome in test.outcomes
                if outcome.status == TestCaseStatus.FAILED
                or outcome.status == TestCaseStatus.ERROR
            ],
        )

    @computed_field
    @property
    def percentage_passed(self) -> float:
        """The percentage of tests that passed."""
        if self.test_count == 0:
            return 0.0

        return self.tests_passed / self.test_count

    @computed_field
    @property
    def test_count(self) -> int:
        """The number of test cases."""
        return sum([len(test.outcomes) for test in self.tests])

    @computed_field
    @property
    def total_errors(self) -> int:
        """The total number of errors in the tests."""
        return sum(
            [
                len([message for message in test.messages if message.level == "error"])
                for test in self.tests
            ]
        )

    @computed_field
    @property
    def total_warnings(self) -> int:
        """The total number of warnings in the tests."""
        return sum(
            [
                len(
                    [message for message in test.messages if message.level == "warning"]
                )
                for test in self.tests
            ]
        )

    @computed_field
    @property
    def total_prompt_duration(self) -> float:
        """The total duration of the prompts."""
        return sum(
            [
                outcome.prompt_duration
                for test in self.tests
                for outcome in test.outcomes
            ],
        )

    @computed_field
    @property
    def total_test_duration(self) -> float:
        """The total duration of the tests."""
        return sum(
            [outcome.test_duration for test in self.tests for outcome in test.outcomes],
        )

    @computed_field
    @property
    def total_prompt_costs(self) -> float:
        """Get the total cost of the prompts executed in the tests."""
        return sum(
            outcome.prompt_costs for test in self.tests for outcome in test.outcomes
        )

    @computed_field
    @property
    def total_test_costs(self) -> float:
        """Get the total cost of the tests executed in the tests."""
        return sum(
            outcome.test_costs for test in self.tests for outcome in test.outcomes
        )

    @computed_field
    @property
    def messages(self) -> List[TestRunMessage]:
        """The messages recorded during the test cases."""
        return [message for test in self.tests for message in test.messages]


class TestRunMessage(BaseModel):
    """A message generated during the test run.

    Attributes
    ----------
    level : Literal["warning", "error"]
        The level of the message
    message : str
        The message content.

    """

    level: Literal["warning", "error"]
    message: str


class TestSessionReport(BaseModel):
    """Defines the format for a test report for a session.

    Attributes
    ----------
    files : List[PromptFileTestReport]
        The test reports for the files
    messages : List[TestRunMessage]
        The messages generated during
    tests_failed : int
        The number of tests that failed
    tests_passed : int
        The number of tests that passed
    total_duration: float
        The total duration of the tests
    total_costs: float
        The total cost of the prompts executed in the tests
    files_without_tests: List[EngineeredPromptSpecification]
        The files without tests
    files_with_tests: List[PromptFileTestReport]
        The files with tests
    percentage_with_tests: float
        The percentage of files with tests
    total_prompt_duration: float
        Total duration of the prompts
    total_test_duration: float
        Total duration of the tests
    total_prompt_costs: float
        Total cost of the prompts executed in the tests
    total_test_costs: float
        Total cost of the test prompts executed in the tests
    """

    files: List[PromptFileTestReport]
    messages: List[TestRunMessage] = []

    @computed_field
    @property
    def tests_failed(self) -> int:
        """The number of tests that failed."""
        return sum([file.tests_failed for file in self.files])

    @computed_field
    @property
    def tests_passed(self) -> int:
        """The number of tests that passed."""
        return sum([file.tests_passed for file in self.files])

    @computed_field
    @property
    def files_without_tests(self) -> List[EngineeredPromptSpecification]:
        """The files without tests."""
        return [
            file.specification
            for file in self.files
            if not file.specification.has_tests
        ]

    @computed_field
    @property
    def files_with_tests(self) -> List[PromptFileTestReport]:
        """The files with tests."""
        return [file for file in self.files if file.specification.has_tests]

    @computed_field
    @property
    def percentage_with_tests(self) -> float:
        """The percentage of files with tests."""
        if len(self.files) == 0:
            return 0.0

        return len(self.files_with_tests) / len(self.files)

    @computed_field
    @property
    def total_prompt_duration(self) -> float:
        """The total duration of the prompts."""
        return sum([file.total_prompt_duration for file in self.files])

    @computed_field
    @property
    def total_test_duration(self) -> float:
        """The total duration of the tests."""
        return sum([file.total_test_duration for file in self.files])

    @computed_field
    @property
    def total_prompt_costs(self) -> float:
        """The total cost of the prompts executed in the tests."""
        return sum([file.total_prompt_costs for file in self.files])

    @computed_field
    @property
    def total_test_costs(self) -> float:
        """The total cost of the tests executed in the tests."""
        return sum([file.total_test_costs for file in self.files])


class TestReporter(ABC):
    """Base class for building a test reporter."""

    report_path: str

    def __init__(self, report_path: str) -> None:
        """Initialize the test reporter.

        Parameters
        ----------
        report_path : str
            The path to the report

        """
        self.report_path = report_path

    @abstractmethod
    def generate_report(
        self,
        prompts: List[EngineeredPromptSpecification],
        test_outcomes: List[TestCaseOutcome],
    ) -> None:
        """Generate a test report from the test outcomes in a session.

        Parameters
        ----------
        template_location : str
            The path to the template file
        report_location : str
            The path to the report file
        prompts : List[EngineeredPromptSpecification]
            The prompts that were tested
        test_outcomes : List[TestCaseOutcome]
            The outcomes of the test cases

        """
        raise NotImplementedError()

    @staticmethod
    def _collect_results(
        prompt_specs: List[EngineeredPromptSpecification],
        test_outcomes: List[TestCaseOutcome],
    ) -> TestSessionReport:
        """Collect the test results and combine them into a reportable structure.

        Parameters
        ----------
        prompt_specs : List[EngineeredPromptSpecification]
            The specifications for the prompts
        test_outcomes : List[TestCaseOutcome]
            The outcomes of the tests

        Returns
        -------
        TestSessionReport
            The report of the test session

        """
        test_files = []

        for prompt_spec in prompt_specs:
            related_tests = [
                test_outcome
                for test_outcome in test_outcomes
                if test_outcome.prompt_file == prompt_spec.filename
            ]

            tests = []

            for test_spec_key in prompt_spec.metadata.tests:
                test_spec = prompt_spec.metadata.tests[test_spec_key]

                test = TestSpecificationReport(
                    test_id=test_spec_key,
                    specification=test_spec,
                    outcomes=[
                        test_outcome
                        for test_outcome in related_tests
                        if test_outcome.test_id == test_spec_key
                    ],
                )

                tests.append(test)

            test_files.append(
                PromptFileTestReport(
                    date_created=datetime.now(),  # noqa: DTZ005
                    specification=prompt_spec,
                    tests=tests,
                ),
            )

        return TestSessionReport(
            files=test_files,
        )
