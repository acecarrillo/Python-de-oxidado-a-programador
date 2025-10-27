# MÉTODO TRADICIONAL
cuadrados_dict = {} # 1. Creamos un diccionario vacío
for numero in range(5):
    # 2. Asignamos la llave (numero) al valor (numero * numero)
    cuadrados_dict[numero] = numero * numero

print(f"Dict Tradicional: {cuadrados_dict}")
# Salida: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# MÉTODO MODERNO
cuadrados_dict_moderno = {numero: numero * numero for numero in range(5)}

print(f"Dict Moderno:   {cuadrados_dict_moderno}")
# Salida: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# TASK
# Tu objetivo: Crea un diccionario usando comprensión de diccionarios que contenga solo las palabras de la lista que tengan más de 3 letras.
# La llave debe ser la palabra (ej. "hola").
# El valor debe ser la longitud de esa palabra (ej. 4).
# (Pista: Puedes obtener la longitud de un string con len(palabra)).
# El resultado final debería verse así: {'hola': 4, 'repo': 4, 'python': 6, 'oxidado': 7}
palabras = ["hola", "soy", "un", "repo", "de", "python", "oxidado"]
        
lista_dict_moderno = {palabra: len(palabra) for palabra in palabras if len(palabra) >= 4}
print(lista_dict_moderno)