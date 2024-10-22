"""Tests for EngineeredPromptAnalyzer"""

import pytest
from promptarchitect.analysis.tests import TestAnalyzer


@pytest.mark.llm
def test_no_tests():
    analyzer = TestAnalyzer()

    suggestions = analyzer.run(
        prompt_file=str("tests/analysis/no_tests.prompt"),
    )

    assert suggestions == "No tests found in the prompt file."
