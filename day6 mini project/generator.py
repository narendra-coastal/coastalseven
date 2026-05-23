import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_content(prompt):
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    data = response.json()

    return data["response"]
