from pathlib import Path

from promptarchitect.prompting import EngineeredPrompt

# Set the base path for input and output directories
base_path = Path("examples/prompt_over_multiple_inputs")

# Read all prompts from the prompts directory and sort them by name
input_files = sorted(base_path.joinpath("input").glob("*.txt"))

# We will read all input files from the input directory
# And use each input file as the input for the prompt
# We'll repeat this process for each input file

output_directory = base_path.joinpath("output_directory")

# Get all input files from the input directory
for input_file_path in input_files:
    # Create a prompt file for each input file
    # And execute the prompt using the EngineeredPrompt class

    # Initialize the EngineeredPrompt with the prompt file
    # Make sure the different output files are saved in different directories

    prompt = EngineeredPrompt(
        prompt_file=base_path.joinpath("prompts/01 - Generate titles.prompt"),
        output_path=output_directory,
    )

    # Execute the prompt
    response = prompt.run(input_file=str(input_file_path))

    # Show the response from the model
    print(response)
