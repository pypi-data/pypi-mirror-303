"""Implementation of test cases for the prompt validation."""

import json
import re
from pathlib import Path

import langdetect
import opentelemetry.trace
from bs4 import BeautifulSoup
from langdetect import DetectorFactory

from promptarchitect.prompting import (
    EngineeredPrompt,
)
from promptarchitect.specification import (
    FormatTestSpecification,
    KeywordTestSpecification,
    LanguageTestSpecification,
    MetricTestSpecification,
    PromptInput,
    PromptOutputFormat,
    PropertyTestSpecification,
    PropertyUnit,
    QuestionTestSpecification,
    ScoreTestSpecification,
    TestSpecificationTypes,
)
from promptarchitect.validation.core import (
    TestCase,
    TestCaseOutcome,
    TestCaseStatus,
)

tracer = opentelemetry.trace.get_tracer(__name__)


class PropertyTestCase(TestCase):
    """Implementation of a test case for a property based test.

    This test case validates that the text exhibits a particular property
    like a number of words, sentences, or lines.

    Attributes
    ----------
    specification: PropertyTestSpecification
        The specification for the property test.

    """

    def __init__(
        self,
        test_id: str,
        prompt: EngineeredPrompt,
        input_sample: PromptInput,
        specification: PropertyTestSpecification,
    ) -> None:
        """Initialize the property test case.

        Parameters
        ----------
        test_id: str
            The unique identifier for the test case.
        prompt: EngineeredPrompt
            The engineered prompt to be used in the test case.
        input_sample: PromptInput
            The input sample to be used in the test case.
        specification: PropertyTestSpecification
            The specification for the property test.

        """
        super().__init__(test_id, prompt, input_sample)
        self.specification = specification

    def run(self) -> TestCaseOutcome:
        """Run the test case.

        Returns
        -------
        TestCaseOutcome
            The outcome of the test case.

        """
        with tracer.start_as_current_span("PropertyTestCase.run") as span:
            response = self._run_prompt(self.prompt, self.input_sample)

            items = []

            if self.specification.unit == PropertyUnit.WORDS:
                items = response.split()
            elif self.specification.unit == PropertyUnit.SENTENCES:
                items = re.split(r"[.!?]", response)
            elif self.specification.unit == PropertyUnit.LINES:
                items = response.split("\n")
            elif self.specification.unit == PropertyUnit.PARAGRAPHS:
                items = response.split("\n\n")
            elif self.specification.unit == PropertyUnit.CHARACTERS:
                items = list(response)
            else:
                error_message = f"Unknown unit {self.specification.unit}."
                raise ValueError(error_message)

            # We strip out empty lines, words, sentences, etc.
            # People sometimes have extra characters like line endings in the output of
            # the prompt.

            if self.specification.unit != PropertyUnit.CHARACTERS:
                items = [item for item in items if item.strip()]

            error_message = None

            if self.specification.equals is not None:
                status = (
                    TestCaseStatus.PASSED
                    if len(items) == self.specification.equals
                    else TestCaseStatus.FAILED
                )

                error_message = (
                    (
                        f"Expected {self.specification.equals} "
                        f"{self.specification.unit}, "
                        f"but got {len(items)}."
                    )
                    if status == TestCaseStatus.FAILED
                    else None
                )
            else:
                status = (
                    TestCaseStatus.PASSED
                    if self.specification.limit.between(len(items))
                    else TestCaseStatus.FAILED
                )

                error_message = (
                    (
                        f"Expected between {self.specification.limit.min} and "
                        f"{self.specification.limit.max} {self.specification.unit}, "
                        f"but got {len(items)}."
                    )
                    if status == TestCaseStatus.FAILED
                    else None
                )

            span.set_attribute("test.id", self.test_id)
            span.set_attribute("prompt.filename", self.prompt.specification.filename)
            span.set_attribute("input.sample.filename", self.input_sample.filename)
            span.set_attribute("test.cost", self.prompt.completion.cost)
            span.set_attribute("test.input_tokens", self.prompt.completion.input_tokens)
            span.set_attribute(
                "test.output_tokens",
                self.prompt.completion.output_tokens,
            )

            if status == TestCaseStatus.FAILED or status == TestCaseStatus.ERROR:
                self.log_error(error_message)

            return TestCaseOutcome(
                test_id=self.test_id,
                prompt_file=self.prompt.specification.filename,  # type: ignore
                status=status,
                duration=self.prompt.completion.duration,
                prompt_duration=self.prompt.completion.duration,
                test_duration=0,
                prompt_costs=self.prompt.completion.cost,
                test_costs=0,
                input_sample=self.input_sample,
                messages=self.messages,
                response=response,
            )


