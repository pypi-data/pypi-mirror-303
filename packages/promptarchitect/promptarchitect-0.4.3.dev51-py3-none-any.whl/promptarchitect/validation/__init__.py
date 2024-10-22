"""Validation support for engineered prompts.

This module is responsible for running tests against an engineered prompt. It provides
a `TestSession` class that can be used to run tests against a set of engineered prompts.
The `TestSession` class automatically detects test cases from the provided path and runs
them. At the end of the test run, you'll get a report using the configured reporter.

Supported Reporters
-------------------
Depending on your needs we support different types of reporters to generate
the test report:

- `HTMLReporter`: Generates an HTML report.

Supported Test Cases
--------------------
We support a number of test case types to validate various aspects of an engineered
prompt. Currently we support:

- `CompletionTestCase`: A test case for completion tasks.
- `ClassificationTestCase`: A test case for classification tasks.
- `GenerationTestCase`: A test case for generation tasks.
"""

import logging
import os
from itertools import product
from os import PathLike
from typing import List, Tuple

import opentelemetry.trace

from promptarchitect.prompting import EngineeredPrompt
from promptarchitect.reporting import create_test_reporter
from promptarchitect.specification import (
    EngineeredPromptSpecification,
    PromptInput,
    TestProfile,
)
from promptarchitect.validation.core import SessionConfiguration, TestCaseStatus
from promptarchitect.validation.testcases import (
    TestCase,
    TestCaseOutcome,
    create_test_case,
)

logger = logging.getLogger(__name__)
tracer = opentelemetry.trace.get_tracer(__name__)


def discover_input_samples(
    base_path: PathLike,
    prompt_spec: EngineeredPromptSpecification,
) -> List[PromptInput]:
    """Discover input samples for an engineered prompt specification.

    Parameters
    ----------
    prompt_spec: EngineeredPromptSpecification

    Returns
    -------
    List[PromptInput]
        List of input samples for the prompt.

    """
    sample_files = sorted(
        [
            f
            for f in os.listdir(os.path.join(base_path, prompt_spec.metadata.test_path))
            if f.endswith(".md") or f.endswith(".txt")
        ],
    )

    return [
        PromptInput.from_file(
            os.path.join(base_path, prompt_spec.metadata.test_path, f)
        )
        for f in sample_files
    ]


def discover_test_cases(
    path: PathLike,
) -> Tuple[List[EngineeredPromptSpecification], List[TestCase]]:
    """Discovers test cases from the given ø.

    Parameters
    ----------
    path: Path where to search for prompt files.

    Returns
    -------
    Tuple[List[EngineeredPromptSpecification], List[TestCase]]
        Tuple containing the list of discovered prompts and test cases.

    """
    prompt_files = sorted([f for f in os.listdir(path) if f.endswith(".prompt")])

    prompt_specs = [
        EngineeredPromptSpecification.from_file(os.path.join(path, f))
        for f in prompt_files
    ]

    test_cases = []

    for prompt_spec in prompt_specs:
        if not prompt_spec.metadata.test_path:
            logger.warning(
                "Prompt file %s has tests but no test_path set. Skipping.",
                prompt_spec.filename,
            )
            continue

        prompt = EngineeredPrompt(prompt_spec)
        prompt_base_path = os.path.dirname(prompt_spec.filename)
        input_samples = discover_input_samples(prompt_base_path, prompt_spec)

        if not input_samples:
            logger.warning(
                "Prompt file %s has tests but no test samples found in %s. Skipping.",
                prompt_spec.filename,
                prompt_spec.metadata.test_path,
            )
            continue

        # We're generating a cartesian product of the input samples and test
        # specifications. We need a test case per input spample per test spec.
        test_input_combinations = product(
            input_samples,
            prompt_spec.metadata.tests.keys(),
        )

        for input_sample, test_spec_id in test_input_combinations:
            test_spec = prompt_spec.metadata.tests[test_spec_id]

            test_case = create_test_case(
                test_id=test_spec_id,
                prompt=prompt,
                spec=test_spec,
                input_sample=input_sample,
            )

            test_cases.append(test_case)

    return (prompt_specs, test_cases)


