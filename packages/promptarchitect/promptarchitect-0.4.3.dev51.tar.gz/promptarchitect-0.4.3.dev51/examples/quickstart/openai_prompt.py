from promptarchitect.prompting import EngineeredPrompt

# Initialize the EngineeredPrompt
prompt = EngineeredPrompt(
    prompt_file="examples/quickstart/prompts/generate_titles_openai.prompt",
    output_path="examples/quickstart/output_directory",
)

# Execute the prompt
response = prompt.run()

print(response)
