import os

import pytest
from promptarchitect.reporting.html import HtmlTestReporter


@pytest.fixture
def prompt_specifications(prompt_specification_with_multiple_tests):
    return [prompt_specification_with_multiple_tests]


@pytest.fixture
def report_output_path(tmp_path):
    output_path = tmp_path / "output"

    os.makedirs(output_path, exist_ok=True)

    return output_path


def test_generate_report(report_output_path, prompt_specifications, test_outcomes):
    reporter = HtmlTestReporter(report_output_path, "blue")
    reporter.generate_report(prompt_specifications, test_outcomes)

    files = os.listdir(report_output_path)

    assert len(files) == 2

    assert "index.html" in files
    assert "test02.html" in files


def test_generate_report_nonexisting_directory(
    report_output_path,
    prompt_specifications,
    test_outcomes,
):
    reporter = HtmlTestReporter(report_output_path / "nonexisting", "blue")
    reporter.generate_report(prompt_specifications, test_outcomes)

    files = os.listdir(report_output_path / "nonexisting")

    assert len(files) == 2
    assert "index.html" in files
    assert "test02.html" in files
