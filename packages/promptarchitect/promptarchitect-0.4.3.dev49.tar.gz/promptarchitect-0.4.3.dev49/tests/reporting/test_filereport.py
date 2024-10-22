def test_tests_passed(prompt_file_test_report):
    assert prompt_file_test_report.tests_passed == 1


def test_tests_failed(prompt_file_test_report):
    assert prompt_file_test_report.tests_failed == 1


def test_percentage_passed_with_tests(prompt_file_test_report):
    assert prompt_file_test_report.percentage_passed == 0.5


def test_percentage_passed_without_tests(prompt_file_test_report_without_tests):
    assert prompt_file_test_report_without_tests.percentage_passed == 0.0


def test_test_count(prompt_file_test_report):
    assert prompt_file_test_report.test_count == 2


def test_total_errors(prompt_file_test_report):
    assert prompt_file_test_report.total_errors == 0


def test_total_warnings(prompt_file_test_report):
    assert prompt_file_test_report.total_warnings == 0
