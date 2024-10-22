import tempfile

import frontmatter
from promptarchitect.specification import PromptInput


def test_prompt_input_initialization():
    prompt_input = PromptInput(
        id="test",
        input="Test input",
        properties={"key": "value"},
    )

    assert prompt_input.id == "test"
    assert prompt_input.input == "Test input"
    assert prompt_input.properties == {"key": "value"}


def test_prompt_input_from_file():
    with tempfile.NamedTemporaryFile(delete=False, mode="w+") as temp_file:
        temp_file.write("""---
key: value
---
Test input
""")
        temp_file.flush()
        temp_file.seek(0)

        prompt_input = PromptInput.from_file(temp_file.name)

        assert prompt_input.id is not None
        assert prompt_input.input == "Test input"
        assert prompt_input.properties == {"key": "value"}


def test_prompt_input_save():
    prompt_input = PromptInput(
        id="1234",
        input="Test input",
        properties={"key": "value"},
    )
    with tempfile.NamedTemporaryFile(delete=False, mode="w+") as temp_file:
        prompt_input.save(temp_file.name)
        temp_file.flush()
        temp_file.seek(0)
        loaded_content = frontmatter.load(temp_file.name)
        assert loaded_content.content == "Test input"
        assert loaded_content.metadata == {"key": "value"}


def test_prompt_input_hash():
    prompt_input1 = PromptInput(
        id="1234",
        input="Test input",
        properties={"key": "value"},
    )
    prompt_input2 = PromptInput(
        id="1234",
        input="Test input",
        properties={"key": "value"},
    )
    prompt_input3 = PromptInput(
        id="5678",
        input="Different input",
        properties={"key": "different_value"},
    )
    assert hash(prompt_input1) == hash(prompt_input2)
    assert hash(prompt_input1) != hash(prompt_input3)
