import pytest
from promptarchitect.analysis.specification import SpecificationAnalyzer


@pytest.mark.llm
def test_analyze_specification():
    analyzer = SpecificationAnalyzer()

    suggestions = analyzer.run(
        prompt_file=str("tests/analysis/article.prompt"),
    )

    assert suggestions is not None
