"""The official engineered prompt specification.

We use this specification to write prompt files. We can use this specification to
process specifications into engineered prompts, and test cases. The specification is
based off pydantic models for easy validation and serialization.

The specification is divided into two main parts:

1. EngineeredPromptMetadata: This is the metadata for the prompt. It contains test
   cases, and information to configure the prompt. The metadata is stored in the
   front-matter of the prompt file.

2. EngineeredPromptSpecification: This is the main specification for the prompt. It
   contains the metadata and the prompt text. We can use this specification to create
   an EngineeredPrompt object, and test cases.
"""

import json
from enum import Enum
from typing import Annotated, Dict, List, Literal, Optional, Union
from uuid import uuid4

import frontmatter
from pydantic import BaseModel, Field, field_validator, model_validator

VALID_LANGCODES = [
    "en",
    "es",
    "fr",
    "de",
    "it",
    "nl",
    "ru",
    "zh",
    "ja",
    "ko",
    "pt",
    "ar",
    "hi",
    "bn",
    "pa",
    "fa",
    "ur",
    "tr",
    "sv",
    "no",
    "da",
    "fi",
    "pl",
    "cs",
    "hu",
    "ro",
    "el",
    "he",
    "th",
    "vi",
    "id",
    "ms",
    "ta",
    "te",
    "kn",
    "ml",
    "mr",
    "gu",
    "or",
    "as",
    "bh",
    "ne",
    "si",
    "km",
    "lo",
    "my",
    "sd",
    "ps",
    "uz",
    "kk",
    "ky",
    "tg",
    "tk",
    "mn",
    "bo",
    "am",
    "om",
    "so",
    "sw",
    "yo",
    "ig",
    "ha",
    "rw",
    "ny",
    "sn",
    "st",
    "tn",
    "ts",
    "ve",
    "xh",
    "zu",
]


class Limits(BaseModel):
    """Used to configure limits for a property test.

    You can either specify a min value, max value, or both. If you specify both, the
    value must be within the range.

    Attributes
    ----------
    min : Optional[int] = None
        The minimum value for the property.
    max : Optional[int] = None
        The maximum value for the property.

    """

    min: Optional[int] = None
    max: Optional[int] = None

    @model_validator(mode="after")
    def _ensure_correct_limits(self) -> "Limits":
        if self.min is None and self.max is None:
            error_message = "You must specify at least one of min or max values."
            raise ValueError(error_message)

        if self.min is not None and self.max is not None and self.min > self.max:
            error_message = "The min value must be less than the max value."
            raise ValueError(error_message)

        return self

    def between(self, value: int) -> bool:
        """Check if the value is within the limits.

        Parameters
        ----------
        value : int
            The value to check.

        Returns
        -------
        bool
            True if the value is within the limits, False otherwise.

        """
        if self.max is None:
            return self.min <= value
        if self.min is None:
            return value <= self.max

        return self.min <= value <= self.max


class PreciseLimits(BaseModel):
    """Precise limits for a score test.

    You can either specify a min value, max value, or both. If you specify both, the
    value must be within the range.

    Attributes
    ----------
    min : Optional[float] = None
        The minimum value for the score.
    max : Optional[float] = None
        The maximum value for the score.

    """

    min: Optional[float] = None
    max: Optional[float] = None

    @model_validator(mode="after")
    def _ensure_correct_limits(self) -> "PreciseLimits":
        if self.min is None and self.max is None:
            error_message = "You must specify at least one of min or max values."
            raise ValueError(error_message)

        if self.min is not None and self.max is not None and self.min > self.max:
            error_message = "The min value must be less than the max value."
            raise ValueError(error_message)

        return self


class QuestionTestSpecification(BaseModel):
    """A test that validates the prompt output answers a specific question.

    The prompt is considered correct if the question in the prompt property of this test
    is answered with an affirmative.

    Attributes
    ----------
    prompt: str
        The question to ask about the prompt output. The question should result in a yes
        or no answer.

        When the question doesn't specify that the model must answer with yes or no,
        we'll automatically add this instruction to it so the answer can be validated
        correctly.

    """

    type: Literal["question"] = "question"
    prompt: str

    @property
    def description(self) -> str:
        """Get the description of the test.

        Returns
        -------
        str
            The description of the test.

        """
        return f"{self.prompt}"


class PromptOutputFormat(str, Enum):
    """Enum to represent the various output formats for a format test."""

    HTML = "html"
    JSON = "json"
    MARKDOWN = "markdown"


