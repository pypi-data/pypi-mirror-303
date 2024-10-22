# Contributing guide

This guide helps you get started with the repository. But before we start, thank you for
helping us out! We hope you enjoy working with this code as much as we do.

## System requirements

For developing promptarchitect you need:

- Visual Studio Code
- Docker Desktop

## Setting up Git

Our codebase is edited on Linux/Mac for most of the time, so we have a little particular
setup for things like shell scripts and line endings. However, we do support Windows!

Please make sure you configure git by running the following command in a terminal:

```bash
git config core.autocrlf true
```

This setting makes sure that Windows computer don't mess up our line endings. If you
don't have this we'll be pretty sad.

## Setting up the development tools

### Using the development container

You're free to set up your system the way you like, but we recommend running the 
development container. It's easy to use when you have Docker Desktop.

- First, clone the repository to disk.
- Then, open the repository in Visual Studio Code and follow the notifications.

You'll first get a notification about the remote development extension in Visual Studio
Code. Next, you'll get a notification asking you to reopen the project in the container.

When you reopen the project in the development container you'll find that all
dependencies for the project have been installed automatically. We also took care of 
extensions in Visual Studio Code and some recommended settings. The whole process should
take no more than a few minutes, so it's well worth a try.

### Manual configuration

If you're not using the development container you'll need to install 
[Rye](https://rye.astral.sh/) from the website.

Next, run the following command:

```bash
rye sync
```

This will download and install python, sync the dependencies, and install
prompt architect in editable mode.

For Visual Studio Code you'll need the following extensions:

- [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)
- [Ruff Extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
- [Markdown All in One Extension](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)

## Managing code quality

### Using pre-commit hooks

We have some useful pre-commit hooks that help you verify the code before committing it.
You can install the pre-commit hooks using the following command:

```sh
pre-commit install
```

### Running tests

We try to automate as much as possible in our codebase. We use
[Pytest](https://docs.pytest.org/en/stable/) to write unit-tests. 

Test cases that interact with LLMs are marked with `@pytest.mark.llm()` to exclude them
from the CI pipeline. You'll still be able to run the tests locally. 

We recommend using Pytest fixtures to create test data for your tests. The manual will
explain you how. Alternatively, you can check out the existing tests to understand how
we use fixtures.

### Linting

Our code base is validated using a long list of linting rules governed 
by [Ruff](https://docs.astral.sh/ruff/). Please make sure you have the extension installed!

## Submitting pull requests

We love pull-requests, but only if you've described them well and linked them to an existing issue.
So before you submit your pull-request, please create an issue first, so we can discuss the change.