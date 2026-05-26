import requests

url = "http://localhost:11434/api/generate"


prompt = input("Enter your prompt: ")

if prompt.lower() == "exit":
        print("Chat ended.")
        

payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

response = requests.post(url, json=payload)

data = response.json()

print("\nAI Response:")
print(data["response"])
print()