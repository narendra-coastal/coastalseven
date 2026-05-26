import requests
import json

url = "http://localhost:11434/api/generate"

data = {
    "model": "llama3",
    "prompt": "Write a poem about nature",
    "stream": True
}

response = requests.post(url, json=data, stream=True)

for line in response.iter_lines():

    if line:

        chunk = json.loads(line)

        print(chunk["response"], end="")