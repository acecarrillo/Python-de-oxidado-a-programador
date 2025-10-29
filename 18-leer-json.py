import json

try: 
    with open("usuarios.json","r") as f:
        lista_usuarios_local = json.load(f)
        emails_local = [email["email"] for email in lista_usuarios_local]
        print(emails_local)
except FileNotFoundError:
    print("Error: El archivo 'usuarios.json' no existe.")
    print("¡Ejecuta el script 17 primero!")
except json.JSONDecodeError:
    print("Error: El archivo JSON está corrupto o mal formateado.")