import json

from promptarchitect.prompting import EngineeredPrompt

# Initialize the EngineeredPrompt
prompt = EngineeredPrompt(
    prompt_file="examples/logging/prompts/generate_titles_ollama.prompt",
    output_path="examples/logging/output_directory",
)

# Download the model in this case gemma2, but you can use any other model
# supported by Ollama (see https://ollama.com/library)
# Only the first time you run the prompt you need to download the model
# prompt.completion.download_model("gemma2")

# Execute the prompt
response = prompt.run()

# Save the prompt information as a JSON file
file_path = "examples/logging/output_directory/prompt_info_ollama.json"
with open(file_path, "w") as file:
    json.dump(prompt.to_dict(), file, indent=4)