class FormatTestSpecification(BaseModel):
    """A type of test that validates the prompt output is in a specific format.

    Attributes
    ----------
    format: Literal["html", "json", "markdown"]
        The expected format of the prompt output.

    """

    type: Literal["format"] = "format"
    format: PromptOutputFormat

    @property
    def description(self) -> str:
        """Get the description of the test.

        Returns
        -------
        str
            The description of the test.

        """
        return f"Validate the output is in {self.format.value}"


class PropertyUnit(str, Enum):
    """Enum to represent the various units for a property test."""

    WORDS = "words"
    SENTENCES = "sentences"
    LINES = "lines"
    PARAGRAPHS = "paragraphs"
    CHARACTERS = "characters"


class PropertyTestSpecification(BaseModel):
    """A type of test that validates if the output has a specific property.

    For example, does the prompt output a text that has a specific number of words,
    sentences, lines, or paragraphs. The configured limits must have a min or max value,
    or both.

    Attributes
    ----------
    unit: Literal["words", "sentences", "lines", "paragraphs"]
        The unit of the property to check.
    limit: Limits
        The limits for the property.
    equals: Optional[int] = None

    """

    type: Literal["property"] = "property"
    unit: PropertyUnit
    limit: Optional[Limits] = None
    equals: Optional[int] = None

    @model_validator(mode="after")
    def _limit_or_equals_specified(self) -> "PropertyTestSpecification":
        if self.limit is None and self.equals is None:
            error_message = "You must specify at least one of limit or equals values."
            raise ValueError(error_message)

        return self

    @property
    def description(self) -> str:
        """Get the description of the test.

        Returns
        -------
        str
            The description of the test.

        """
        if self.limit:
            return (
                f"Validate the output has {self.limit.min} to "
                f"{self.limit.max} {self.unit}"
            )

        return f"Validate the output has {self.equals} {self.unit}"


class MetricTestSpecification(BaseModel):
    """A type of test that scores the output of the prompt against a named metric.

    The test passes if the score is within the specified limits.

    Attributes
    ----------
    metric: str
        The name of the metric to score the prompt output against.
    input: Dict[str, str]
        The mapping of input/output fields in the test samples to the fields required
        for metric.

        The keys in the input dictionary are the fields required by the metric, and the
        values are the fields in the test context data dictionary.

        The test context data dictionary will always contain the prompt output under
        the key "output". It also contains the input fields specified in the test
        samples. Finally, it contains the body of the test sample under the key "input".
    limit: PreciseLimits
        The limits for the score.

    """

    type: Literal["metric"] = "metric"
    metric: str
    input: Dict[str, str]
    limit: PreciseLimits

    @property
    def description(self) -> str:
        """Get the description of the test.

        Returns
        -------
        str
            The description of the test.

        """
        return (
            f"Validate '{self.metric}' is between {self.limit.min} "
            f"and {self.limit.max}."
        )


class ScoreTestSpecification(BaseModel):
    """A type of test that scores the output of the prompt against a threshold.

    The test passes if the score is above the threshold.

    Attributes
    ----------
    prompt: str
        The prompt to ask for a score.
    min: float
        The minimum value for the score.
    max: float
        The maximum value for the score.
    threshold: float
        The threshold value for the score.

    """

    type: Literal["score"] = "score"
    prompt: str
    min: float
    max: float
    threshold: float

    @model_validator(mode="after")
    def _ensure_correct_limits(self) -> "ScoreTestSpecification":
        if self.min > self.max:
            error_message = "The min value must be less than the max value."
            raise ValueError(error_message)

        if not (self.min <= self.threshold <= self.max):
            error_message = "The threshold must be within the min and max values."
            raise ValueError(error_message)

        return self

    @property
    def description(self) -> str:
        """Get the description of the test.

        Returns
        -------
        str
            The description of the test.

        """
        return (
            f"Validate the score is between {self.min} and {self.max}, "
            f"and above the threshold {self.threshold}."
        )


class LanguageTestSpecification(BaseModel):
    """Validates that the prompt output is in a specific language.

    Attributes
    ----------
    lang: str
        The target language to validate.
    """

    type: Literal["language"] = "language"
    lang_code: str

    @field_validator("lang_code", mode="before")
    @classmethod
    def _validate_lang_code(cls, v: str) -> str:
        if len(v) != 2 or not v.isalpha() or not v.islower():
            error_message = "lang_code must be a two-letter lowercase ISO 639-1 code."
            raise ValueError(error_message)

        if v not in VALID_LANGCODES:
            error_message = f"lang_code '{v}' is not a valid ISO 639-1 language code."
            raise ValueError(error_message)
        return v


