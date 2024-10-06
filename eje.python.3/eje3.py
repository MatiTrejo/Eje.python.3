class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def identificar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    def mayor(self):
        if self.edad >= 18:
            return f"La persona {self.nombre} es mayor de edad."
        else:
            return f"La persona {self.nombre} es menor de edad."


persona1 = Persona("Trejo", 26)
persona1.identificar()
print(persona1.mayor())

persona2 = Persona("Albarracín", 16)
persona2.identificar()
print(persona2.mayor())