class MetricTestCase(TestCase):
    """Implementation of a test case for a score based test.

    Attributes
    ----------
    specification: ScoreTestSpecification
        The specification for the score test.

    """

    specification: MetricTestSpecification

    def __init__(
        self,
        test_id: str,
        prompt: EngineeredPrompt,
        input_sample: PromptInput,
        specification: MetricTestSpecification,
    ) -> None:
        """Initialize the question test case.

        Parameters
        ----------
        test_id: str
            The unique identifier for the test case.
        prompt: EngineeredPrompt
            The engineered prompt to be used in the test case.
        input_sample: PromptInput
            The input sample to be used in the test case.
        specification: QuestionTestSpecification
            The specification for the question test.

        """
        super().__init__(test_id, prompt, input_sample)

        self.specification = specification

    def run(self) -> TestCaseOutcome:
        """Run the test case.

        Returns
        -------
        TestCaseOutcome
            The outcome of the test case.

        """
        with tracer.start_as_current_span("MetricTestCase.run") as span:
            raise NotImplementedError()

            span.set_attribute("test.id", self.test_id)
            span.set_attribute("prompt.filename", self.prompt.specification.filename)
            span.set_attribute("input.sample.filename", self.input_sample.filename)
            span.set_attribute("test.cost", self.prompt.completion.cost)
            span.set_attribute("test.input_tokens", self.prompt.completion.input_tokens)
            span.set_attribute(
                "test.output_tokens",
                self.prompt.completion.output_tokens,
            )


class QuestionTestCase(TestCase):
    """Implementation of a test case for a question based test.

    Attributes
    ----------
    specification: QuestionTestSpecification
        The specification for the question test

    """

    specification: QuestionTestSpecification

    def __init__(
        self,
        test_id: str,
        prompt: EngineeredPrompt,
        input_sample: PromptInput,
        specification: QuestionTestSpecification,
    ) -> None:
        """Initialize the question test case.

        Parameters
        ----------
        test_id: str
            The unique identifier for the test case.
        prompt: EngineeredPrompt
            The engineered prompt to be used in the test case.
        input_sample: PromptInput
            The input sample to be used in the test case.
        specification: QuestionTestSpecification
            The specification for the question test.

        """
        super().__init__(test_id, prompt, input_sample)
        self.specification = specification

    def run(self) -> TestCaseOutcome:
        """Run the test case.

        Returns
        -------
        TestCaseOutcome
            The outcome of the test case.

        """
        with tracer.start_as_current_span("QuestionTestCase.run") as span:
            input_response = self._run_prompt(self.prompt, self.input_sample)

            # Read the enhanced prompt template
            test_file_path = (
                Path(__file__).parent / "prompts" / "question_testcase.prompt"
            )
            properties = {"test_prompt": self.specification.prompt}

            engineered_test_prompt = EngineeredPrompt(prompt_file=str(test_file_path))

            # Change the provider and model to the one used in the input prompt
            engineered_test_prompt.specification.metadata.provider = (
                self.prompt.specification.metadata.provider
            )
            engineered_test_prompt.specification.metadata.model = (
                self.prompt.specification.metadata.model
            )

            question_response = engineered_test_prompt.run(
                input_text=input_response, properties=properties
            )

            try:
                response_json = json.loads(question_response)
                answer = response_json.get("answer")

                if answer is None:
                    error_message = (
                        "The response does not contain a 'answer' "
                        f"key: {question_response}"
                    )

                    self.log_error(error_message)

                    return TestCaseOutcome(
                        status=TestCaseStatus.ERROR,
                        test_id=self.test_id,
                        prompt_file=self.prompt.specification.filename,  # type: ignore
                        duration=0,
                        prompt_duration=self.prompt.completion.duration,
                        test_duration=0,
                        prompt_costs=self.prompt.completion.cost,
                        test_costs=0,
                        input_sample=self.input_sample,
                        messages=self.messages,
                        response=response_json.get("explanation", None),
                    )

            except json.JSONDecodeError as err:
                error_message = "The response is not valid JSON."

                self.log_error(error_message, exc_info=err)

                return TestCaseOutcome(
                    test_id=self.test_id,
                    prompt_file=self.prompt.specification.filename,  # type: ignore
                    status=TestCaseStatus.ERROR,
                    duration=engineered_test_prompt.completion.duration,
                    prompt_duration=self.prompt.completion.duration,
                    test_duration=engineered_test_prompt.completion.duration,
                    prompt_costs=self.prompt.completion.cost,
                    test_costs=engineered_test_prompt.completion.cost,
                    input_sample=self.input_sample,
                    messages=self.messages,
                )

            status = (
                TestCaseStatus.PASSED
                if "YES" in question_response
                else TestCaseStatus.FAILED
            )

            error_message = (
                (
                    "The question was not answered with a positive response."
                    f"Got response: {question_response}"
                )
                if status == TestCaseStatus.FAILED
                else None
            )

            if status == TestCaseStatus.FAILED or status == TestCaseStatus.ERROR:
                self.log_error(error_message)

            span.set_attribute("test.id", self.test_id)
            span.set_attribute("prompt.filename", self.prompt.specification.filename)
            span.set_attribute("input.sample.filename", self.input_sample.filename)
            span.set_attribute("test.cost", self.prompt.completion.cost)
            span.set_attribute("test.input_tokens", self.prompt.completion.input_tokens)
            span.set_attribute(
                "test.output_tokens",
                self.prompt.completion.output_tokens,
            )

            return TestCaseOutcome(
                test_id=self.test_id,
                prompt_file=self.prompt.specification.filename,  # type: ignore
                status=status,
                duration=self.prompt.completion.duration,
                prompt_duration=self.prompt.completion.duration,
                test_duration=engineered_test_prompt.completion.duration,
                prompt_costs=self.prompt.completion.cost,
                test_costs=engineered_test_prompt.completion.cost,
                input_sample=self.input_sample,
                messages=self.messages,
                response=input_response,
            )


