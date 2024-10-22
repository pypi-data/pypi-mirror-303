from promptarchitect.prompting import EngineeredPrompt

# Initialize the EngineeredPrompt
prompt = EngineeredPrompt(
    prompt_file="examples/json_output/prompts/aida.prompt",
    output_path="examples/json_output/output_directory",
)

# Execute the prompt
response = prompt.run(input_file='examples/json_output/input/article.txt')

print("-"*20)
print(response)

# Read the json output file
with open("examples/json_output/output_directory/aida.json", "r") as file:
    data = file.read()

print("-"*20)
print(data)