def filter_test_cases(
    test_cases: List[TestCase], test_profile: TestProfile
) -> List[TestCase]:
    """Filter test cases based on the provided test profile.

    Parameters
    ----------
    test_cases: List[TestCase]
        The list of test cases to filter.
    test_profile: TestProfile
        The test profile to use for filtering.

    Returns
    -------
    List[TestCase]
        The filtered list of test cases.
    """
    filtered_test_cases = []

    for test_case in test_cases:
        # We check that the filename of the test case ends with the file path
        # included in the test profile. We do this, because the filename is an absolute
        # path, while the test profile will always list relative paths.

        included_files = list(
            filter(
                lambda x: test_case.prompt.specification.filename.endswith(x.filename),
                test_profile.include,
            )
        )

        if len(included_files) == 0:
            continue

        included_tests = [test for file in included_files for test in file.tests]

        related_tests = list(
            filter(lambda x: x.id == test_case.test_id, included_tests)
        )

        related_samples = [
            sample
            for included_test in related_tests
            for sample in included_test.samples
        ]

        if len(included_tests) > 0 and len(related_samples) > 0:
            # We check that the filename of the test sample ends with the file path
            # included in the test profile. We do this, because the filename is
            # an absolute path, while the test profile will always list relative paths.

            filtered_samples = [
                sample
                for sample in related_samples
                if test_case.input_sample.filename.endswith(sample)
            ]

            if len(filtered_samples) > 0:
                filtered_test_cases.append(test_case)

    return filtered_test_cases


class TestSession:
    """Controls the flow for a single test session.

    Attributes
    ----------
    config: SessionConfiguration
        The configuration for the test session.
    test_cases: List[TestCase]
        The list of discovered test cases.

    """

    __test__ = False  # Mark this for pytest to ignore

    prompts: List[EngineeredPromptSpecification]
    test_cases: List[TestCase]
    test_outcomes: List[TestCaseOutcome]

    def __init__(self, config: SessionConfiguration) -> None:
        """Initialize the test session.

        Parameters
        ----------
        config: SessionConfiguration
            The configuration for the test session.

        """
        self.config = config

    def start(self) -> bool:
        """Start the test session.

        Returns
        -------
        bool
            True if all tests passed, Falss otherwise.

        """
        with tracer.start_as_current_span("TestSession.start") as span:
            self._discover_tests()
            self._run_tests()
            self._report_test_results()

            logger.info("Test session completed.")

            span.set_attribute("test.session.prompts", len(self.prompts))
            span.set_attribute("test.session.test_cases", len(self.test_cases))
            span.set_attribute("test.session.test_outcomes", len(self.test_outcomes))

            return not any(
                outcome.status == TestCaseStatus.FAILED
                or outcome.status == TestCaseStatus.ERROR
                for outcome in self.test_outcomes
            )

    def _discover_tests(self) -> None:
        with tracer.start_as_current_span("TestSession._discover_tests") as span:
            logger.info("Discovering test cases from path %s", self.config.prompt_path)

            self.prompts, self.test_cases = discover_test_cases(self.config.prompt_path)

            logger.info(
                "Discovered %d prompts and %d test cases.",
                len(self.prompts),
                len(self.test_cases),
            )

            span.set_attribute("test.session.prompts", len(self.prompts))
            span.set_attribute("test.session.test_cases", len(self.test_cases))

    def _filter_tests_by_profile(self) -> None:
        with open(self.config.test_profile_path, "r") as f:
            test_profile = TestProfile.model_validate_json(f.read())

        self.test_cases = filter_test_cases(self.test_cases, test_profile)

    def _run_tests(self) -> None:
        with tracer.start_as_current_span("TestSession._run_tests") as span:
            logger.info("Running test cases.")

            test_outcomes = []

            for test_case in self.test_cases:
                outcome = test_case.run()
                test_outcomes.append(outcome)

                logger.info(
                    "Test case %s completed with status %s",
                    test_case.test_id,
                    outcome.status,
                )

            self.test_outcomes = test_outcomes

            span.set_attribute("test.session.test_outcomes", len(self.test_outcomes))

    def _report_test_results(self) -> None:
        with tracer.start_as_current_span("TestSession._report_test_results") as span:
            logger.info("Generating test report.")

            reporter = create_test_reporter(self.config)

            reporter.generate_report(
                self.prompts,
                self.test_outcomes,
            )

            logger.info("Completed generating report at %s.", self.config.report_path)

            span.set_attribute("test.session.report_path", self.config.report_path)
