class Persona:
    def __init__(self, nombre="", edad=0):
        self.nombre = nombre
        self.edad = edad

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def identificar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    def mayor(self, otra_persona):
        if self.edad > otra_persona.edad:
            return f"La persona {self.nombre} es mayor que {otra_persona.nombre}."
        elif self.edad < otra_persona.edad:
            return f"La persona {self.nombre} es menor que {otra_persona.nombre}."
        else:
            return f"La persona {self.nombre} y {otra_persona.nombre} tienen la misma edad."



persona1 = Persona("Trejo", 26)
persona1.identificar()

persona2 = Persona()
nombre2 = input("Ingresa el nombre de la segunda persona: \n")
edad2 = int(input("Ingresa la edad de la segunda persona: \n"))
persona2.set_nombre(nombre2)
persona2.set_edad(edad2)

persona1.identificar()
print(persona1.mayor(persona2))
persona2.identificar()
