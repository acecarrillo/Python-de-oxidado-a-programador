from flask import Flask, jsonify

# 1. Creamos la "aplicación" de Flask
app = Flask(__name__)

# 2. Definimos una "ruta" (una URL)
#    Esto le dice a Flask: "Cuando alguien visite la página principal ('/')..."
@app.route("/")
def home():
    # "...ejecuta esta función."
    return "¡Hola, mundo! Bienvenido a mi primera API."

# 3. Creamos una segunda ruta (para simular una API)
#    Esta devolverá un JSON, como las APIs que ya conoces.
@app.route("/api/v1/saludo")
def api_saludo():
    # 'jsonify' es un helper de Flask que crea un JSON bien formateado
    data = {
        "mensaje": "Hola desde la API",
        "usuario": "maestro_desoxidado"
    }
    return jsonify(data)

# 4. El "if __name__" que ya conoces.
#    Esto inicia el servidor.
if __name__ == "__main__":
    # debug=True: Hace que el servidor se reinicie solo cada vez que guardas cambios.
    # host='0.0.0.0': Le dice a tu OS que "escuche" peticiones de cualquier lado.
    # port=5000: El "puerto" donde vivirá.
    app.run(debug=True, host='0.0.0.0', port=5001)