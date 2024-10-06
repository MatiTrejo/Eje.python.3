# ESTE LO SAQUE DEL CHATGPT, PERDON PROFE jajaja

# Clase Triangulo
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    # Método para determinar y mostrar el lado mayor
    def lado_mayor(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado mayor es: {mayor}")

    # Método para determinar el tipo de triángulo
    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero.")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("El triángulo es isósceles.")
        else:
            print("El triángulo es escaleno.")

# Función para ingresar datos y crear el triángulo
def ingresar_datos():
    lado1 = float(input("Ingrese el valor del lado 1: "))
    lado2 = float(input("Ingrese el valor del lado 2: "))
    lado3 = float(input("Ingrese el valor del lado 3: "))
    return Triangulo(lado1, lado2, lado3)

# Crear una instancia de Triangulo e imprimir resultados
triangulo = ingresar_datos()
triangulo.lado_mayor()
triangulo.tipo_triangulo()