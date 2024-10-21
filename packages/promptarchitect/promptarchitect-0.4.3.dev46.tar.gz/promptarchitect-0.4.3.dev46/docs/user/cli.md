# Command Line Interface (CLI) Usage

This document provides detailed instructions on how to use the CLI commands available in the `promptarchitect` package.

## Overview

The `promptarchitect` package provides a command line interface (CLI) for analyzing and testing engineered prompts. The CLI is built using the `typer` library and offers several commands to help you work with your prompts.

## Installation

To use the CLI, you need to have the `promptarchitect` package installed. You can install it using pip:

```bash
pip install promptarchitect
```

## CLI Commands

The CLI commands are organized into two main groups: `analyze` and `test`. Each group contains specific commands for different tasks.

### Analyze Commands

The `analyze` group contains commands for analyzing engineered prompts. These commands are defined in `src/promptarchitect/analysis/cli.py`.

#### Analyze Tests

Analyze test cases in the prompt file.

```bash
promptarchitect analyze tests --input <prompt_file> [--output <report_file>]
```

- `--input`: Filename of the prompt file.
- `--output`: (Optional) Filename of the report with the extension .md. If not provided, a default report file will be created in the `reports` directory.

#### Analyze Prompt

Analyze the prompt with PSI.

```bash
promptarchitect analyze prompt --input <prompt_file> [--output <report_file>]
```

- `--input`: Filename of the prompt file.
- `--output`: (Optional) Filename of the report with the extension .md. If not provided, a default report file will be created in the `reports` directory.

#### Analyze Specification

Analyze the specification.

```bash
promptarchitect analyze specification --input <prompt_file> [--output <report_file>]
```

- `--input`: Filename of the prompt file.
- `--output`: (Optional) Filename of the report with the extension .md. If not provided, a default report file will be created in the `reports` directory.

### Test Commands

The `test` group contains commands for testing engineered prompts. These commands are defined in `src/promptarchitect/validation/cli.py`.

#### Run Tests

Create a test session and run the tests.

```bash
promptarchitect test run --prompts <prompt_path> --output <output_path> [--templates <template_path>] [--report_path <report_path>] [--report_format <report_format>] [--report_theme <report_theme>] [--test_profile <test_profile>]
```

- `--prompts`: Path to the prompt files.
- `--output`: Path to the output directory.
- `--templates`: (Optional) Path to the template files.
- `--report_path`: (Optional) Path to the report directory. Default is `dashboard`.
- `--report_format`: (Optional) Format of the report. Default is `html`.
- `--report_theme`: (Optional) Theme of the report. Default is `pajamas`.
- `--test_profile`: (Optional) Path to the test profile file.

## Examples

Here are some examples of how to use the CLI commands.

### Example 1: Analyze Tests

```bash
promptarchitect analyze tests --input example.prompt --output reports/tests.example.md
```

### Example 2: Analyze Prompt

```bash
promptarchitect analyze prompt --input example.prompt --output reports/prompt.example.md
```

### Example 3: Analyze Specification

```bash
promptarchitect analyze specification --input example.prompt --output reports/specification.example.md
```

### Example 4: Run Tests

```bash
promptarchitect test run --prompts prompts/ --output output/ --templates templates/ --report_path reports/ --report_format html --report_theme pajamas --test_profile testprofile.json
```

## Conclusion

The `promptarchitect` CLI provides a powerful and flexible way to analyze and test your engineered prompts. By using the commands described in this document, you can ensure that your prompts are well-structured, thoroughly tested, and ready for use in your AI applications.