class FormatTestCase(TestCase):
    """Implementation of a test case for a format based test.

    Attributes
    ----------
    specification: FormatTestSpecification
        The specification for the format test.

    """

    specification: FormatTestSpecification

    def __init__(
        self,
        test_id: str,
        prompt: EngineeredPrompt,
        input_sample: PromptInput,
        specification: FormatTestSpecification,
    ) -> None:
        """Initialize the format test case.

        Parameters
        ----------
        test_id: str
            The unique identifier for the test case.
        prompt: EngineeredPrompt
            The engineered prompt to be used in the test case.
        input_sample: PromptInput
            The input sample to be used in the test case.
        specification: FormatTestSpecification
            The specification for the format test.

        """
        super().__init__(test_id, prompt, input_sample)
        self.specification = specification

    def run(self) -> TestCaseOutcome:
        """Run the test case.

        Returns
        -------
        TestCaseOutcome
            The outcome of the test case.

        """
        with tracer.start_as_current_span("FormatTestCase.run") as span:
            response = self._run_prompt(self.prompt, self.input_sample)

            if self.specification.format == PromptOutputFormat.HTML:
                status = (
                    TestCaseStatus.PASSED
                    if self._is_valid_html(response)
                    else TestCaseStatus.FAILED
                )

                error_message = (
                    "The output is not valid HTML."
                    if status == TestCaseStatus.FAILED
                    else None
                )
            elif self.specification.format == PromptOutputFormat.JSON:
                status = (
                    TestCaseStatus.PASSED
                    if self._is_valid_json(response)
                    else TestCaseStatus.FAILED
                )

                error_message = (
                    "The output is not valid JSON."
                    if status == TestCaseStatus.FAILED
                    else None
                )
            elif self.specification.format == PromptOutputFormat.MARKDOWN:
                status = (
                    TestCaseStatus.PASSED
                    if self._is_valid_markdown(response)
                    else TestCaseStatus.FAILED
                )

                error_message = (
                    "The output is not valid Markdown."
                    if status == TestCaseStatus.FAILED
                    else None
                )
            else:
                status = TestCaseStatus.PASSED
                error_message = None

            span.set_attribute("test.id", self.test_id)
            span.set_attribute("prompt.filename", self.prompt.specification.filename)
            span.set_attribute("input.sample.filename", self.input_sample.filename)
            span.set_attribute("test.cost", self.prompt.completion.cost)
            span.set_attribute("test.input_tokens", self.prompt.completion.input_tokens)
            span.set_attribute(
                "test.output_tokens",
                self.prompt.completion.output_tokens,
            )

            if status == TestCaseStatus.FAILED or status == TestCaseStatus.ERROR:
                self.log_error(error_message)

            return TestCaseOutcome(
                test_id=self.test_id,
                prompt_file=self.prompt.specification.filename,  # type: ignore
                status=status,
                duration=self.prompt.completion.duration,
                prompt_duration=self.prompt.completion.duration,
                test_duration=0,
                prompt_costs=self.prompt.completion.cost,
                test_costs=0,
                input_sample=self.input_sample,
                messages=self.messages,
                response=response,
            )

    def _is_valid_html(self, data: str) -> bool:
        soup = BeautifulSoup(data, "html.parser")
        return data.startswith("<") and bool(soup.find())

    def _is_valid_json(self, data: str) -> bool:
        try:
            json.loads(data)
            return True
        except json.JSONDecodeError:
            return False

    def _is_valid_markdown(self, _data: str) -> bool:
        # Everything that's HTML or plain-text is also valid markdown.
        # If this ever changes, we'll add a proper check here.
        return True


