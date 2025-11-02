
import os
import requests

# Config - update these!
input_folder = "processed"
output_folder = "final"
api_url = "http://127.0.0.1:8080/v1/chat/completions"
model_name = "nous-hermes-7b"

os.makedirs(output_folder, exist_ok=True)

def generate_learning_material(text):
    data = {
        "model": model_name,
        "messages": [
            {"role": "user", "content": f"Please create a concise learning summary based on this text:\n\n{text}"}
        ]
    }

    print("  Sending request to llama-server...")
    response = requests.post(api_url, json=data)
    print(f"  Received response: {response.status_code} {response.reason}")
    response.raise_for_status()
    print(f"  Response size: {len(response.content)} bytes")

    return response.json()["choices"][0]["message"]["content"]

def main():
    files = [f for f in os.listdir(input_folder) if f.endswith(".txt")]
    total_files = len(files)
    print(f"Found {total_files} .txt files to process.\n")

    for i, filename in enumerate(files, start=1):
        print(f"[{i}/{total_files}] Processing {filename}...")
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename + ".out.txt")

        with open(input_path, "r", encoding="utf-8") as f:
            content = f.read()

        try:
            result = generate_learning_material(content)
        except Exception as e:
            print(f"  Failed on {filename}: {e}\n")
            continue

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result)

        print(f"  Saved output to {output_path}\n")

if __name__ == "__main__":
    main()

