"""Core classes used for analyzing prompt files."""

from abc import ABC, abstractmethod


class Analyzer(ABC):
    """Analyze engineered prompt files."""

    @abstractmethod
    def run(self, prompt_file: str) -> str:
        """Analyze the engineered prompt file.

        Arguments
        ----------
        prompt_file: str
            The path to the engineered prompt file to analyze.

        Returns
        -------
        str
            The analysis report.
        """
        raise NotImplementedError()
