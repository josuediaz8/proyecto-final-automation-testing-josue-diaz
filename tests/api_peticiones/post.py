import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {"name":"Josue", "job":"Ingeniero"}

response = requests.post(url,json=payload)

print(response.status_code)
print(response.json())
