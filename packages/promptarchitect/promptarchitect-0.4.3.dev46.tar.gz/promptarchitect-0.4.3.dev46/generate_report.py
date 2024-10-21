import os

from promptarchitect.reporting.html import HtmlTestReporter
from promptarchitect.specification import (
    EngineeredPromptMetadata,
    EngineeredPromptSpecification,
    FormatTestSpecification,
    PromptInput,
    QuestionTestSpecification,
)
from promptarchitect.validation.testcases import (
    ModelCosts,
    TestCaseOutcome,
    TestCaseStatus,
)


def generate_spec(filename="test.prompt", with_tests=True):
    test_specs = {}

    if with_tests:
        test_specs = {
            "test01": QuestionTestSpecification(
                prompt="Sample prompt question",
            ),
            "test02": FormatTestSpecification(format="json"),
        }

    return EngineeredPromptSpecification(
        filename="test.prompt",
        prompt="This is a sample prompt.",
        metadata=EngineeredPromptMetadata(
            provider="openai", model="gpt-4o-mini", tests=test_specs
        ),
    )


def generate_outcomes():
    test_outcome_1 = TestCaseOutcome(
        test_id="test01",
        prompt_file="test.prompt",
        status=TestCaseStatus.PASSED,
        costs=ModelCosts(costs=0.5, input_tokens=100, output_tokens=100),
        input_sample=PromptInput(
            id="input-1", input="Sample input", filename="sample-1.txt"
        ),
        prompt_duration=0,
        prompt_costs=0,
        test_duration=0,
        test_costs=0,
    )

    test_outcome_2 = TestCaseOutcome(
        test_id="test02",
        prompt_file="test.prompt",
        status=TestCaseStatus.FAILED,
        error_message="The output is not in the expected format",
        costs=ModelCosts(costs=0.5, input_tokens=100, output_tokens=100),
        input_sample=PromptInput(
            id="input-1", input="Sample input", filename="sample-1.txt"
        ),
        prompt_duration=0,
        prompt_costs=0,
        test_duration=0,
        test_costs=0,
    )

    return [test_outcome_1, test_outcome_2]


def generate_report():
    os.makedirs("./reports", exist_ok=True)

    test_outcomes = generate_outcomes()
    spec_1 = generate_spec()
    spec_2 = generate_spec("test2.prompt", with_tests=False)

    reporter = HtmlTestReporter("./reports", "pajamas")
    reporter.generate_report([spec_1, spec_2], test_outcomes)


if __name__ == "__main__":
    generate_report()
