class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def identificar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

persona1 = Persona("Trejo", 26)
persona1.identificar()

