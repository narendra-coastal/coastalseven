import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

updated_data = {
    "id": 1,
    "title": "Updated Title",
    "body": "This post is updated using PUT request",
    "userId": 1
}

response = requests.put(url, json=updated_data)

print("Status Code:", response.status_code)
print("Response Data:")
print(response.json())