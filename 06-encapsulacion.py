class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular  # Público
        self.__saldo = saldo_inicial # Privado
        print(f"Cuenta creada para {self.titular} con ${self.__saldo}")

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: ${self.__saldo}")
        else:
            print("La cantidad debe ser positiva.")
            
    def consultar_saldo(self):
        print(f"El saldo de {self.titular} es ${self.__saldo}")
        
    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Saldo restante: {self.__saldo}")
        else:
            print(f"No se puede retirar {cantidad}, saldo insuficiente")
        

mi_cuenta = CuentaBancaria("Ana", 1000)
mi_cuenta.depositar(200)
mi_cuenta.retirar(500)
mi_cuenta.retirar(1000)
mi_cuenta.consultar_saldo()

