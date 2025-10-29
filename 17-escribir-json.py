import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)
    response.raise_for_status()
    
    users = response.json()
    # print(json.dumps(users, indent=2))
    with open("usuarios.json", "w") as f:
        json.dump(users, f, indent=4)

    print("¡Archivo JSON guardado!")
except requests.exceptions.RequestException as e:
    print(f"¡Error al conectar con la API!: {e}")