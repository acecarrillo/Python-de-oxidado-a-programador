from flask import Flask, jsonify, request
import sqlite3
import os
import json
import flask_utilities

app = Flask(__name__)

# Definimos DÓNDE vivirá nuestra base de datos
# La pondremos en una carpeta llamada /data
# (Que Docker manejará por nosotros)
DB_PATH = "/data/mi_base_de_datos.db"

# 2. Definimos una "ruta" (una URL)
#    Esto le dice a Flask: "Cuando alguien visite la página principal ('/')..."
@app.route("/")
def home():
    # Aseguramos que la carpeta /data exista
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    # Nos conectamos a la BD (¡la crea si no existe!)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Creamos una tabla si no existe
    cursor.execute("CREATE TABLE IF NOT EXISTS visitas (id INTEGER PRIMARY KEY, contador INTEGER)")
    
    # Revisamos el contador
    cursor.execute("SELECT contador FROM visitas WHERE id = 1")
    resultado = cursor.fetchone()
    
    if resultado is None:
        # Si es la primera visita
        nuevo_contador = 1
        cursor.execute("INSERT INTO visitas (id, contador) VALUES (1, ?)", (nuevo_contador,))
    else:
        # Si ya existe, le sumamos 1
        nuevo_contador = resultado[0] + 1
        cursor.execute("UPDATE visitas SET contador = ? WHERE id = 1", (nuevo_contador,))
        
    conn.commit() # Guardamos los cambios
    conn.close()
    
    return f"¡Hola, mundo! Esta página ha sido visitada {nuevo_contador} veces."

# 3. Creamos una segunda ruta (para simular una API)
#    Esta devolverá un JSON, como las APIs que ya conoces.
@app.route("/api/v1/saludo")
def api_saludo():
    # 'jsonify' es un helper de Flask que crea un JSON bien formateado
    data = {
        "mensaje": "Hola desde la API",
        "usuario": "tester2"
    }
    return jsonify(data)

@app.route("/saludo/<nombre>")
def saludo_personalizado(nombre):
    # Flask mágicamente toma el valor de la URL 
    # y te lo pasa como argumento a la función.
    return f"¡Hola, {nombre}! ¡Bienvenido a tu página personalizada!"


@app.route("/api/v1/usuario/<username>")
def api_usuario(username):
    # ¡Funciona igual para APIs!
    # (Simulamos una búsqueda de base de datos)
    if username == "angelcarrillo":
        datos = {"id": 1, "rol": "Coordinador", "status": "Activo"}
    else:
        datos = {"id": None, "rol": "Invitado", "status": "No encontrado"}
        
    return jsonify(datos)


@app.route("/api/v1/items", methods=["GET", "POST"])
def api_json_users():
    JSON_PATH = "/data/tareas.json"
    try: 
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        os.makedirs(os.path.dirname(JSON_PATH), exist_ok=True)
        if request.method == "POST":
            datos_recibidos = request.json
            guardar_json = flask_utilities.cargar_tareas(datos_recibidos)
            return jsonify({"mensaje": "Datos recibidos"})
        if request.method == "GET":
            obtener_json_local = flask_utilities.ver_tareas(JSON_PATH)
            return jsonify(obtener_json_local)

    except FileNotFoundError:
        print("Archivo no encontrado")
    except json.JSONDecodeError:
        print("Error: El archivo JSON está corrupto o mal formateado.")

# 4. El "if __name__" que ya conoces.
#    Esto inicia el servidor.
if __name__ == "__main__":
    # debug=True: Hace que el servidor se reinicie solo cada vez que guardas cambios.
    # host='0.0.0.0': Le dice a tu OS que "escuche" peticiones de cualquier lado.
    # port=5000: El "puerto" donde vivirá.
    app.run(debug=True, host='0.0.0.0', port=5001)