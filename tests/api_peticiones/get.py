import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

print(f"El codigo devuelto es: {response.status_code}")

data = response.json() #guardo el response

print(data) #imprimo el response para ver que info trae