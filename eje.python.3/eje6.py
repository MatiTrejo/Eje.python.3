class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def estado(self):
        print(f"Estado del alumno {self.nombre}: Su nota es {self.nota} y esta ", end="")
        if self.nota <= 4:
            print("desaprobado.")
        elif self.nota > 4:
            print("aprobado.")

Alumno1 = Alumno("Juan", 9)
Alumno2 = Alumno("Pedro", 3)
Alumno1.estado()
Alumno2.estado()