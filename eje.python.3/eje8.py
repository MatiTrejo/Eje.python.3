class Calculadora:
    
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def sumar(self):
        return self.n1 + self.n2

    def restar(self):
        return self.n1 - self.n2

    def multiplicar(self):
        return self.n1 * self.n2

    def dividir(self):
        if self.n2 != 0:
            return self.n1 / self.n2
        else:
            return "Error: División por cero no permitida."


n1 = int(input("Ingrese el primer número: \n" ))
n2 = int(input("Ingrese el segundo número: \n"))

calculadora = Calculadora(n1, n2)

print(f"Suma: {calculadora.sumar()}")
print(f"Resta: {calculadora.restar()}")
print(f"Multiplicación: {calculadora.multiplicar()}")
print(f"División: {calculadora.dividir()}")
