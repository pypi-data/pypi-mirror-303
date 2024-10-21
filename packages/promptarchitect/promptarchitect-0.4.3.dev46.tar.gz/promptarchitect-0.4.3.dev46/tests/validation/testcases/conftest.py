from uuid import uuid4

import pytest
from promptarchitect.prompting import EngineeredPrompt
from promptarchitect.specification import (
    EngineeredPromptMetadata,
    EngineeredPromptSpecification,
    PromptInput,
)


@pytest.fixture
def input_sample():
    return PromptInput(id=str(uuid4()), input="This is a test input.", properties={})


@pytest.fixture
def valid_prompt_specification():
    return EngineeredPromptSpecification(
        metadata=EngineeredPromptMetadata(
            provider="openai",
            model="gpt-4o-mini",
            tests={
                "test01": {
                    "type": "question",
                    "prompt": (
                        "Are all 5 titles written in normal casing? Answer with YES"
                        " or NO. Explain why."
                    ),
                },
            },
        ),
        filename="prompt01.prompt",
        prompt=(
            "Please give me 5 titles for a podcast about machine learning. Write each "
            "title in a separate bullet point. Use normal casing for the titles."
        ),
    )


@pytest.fixture
def engineered_prompt(valid_prompt_specification):
    return EngineeredPrompt(
        specification=valid_prompt_specification,
    )
