import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)
    response.raise_for_status()
    
    users = response.json()
    # print(json.dumps(users, indent=2))
    users_name = [user["name"] for user in users]
    print(users_name)
except requests.exceptions.RequestException as e:
    print(f"¡Error al conectar con la API!: {e}")