"""CLI commands for analyzing engineered prompts."""

import os
from pathlib import Path
from typing import Annotated, Optional

import typer

from promptarchitect.analysis.psi import PsiEngineeredPromptAnalyzer
from promptarchitect.analysis.specification import SpecificationAnalyzer
from promptarchitect.analysis.tests import TestAnalyzer

app = typer.Typer()


def _default_report_output_path(prefix: str, file_path: str) -> str:
    prompt_file_name = Path(file_path).stem

    os.makedirs("reports", exist_ok=True)
    return f"reports/{prefix}.{prompt_file_name}.md"


@app.command("tests")
def analyze_tests(
    input: Annotated[str, typer.Option(help="Filename of the prompt file")],  # noqa: A002
    output: Annotated[
        Optional[str],
        typer.Option(help="Filename of the report with the extension .md"),
    ] = None,
) -> None:  # noqa
    """Analyze test cases in the prompt file."""
    analyzer = TestAnalyzer()
    result = analyzer.analyze_test_cases(input)

    if output is None:
        output = _default_report_output_path("tests", input)

    with open(output, "w") as f:
        f.write(result)


@app.command("prompt")
def analyze_prompt(
    input: Annotated[str, typer.Option(help="Filename of the prompt file")],  # noqa: A002
    output: Annotated[
        Optional[str],
        typer.Option(help="Filename of the report with the extension .md"),
    ] = None,
) -> None:
    """Analyze the prompt with PSI."""
    analyzer = PsiEngineeredPromptAnalyzer()
    result = analyzer.analyze_prompt(input)

    if output is None:
        output = _default_report_output_path("prompt", input)

    with open(output, "w") as f:
        f.write(result)


@app.command("specification")
def analyze_specification(
    input: Annotated[str, typer.Option(help="Filename of the prompt file")],  # noqa: A002
    output: Annotated[
        Optional[str],
        typer.Option(help="Filename of the report with the extension .md"),
    ] = None,
) -> None:
    """Analyze the specification."""
    analyzer = SpecificationAnalyzer()
    result = analyzer.analyze_specification(input)

    if output is None:
        output = _default_report_output_path("specification", input)

    with open(output, "w") as f:
        f.write(result)
