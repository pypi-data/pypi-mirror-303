# Prompt file specification

This section of the user documentation describes the prompt file structure as it's used by Promptarchitect to execute
and validate prompts.

## Representing an engineered prompt

The core of promptarchitect is the engineered prompt. A prompt file contains a single engineered prompt.
A prompt file is written in markdown with frontmatter to configure additional details for the prompt. The frontmatter is written in YAML and is enclosed by `---`.

A prompt file looks like this:

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
author: John Doe
date_created: 2023-10-01
description: This prompt generates a poem about prompt engineering.
---

Write a poem about prompt engineering using the following input:

{{input}}
```

The body of the markdown is the prompt to be executed. The front-matter contains these additional properties:

| Property     | Description                                               | Required |
| ------------ | --------------------------------------------------------- | -------- |
| provider     | The provider for the LLM                                  | No       |
| model        | The alias or full identifier for the LLM to use           | Yes      |
| parameters   | The generation parameters to use for the prompt.          | No       |
| test_path    | The path where the test samples are stored for the prompt | No       |
| tests        | A dictionary containing the tests to validate the prompt  | No       |
| author       | The author of the prompt                                  | No       |
| date_created | The date the prompt was created                           | No       |
| description  | A brief description of the prompt                         | No       |

The `parameters` property is optional and is used to configure the generation parameters for the prompt. The parameters
vary depending on the provider and model you're using. Not all providers support the same set of parameters. Please
check the [Model configuration](#model-configuration) section for more details.

You can start writing a prompt file without specifying tests or test samples. However, you'll want to use tests to
validate that your prompt is working as intended. When you do specify `tests` in the markdown file, you'll also need to
specify the `test_path` where the test_samples are stored.

### Prompt placeholders

The body of a prompt file can contain placeholders that are replaced with properties from the input files. We're using
[mustache templates](https://github.com/noahmorrison/chevron) to render the placeholders into the final prompt.

Consider `{{input}}` to be a placeholder for the body of the input file described in the next section.
The use of `{{input}}` is optional. If we don't find a placeholder for the input, we'll append the input tot the
end of the prompt.

### Using test samples

A prompt can list multiple samples as input files. The test files are located in a directory specified by the `test_path` directory.

Each test sample file is a markdown file that has a similar structure to the prompt file itself. The body of the file is the input you want to process with the prompt. The front-matter contains additional properties that will be used to fill in the placeholders in the prompt.

A sample of an input file is shown below:

```markdown
---
my_property: some_value
another_property: another_value
---

This is the input to be processed by the prompt.
```

You can provide any set of properties in the front-matter of the file. Properties that match placeholders in the
prompt will be used to fill in the placeholders. The body of the file is the input that will be processed by the
prompt.

### Adding tests to an engineered prompt

It's considered a best practice to have one or more tests associated with each prompt to ensure the prompt is working
as intended. Test files are written in YAML and have a different structure depending on the type of test you're running.

The following test types are supported.

- `question` - This test type is used to ask a question using an LLM about the output produced for a sample input.
- `score` - This test type is used to score the output using an LLM produced for a sample input.
- `property` - This test type is used to validate a property of the output produced for a sample input.
- `format` - This test is used to validate the format of the output produced for a sample input.
- `language` - This test is used to validate the language of the output produced for a sample input.

Please find the details for each test type under the [Test configuration](#test-configuration) section.

## Test configuration

### Question test

To validate that your prompt produces the correct output, you can ask a question about the output
using GPT-4o mini. A sample of this test type is shown below.

```yaml
type: question
prompt: Your prompt that gives a yes/no answer to a question about the output produced for the prompt.
```

The following properties are supported

| Property | Description                      | Required |
| -------- | -------------------------------- | -------- |
| type     | The type of test you're running. | Yes      |
| prompt   | The prompt to execute            | Yes      |

### Metric test

You can score the output against a reference metric to validate that the output is correct. Currently, we only support
faithfulness as a metric.

```yaml
type: metric
metric: faithfulness
input:
  question: input
  answer: output
  context: my_property
limit:
  max: 0.9
  min: 0.1
```

The following properties are supported:

| Property | Description                               | Required |
| -------- | ----------------------------------------- | -------- |
| type     | The type of test you're running.          | Yes      |
| metric   | The metric to use for scoring the output. | Yes      |
| input    | The input to use for scoring the output.  | Yes      |
| limit    | The limits for the score.                 | Yes      |

The `limit` property has two sub-properties:

- `min`: The minimum score that is acceptable.
- `max`: The maximum score that is acceptable.

At least one of the limits must be provided.

The input for faithfulness has three properties:

- `context`: The property containing the context for the question.
- `question`: The property containing the question.
- `answer`: The property containing the answer.

### Property test

You can validate a property of the output produced by the prompt. A sample of this test type is shown below.

```yaml
type: property
property:
  unit: lines
  max: 10
  min: 1
```

The following properties are supported:

| Property | Description                      | Required |
| -------- | -------------------------------- | -------- |
| type     | The type of test you're running. | Yes      |
| property | The property to validate.        | Yes      |

The property has the following sub-properties:

- `unit`: The unit of the property. Currently, we support `lines` or `words`.
- `min`: The minimum value for the property.
- `max`: The maximum value for the property.

You must provide at least one of the limits (min or max).

### Format test

You can validate the format of the output produced by the prompt. A sample of this test type is shown below.

```yaml
type: format
format: json
```

We currently support checking for `json`, `html`, `markdown`, and `text` formats.

### Language test

You can validate the language of the output produced by the prompt. A sample of this test type is shown below.

```yaml
type: language
lang_code: en
```

The following properties are supported:

| Property  | Description                      | Required |
| --------- | -------------------------------- | -------- |
| type      | The type of test you're running. | Yes      |
| lang_code | The target language to validate. | Yes      |

The `lang` property should be a valid language code (e.g., `en` for English, `fr` for French).

### Score test

You can validate the score of the output produced by the prompt. A sample of this test type is shown below.

```yaml
type: score
prompt: Please provide a score between 0 and 100.
min: 0
max: 100
threshold: 50
```

The following properties are supported:

| Property  | Description                        | Required |
| --------- | ---------------------------------- | -------- |
| type      | The type of test you're running.   | Yes      |
| prompt    | The prompt to ask for a score.     | Yes      |
| min       | The minimum value for the score.   | Yes      |
| max       | The maximum value for the score.   | Yes      |
| threshold | The threshold value for the score. | Yes      |
