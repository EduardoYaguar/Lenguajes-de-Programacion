class CuentaBancaria:

    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo
    def depositar(self, cantidad):
        self.saldo += cantidad
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("saldo insuficiente")
    def __str__(self) -> str:
        return f"Cuenta bancaria de {self.nombre} con saldo de {self.saldo}"
    

cuenta = CuentaBancaria("Juan Perez", 1000)
cuenta2 = CuentaBancaria("Andres Lopez", 500)
cuenta3 = CuentaBancaria("Sofia Gonzalez", 1200)

cuenta.depositar(500)

print(cuenta,'\n',cuenta2, '\n', cuenta3)