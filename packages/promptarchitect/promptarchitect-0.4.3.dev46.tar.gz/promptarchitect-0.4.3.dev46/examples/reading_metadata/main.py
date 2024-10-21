from promptarchitect.prompting import EngineeredPrompt

# Initialize the EngineeredPrompt
prompt = EngineeredPrompt(
    prompt_file="examples/reading_metadata/prompts/generate_titles_ollama.prompt",
    output_path="output_directory",
)

# Get all the metadata from the prompt file
print(prompt.specification.metadata)
