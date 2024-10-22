from promptarchitect.prompting import EngineeredPrompt

# Initialize the EngineeredPrompt
prompt = EngineeredPrompt(
    prompt_file="examples/system_role/generate_titles.prompt",
    output_path="examples/system_role/output_directory",
)

# Execute the prompt
response = prompt.run()

print(response)

print(f"System role file: {prompt.specification.metadata.system_role}")
print(f"System role text: {prompt.specification.metadata.system_role_text}")
