# Support for Ollama Models

PromptArchitect supports the use of open-source language models running locally via [Ollama](https://ollama.ai). This feature allows you to leverage powerful, locally hosted models, giving you greater control over your AI deployments.

---

## Table of Contents

- [Support for Ollama Models](#support-for-ollama-models)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Benefits of Using Ollama Models](#benefits-of-using-ollama-models)
  - [Supported Models](#supported-models)
  - [Requirements](#requirements)
  - [Installation and Setup](#installation-and-setup)
    - [Step 1: Install Ollama](#step-1-install-ollama)
    - [Step 2: Verify Installation](#step-2-verify-installation)
  - [Downloading Models](#downloading-models)
    - [Example: Downloading Gemma2](#example-downloading-gemma2)
  - [Configuration](#configuration)
    - [Provider Configuration File (`providers.json`)](#provider-configuration-file-providersjson)
    - [Environment Variables](#environment-variables)
  - [Using Ollama Models in Prompts](#using-ollama-models-in-prompts)
    - [Example Prompt Configuration](#example-prompt-configuration)
  - [Example Prompt File](#example-prompt-file)
  - [Best Practices](#best-practices)
  - [Troubleshooting](#troubleshooting)
    - [Common Issues](#common-issues)
    - [Checking Ollama Status](#checking-ollama-status)
  - [Additional Resources](#additional-resources)

---

## Introduction

Ollama provides a platform for running large language models (LLMs) locally on your machine. By integrating Ollama with PromptArchitect, you can execute prompts using local models without relying on external APIs or cloud services.

## Benefits of Using Ollama Models

- **Privacy and Security**: Keep your data local, enhancing privacy and reducing the risk of data leakage.
- **Cost Efficiency**: Avoid API usage fees and reduce operational costs by utilizing local hardware.
- **Customization**: Fine-tune models to better suit your specific use cases.
- **Flexibility**: Switch between different models as needed without changing your codebase significantly.

## Supported Models

PromptArchitect supports several models available through Ollama:

- **Gemma2**: A robust model suitable for various natural language processing tasks.
- **Llama3.1**: An advanced model offering high performance in language understanding and generation.
- **Mistral**: A lightweight model designed for quick responses with lower resource usage.

## Requirements

- **Ollama Installed**: You must have Ollama installed on your local machine. Visit the [Ollama Installation Guide](https://ollama.ai/docs/installation) for instructions.
- **Compatible Hardware**: Running large models locally requires sufficient CPU and memory resources. Ensure your hardware meets the requirements specified by Ollama for the models you intend to use.

## Installation and Setup

### Step 1: Install Ollama

Follow the official instructions to install Ollama for your operating system:

- **macOS**: Use Homebrew

```bash
  brew install ollama
```

- **Linux**: Download the appropriate package from the [Ollama Releases](https://github.com/ollama/ollama/releases) page.
- **Windows**: Ollama currently does not officially support Windows. Consider using a virtual machine or Docker container.

### Step 2: Verify Installation

Confirm that Ollama is installed correctly:

```bash
ollama --version
```

You should see the version number printed in the terminal.

## Downloading Models

Before using a model, you need to download it using Ollama's command-line interface.

### Example: Downloading Gemma2

```bash
ollama pull gemma2
```

Repeat this process for any other models you wish to use (e.g., `llama3.1`, `mistral`).

Alternatively, you can download models programmatically in your Python code:

```python
from promptarchitect import EngineeredPrompt

prompt = EngineeredPrompt()
prompt.completion.download_model("gemma2")
```

## Configuration

To use Ollama models with PromptArchitect, update your provider configuration files to include Ollama as a provider and specify the models.

### Provider Configuration File (`providers.json`)

Create or update the providers.json file in your project's configuration directory:

```json
{
    "ollama": {
        "gemma2": {
            "input_tokens": 0.0,
            "output_tokens": 0.0
        },
        "llama3.1": {
            "input_tokens": 0.0,
            "output_tokens": 0.0,
            "default": true
        },
        "mistral": {
            "input_tokens": 0.0,
            "output_tokens": 0.0
        }
    }
}
```

**Notes:**

- **input_tokens and output_tokens**: Set to `0.0` since local models do not incur token-based costs.
- **default**: You can specify a default model by setting `"default": true`.

### Environment Variables

Ensure that any necessary environment variables for Ollama are correctly set. This may include paths to model directories or configuration files if not using default locations.

## Using Ollama Models in Prompts

When writing your prompt files, specify ollama as the provider and the model name you've configured.

### Example Prompt Configuration

```yaml
---
provider: ollama
model: gemma2
parameters:
  temperature: 0.7
  max_tokens: 2500
---
```

**Notes:**

- **temperature**: Controls the randomness of the output (same as with other models).
- **max_tokens**: Sets the maximum number of tokens to generate.

## Example Prompt File

Here's a complete example of a .prompt file using an Ollama model:

```yaml
---
provider: ollama
model: gemma2
prompt_version: 1.0
parameters:
  temperature: 0.5
  max_tokens: 500
input: examples/inputs/article.txt
output: outputs/summary.txt
test_path: tests/ollama_tests
---
# Instructions

Summarize the following article in three concise paragraphs.

{{input}}
```

In this example:

- **provider**: Set to `ollama` to use a local Ollama model.
- **model**: Specify the model name (`gemma2`).
- **input**: Path to the input file containing the article to summarize.
- **output**: Path where the summary will be saved.
- **test_path**: Directory containing tests for this prompt.

## Best Practices

- **Resource Management**: Running large models locally can consume significant resources. Monitor your system's CPU and memory usage.
- **Model Selection**: Choose models that fit your hardware capabilities and performance requirements.
- **Updates**: Keep Ollama and your models up to date to benefit from performance improvements and new features.

## Troubleshooting

### Common Issues

- **High Resource Usage**: If your system becomes unresponsive, try using a smaller model or reducing max_tokens.
- **Model Not Found**: Ensure the model name in your prompt file matches the one downloaded via Ollama.
- **Ollama Not Installed**: Confirm that Ollama is installed and accessible from your PATH.
- **Permission Errors**: Run your terminal or script with appropriate permissions to access necessary files and directories.

### Checking Ollama Status

You can check the status of Ollama and available models:

```bash
ollama list
```

This will display all the models that are installed and ready to use.

## Additional Resources

- Ollama Documentation: [Official Ollama Docs](https://ollama.com)
- PromptArchitect Examples: See `examples/ollama_models` in the PromptArchitect repository.
