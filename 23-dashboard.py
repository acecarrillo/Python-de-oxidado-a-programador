# 23-dashboard.py
import streamlit as st
import pandas as pd
import json
import requests # ¡Reutilizando conocimiento!

# Título del Dashboard
st.title("Dashboard de Usuarios (Reemplazo de PBI)")

# ---- Cargar Datos ----
# (Usamos tu conocimiento de la Lección 18, ¡leer JSON!)
@st.cache_data # Mágico: ¡guarda en caché el resultado!
def cargar_datos_api():
    try:
        # ¡Usamos el archivo JSON que ya tienes!
        with open("usuarios.json", "r") as f:
            datos = json.load(f)
        return pd.DataFrame(datos) # Convierte JSON a "tabla" de Pandas
    except FileNotFoundError:
        st.error("¡No se encontró usuarios.json! Corre la lección 17.")
        return pd.DataFrame() # Devuelve tabla vacía

df = cargar_datos_api()

if not df.empty:
    st.header("Datos de Usuarios (desde JSON local)")

    # --- Interactivo ---
    # Un checkbox para mostrar la tabla
    if st.checkbox("Mostrar datos crudos"):
        st.write(df)

    # --- Gráfica ---
    st.header("Usuarios por Ciudad")
    # Cuenta cuántas veces aparece cada ciudad y haz una gráfica de barras
    city_counts = df['address'].apply(lambda x: x['city']).value_counts()
    st.bar_chart(city_counts)