"""Test case analysis for prompt files."""

from pathlib import Path
from typing import Dict

from promptarchitect.analysis.core import Analyzer
from promptarchitect.prompting import EngineeredPrompt


class TestAnalyzer(Analyzer):
    """Analyze the tests in an engineered prompt file."""

    __test__ = False  # Mark this for pytest to ignore

    def __init__(self) -> None:
        super().__init__()

        self.prompt_path = (
            Path(__file__).parent.parent
            / "analysis"
            / "prompts"
            / "analyze_test_cases.prompt"
        )

    def run(self, prompt_file: str) -> str:
        """
        Evaluate the quality of tests associated with a given input prompt.

        This function analyzes existing tests, scoring each test from 1 to 5, with 5 representing a highly effective test.
        The scoring is based on clarity, effectiveness, and alignment with the prompt's expected outcome.
        For tests receiving a score of 1-3, the function provides recommendations to improve the test.
        Additionally, it suggests new tests, if necessary, to enhance coverage and validation of the prompt's output.

        Arguments
        ---------
        prompt_file: str
            The path to the prompt file to analyze.
        """  # noqa: E501
        input_prompt = EngineeredPrompt(prompt_file=prompt_file)

        metadata = input_prompt.specification.metadata

        if metadata.tests is None or len(metadata.tests.keys()) == 0:
            return "No tests found in the prompt file."

        analysis_prompt = EngineeredPrompt(
            prompt_file=str(self.prompt_path),
        )

        test_cases = ""

        if metadata.tests is not None:
            for key, value in metadata.tests.items():
                test_cases += f"{key}: {str(value.model_dump())}\n"

        properties: Dict[str, object] = {
            "prompt_specification": test_cases,
            "prompt_text": input_prompt.specification.prompt,
        }

        return analysis_prompt.run(input_file=prompt_file, properties=properties)
