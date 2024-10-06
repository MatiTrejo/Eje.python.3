class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def constructor(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def identificar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

persona1 = Persona("Trejo", 26)
persona1.identificar()
persona1.edad = 20
persona1.nombre= "Albarracin"
persona1.identificar()