# 1. La base (¡la versión nueva!)
FROM python:3.11-slim

# 2. La carpeta de trabajo
WORKDIR /app

# 3. Copia e instala los requisitos
COPY requirements.txt .
RUN pip install -r requirements.txt

# 4. Copia el resto del código
COPY . .

# 5. Expone el puerto de Flask
EXPOSE 5001

# 6. El comando para iniciar Flask
CMD ["python", "22-app-flask.py"]