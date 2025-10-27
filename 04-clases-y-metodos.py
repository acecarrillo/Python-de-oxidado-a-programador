class Coche:
    def __init__(self, marca, modelo):
        self.marca_coche = marca
        self.modelo_coche = modelo
        
    def describir(self):
        print(f"Este coche es un {self.marca_coche} {self.modelo_coche}")
        
        
print("Imprimiendo datos almacenados en una clase:")
mi_nissan = Coche("Nissan", "Tsuru")
mi_vw = Coche("Volkswagen", "Golf")

mi_nissan.describir()
mi_vw.describir()