class KeywordTestSpecification(BaseModel):
    """A type of test that validates if the output contains a specific keyword.

    The test passes if the keyword is found in the output.

    Attributes
    ----------
    keyword: str
        The keyword to check in the output.

    """

    type: Literal["keyword"] = "keyword"
    keyword: str

    @property
    def description(self) -> str:
        """Get the description of the test.

        Returns
        -------
        str
            The description of the test.

        """
        return f"Validate the output contains the keyword '{self.keyword}'"


TestSpecificationTypes = Union[
    MetricTestSpecification,
    PropertyTestSpecification,
    FormatTestSpecification,
    QuestionTestSpecification,
    LanguageTestSpecification,
    ScoreTestSpecification,
    KeywordTestSpecification,
]


class EngineeredPromptMetadata(BaseModel):
    """Defines the structure of the front-matter portion of a prompt file.

    Attributes
    ----------
    provider : str
        The provider of the model.
    model : str
        The model identifier or alias.
    test_path: str
        The path where the test samples for the prompt are stored.
    tests : dict
        A dictionary of test specifications.
    author : Optional[str]
        The author of the prompt.
    date_created : Optional[str]
        The date the prompt was created.
    description : Optional[str]
        A brief description of the prompt.

    """

    provider: str
    model: str
    prompt_version: Optional[str] = None
    author: Optional[str] = None
    date_created: Optional[str] = None
    description: Optional[str] = None
    input: Optional[str] = None
    output: Optional[str] = None
    output_format: Optional[str] = None
    max_tokens: Optional[int] = None
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    presence_penalty: Optional[float] = None
    frequency_penalty: Optional[float] = None
    test_path: Optional[str] = None
    tests: Optional[
        Dict[
            str,
            Annotated[
                TestSpecificationTypes,
                Field(discriminator="type"),
            ],
        ]
    ] = {}
    system_role: Optional[str] = None
    system_role_text: str = "You are a helpfull assistant."

    @field_validator("prompt_version", mode="before")
    @classmethod
    def _convert_float_to_string(cls, v: float | str) -> str:
        if isinstance(v, float):
            return str(v)
        return v

    def to_dict(self) -> dict:
        """Convert the metadata to a dictionary.

        Returns
        -------
        dict
            The dictionary representation of the metadata.

        """
        return {
            "provider": self.provider,
            "model": self.model,
            "prompt_version": self.prompt_version,
            "input": self.input,
            "output": self.output,
            "output_format": self.output_format,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "top_p": self.top_p,
            "presence_penalty": self.presence_penalty,
            "frequency_penalty": self.frequency_penalty,
            "test_path": self.test_path,
            "tests": {key: value.dict() for key, value in self.tests.items()}
            if self.tests
            else None,
            "system_role": self.system_role,
            "system_role_text": self.system_role_text,
            "author": self.author,
            "date_created": self.date_created,
            "description": self.description,
        }

    def to_json(self) -> str:
        """Convert the metadata to a JSON string.

        Returns
        -------
        str
            The JSON string representation of the metadata.

        """
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data: dict) -> "EngineeredPromptMetadata":
        """Create an EngineeredPromptMetadata instance from a dictionary.

        Parameters
        ----------
        data : dict
            A dictionary containing the data to create an EngineeredPromptMetadata
            instance.

        Returns
        -------
        EngineeredPromptMetadata
            An EngineeredPromptMetadata instance created from the provided dictionary.

        """
        if data.get("tests"):
            data["tests"] = {
                key: TestSpecificationTypes(**value)
                for key, value in data["tests"].items()
            }
        return cls(**data)

    @classmethod
    def from_json(cls, json_str: str) -> "EngineeredPromptMetadata":
        """Create an EngineeredPromptMetadata instance from a JSON string.

        Parameters
        ----------
        json_str : str
            A JSON string containing the data to create an EngineeredPromptMetadata
            instance.

        Returns
        -------
        EngineeredPromptMetadata
            An EngineeredPromptMetadata instance created from the provided JSON string.

        """
        return cls.from_dict(json.loads(json_str))

    @staticmethod
    def model_validate(data: dict) -> "EngineeredPromptMetadata":
        """Validate the metadata dictionary.

        Parameters
        ----------
        data : dict
            The dictionary representation of the metadata.

        Returns
        -------
        EngineeredPromptMetadata
            The metadata object.

        """
        return EngineeredPromptMetadata(**data)


