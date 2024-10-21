"""CLI interface for the validation module."""

from typing import Annotated

import typer

from promptarchitect.validation import TestSession
from promptarchitect.validation.core import SessionConfiguration
from promptarchitect.tracing import setup_tracing
from dotenv import load_dotenv

app = typer.Typer()


@app.command()
def run(
    prompts: Annotated[str, typer.Option()],
    output: Annotated[str, typer.Option()],
    templates: Annotated[str, typer.Option()] = None,
    report_path: Annotated[str, typer.Option()] = "dashboard",
    report_format: Annotated[str, typer.Option()] = "html",
    report_theme: Annotated[str, typer.Option()] = "pajamas",
    test_profile: Annotated[str, typer.Option()] = None,
) -> None:
    """Create a test session and run the tests."""
    setup_tracing()

    load_dotenv()

    configuration = SessionConfiguration(
        prompt_path=prompts,
        template_path=templates,
        report_format=report_format,
        output_path=output,
        report_path=report_path,
        report_theme=report_theme,
        test_profile_path=test_profile,
    )

    session = TestSession(configuration)

    if not session.start():
        return 1

    return 0
