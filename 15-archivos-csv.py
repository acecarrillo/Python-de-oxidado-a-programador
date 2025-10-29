import csv

header = ['nombre', 'puesto', 'salario']
data = [
    ['Ana', 'CEO', 100000],
    ['Beto', 'Developer', 80000],
    ['Carla', 'RH', 50000]
]

# 'w' de write.
# OJO: El 'newline=""' es un truco de magia necesario
# para que los saltos de línea funcionen bien en todos
# los sistemas operativos (Windows/Mac/Linux). ¡Ponlo siempre!
with open('personal.csv', 'w', newline='') as archivo_csv:
    
    # 1. Creamos un "escritor" de CSV
    escritor = csv.writer(archivo_csv)
    
    # 2. Escribimos UNA fila (el encabezado)
    escritor.writerow(header)
    
    # 3. Escribimos TODAS las filas de golpe
    escritor.writerows(data)

print("¡Archivo 'personal.csv' creado!")

print("Leyendo archivo recien creado")

try:
    with open('personal.csv', 'r') as archivo_csv:
        lector = csv.reader(archivo_csv)
        
        # 2. Iteramos sobre el lector.
        # ¡Cada 'fila' que nos da es una LISTA de strings!
        # print(lector.keys[1])
        for fila in lector:
            if fila[1] != "CEO" and fila[0] != "nombre":
                print(fila)

except FileNotFoundError:
    print("No se encontró el archivo.")