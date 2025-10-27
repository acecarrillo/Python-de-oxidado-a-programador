# Define el "plano": Escribe una clase llamada Coche.
# Define el "constructor" (__init__):
# Debe aceptar self (¡siempre va primero!) y dos argumentos más: marca y modelo.
# Dentro del __init__, guarda esos argumentos en el objeto. (ej. self.marca_coche = marca y self.modelo_coche = modelo).
# Crea los "objetos":
# Crea (instancia) un objeto llamado mi_nissan que sea un Coche de marca "Nissan" y modelo "Tsuru".
# Crea otro objeto llamado mi_vw que sea un Coche de marca "Volkswagen" y modelo "Golf".
# Verifica tu trabajo:
# Añade print()s al final para imprimir el modelo del Tsuru y la marca del Golf (accediendo a ellos con mi_nissan.modelo_coche y mi_vw.marca_coche).

class Coche:
    def __init__(self, marca, modelo):
        self.marca_coche = marca
        self.modelo_coche = modelo
        
print("Imprimiendo datos almacenados en una clase:")
mi_nissan = Coche("Nissan", "Tsuru")
mi_vw = Coche("Volkswagen", "Golf")

print(f"El modelo de mi {mi_nissan.marca_coche} es {mi_nissan.modelo_coche}")
print(f"El modelo de mi {mi_vw.marca_coche} es {mi_vw.modelo_coche}")