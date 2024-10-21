"""Tests for PsiEngineeredPromptAnalyzer"""

import pytest
from promptarchitect.analysis.psi import PsiEngineeredPromptAnalyzer


@pytest.mark.llm
def test_analyze_test_case():
    analyzer = PsiEngineeredPromptAnalyzer()
    psi_and_recommendations = analyzer.analyze_prompt(
        prompt_file_path=str("tests/analysis/article.prompt"),
    )

    assert psi_and_recommendations is not None


@pytest.mark.llm
def test_no_tests():
    analyzer = PsiEngineeredPromptAnalyzer()
    psi_and_recommendations = analyzer.analyze_prompt(
        prompt_file_path=str("tests/analysis/no_tests.prompt"),
    )

    assert psi_and_recommendations is not None
