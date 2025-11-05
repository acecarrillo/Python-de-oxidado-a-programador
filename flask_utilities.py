from flask import Flask, jsonify, request
import json


def cargar_tareas():
    pass

def dummy():
    datos = [{"id": 1, "nombre": "Laptop"}, {"id": 2, "nombre": "Mouse"}]
    return jsonify(datos)

def ver_tareas(JSON_PATH):
    try: 
        datos = [{"id": 1, "nombre": "Laptop"}, {"id": 2, "nombre": "Mouse"}]
        with open(JSON_PATH, "r") as f: 
                        json_local = json.load(f) 
                        if not json_local: 
                            return datos
                        else:
                            # datos = [{"id": 1, "nombre": "Laptop"}, {"id": 2, "nombre": "Mouse"}]
                            datos = json_local
                            return datos
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []