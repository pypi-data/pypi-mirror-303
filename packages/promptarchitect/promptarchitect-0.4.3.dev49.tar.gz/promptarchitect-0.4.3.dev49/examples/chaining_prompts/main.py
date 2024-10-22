from pathlib import Path

from promptarchitect.prompting import EngineeredPrompt

# Read all prompts from the prompts directory
# And sort them by name
prompt_files = sorted(Path("examples/chaining_prompts/prompts").glob("*.prompt"))

# We will be using the first prompt as the input for the second prompt
# Take a close look in the prompt file for the first prompt
# And notice the output key 'output' which is used to reference the output
# of the first prompt
# We'll repeat this process for the second prompt

# We're using multiple prompts to chain the prompts so
# we have control over the 'creativity' of the model
# by leveraging the temperature setting in the prompt file
# The higher the temperature, the more creative the model will be

for prompt_path in prompt_files:
    # Create a prompt file for each prompt
    # And execute the prompt using the EngineeredPrompt class

    # Initialize the EngineeredPrompt with the prompt file
    prompt = EngineeredPrompt(
        prompt_file=prompt_path,
        output_path="examples/chaining_prompts/output_directory",
    )

    # Execute the prompt
    response = prompt.execute()

    # Show the response from the model
    print(response)
