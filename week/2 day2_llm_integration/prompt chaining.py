import requests

url = "http://localhost:11434/api/generate"

article = """
Artificial Intelligence is transforming industries by automating tasks,
improving decision making, and increasing productivity.
"""

# STEP 1 — SUMMARY

summary_prompt = f"Summarize this:\n{article}"

summary_data = {
    "model": "llama3",
    "prompt": summary_prompt,
    "stream": False
}

summary_response = requests.post(url, json=summary_data)

summary = summary_response.json()["response"]

print("SUMMARY:\n")
print(summary)

# STEP 2 — QUIZ GENERATION

quiz_prompt = f"Create 5 quiz questions from this summary:\n{summary}"

quiz_data = {
    "model": "llama3",
    "prompt": quiz_prompt,
    "stream": False
}

quiz_response = requests.post(url, json=quiz_data)

quiz = quiz_response.json()["response"]

print("\nQUIZ:\n")
print(quiz)