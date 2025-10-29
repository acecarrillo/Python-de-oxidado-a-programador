import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)
    response.raise_for_status()
    
    users = response.json()
    # print(json.dumps(users, indent=2))
    usuarios_con_c = [user["name"] for user in users if user["name"].startswith("C")]
    print(usuarios_con_c)
except requests.exceptions.RequestException as e:
    print(f"¡Error al conectar con la API!: {e}")