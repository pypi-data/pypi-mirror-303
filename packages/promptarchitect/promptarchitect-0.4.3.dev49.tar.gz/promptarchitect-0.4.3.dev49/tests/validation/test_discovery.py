import os
import shutil

import pytest
from promptarchitect.specification import (
    EngineeredPromptMetadata,
    EngineeredPromptSpecification,
    QuestionTestSpecification,
    TestProfile,
    TestProfileInclude,
    TestSpecificationInclude,
)
from promptarchitect.validation import discover_test_cases, filter_test_cases


@pytest.fixture
def input_samples_dir(tmp_path):
    sample_dir = tmp_path / "input_samples"

    os.makedirs(sample_dir, exist_ok=True)

    (sample_dir / "sample1.md").write_text("Sample 1")
    (sample_dir / "sample2.md").write_text("Sample 2")
    (sample_dir / "sample3.txt").write_text("Sample 3")
    (sample_dir / "sample4.txt").write_text("Sample 4")

    return sample_dir


@pytest.fixture
def valid_prompt_spec(input_samples_dir):
    return EngineeredPromptSpecification(
        metadata=EngineeredPromptMetadata(
            provider="openai",
            model="gpt-4o-mini",
            test_path=str(input_samples_dir),
            tests={
                "test01": QuestionTestSpecification(prompt="Prompt 1"),
                "test02": QuestionTestSpecification(prompt="Prompt 2"),
            },
        ),
        prompt="Placeholder prompt.",
        filename="test_prompt.prompt",
    )


@pytest.fixture
def prompt_directory(tmp_path, valid_prompt_spec):
    dir_path = tmp_path / "prompts"

    os.makedirs(dir_path, exist_ok=True)

    valid_prompt_spec.save(dir_path / "test_prompt_01.prompt")
    valid_prompt_spec.save(dir_path / "test_prompt_02.prompt")

    yield dir_path

    shutil.rmtree(tmp_path)


@pytest.fixture
def test_profile():
    return TestProfile(
        version="0.0.1",
        include=[
            TestProfileInclude(
                filename="test_prompt_01.prompt",
                tests=[TestSpecificationInclude(id="test01", samples=["sample1.md"])],
            )
        ],
    )


def test_discover_tests(prompt_directory):
    prompts, test_cases = discover_test_cases(prompt_directory)

    prompt_filenames = [prompt.filename for prompt in prompts]

    assert len(prompts) == 2
    assert len(test_cases) == 16

    # The sorted list of filenames must be the same as the original list of filenames
    assert prompt_filenames == sorted(prompt_filenames)


def test_discover_tests_without_test_path(tmp_path):
    prompt_spec = EngineeredPromptSpecification(
        metadata=EngineeredPromptMetadata(
            provider="openai",
            model="gpt-4o-mini",
            tests={
                "test01": QuestionTestSpecification(prompt="Prompt 1"),
            },
        ),
        prompt="Placeholder prompt.",
        filename="test_prompt.prompt",
    )

    prompt_dir = tmp_path / "prompts"
    os.makedirs(prompt_dir, exist_ok=True)
    prompt_spec.save(prompt_dir / "test_prompt_01.prompt")

    prompts, test_cases = discover_test_cases(prompt_dir)

    assert len(prompts) == 1
    assert len(test_cases) == 0


def test_discover_tests_with_empty_test_path(tmp_path):
    prompt_spec = EngineeredPromptSpecification(
        metadata=EngineeredPromptMetadata(
            provider="openai",
            model="gpt-4o-mini",
            test_path=str(tmp_path / "empty_samples"),
            tests={
                "test01": QuestionTestSpecification(prompt="Prompt 1"),
            },
        ),
        prompt="Placeholder prompt.",
        filename="test_prompt.prompt",
    )

    prompt_dir = tmp_path / "prompts"

    os.makedirs(prompt_dir, exist_ok=True)
    os.makedirs(prompt_spec.metadata.test_path, exist_ok=True)

    prompt_spec.save(prompt_dir / "test_prompt_01.prompt")

    prompts, test_cases = discover_test_cases(prompt_dir)

    assert len(prompts) == 1
    assert len(test_cases) == 0


def test_discover_tests_with_profile(prompt_directory, test_profile):
    specs, test_cases = discover_test_cases(prompt_directory)
    filtered_tests = filter_test_cases(test_cases, test_profile)

    assert len(filtered_tests) == 1
