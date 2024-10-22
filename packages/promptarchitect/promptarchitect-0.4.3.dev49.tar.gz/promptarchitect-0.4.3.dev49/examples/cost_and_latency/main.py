from pathlib import Path

from promptarchitect.prompting import EngineeredPrompt

# Create the output directory if it does not exist
output_directory = Path("output_directory")
output_directory.mkdir(exist_ok=True)

# Define the path to the prompt and input file
prompt_path = Path("examples/cost_and_latency/prompts/generate_titles_claude.prompt")

# Initialize the EngineeredPrompt
prompt = EngineeredPrompt(
    prompt_file=str(prompt_path), output_path="output_directory"
)

# Execute the prompt
response = prompt.run()

print(response)

# Show the cost and duration for this prompt execution
print(f"Cost: {prompt.completion.cost:.6f}")  # Cost is in USD per million tokens
print(f"Latency: {prompt.completion.duration:.2f}s")  # Latency is in seconds
