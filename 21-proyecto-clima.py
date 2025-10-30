# 21-proyecto-clima.py

import sys
import requests
import json

# --- 1. Tu Módulo de Clases (POO) ---
# Vamos a organizar nuestro código limpiamente.

class ClimaService:
    """
    Una clase que se encarga de toda la lógica
    de hablar con las APIs del clima.
    """
    
    def __init__(self):
        # El servicio de Geocodificación (ciudad -> lat/lon)
        self.geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
        # El servicio de Clima (lat/lon -> clima)
        self.weather_url = "https://api.open-meteo.com/v1/forecast"

    def obtener_coordenadas(self, ciudad):
        """
        Toma un nombre de ciudad y devuelve (latitud, longitud).
        """
        print(f"Buscando coordenadas para '{ciudad}'...")
        params = {
            "name": ciudad,
            "count": 1 # Solo queremos el primer resultado
        }
        try:
            response = requests.get(self.geocoding_url,params)
            response.raise_for_status()
            coord = response.json()
            # print(json.dumps(coord, indent=2))
            if "results" not in coord or not coord["results"]:
                print("No se encontro la ciudad")
                return None, None
            else: 
                latitud, longitud = coord["results"][0]["latitude"], coord["results"][0]["longitude"]
                print(f"Coordenadas encontradas {latitud, longitud}")
                return latitud, longitud
            
        except requests.exceptions.RequestException as e:
            print(f"¡Error al conectar con la API!: {e}")

    def obtener_clima_actual(self, lat, lon):
        """
        Toma lat/lon y devuelve el clima actual.
        """
        print(f"Obteniendo clima para ({lat}, {lon})...")
        
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True # ¡Importante!
        }
        
        try:
            response = requests.get(self.weather_url,params)
            response.raise_for_status()
            clima = response.json()
            # print(json.dumps(clima, indent=2))
            return clima["current_weather"]
        except requests.exceptions.RequestException as e:
            print(f"¡Error al conectar con la API!: {e}")




def main():
    """
    Función principal del script.
    """
    if len(sys.argv) != 2:
        print("Error: Debes pasar el nombre de la ciudad.")
        print("Uso: python 21-proyecto-clima.py \"Nombre de la Ciudad\"")
        sys.exit(1)
        
    ciudad_nombre = sys.argv[1]
    
    try:
        servicio_clima = ClimaService()
        
        lat, lon = servicio_clima.obtener_coordenadas(ciudad_nombre)
        
        if lat is None:
            print(f"Error: No se pudo encontrar la ciudad '{ciudad_nombre}'.")
            sys.exit(1)
            
        clima = servicio_clima.obtener_clima_actual(lat, lon)
        
        # 4. Imprime el reporte final
        print("\n--- Reporte del Clima ---")
        print(f"Ciudad: {ciudad_nombre}")
        print(f"Temperatura: {clima['temperature']} °C")
        print(f"Velocidad Viento: {clima['windspeed']} km/h")
        print("-------------------------")

    except requests.exceptions.RequestException as e:
        print(f"Error de red: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()