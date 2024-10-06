class Cliente:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0

    def depositar(self, monto):
        self.cantidad += monto
        print(f"{self.nombre} ha depositado {monto}. Saldo actual: {self.cantidad}\n")

    def extraer(self, monto):
        if monto > self.cantidad:
            print(f"{self.nombre} no tiene suficiente saldo para extraer {monto}. Saldo actual: {self.cantidad}\n")
        else:
            self.cantidad -= monto
            print(f"{self.nombre} ha extraído {monto}. Saldo actual: {self.cantidad}\n")

    def mostrar_total(self):
        print(f"Cliente: {self.nombre}, Saldo total: {self.cantidad}\n")
        return self.cantidad

class Banco:
    def __init__(self):
        self.clientes = [Cliente("Pedro"), Cliente("Juan"), Cliente("Carlos")]

    def operar(self):
        print("\n--- Operaciones del banco ---\n")
        self.clientes[0].depositar(10000)
        self.clientes[1].depositar(5000)
        self.clientes[2].depositar(20000)

        self.clientes[0].extraer(3000)
        self.clientes[1].extraer(7000)
        self.clientes[2].extraer(10000)

    def deposito_total(self):
        total = sum(cliente.mostrar_total() for cliente in self.clientes)
        print(f"\nTotal depositado en el banco: {total}\n")

banco = Banco()
banco.operar()
banco.deposito_total()