class LanguageTestCase(TestCase):
    """Implementation of a test case for a language based test."""

    specification: LanguageTestSpecification

    def __init__(
        self,
        test_id: str,
        prompt: EngineeredPrompt,
        input_sample: PromptInput,
        specification: LanguageTestSpecification,
    ) -> None:
        """
        Initialize the test case.

        Parameters
        ----------
        test_id : str
            The unique identifier for the test case.
        prompt : EngineeredPrompt
            The engineered prompt to be used in the test case.
        input_sample : PromptInput
            The input sample to be used in the test case.
        specification : LanguageTestSpecification
            The specification for the language test.

        """
        super().__init__(test_id, prompt, input_sample)
        self.specification = specification

    def run(self) -> TestCaseOutcome:
        """Run the test case.

        Returns
        -------
        TestCaseOutcome
            The outcome of the test case.

        """
        with tracer.start_as_current_span("LanguageTestCase.run") as span:
            response = self._run_prompt(self.prompt, self.input_sample)

            # Language detection algorithm is non-deterministic, which means that if you
            # try to run it on a text which is either too short or too ambiguous, you
            # might get different results everytime you run it.

            # To enforce consistent results, call following code before the first
            # language detection:
            DetectorFactory.seed = 0

            # We'll use the langdetect library to detect the language of the response.
            # But not the complete response, because that could be too long.
            # We'll just use the first 100 characters.
            language_response = langdetect.detect(response[:100])

            status = (
                TestCaseStatus.PASSED
                if self.specification.lang_code in language_response
                else TestCaseStatus.FAILED
            )

            error_message = (
                f"The language of the prompt output does not match the specified "
                f"language. Got response: {language_response}"
                if status == TestCaseStatus.FAILED
                else None
            )

            span.set_attribute("test.id", self.test_id)
            span.set_attribute("prompt.filename", self.prompt.specification.filename)
            span.set_attribute("input.sample.filename", self.input_sample.filename)
            span.set_attribute("test.cost", self.prompt.completion.cost)
            span.set_attribute("test.input_tokens", self.prompt.completion.input_tokens)
            span.set_attribute(
                "test.output_tokens",
                self.prompt.completion.output_tokens,
            )

            if status == TestCaseStatus.FAILED or status == TestCaseStatus.ERROR:
                self.log_error(error_message)

            return TestCaseOutcome(
                test_id=self.test_id,
                input_sample=self.input_sample,
                prompt_file=self.prompt.specification.filename,  # type: ignore
                status=status,
                duration=self.prompt.completion.duration,
                prompt_duration=self.prompt.completion.duration,
                test_duration=0,
                prompt_costs=self.prompt.completion.cost,
                test_costs=0,
                messages=self.messages,
                response=response,
            )