class EngineeredPromptSpecification(BaseModel):
    """EngineeredPromptSpecification is the specification for a prompt file.

    From this specification, we can create an EngineeredPrompt object, and test cases.

    Attributes
    ----------
    metadata : EngineeredPromptMetadata
        The metadata for the prompt.
    prompt : str
        The prompt text.
    filename: str
        The filename where the prompt specification is stored.

    """

    metadata: EngineeredPromptMetadata
    prompt: str
    filename: Optional[str] = None

    @staticmethod
    def from_file(filename: str) -> "EngineeredPromptSpecification":
        """Load a engineered prompt specification from file, and validate it."""
        with open(filename, "r") as f:
            file_content = frontmatter.load(f)

            metadata = EngineeredPromptMetadata.model_validate(file_content.metadata)
            prompt = file_content.content.strip()

            return EngineeredPromptSpecification(
                metadata=metadata,
                prompt=prompt,
                filename=filename,
            )

    def save(self, filename: str) -> None:
        """Save the specification to a file.

        Parameters
        ----------
        filename : str
            The path to the file.

        """
        self.filename = filename

        file_content = frontmatter.Post(self.prompt, **self.metadata.model_dump())
        frontmatter.dump(file_content, filename)

    def to_dict(self) -> dict:
        """Convert the specification to a dictionary.

        Returns
        -------
        dict
            The dictionary representation of the specification.

        """
        return {
            "metadata": self.metadata.dict(),
            "prompt": self.prompt,
            "filename": self.filename,
        }

    @staticmethod
    def from_dict(data: dict) -> "EngineeredPromptSpecification":
        """Create an EngineeredPromptSpecification from a dictionary.

        Parameters
        ----------
        data : dict
            The dictionary representation of the specification.

        Returns
        -------
        EngineeredPromptSpecification
            The specification object.

        """
        return EngineeredPromptSpecification(
            metadata=EngineeredPromptMetadata(**data["metadata"]),
            prompt=data["prompt"],
            filename=data["filename"],
        )

    @property
    def has_tests(self) -> bool:
        """Flag to indicate the specification contains tests."""
        return len(self.metadata.tests.keys()) > 0


class PromptInput(BaseModel):
    """Represents an input sample for an engineered prompt.

    You can load the prompt input from a markdown file using the `from_file` method.
    Alternatively, you can create a `PromptInput` object directly.

    Attributes
    ----------
    input : str
        The input text to the prompt.
    properties : Dict[str, object]
        Additional properties for the prompt input.

    """

    id: str
    input: str
    properties: Dict[str, object] = {}
    filename: Optional[str] = None

    @staticmethod
    def from_file(input_file: str) -> "PromptInput":
        """Load prompt input from a data file.

        Parameters
        ----------
        input_file : str
            The path to the input file.

        Returns
        -------
        PromptInput
            The prompt input.

        """
        with open(input_file, "r") as f:
            input_data = frontmatter.load(f)

        return PromptInput(
            id=str(uuid4()),
            input=input_data.content,
            properties=input_data.metadata,
            filename=input_file,
        )

    def save(self, filename: str) -> None:
        """Save the specification to a file.

        Parameters
        ----------
        filename : str
            The path to the file.

        """
        file_content = frontmatter.Post(self.input, **self.properties)
        frontmatter.dump(file_content, filename)

    def __hash__(self) -> int:
        """Hash the input and properties."""
        return hash((self.input, frozenset(self.properties.items())))


class TestSpecificationInclude(BaseModel):
    """Specifies a test case and a list of samples to include in the test profile."""

    id: str
    samples: List[str]


class TestProfileInclude(BaseModel):
    """Represents an include entry in the test profile.

    Attributes
    ----------
    filename : str
        The path to the prompt file.
    tests : Optional[List[str]]
        The list of tests to include from the prompt file. If not provided, all tests
        from the prompt file will be included.

    """

    filename: str
    tests: Optional[List[TestSpecificationInclude]] = None


class TestProfile(BaseModel):
    """Represents a test profile.

    Attributes
    ----------
    version : str
        The version of the test profile.
    include : List[TestProfileInclude]
        The list of includes for the test profile.

    """

    version: str
    include: List[TestProfileInclude]
