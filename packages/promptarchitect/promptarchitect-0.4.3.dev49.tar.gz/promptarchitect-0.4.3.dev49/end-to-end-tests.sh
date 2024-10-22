mkdir -p end-to-end/output

for example_dir in ./examples/*; do
    echo "Running tests in ${example_dir}"

    mkdir -p end-to-end/output/$(basename $example_dir)
    promptarchitect --prompts $example_dir --output end-to-end/output/$(basename $example_dir)
done