# Importamos el módulo que acabamos de instalar
import requests
import json # Este módulo SÍ viene con Python

# Esta es la URL de un "post" de prueba
url = "https://jsonplaceholder.typicode.com/users/5"

print(f"Haciendo una petición a: {url}")

try:
    # 1. Usamos el módulo 'requests' para hacer un GET (pedir datos)
    respuesta = requests.get(url)

    # 2. El módulo puede revisar si la petición fue exitosa (código 200)
    respuesta.raise_for_status()

    # 3. El módulo 'requests' tiene un helper .json()
    #    para convertir la respuesta de texto (JSON) a un diccionario de Python
    datos = respuesta.json()

    print("\n¡Éxito! Respuesta recibida:")
    
    # 4. 'json.dumps' es una forma "bonita" de imprimir un diccionario
    print(json.dumps(datos, indent=2))
    
    print("\nNombre:")
    print(datos['name'])
    print("\nEmail:")
    print(datos['email'])

except requests.exceptions.RequestException as e:
    print(f"¡Error al conectar con la API!: {e}")