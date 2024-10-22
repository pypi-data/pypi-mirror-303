def test_tests_failed(test_session_report):
    assert test_session_report.tests_failed == 1


def test_tests_passed(test_session_report):
    assert test_session_report.tests_passed == 1


def test_total_duration(test_session_report):
    assert test_session_report.total_prompt_duration == 0.0
    assert test_session_report.total_test_duration == 0.0


def test_total_costs(test_session_report):
    assert test_session_report.total_test_costs == 0.0
    assert test_session_report.total_prompt_costs == 0.0


def test_files_without_tests(test_session_report):
    assert len(test_session_report.files_without_tests) == 0


def test_files_with_tests(test_session_report):
    assert len(test_session_report.files_with_tests) == 1


def test_percentage_with_tests(test_session_report):
    assert test_session_report.percentage_with_tests == 1.0


def test_percentage_with_tests_no_files(test_session_report_without_tests):
    assert test_session_report_without_tests.percentage_with_tests == 0.0
