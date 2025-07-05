import yaml
import subprocess

def refine_tests():
    print("[INFO] Refining existing tests using LLM...")

    # Load YAML prompt
    with open("prompts/refine_prompt.yaml", "r") as f:
        prompt_data = yaml.safe_load(f)

    if not prompt_data or "prompt" not in prompt_data:
        print("[ERROR] Prompt YAML is malformed or missing 'prompt' key.")
        return

    # Load test content
    test_file_path = "tests/test_main.cpp"
    with open(test_file_path, "r") as test_file:
        test_content = test_file.read()

    # Combine with YAML strict instructions
    final_prompt = prompt_data["prompt"] + "\n" + test_content

    try:
        # Call Ollama with direct input
        output = subprocess.check_output(
            ["ollama", "run", "codellama"],
            input=final_prompt,
            text=True
        )

        # Overwrite test file with refined output
        with open(test_file_path, "w") as f:
            f.write(output)

        print("[INFO] Tests refined using LLM.")

    except subprocess.CalledProcessError as e:
        print("[ERROR] Refinement failed:", e.output)


def has_duplicate_tests(test_code):
    lines = test_code.splitlines()
    test_names = [line for line in lines if line.strip().startswith("TEST")]
    return len(test_names) != len(set(test_names))
