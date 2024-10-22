import os
import shutil
import json
import pytest
from promptarchitect.reporting.json import JsonTestReporter


@pytest.fixture
def prompt_specifications(prompt_specification_with_multiple_tests):
    return [prompt_specification_with_multiple_tests]


@pytest.fixture
def report_output_path(tmp_path):
    report_path = tmp_path / "json_reporter"
    os.makedirs(report_path, exist_ok=True)

    yield report_path

    shutil.rmtree(report_path)


def test_generate_report(report_output_path, prompt_specifications, test_outcomes):
    reporter = JsonTestReporter(report_output_path)
    reporter.generate_report(prompt_specifications, test_outcomes)

    with open(report_output_path / "report.json", "r", encoding="utf-8") as report_file:
        report_data = json.load(report_file)

    assert "files" in report_data
    assert len(report_data["files"]) == 1
    assert "tests" in report_data["files"][0]
    assert len(report_data["files"][0]["tests"]) == 2


def test_json_output_fields(report_output_path, prompt_specifications, test_outcomes):
    reporter = JsonTestReporter(report_output_path)
    reporter.generate_report(prompt_specifications, test_outcomes)

    with open(report_output_path / "report.json", "r", encoding="utf-8") as report_file:
        report_data = json.load(report_file)

    assert "files" in report_data
    assert len(report_data["files"]) == 1

    file_report = report_data["files"][0]
    assert "specification" in file_report
    assert "tests" in file_report

    test_report = file_report["tests"][0]
    assert "test_id" in test_report
    assert "specification" in test_report
    assert "outcomes" in test_report

    outcome = test_report["outcomes"][0]
    assert "test_id" in outcome
    assert "status" in outcome
    assert "input_sample" in outcome
    assert "messages" in outcome
