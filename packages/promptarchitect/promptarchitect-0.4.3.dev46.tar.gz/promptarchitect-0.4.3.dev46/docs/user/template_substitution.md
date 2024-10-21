# Template String Substitution

PromptArchitect includes a powerful feature that allows for dynamic template string substitution within prompt files. This enables you to create flexible and reusable prompts by defining placeholders that can be replaced with specific values at runtime.

---

## Table of Contents

- [Template String Substitution](#template-string-substitution)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Understanding Template Strings](#understanding-template-strings)
  - [Defining Placeholders in Prompts](#defining-placeholders-in-prompts)
  - [Providing Values for Placeholders](#providing-values-for-placeholders)
    - [Using Front Matter in Input Files](#using-front-matter-in-input-files)
    - [Setting Template Variables Programmatically](#setting-template-variables-programmatically)
  - [Examples](#examples)
    - [Example 1: Simple Placeholder Replacement](#example-1-simple-placeholder-replacement)
    - [Example 2: Multiple Placeholders](#example-2-multiple-placeholders)
  - [Best Practices](#best-practices)
  - [Troubleshooting](#troubleshooting)

---

## Introduction

Template string substitution allows you to design prompts with placeholders that can be dynamically replaced with actual values when the prompt is executed. This feature enhances the flexibility of your prompts, enabling you to reuse the same prompt structure with different inputs.

## Understanding Template Strings

PromptArchitect uses [Mustache templates](https://mustache.github.io/) for placeholder syntax. Placeholders are defined within double curly braces `{{ }}` and are replaced with corresponding values during execution.

**Syntax:**

```mustache
{{placeholder_name}}
```

- `placeholder_name` is the key that will be replaced with an actual value.

## Defining Placeholders in Prompts

In your prompt files, you can include placeholders anywhere in the text where you want dynamic content to be inserted.

Example Prompt File:

```markdown
---
provider: openai
model: gpt-4o
parameters:
  temperature: 0.7
  max_tokens: 2500
---

Write a {{content_type}} about {{topic}}.

{{input}}
```

In this example:

- `{{content_type}}` and `{{topic}}` are placeholders that will be replaced with actual values.
- `{{input}}` is a special placeholder representing the content of the input file.

## Providing Values for Placeholders

Values for placeholders can be provided in two ways:

1. Using Front Matter in Input Files
2. Setting Template Variables Programmatically

### Using Front Matter in Input Files

You can define placeholder values in the front matter of your input files. The body of the input file can also be accessed using the {{input}} placeholder.

**Example Input File (`input.md`)**

```markdown
---
content_type: "blog post"
topic: "artificial intelligence"
---

This is the body of the input file that can be accessed using {{input}}.
```

### Setting Template Variables Programmatically

You can set placeholder values directly in your code when executing the prompt.

**Example in Python:**

```python
from promptarchitect import EngineeredPrompt

prompt = EngineeredPrompt(
    prompt_file_path='path/to/prompt_file.prompt',
    output_path='output_directory'
)

# Set template variables programmatically
prompt.set_template_variables({
    'content_type': 'blog post',
    'topic': 'artificial intelligence'
})

# Execute the prompt
response = prompt.execute(input_file='path/to/input_file.txt')
print(response)
```

## Examples

### Example 1: Simple Placeholder Replacement

**Prompt File (`simple_placeholder.prompt`):**

```markdown
---
provider: openai
model: gpt-4o
parameters:
  temperature: 0.5
  max_tokens: 500
---

Generate a summary of the following {{document_type}}:

{{input}}
```

**Input File (`article.md`):**

```markdown
---
document_type: "research article"
---

[The body of the research article goes here.]
```

**Execution:**

When you execute the prompt, `{{document_type}}` will be replaced with "research article," and `{{input}}` will be replaced with the content of `article.md`.

### Example 2: Multiple Placeholders

**Prompt File (**multi_placeholder.prompt**):**

```markdown
---
provider: openai
model: gpt-4o
parameters:
  temperature: 0.6
  max_tokens: 750
---

Dear {{recipient_name}},

We are pleased to inform you that your application for the position of {{position}} has been {{application_status}}.

Best regards,
{{sender_name}}
```

**Input File (`application_response.md`):**

```markdown
---
recipient_name: "John Doe"
position: "Software Engineer"
application_status: "approved"
sender_name: "HR Department"
---

[Optional body content can go here.]
```

**Execution:**

The placeholders will be replaced with the values provided in the input file's front matter, generating a personalized message.

## Best Practices

- **Consistent Naming**: Use clear and consistent names for placeholders to avoid confusion.
- **Default Values**: Consider providing default values in your code if placeholders might be missing.
- **Validation**: Ensure that all required placeholders have corresponding values to prevent runtime errors.
- **Security**: Be cautious when substituting user-provided values to avoid injection attacks.

## Troubleshooting

- **Placeholder Not Replaced**: Check that the placeholder name in the prompt matches the key in the input file or the template variables set in the code.
- **Missing Values**: Ensure that all placeholders have corresponding values provided either in the input file or programmatically.
- **Syntax Errors**: Verify that the placeholder syntax {{placeholder_name}} is correct and that there are no typos.
