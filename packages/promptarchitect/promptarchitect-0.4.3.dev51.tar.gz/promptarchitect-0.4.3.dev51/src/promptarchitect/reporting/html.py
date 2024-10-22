"""Reporter implementation for HTML-based test reports.

The HTML reporter uses jinja2 templates to render the test reports in HTML format.
We're supporting two themes: "blue" and "pajamas". But you can specify your own
templates as long as they're compatible with the jinja2 templating engine.

The jinja2 engine we use is configured with the following set of tag filters for easier
formatting:

- `percentage`: Formats a number as a percentage.
- `value`: Returns the value of an enum object.
- `lowercase`: Converts a string to lowercase.
- `detail_report_path`: Returns the path to the detailed report for a prompt file.
"""

import os
from pathlib import Path
from typing import List

from jinja2 import Environment, FileSystemLoader

from promptarchitect.reporting.core import (
    PromptFileTestReport,
    TestReporter,
    TestSessionReport,
)
from promptarchitect.specification import EngineeredPromptSpecification
from promptarchitect.validation.core import TestCaseOutcome


class HtmlTestReporter(TestReporter):
    """Reports test results in HTML format."""

    def __init__(
        self,
        report_path: str,
        theme: str = "blue",
        template_path: str | None = None,
    ) -> None:
        """Initialize the HTML test reporter.

        Parameters
        ----------
        report_path : str
            The path to the report
        theme : str, optional
            The theme to use, by default "blue".
            You can choose between "blue", and "pajamas".
        template_path : str, optional
            The path to the template directory, by default None

        """
        super().__init__(report_path)
        self._create_template_env(theme, template_path)

    def generate_report(
        self,
        prompts: List[EngineeredPromptSpecification],
        test_outcomes: List[TestCaseOutcome],
    ) -> None:
        """Generate the HTML test report.

        Parameters
        ----------
        template_location : str
            The path to the template file
        report_location : str
            The path to the report file
        prompts : List[EngineeredPromptSpecification]
            The prompts that were tested
        test_outcomes : List[TestCaseOutcome]
            The outcomes of the test cases

        """
        os.makedirs(self.report_path, exist_ok=True)

        test_report = self._collect_results(prompts, test_outcomes)

        for file_report in test_report.files_with_tests:
            self._render_prompt_file_report(file_report)

        self._render_dashboard_report(test_report)

    def _render_prompt_file_report(self, file_report: PromptFileTestReport) -> None:
        file_report_content = self._template_env.get_template(
            "prompt_file.html",
        ).render(file_report.model_dump())

        report_file_path = (
            Path(file_report.specification.filename).with_suffix(".html").name
        )

        with open(
            f"{self.report_path}/{report_file_path}",
            "w",
            encoding="utf-8",
        ) as file_report_file:
            file_report_file.write(file_report_content)

    def _render_dashboard_report(self, test_report: TestSessionReport) -> None:
        dashboard_report_content = self._template_env.get_template(
            "dashboard.html",
        ).render(test_report.model_dump())

        with open(f"{self.report_path}/index.html", "w", encoding="utf-8") as dashboard:
            dashboard.write(dashboard_report_content)

    def _create_template_env(
        self,
        theme: str,
        template_path: str | None = None,
    ) -> Environment:
        """Create a Jinja2 template environment with the given theme.

        Parameters
        ----------
        theme : str
            The name of the theme to use
        template_path : str, optional
            The path to the template directory, by default None

        Returns
        -------
        Environment
            The Jinja2 template environment

        """
        base_template_path = (
            Path(__file__).parent.parent / "templates" / "reports" / "themes" / theme
        )

        template_locations = []

        if template_path is not None:
            template_locations.append(template_path)

        template_locations.append(str(base_template_path))

        environment = Environment(
            loader=FileSystemLoader(template_locations),
            autoescape=True,
        )

        environment.filters["percentage"] = lambda x: f"{x:.0%}"
        environment.filters["value"] = lambda x: x.value
        environment.filters["lowercase"] = lambda x: str(x).lower()
        environment.filters["detail_report_path"] = (
            lambda x: Path(x["specification"]["filename"]).stem + ".html"
        )
        environment.filters["round"] = lambda x: str(round(x, 2))

        self._template_env = environment
