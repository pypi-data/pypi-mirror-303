"""Core types used in the validation module."""

import logging
from abc import ABC, abstractmethod
from datetime import UTC, datetime
from enum import Enum
from functools import cache
from os import PathLike
from typing import List, Literal, Optional

from pydantic import BaseModel

from promptarchitect.prompting import EngineeredPrompt
from promptarchitect.specification import PromptInput

logger = logging.getLogger(__name__)


class TestRunMessageLevel(str, Enum):
    """Enum to represent the various levels of a test run message."""

    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class TestRunMessage(BaseModel):
    """Model to represent a message generated during a test run."""

    timestamp: datetime
    level: TestRunMessageLevel
    message: str


class SessionConfiguration(BaseModel):
    """Configures the test session.

    Attributes
    ----------
    prompt_path: PathLike
        The path to the directory containing the prompts.
    output_path: PathLike
        The path to the directory where the generated prompts will be saved.
    template_path: PathLike
        The path to the directory containing the templates for the test report.
    report_path: PathLike
        The path to the directory where the test report will be saved.
    report_format: Literal["html", "json"]
        The format of the test report
    report_theme: str
        The theme to use for the test report.
    test_profile_path: Optional[PathLike]
        The path to the test profile file.

    """

    prompt_path: PathLike
    output_path: PathLike
    template_path: PathLike | None = None
    report_path: PathLike
    report_format: Literal["html", "json"]
    report_theme: str
    test_profile_path: Optional[PathLike] = None


class TestCaseStatus(str, Enum):
    """Enum to represent the various states of a test case."""

    __test__ = False  # Mark this for pytest to ignore

    PASSED = "PASSED"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"
    ERROR = "ERROR"


class TestCaseOutcome(BaseModel):
    """Models the outcome of a test case.

    Attributes
    ----------
    status: TestCaseStatus
        The status of the test case.
    error_message: Optional[str]
        The error message if the test case failed or errored.
    duration: int
        The duration of the test case in milliseconds.
    score: Optional[float]
        The score of the test case.
    response: Optional[str]
        The response of the test case.
    """

    __test__ = False  # Mark this for pytest to ignore

    test_id: str
    prompt_file: str
    status: TestCaseStatus
    error_message: Optional[str] = None
    prompt_duration: float
    test_duration: float
    prompt_costs: float
    test_costs: float
    input_sample: PromptInput
    messages: List[TestRunMessage]
    score: float | None = None
    response: str | None = None


class TestCase(ABC):
    """Represents a test case.

    A test case is a concrete implementation of a test specification for a single prompt
    and input sample combination. When you have a single prompt file, with 2 input
    samples, and 2 tests, you'll have a total of 4 test cases for the prompt file.

    Attributes
    ----------
    test_id: str
        The unique identifier for the test case.
    prompt: EngineeredPrompt
        The engineered prompt that the test case is for.

    """

    __test__ = False  # Mark this for pytest to ignore

    test_id: str
    prompt: EngineeredPrompt
    input_sample: PromptInput
    messages: List[TestRunMessage]

    def __init__(
        self,
        test_id: str,
        prompt: EngineeredPrompt,
        input_sample: PromptInput,
    ) -> None:
        self.test_id = test_id
        self.prompt = prompt
        self.input_sample = input_sample
        self.messages = []

    @abstractmethod
    def run(self) -> TestCaseOutcome:
        """Run the test case.

        Returns
        -------
        TestCaseOutcome
            The outcome of the test case.

        """
        raise NotImplementedError()

    def log_error(self, message: str, *args: object, exc_info: object = None) -> None:
        """Log an error message for the test case.

        The message is formatted using `message % args`. And written to the regular
        logging output of python, and recorded as part of the test case.

        Arguments
        ---------
        message: str
            The error message to log.
        args: object
            The arguments to format the error message with.
        exc_info: object
            The exception information to log.
        """
        self.messages.append(
            TestRunMessage(
                timestamp=datetime.now(UTC),
                level=TestRunMessageLevel.ERROR,
                message=message % args,
            ),
        )

        logger.error(message, *args, exc_info=exc_info)

    def log_warning(self, message: str, *args: object) -> None:
        """Log a warning message for the test case.

        Arguments
        ---------
        message: str
            The warning message to log.
        args: object
            The arguments to format the warning message with.
        """
        self.messages.append(
            TestRunMessage(
                timestamp=datetime.now(UTC),
                level=TestRunMessageLevel.WARNING,
                message=message % args,
            ),
        )

        logger.error(message, *args)

    def log_info(self, message: str, *args: object) -> None:
        """Log an info message for the test case.

        Arguments
        ---------
        message: str
            The info message to log.
        args: object
            The arguments to format the info message with.
        """
        self.messages.append(
            TestRunMessage(
                timestamp=datetime.now(UTC),
                level=TestRunMessageLevel.INFO,
                message=message % args,
            ),
        )

        logger.info(message, *args)

    @cache  # noqa: B019
    def _run_prompt(self, prompt: EngineeredPrompt, input_sample: PromptInput) -> str:
        return prompt.run(
            input_text=input_sample.input,
            properties=input_sample.properties,
        )
