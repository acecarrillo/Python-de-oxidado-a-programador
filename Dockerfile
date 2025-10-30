# --- El Plano de la Caja ---

# 1. ¿Cuál es la base?
# Usaremos una imagen oficial de Python 3.10 (una mini-Linux con Python ya instalado).
FROM python:3.10-slim

# 2. ¿Dónde vivirá el código dentro de la caja?
# Creamos una carpeta llamada /app
WORKDIR /app

# 3. ¿Qué necesitamos instalar?
# Copiamos SOLO el archivo de requisitos primero.
COPY requirements.txt .

# 4. Instalamos las dependencias (Flask, requests) DENTRO de la caja.
RUN pip install --no-cache-dir -r requirements.txt

# 5. ¿Cuál es el código de la app?
# Copiamos el resto de tu código (tu app de Flask) a la caja.
COPY . .

# 6. ¿Qué puerto usa la app?
# Le "informamos" a Docker que la app usará el puerto 5001.
EXPOSE 5001

# 7. ¿Cómo "enciendo" la app?
# Este es el comando que se correrá al encender la caja.
# Es lo mismo que tú escribes en tu terminal.
CMD ["python", "22-app-flask.py"]