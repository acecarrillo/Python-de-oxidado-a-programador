class Coche:
    def __init__(self, marca, modelo):
        self.marca_coche = marca
        self.modelo_coche = modelo
        
    def describir(self):
        return f"Este coche es un {self.marca_coche} {self.modelo_coche}"
        

class CocheElectrico(Coche):
    def __init__(self, marca, modelo, bateria_kwh):
        super().__init__(marca, modelo)
        self.bateria_kwh = bateria_kwh
        
    def describir(self):
        return f"{super().describir()}. Tiene una bateria {self.bateria_kwh}"      
print("Imprimiendo datos almacenados en una clase:")

mi_tesla = CocheElectrico("Tesla", "Model S", 100)
mi_vw = Coche("Volkswagen", "Golf")

print(mi_tesla.describir())
print(mi_vw.describir())