# PromptArchitect

## Table of Contents

- [PromptArchitect](#promptarchitect)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Prompt Engineering Stages](#prompt-engineering-stages)
  - [Features and Documentation](#features-and-documentation)
  - [Installation](#installation)
  - [Quickstart](#quickstart)
  - [Examples](#examples)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Introduction

PromptArchitect is a tool designed for crafting and managing **Engineered Prompts**—structured inputs for AI models that ensure consistent and reliable outputs. Engineered prompts are integral to automated processes involving large language models (LLMs) and other AI systems.

## Prompt Engineering Stages

![Prompt Engineering Stages](docs/user/images/PromptArchitect%20-%20Stages.png)

Prompt engineering is broken down into three key stages to ensure that prompts are designed, executed, and improved in a systematic and effective manner:

1. **Prompt Design**:
   - In this initial phase, prompts are crafted and refined through multiple iterations using a series of test cases. The goal is to create prompts that are tailored for specific tasks and environments. By optimizing the prompts based on the performance criteria, this stage helps in minimizing errors before deployment.
   - **Key Steps**:
     - Writing prompts
     - Creating and running test cases
     - Iterative refinement of engineered prompts

2. **Prompt Execution**:
   - After the prompts have been designed, they are deployed in a production environment. In this stage, prompts are executed using real-world data. The focus here is to log inputs and outputs to ensure traceability, transparency, and proper decision-making based on the prompt logic.
   - **Key Steps**:
     - Processing text input
     - Deploying the engineered prompt
     - Capturing results
     - Maintaining a detailed prompt log

3. **Prompt Improvement**:
   - This final stage focuses on refining and evolving the prompts. By analyzing data from the execution phase, including test results and prompt logs, inefficiencies or issues can be addressed. This ensures the prompt is re-engineered to meet updated requirements, improving robustness and reliability over time.
   - **Key Steps**:
     - Review and analysis of the prompt log
     - Running additional test cases to identify areas for improvement
     - Implementing prompt recommendations for future deployments

The combination of these stages ensures that prompts are developed, deployed, and continuously refined to maintain high performance and reliability in real-world applications.

## Features and Documentation

For detailed information on using PromptArchitect, please refer to the documentation in the `docs` folder:

- **[Detailed Features](docs/user/features.md)**: Explore all the features of PromptArchitect.
- **[Structured Prompt Development](docs/user/structured_prompt_development.md)**: Create precise and reusable prompts with versioning and documentation.
- **[Testing Engineered Prompts](docs/user/testing.md)**: Learn how to test your prompts using unit, integration, performance, and regression tests.
- **[Command Line Interface (CLI) Usage](docs/user/cli.md)**: Instructions on how to use PromptArchitect via the CLI.
- **[Support for Ollama Models](docs/user/ollama_models.md)**: Information on using open-source models like Gemma2, Llama3.1, and Mistral with PromptArchitect.
- **[Template String Substitution](docs/user/template_substitution.md)**: Learn how to use dynamic placeholders within prompts.
- **[Cost Control](docs/cost_control.md)**: Guidance on managing and optimizing costs when using PromptArchitect with LLMs.
- **[Dashboard Customization](docs/user/dashboard_customization.md)**: Customize the PromptArchitect dashboard with custom themes.

## Installation

Install PromptArchitect using pip:

```bash
pip install promptarchitect
```

## Quickstart

```python
from promptarchitect import EngineeredPrompt

# Initialize the EngineeredPrompt
prompt = EngineeredPrompt(
    prompt_file_path='path_to_prompt_file.prompt',
    output_path='output_directory'
)

# Execute the prompt
response = prompt.execute(input_file='path_to_input_file.txt')
print(response)
```

## Examples

Explore the `examples` folder for practical use cases. Detailed instructions can be found in the `docs/examples` directory:

- **Quick Start**: Set up an Engineered Prompt for different providers and models.
- **Defining Test Cases**: Define semantic and format tests.
- **System Role**: Use a custom system role with prompts.
- **Configuring Models**: Customize model settings.
- **Retrieving Cost and Duration**: Get cost and duration per executed prompt.
- **Chaining Prompts**: Use the output of one prompt as input for another.
- **Template Strings in Prompts**: Substitute template strings within prompts.
- **Automatic Caching with Expiration**: Optimize performance and manage execution costs.

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for more details on our contribution guidelines.

## License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this software. See the [LICENSE](LICENSE) file for the full license text.

## Contact

If you have any questions, issues, or suggestions, please open an issue on this GitHub repository or reach out to the maintainers:

- **GitHub Issues**: [Issue Tracker](https://github.com/yourusername/PromptArchitect/issues)
