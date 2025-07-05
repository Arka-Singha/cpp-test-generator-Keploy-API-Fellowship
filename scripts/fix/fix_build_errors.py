import requests
import yaml

def fix_build_errors():
    print("[INFO] Fixing build errors...")

    with open("prompts/fix_build_prompt.yaml", "r") as f:
        prompt = yaml.safe_load(f)["prompt"]

    with open("build/build_log.txt", "r") as f:
        logs = f.read()

    with open("tests/test_main.cpp", "r") as f:
        tests = f.read()

    full_prompt = f"{prompt}\n\nBuild Logs:\n{logs}\n\nGenerated Test Code:\n{tests}"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "codellama", "prompt": full_prompt, "stream": False}
    )

    fixed_code = response.json()["response"]
    with open("tests/test_main.cpp", "w") as f:
        f.write(fixed_code)

    print("[INFO] Build errors resolved using LLM.")
