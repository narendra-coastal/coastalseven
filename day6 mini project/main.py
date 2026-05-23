from generator import generate_content
from prompts import PROMPTS


import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def save_history(data):
    history_dir = os.path.join(BASE_DIR, "history")

    os.makedirs(history_dir, exist_ok=True)

    file_path = os.path.join(history_dir, "generated.txt")

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(data + "\n")

while True:
    print("\nAI Content Generator")
    print("1. Email")
    print("2. Blog")
    print("3. LinkedIn Post")
    print("4. YouTube Script")
    print("5. Exit")

    choice = input("Choose option: ")

    options = {
        "1": "email",
        "2": "blog",
        "3": "linkedin",
        "4": "youtube"
    }

    if choice == "5":
        print("Goodbye!")
        break

    if choice not in options:
        print("Invalid choice.")
        continue

    topic = input("Enter topic: ")

    content_type = options[choice]

    final_prompt = f"{PROMPTS[content_type]} {topic}"

    result = generate_content(final_prompt)

    print("\nGenerated Content:\n")
    print(result)

    save_history(result)
