from promptarchitect.prompting import EngineeredPrompt

# Initialize the EngineeredPrompt
prompt = EngineeredPrompt(
    prompt_file="examples/template_strings_in_prompt/generate_titles.prompt",
    output_path="examples/template_strings_in_prompt/output_directory",
)

# The prompt file has two template strings we want to replace
# number and type_of_media
properties = {
    "number": "3",
    "type_of_media": "podcast",
}

# Execute the prompt
response = prompt.run(properties=properties)

print("============= 3 podcast titles =============")
# See the response
print(response)

properties["number"] = "5"
properties["type_of_media"] = "blog post"

# Execute the prompt again but with the new template strings
response = prompt.run(properties=properties)

print("============= 5 blog post titles =============")
# See the response
print(response)