class ScoreTestCase(TestCase):
    """Implementation of a test case for a score based test.

    Attributes
    ----------
    specification: ScoreTestSpecification
        The specification for the score test.

    """

    specification: ScoreTestSpecification

    def __init__(
        self,
        test_id: str,
        prompt: EngineeredPrompt,
        input_sample: PromptInput,
        specification: ScoreTestSpecification,
    ) -> None:
        """Initialize the score test case.

        Parameters
        ----------
        test_id: str
            The unique identifier for the test case.
        prompt: EngineeredPrompt
            The engineered prompt to be used in the test case.
        input_sample: PromptInput
            The input sample to be used in the test case.
        specification: ScoreTestSpecification
            The specification for the score test.

        """
        super().__init__(test_id, prompt, input_sample)
        self.specification = specification

    def run(self) -> TestCaseOutcome:
        """Run the test case.

        Returns
        -------
        TestCaseOutcome
            The outcome of the test case.

        """
        with tracer.start_as_current_span("ScoreTestCase.run") as span:
            # TODO: This is a design flaw. Now for each test case, we have to run the prompt for each test case. # noqa
            input_response = self._run_prompt(self.prompt, self.input_sample)

            test_file_path = Path(__file__).parent / "prompts" / "score_testcase.prompt"
            properties = {
                "test_prompt": self.specification.prompt,
                "min_value": self.specification.min,
                "max_value": self.specification.max,
            }

            engineered_test_prompt = EngineeredPrompt(prompt_file=str(test_file_path))

            # Change the provider and model to the one used in the input prompt
            engineered_test_prompt.specification.metadata.provider = (
                self.prompt.specification.metadata.provider
            )
            engineered_test_prompt.specification.metadata.model = (
                self.prompt.specification.metadata.model
            )

            response = engineered_test_prompt.run(
                input_text=input_response, properties=properties
            )

            try:
                response_json = json.loads(response)
                score = response_json.get("score")
                if score is None:
                    error_message = "The response does not contain a 'score' key."

                    self.log_error(error_message)

                    return TestCaseOutcome(
                        status=TestCaseStatus.ERROR,
                        test_id=self.test_id,
                        prompt_file=self.prompt.specification.filename,  # type: ignore
                        prompt_duration=self.prompt.completion.duration,
                        test_duration=engineered_test_prompt.completion.duration,
                        prompt_costs=self.prompt.completion.cost,
                        test_costs=engineered_test_prompt.completion.cost,
                        input_sample=self.input_sample,
                        messages=self.messages,
                        response=response_json.get("response", None),
                        score=score,
                    )

            except json.JSONDecodeError as err:
                error_message = "The response is not valid JSON."

                self.log_error(error_message, exc_info=err)

                return TestCaseOutcome(
                    test_id=self.test_id,
                    prompt_file=self.prompt.specification.filename,  # type: ignore
                    status=TestCaseStatus.ERROR,
                    duration=engineered_test_prompt.completion.duration,
                    prompt_duration=self.prompt.completion.duration,
                    test_duration=engineered_test_prompt.completion.duration,
                    prompt_costs=self.prompt.completion.cost,
                    test_costs=engineered_test_prompt.completion.cost,
                    input_sample=self.input_sample,
                    messages=self.messages,
                )

            status = (
                TestCaseStatus.PASSED
                if score >= self.specification.threshold
                else TestCaseStatus.FAILED
            )

            error_message = (
                (
                    f"The score {score} is not above the threshold "
                    f"{self.specification.threshold}."
                )
                if status == TestCaseStatus.FAILED
                else None
            )

            span.set_attribute("test.id", self.test_id)
            span.set_attribute("prompt.filename", self.prompt.specification.filename)
            span.set_attribute("input.sample.filename", self.input_sample.filename)
            span.set_attribute("test.cost", engineered_test_prompt.completion.cost)
            span.set_attribute(
                "test.input_tokens",
                engineered_test_prompt.completion.input_tokens,
            )
            span.set_attribute(
                "test.output_tokens",
                engineered_test_prompt.completion.output_tokens,
            )

            if status == TestCaseStatus.FAILED or status == TestCaseStatus.ERROR:
                self.log_error(error_message)

            return TestCaseOutcome(
                test_id=self.test_id,
                prompt_file=self.prompt.specification.filename,  # type: ignore
                status=status,
                duration=engineered_test_prompt.completion.duration,
                prompt_duration=self.prompt.completion.duration,
                test_duration=engineered_test_prompt.completion.duration,
                prompt_costs=self.prompt.completion.cost,
                test_costs=engineered_test_prompt.completion.cost,
                input_sample=self.input_sample,
                messages=self.messages,
                score=score,
                response=response_json.get("response", None),
            )


