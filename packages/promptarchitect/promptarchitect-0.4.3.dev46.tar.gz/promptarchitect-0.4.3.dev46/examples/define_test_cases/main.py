from pathlib import Path

from promptarchitect.prompting import EngineeredPrompt

# Create the output directory if it does not exist
output_directory = Path("output_directory")
output_directory.mkdir(exist_ok=True)

# Define the path to the prompt and input file
prompt_path = Path("examples/define_test_cases/generate_titles_claude.prompt")

# Initialize the EngineeredPrompt
prompt = EngineeredPrompt(
    prompt_file=str(prompt_path), output_path="output_directory"
)

# Execute the prompt
response = prompt.run()

# Show the response from the model
print(response)

## To run the test, execute see the read.me of this repository
