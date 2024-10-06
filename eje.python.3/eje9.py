class Contacto:

    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self):
        nombre = input("Ingrese el nombre del contacto: \n")
        telefono = input("Ingrese el teléfono del contacto: \n")
        email = input("Ingrese el email del contacto: \n")
        contacto = Contacto(nombre, telefono, email)
        self.contactos.append(contacto)
        print(f"Contacto {nombre} añadido con éxito.")

    def listar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            for idx, contacto in enumerate(self.contactos, 1):
                print(f"{idx}. Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")

    def buscar_contacto(self):
        nombre = input("Ingrese el nombre del contacto a buscar: \n")
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print(f"Contacto encontrado - Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")
                return contacto
        print("Contacto no encontrado.")
        return None

    def editar_contacto(self):
        contacto = self.buscar_contacto()
        if contacto:
            print("Editando contacto...")
            contacto.nombre = input(f"Nuevo nombre (actual: {contacto.nombre}): \n") or contacto.nombre
            contacto.telefono = input(f"Nuevo teléfono (actual: {contacto.telefono}): \n") or contacto.telefono
            contacto.email = input(f"Nuevo email (actual: {contacto.email}): \n") or contacto.email
            print("Contacto actualizado con éxito.")

    def cerrar_agenda(self):
        print("Cerrando la agenda. ¡Hasta pronto!")
        exit()

    def mostrar_menu(self):
        while True:
            print("\n--- Menú de la Agenda ---")
            print("1. Añadir contacto")
            print("2. Listar contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            opcion = input("Seleccione una opción: \n")

            if opcion == '1':
                self.añadir_contacto()
            elif opcion == '2':
                self.listar_contactos()
            elif opcion == '3':
                self.buscar_contacto()
            elif opcion == '4':
                self.editar_contacto()
            elif opcion == '5':
                self.cerrar_agenda()
            else:
                print("Opción no válida. Intente de nuevo.")

agenda = Agenda()
agenda.mostrar_menu()