class KeywordTestCase(TestCase):
    """Implementation of a test case for a keyword based test.

    Attributes
    ----------
    specification: KeywordTestSpecification
        The specification for the keyword test.

    """

    specification: KeywordTestSpecification

    def __init__(
        self,
        test_id: str,
        prompt: EngineeredPrompt,
        input_sample: PromptInput,
        specification: KeywordTestSpecification,
    ) -> None:
        """Initialize the keyword test case.

        Parameters
        ----------
        test_id: str
            The unique identifier for the test case.
        prompt: EngineeredPrompt
            The engineered prompt to be used in the test case.
        input_sample: PromptInput
            The input sample to be used in the test case.
        specification: KeywordTestSpecification
            The specification for the keyword test.

        """
        super().__init__(test_id, prompt, input_sample)
        self.specification = specification

    def run(self) -> TestCaseOutcome:
        """Run the test case.

        Returns
        -------
        TestCaseOutcome
            The outcome of the test case.

        """
        with tracer.start_as_current_span("KeywordTestCase.run") as span:
            response = self._run_prompt(self.prompt, self.input_sample)

            status = (
                TestCaseStatus.PASSED
                if self.specification.keyword in response
                else TestCaseStatus.FAILED
            )

            error_message = (
                (
                    f"The keyword '{self.specification.keyword}' was not "
                    "found in the response."
                )
                if status == TestCaseStatus.FAILED
                else None
            )

            span.set_attribute("test.id", self.test_id)
            span.set_attribute("prompt.filename", self.prompt.specification.filename)
            span.set_attribute("input.sample.filename", self.input_sample.filename)
            span.set_attribute("test.cost", self.prompt.completion.cost)
            span.set_attribute("test.input_tokens", self.prompt.completion.input_tokens)
            span.set_attribute(
                "test.output_tokens",
                self.prompt.completion.output_tokens,
            )

            if status == TestCaseStatus.FAILED or status == TestCaseStatus.ERROR:
                self.log_error(error_message)

            return TestCaseOutcome(
                test_id=self.test_id,
                prompt_file=self.prompt.specification.filename,  # type: ignore
                status=status,
                prompt_duration=self.prompt.completion.duration,
                test_duration=0,
                prompt_costs=self.prompt.completion.cost,
                test_costs=0,
                input_sample=self.input_sample,
                messages=self.messages,
                response=response,
            )


def create_test_case(
    test_id: str,
    prompt: EngineeredPrompt,
    spec: TestSpecificationTypes,
    input_sample: PromptInput,
) -> TestCase:
    """Create a test case based on the provided specification type.

    Parameters
    ----------
    test_id : str
        The identifier for the test case in the specification.
    prompt: EngineeredPrompt
        The engineered prompt to be used in the test case.
    spec: TestSpecificationTypes
        The specification type for the test case.
    input_sample: PromptInput
        The input sample to be used in the test case.

    Returns
    -------
    TestCase
        An instance of a test case based on the specification type.

    """
    if isinstance(spec, QuestionTestSpecification):
        return QuestionTestCase(test_id, prompt, input_sample, spec)
    if isinstance(spec, MetricTestSpecification):
        return MetricTestCase(test_id, prompt, input_sample, spec)
    if isinstance(spec, FormatTestSpecification):
        return FormatTestCase(test_id, prompt, input_sample, spec)
    if isinstance(spec, LanguageTestSpecification):
        return LanguageTestCase(test_id, prompt, input_sample, spec)
    if isinstance(spec, PropertyTestSpecification):
        return PropertyTestCase(test_id, prompt, input_sample, spec)
    if isinstance(spec, ScoreTestSpecification):
        return ScoreTestCase(test_id, prompt, input_sample, spec)
    if isinstance(spec, KeywordTestSpecification):
        return KeywordTestCase(test_id, prompt, input_sample, spec)

    error_message = "Unknown test specification type."
    raise ValueError(error_message)
