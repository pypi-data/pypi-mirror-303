# Testing Engineered Prompts

Testing your engineered prompts is essential to ensure they produce the desired outputs and behave as expected. PromptArchitect allows you to define and run various types of tests directly within your prompt files. This section explains how to configure and use these tests based on the supported specifications.

---

## Table of Contents

- [Testing Engineered Prompts](#testing-engineered-prompts)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Adding Tests to an Engineered Prompt](#adding-tests-to-an-engineered-prompt)
  - [Supported Test Types](#supported-test-types)
  - [Question Test](#question-test)
    - [Overview Question Test](#overview-question-test)
    - [Configuration Question Test](#configuration-question-test)
    - [Properties Question Test](#properties-question-test)
  - [Score Test](#score-test)
    - [Overview Score Test](#overview-score-test)
    - [Configuration Score Test](#configuration-score-test)
    - [Properties Score Test](#properties-score-test)
  - [Property Test](#property-test)
    - [Overview Property Test](#overview-property-test)
    - [Configuration Property Test](#configuration-property-test)
    - [Properties Property Test](#properties-property-test)
    - [Notes about Property Tests](#notes-about-property-tests)
  - [Format Test](#format-test)
    - [Overview Format Test](#overview-format-test)
    - [Configuration Format Test](#configuration-format-test)
    - [Properties Format Test](#properties-format-test)
  - [Language Test](#language-test)
    - [Overview Language Test](#overview-language-test)
    - [Configuration Language Test](#configuration-language-test)
    - [Properties Language Test](#properties-language-test)
  - [Running Tests](#running-tests)
    - [Test Samples](#test-samples)
      - [Placeholder Usage](#placeholder-usage)
    - [Executing Tests](#executing-tests)
      - [Using the API](#using-the-api)
    - [Interpreting Test Results](#interpreting-test-results)
  - [Best Practices](#best-practices)
  - [Additional Resources](#additional-resources)

---

## Introduction

In PromptArchitect, you can associate one or more tests with each engineered prompt to validate its correctness and reliability. Tests are defined in the front matter of your prompt files and are executed against test samples located in a specified directory.

## Adding Tests to an Engineered Prompt

To add tests to your prompt, include a `tests` section in the front matter of your prompt file. You'll also need to specify the `test_path` where your test samples are stored.

Here's an example prompt file with a test configuration:

```markdown
---
provider: openai
model: gpt-4o-mini
test_path: ./tests
parameters:
  temperature: 0.7
  max_tokens: 2500
tests:
  test_01:
    type: question
    prompt: Is the poem following a haiku scheme?
---

Write a poem about prompt engineering using the following input:

{{input}}
```

In this example:

- `tests` is a dictionary containing test configurations.
- Each test (`test_01` in this case) has a `type` and other properties specific to that test type.
- `test_path` specifies the directory where the test samples are located and is relative to the prompt file.

## Supported Test Types

PromptArchitect supports the following test types:

- [Question Test](#question-test)
- [Score Test](#score-test)
- [Property Test](#property-test)
- Format Test
- Language Test

## Question Test

### Overview Question Test

The question test type allows you to validate the output by asking a question about it using an LLM. The response should typically be a yes/no answer, indicating whether the output meets certain criteria.

### Configuration Question Test

```yaml
tests:
  test_01:
    type: question
    prompt: "Does the output include at least three key points from the input?"
```

### Properties Question Test

- **type**: (Required) Should be set to `question`.
- **prompt**: (Required) The question to ask about the output.

## Score Test

### Overview Score Test

The score test type is used to quantitatively evaluate the output against a specified threshold. You provide a prompt that asks for a score within a defined range.

### Configuration Score Test

```yaml
tests:
  test_01:
    type: score
    prompt: "Rate the clarity of the output on a scale from 1 to 10."
    min: 1
    max: 10
    threshold: 7
```

### Properties Score Test

- **type**: (Required) Should be set to `score`.
- **prompt**: (Required) The prompt to ask for a score.
- **min**: (Required) The minimum possible score.
- **max**: (Required) The maximum possible score.
- **threshold**: (Required) The minimum acceptable score.

## Property Test

### Overview Property Test

The property test type allows you to validate a specific property of the output, such as the number of words or lines.

### Configuration Property Test

```yaml
tests:
  test_01:
    type: property
    property:
      unit: words
      min: 100
      max: 200
```

Or using the equal property:

```yaml
tests:
  test_02:
    type: property
    property:
      unit: lines
      equal: 5
```

### Properties Property Test

Properties Property Test

- **type**: (Required) Should be set to property.
- **property**: (Required) A dictionary specifying:
  - **unit**: The unit to measure (`characters`, `words`, `sentences`, `lines` or `paragraphs`).
  - **min**: (Optional) The minimum acceptable value.
  - **max**: (Optional) The maximum acceptable value.
  - **equal**: (Optional) The exact value that the property should match.

### Notes about Property Tests

- You must provide at least one of the following in the property dictionary:
  - `min`
  - `max`
  - `equal`
- If you specify equal, do not include min or max in the same test, as equal implies an exact match.
- The property test is useful for enforcing structural requirements on the output, such as length constraints.

## Format Test

### Overview Format Test

The format test type checks if the output conforms to a specific format, such as JSON, HTML, Markdown, or plain text.

### Configuration Format Test

```yaml
tests:
  test_01:
    type: format
    format: json
```

### Properties Format Test

- **type**: (Required) Should be set to `format`.
- **format**: (Required) The expected format (`json`, `html`, `markdown`, or `text`).

## Language Test

### Overview Language Test

The language test type validates that the output is in the desired language.

### Configuration Language Test

```yaml

tests:
  test_01:
    type: language
    lang_code: en
```

### Properties Language Test

- **type**: (Required) Should be set to `language`.
- **lang_code**: (Required) The target language code (e.g., `en` for English, `fr` for French). The lang_code should be a valid [ISO 639-1 language code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
  
## Running Tests

### Test Samples

Test samples are input files located in the directory specified by test_path. Each test sample is a markdown file with optional front matter for placeholder properties and a body containing the input text.

Example test sample:

```markdown
---
topic: "artificial intelligence"
---

This is the input text to be processed by the prompt.
```

#### Placeholder Usage

Properties defined in the front matter of the test sample can be used as placeholders in the prompt using mustache templates (e.g., `{{topic}}`).

### Executing Tests

You can run tests using the PromptArchitect CLI or programmatically via the API.

Using the CLI

```bash
promptarchitect --prompts path/to/prompts --run-tests
```

- **--prompts**: Path to your prompt files.
- **--run-tests**: Flag to execute tests defined in the prompts.

#### Using the API

```python
from promptarchitect import EngineeredPrompt

prompt = EngineeredPrompt(
    prompt_file_path='path/to/prompt_file.prompt',
    output_path='output_directory'
)

# Run tests
test_results = prompt.run_tests()
print(test_results)
```

### Interpreting Test Results

Test results will indicate whether each test passed or failed, along with details for any failures to help with debugging.

## Best Practices

- **Organize Tests**: Keep your test configurations well-organized within the prompt files.
- **Use Meaningful Test Names**: Name your tests descriptively to make reports clearer.
- **Version Control**: Track changes to your prompts and tests using version control systems like GitHub.
- **Update Tests Regularly**: Adjust tests when modifying prompts or updating AI models.
- **Use Test Samples**: Create comprehensive test samples to cover various input scenarios.

## Additional Resources

- [Prompt File Specification](prompt-file-specification.md)
- [Mustache Templates](https://github.com/noahmorrison/chevron) for placeholder syntax.
