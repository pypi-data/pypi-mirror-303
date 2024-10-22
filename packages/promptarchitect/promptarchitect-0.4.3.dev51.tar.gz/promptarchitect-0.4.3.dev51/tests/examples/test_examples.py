import os
import subprocess

import pytest


def find_python_scripts(directory):
    scripts = []
    # Walk through all subdirectories and files in the specified directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file is a Python script
            if file.endswith(".py"):
                scripts.append(os.path.join(root, file))
    return scripts


@pytest.mark.llm
@pytest.mark.parametrize("script_path", find_python_scripts("examples"))
def test_python_script(script_path):
    # Run each Python script and ensure it executes without errors
    try:
        # Determine the appropriate virtual environment scripts directory
        # based on the OS
        venv_scripts_dir = ".venv/scripts" if os.name == "nt" else ".venv/bin"

        # Add the virtual environment scripts directory to the PATH
        env = os.environ.copy()
        env["PATH"] = f"{os.path.abspath(venv_scripts_dir)}{os.pathsep}{env['PATH']}"
        env["PYTHONPATH"] = os.path.abspath("src")

        result = subprocess.run(
            [os.path.join(venv_scripts_dir, "python"), script_path],
            check=True,
            capture_output=True,
            text=True,
            env=env,
        )

        assert (
            result.returncode == 0
        ), f"Script failed with return code {result.returncode}"
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Error while running {script_path}:\n{e.stderr}")
