"""PSI Analyzer and recommender for EngineeredPrompts."""

import pathlib

from promptarchitect.prompting import EngineeredPrompt


class PsiEngineeredPromptAnalyzer:
    """Analyze EngineeredPrompts using the Prompt Specification Index (PSI).

    This analysis is performed using a LLM model as specific in the
    src/promptarchitect/analysis/prompts/psi_prompt_recommendations.prompt file.
    """

    def __init__(self) -> None:
        self.prompt_path = (
            pathlib.Path(__file__).parent.parent
            / "analysis"
            / "prompts"
            / "psi_prompt_recommendations.prompt"
        )

    def analyze_prompt(self, prompt_file_path: str) -> str:
        """Analyze test cases for an EngineeredPrompt.

        This function analyzes an EngineeredPrompt and returns the Prompt Sophistication
         Index (PSI) score and gives recommendations on how to improve your prompt
         based on the metrics used within the PSI score.

        Arguments
        ---------
        prompt_file: str
            The path to the prompt file to analyze.
        """
        analysis_prompt = EngineeredPrompt(
            prompt_file=self.prompt_path,
        )

        with open(prompt_file_path, "r") as file:
            prompt_file = file.read()

        return analysis_prompt.run(input_text=prompt_file)
