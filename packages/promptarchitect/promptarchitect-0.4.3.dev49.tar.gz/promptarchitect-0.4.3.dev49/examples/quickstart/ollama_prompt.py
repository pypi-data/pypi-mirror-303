from promptarchitect.prompting import EngineeredPrompt

# Initialize the EngineeredPrompt
prompt = EngineeredPrompt(
    prompt_file="examples/quickstart/prompts/generate_titles_ollama.prompt",
    output_path="examples/quickstart/output_directory",
)

# Download the model in this case gemma2, but you can use any other model
# supported by Ollama (see https://ollama.com/library)
# Only the first time you run the prompt you need to download the model
# prompt.completion.download_model("gemma2")

# Execute the prompt
response = prompt.run()

print(response)
