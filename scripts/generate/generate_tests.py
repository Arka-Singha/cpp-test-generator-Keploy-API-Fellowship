# scripts/generate/generate_tests.py

import requests
import yaml
import json


def generate_tests():
    print("[INFO] Generating initial tests...")

    # Load YAML prompt
    try:
        with open("prompts/generate_prompt.yaml", "r") as f:
            prompt = yaml.safe_load(f)["prompt"]
    except Exception as e:
        print(f"[ERROR] Failed to read prompt file: {e}")
        return

    # Load input code
    try:
        with open("input/main.cpp", "r") as f:
            code = f.read()
    except Exception as e:
        print(f"[ERROR] Failed to read input code: {e}")
        return

    # Construct prompt
    full_prompt = f"{prompt}\n\n```cpp\n{code}\n```"

    # Send request to Ollama
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "tinyllama", "prompt": full_prompt, "stream": False}
        )
        res_json = response.json()

        # Validate response
        if "response" not in res_json:
            print("[ERROR] LLM response failed or was incomplete.")
            print(f"[DEBUG] Response: {json.dumps(res_json, indent=2)}")

            # Additional tip for low-memory failure
            if 'error' in res_json and "memory" in res_json['error'].lower():
                print("\n[HINT] Try using a smaller model like `tinyllama` or reduce code size.")
            return

        # Write test output
        output = res_json["response"]
        with open("tests/test_main.cpp", "w") as f:
            f.write(output)

        print("[INFO] Tests generated successfully.")

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to connect to Ollama server: {e}")
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
