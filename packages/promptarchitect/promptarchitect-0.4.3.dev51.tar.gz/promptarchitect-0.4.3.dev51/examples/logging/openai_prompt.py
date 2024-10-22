import json

from promptarchitect.prompting import EngineeredPrompt

# Initialize the EngineeredPrompt
prompt = EngineeredPrompt(
    prompt_file="examples/logging/prompts/generate_titles_openai.prompt",
    output_path="examples/logging/output_directory",
)

# Execute the prompt
response = prompt.run()

# Save the prompt information as a JSON file
file_path = "examples/logging/output_directory/prompt_info_openai.json"
with open(file_path, "w") as file:
    json.dump(prompt.to_dict(), file, indent=4)
