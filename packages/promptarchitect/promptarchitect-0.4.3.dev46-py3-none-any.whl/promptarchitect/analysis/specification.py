"""Analysis of the prompt specification."""

from pathlib import Path

from promptarchitect.analysis.core import Analyzer
from promptarchitect.prompting import EngineeredPrompt


class SpecificationAnalyzer(Analyzer):
    """Analyzes the specification for optimized settings."""

    def __init__(self) -> None:
        super().__init__()

        self.prompt_path = (
            Path(__file__).parent.parent
            / "analysis"
            / "prompts"
            / "analyze_specification.prompt"
        )

    def run(self, prompt_file: str) -> str:
        """
        Generate a report for a prompt and recommend ideal temperature, and top_p.

        Arguments
        ---------
        prompt_file: str
            The path to the prompt file to analyze.
        """
        # Open the prompt file as text
        with open(prompt_file, "r") as file:
            prompt = file.read()

        analysis_prompt = EngineeredPrompt(
            prompt_file=self.prompt_path,
        )

        properties = {
            "prompt_file": prompt_file,
        }

        report = analysis_prompt.run(
            input_text=prompt,
            properties=properties,
        )

        return self._clean_up_markdown(report)

    def _clean_up_markdown(self, markdown: str) -> str:
        """

        Clean up markdown text.

        Arguments
        ---------
        markdown: str
            The markdown text to clean up.

        Returns
        -------
        str
            The cleaned up markdown text.
        """
        # Sometimes the LLM models respond with some prefixes that we don't want
        if markdown.startswith("```markdown"):
            markdown = markdown.replace("```markdown", "")

        # Remove the last three characters if ``` is present
        if markdown.endswith("```"):
            markdown = markdown[:-3]

        return markdown
