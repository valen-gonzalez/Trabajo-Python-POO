from typing import List


class Miembro:
    def __init__(self, dni: str, nombre: str):
        self.setDni(dni)
        self.__nombre = nombre
        self.libros_prestados: List['Libro'] = []

    def agregarLibroPrestado(self, libro):
        self.libros_prestados.append(libro)

    def quitarLibroPrestado(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def getDni(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def setDni(self, dni):
        if dni.isdigit() and len(dni) >= 6:
            self.__dni = dni
        else:
            print("DNI invalido.")
            self.__dni = dni


class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, ejemplar: int):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ejemplar = ejemplar

        self.prestado_a: List[Miembro] = []

    def prestar_libro(self, miembro: Miembro):
        if self.estaDisponible():
            self.prestado_a.append(miembro)

    def estaDisponible(self):
        if len(self.prestado_a) < self.ejemplar:
            return True
        else:
            return False

    def devolver_libro(self, miembro: Miembro):
        if miembro in self.prestado_a:
            self.prestado_a.remove(miembro)


class Biblioteca:
    def __init__(self):
        self.libros: List[Libro] = []
        self.miembros: List[Miembro] = []

    def agregarLibro(self):
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el autor del libro: ")
        isbn = input("Ingrese el ISBN del libro: ")

        libro = self.getLibro(isbn)

        if libro:
            agregarejemplar = int(input("Cuantos ejemplares desea agregar: "))
            libro.ejemplar += agregarejemplar
        else:
            agregarejemplar = int(input("Cuantos ejemplares desea agregar: "))
            libro = Libro(titulo, autor, isbn, agregarejemplar)
            self.libros.append(libro)

    def getLibro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro

        return None

    def getMiembro(self, dni):
        for miembro in self.miembros:
            if miembro.getDni() == dni:
                return miembro

        return None

    def quitarLibro(self):
        isbn = input("Ingrese el ISBN del libro a borrar: ")
        libroaBorrar = self.getLibro(isbn)

        if libroaBorrar:
            self.libros.remove(libroaBorrar)
            print("Libro eliminado correctamente.")
        else:
            print("Libro no existe.")

    def quitarEjemplar(self):
        isbn = input("Ingrese el ISBN del libro: ")
        libroaquitarEjemplar = self.getLibro(isbn)

        if libroaquitarEjemplar:
            ejemplaresaquitar = int(
                input("Cuantos ejemplares desea quitar: ")
            )

            if ejemplaresaquitar < libroaquitarEjemplar.ejemplar:
                libroaquitarEjemplar.ejemplar -= ejemplaresaquitar
            else:
                print("No se pueden quitar todos los ejemplares.")
        else:
            print("Libro no existe.")

    def agregarMiembro(self):
        nombre = input("Ingrese el nombre del socio: ")
        dni = input("Ingrese el DNI del socio: ")

        miembroobj = Miembro(dni, nombre)
        self.miembros.append(miembroobj)

    def quitarMiembro(self):
        dni = input("Ingrese el DNI de la persona a borrar: ")
        personaaborrar = self.getMiembro(dni)

        if personaaborrar:
            self.miembros.remove(personaaborrar)
            print("Miembro eliminado correctamente.")
        else:
            print("Miembro no existe.")

    def prestar_libro(self):
        dni = input("Ingrese el DNI de la persona a prestar: ")
        isbn = input("Ingrese el ISBN del libro a prestar: ")

        libroaprestar = self.getLibro(isbn)

        if libroaprestar is None:
            print("Libro no existe.")
            return

        miembroaprestar = self.getMiembro(dni)

        if miembroaprestar is None:
            print("Miembro no existe.")
            return

        if libroaprestar.estaDisponible():
            libroaprestar.prestar_libro(miembroaprestar)
            miembroaprestar.agregarLibroPrestado(libroaprestar)
            print("Libro prestado exitosamente.")
        else:
            print("No hay ejemplares disponibles de este libro.")

    def devolver_libro(self):
        dni = input("Ingrese el DNI de la persona: ")
        isbn = input("Ingrese el ISBN del libro a devolver: ")

        libroaDevolver = self.getLibro(isbn)
        miembro = self.getMiembro(dni)

        if libroaDevolver is None:
            print("Libro no existe.")
            return

        if miembro is None:
            print("Miembro no existe.")
            return

        if miembro in libroaDevolver.prestado_a:
            libroaDevolver.devolver_libro(miembro)
            miembro.quitarLibroPrestado(libroaDevolver)
            print("Libro devuelto exitosamente.")
        else:
            print("Ese miembro no tiene prestado ese libro.")

    def mostrarLibros(self):
        if not self.libros:
            print("\nNo hay libros registrados en la biblioteca.")
            return

        print("\n--- Estado de Libros ---")

        for libro in self.libros:
            prestados_cant = len(libro.prestado_a)
            disponibles = libro.ejemplar - prestados_cant

            estado = (
                "Disponible"
                if libro.estaDisponible()
                else "No disponible (Todos prestados)"
            )

            print(
                f"Titulo: {libro.titulo} | "
                f"Autor: {libro.autor} | "
                f"ISBN: {libro.isbn}"
            )

            print(
                f"Ejemplares totales: {libro.ejemplar} | "
                f"Disponibles: {disponibles} | "
                f"Estado: {estado}"
            )

            if libro.prestado_a:
                nombres_prestados = [
                    m.getNombre() for m in libro.prestado_a
                ]

                print(
                    f"Prestado a: {', '.join(nombres_prestados)}"
                )

            print("-" * 40)

    def mostrarMiembros(self):
        if not self.miembros:
            print("\nNo hay miembros registrados.")
            return

        print("\n--- Lista de Miembros ---")

        for miembro in self.miembros:
            print(
                f"Nombre: {miembro.getNombre()} | "
                f"DNI/ID: {miembro.getDni()}"
            )

            print(
                f"Cantidad de libros en su poder: "
                f"{len(miembro.libros_prestados)}"
            )

            print("-" * 40)

    def mostrarLibrosMiembro(self):
        dni = input("Ingrese el DNI del miembro a consultar: ")
        miembro = self.getMiembro(dni)

        if miembro is None:
            print("Miembro no existe.")
            return

        print(
            f"\n--- Libros prestados a {miembro.getNombre()} "
            f"(DNI: {miembro.getDni()}) ---"
        )

        if not miembro.libros_prestados:
            print("Este miembro no tiene libros prestados.")
        else:
            for libro in miembro.libros_prestados:
                print(
                    f"- {libro.titulo} "
                    f"(ISBN: {libro.isbn})"
                )


def main():
    biblioteca_urquiza = Biblioteca()

    while True:
        opcion = menu()

        if opcion == "10":
            break

        elif opcion == "1":
            biblioteca_urquiza.agregarLibro()

        elif opcion == "2":
            biblioteca_urquiza.quitarLibro()

        elif opcion == "3":
            biblioteca_urquiza.agregarMiembro()

        elif opcion == "4":
            biblioteca_urquiza.quitarMiembro()

        elif opcion == "5":
            biblioteca_urquiza.prestar_libro()

        elif opcion == "6":
            biblioteca_urquiza.devolver_libro()

        elif opcion == "7":
            biblioteca_urquiza.mostrarLibros()

        elif opcion == "8":
            biblioteca_urquiza.mostrarMiembros()

        elif opcion == "9":
            biblioteca_urquiza.mostrarLibrosMiembro()

        else:
            print("Opcion invalida.")

    print("Programa Terminado")


def menu():
    print("\nSistema de Gestion de Biblioteca:")
    print("1- Agregar Libro")
    print("2- Quitar Libro")
    print("3- Agregar Miembro")
    print("4- Borrar Miembro")
    print("5- Prestar Libro")
    print("6- Devolver Libro")
    print("7- Mostrar Libros")
    print("8- Mostrar Miembros")
    print("9- Mostrar Libros Prestados a Miembro")
    print("10- Salir")

    return input("Seleccione una opcion: ")


if __name__ == "__main__":
    main()

