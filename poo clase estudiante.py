class Estudiante:
    contador_id = 1
    def __init__(self, nombre: str, apellido: str, matricula: str, carrera: str):
        self.__nombre = nombre 
        self.__apellido = apellido
        self.__matricula = matricula
        self.carrera = carrera
        self.cursos_inscriptos = []  

        self.id = Estudiante.contador_id
        Estudiante.contador_id += 1

    def __str__(self):
        return f"ID: {self.id} - {self.__nombre} {self.__apellido} - Matricula: {self.__matricula} - Carrera: {self.carrera}"

    def get_nombre (self):
        return self.__nombre

    def get_apellido (self):
        return self.__apellido

    def get_matricula (self):
        return self.__matricula

    def set_nombre(self, nombre):
        self.__nombre=nombre

    def set_apellido(self, apellido):
        self.__apellido=apellido

    def set_matricula(self, matricula):
        self.__matricula=matricula

    def mostrar_estado(self):
        print(f"ID: {self.id}")
        print("Estudiante:", self.__nombre, self.__apellido)
        print("Matricula:", self.__matricula)
        print("Carrera:", self.carrera)
        print("Cursos inscriptos:")

        for curso in self.cursos_inscriptos:
            print("-", curso.nombre_curso)

class Curso:
    def __init__(self, nombre_curso: str, codigo: str, profesor: str, capacidad_max: int):
        self.nombre_curso = nombre_curso
        self.__codigo = codigo
        self.profesor = profesor
        self.capacidad_max = capacidad_max
        self.__cantidad_inscriptos = 0
        self.estudiantes_inscriptos = []

    def get_codigo(self):
        return self.__codigo

    def get_cantidad_inscriptos(self):
        return self.__cantidad_inscriptos

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_cantidad_inscriptos(self, cantidad_inscriptos):
        self.__cantidad_inscriptos = cantidad_inscriptos
    

    def inscribir_estudiante(self, estudiante):
        if estudiante in self.estudiantes_inscriptos:
            print("El estudiante ya esta inscripto en este curso.")
        elif len(self.estudiantes_inscriptos) < self.capacidad_max:
            self.estudiantes_inscriptos.append(estudiante)
            self.__cantidad_inscriptos += 1
            estudiante.cursos_inscriptos.append(self)
            print("Estudiante inscripto correctamente.")
        else:
            print("No hay cupos disponibles.")

    def dar_de_baja(self, estudiante):
        if estudiante in self.estudiantes_inscriptos:
            self.estudiantes_inscriptos.remove(estudiante)
            self.__cantidad_inscriptos -= 1
            estudiante.cursos_inscriptos.remove(self)
            print ("estudiante dado de baja correctamente")
        else:
            print ("el estudiante no esta inscripto en este curso")

    def mostrar_estado(self):
        cupos_disponibles = self.capacidad_max - self.__cantidad_inscriptos
        print("Curso:", self.nombre_curso)
        print("Estudiantes inscriptos:", self.__cantidad_inscriptos)
        print("Cupos disponibles:", cupos_disponibles)


class Facultad:
    def __init__(self):
        self.estudiantes = []
        self.cursos = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante) 
        print("Estudiante agregado correctamente.")

    def agregar_curso(self, curso):
        self.cursos.append(curso) 
        print("Curso agregado correctamente.") 

    def mostrar_estado_cursos(self):
        print("\n--- ESTADO DE TODOS LOS CURSOS ---") 
        for curso in self.cursos: 
            curso.mostrar_estado() 

    def mostrar_estado_estudiantes(self): 
        print("\n--- ESTADO DE TODOS LOS ESTUDIANTES ---") 
        for estudiante in self.estudiantes: 
            estudiante.mostrar_estado()

    

################### MENÚ
def menu():
    print("\n===== SISTEMA DE FACULTAD =====")
    print("1 - Agregar estudiante")
    print("2 - Agregar curso")
    print("3 - Inscribir estudiante en curso")
    print("4 - Dar de baja estudiante de curso")
    print("5 - Mostrar estado de cursos")
    print("6 - Mostrar estado de estudiantes")
    print("7 - Salir")

    return input("Seleccione una opcion: ")


def main():
    facultad = Facultad()

    while True:
        opcion = menu()

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            matricula = input("Ingrese la matricula: ")
            carrera = input("Ingrese la carrera: ")

            estudiante = Estudiante(nombre, apellido, matricula, carrera)
            facultad.agregar_estudiante(estudiante)

        elif opcion == "2":
            nombre_curso = input("Ingrese el nombre del curso: ")
            codigo = input("Ingrese el codigo del curso: ")
            profesor = input("Ingrese el profesor: ")
            capacidad = int(input("Ingrese la capacidad maxima: "))

            curso = Curso(nombre_curso, codigo, profesor, capacidad)
            facultad.agregar_curso(curso)

        elif opcion == "3":
            matricula = input("Ingrese la matricula del estudiante: ")

            codigo = input("Ingrese el codigo del curso: ")

            estudiante_encontrado = None
            curso_encontrado = None

            for estudiante in facultad.estudiantes:
                if estudiante.get_matricula() == matricula:
                    estudiante_encontrado = estudiante

            for curso in facultad.cursos:
                if curso.get_codigo() == codigo:
                    curso_encontrado = curso

            if estudiante_encontrado is None:
                print("Estudiante no encontrado.")

            elif curso_encontrado is None:
                print("Curso no encontrado.")

            else:
                curso_encontrado.inscribir_estudiante(estudiante_encontrado)

        elif opcion == "4":
            matricula = input("Ingrese la matricula del estudiante: ")

            codigo = input("Ingrese el codigo del curso: ")

            estudiante_encontrado = None
            curso_encontrado = None

            for estudiante in facultad.estudiantes:
                if estudiante.get_matricula() == matricula:
                    estudiante_encontrado = estudiante

            for curso in facultad.cursos:
                if curso.get_codigo() == codigo:
                    curso_encontrado = curso

            if estudiante_encontrado is None:
                print("Estudiante no encontrado.")

            elif curso_encontrado is None:
                print("Curso no encontrado.")

            else:
                curso_encontrado.dar_de_baja( estudiante_encontrado )

        elif opcion == "5":
            facultad.mostrar_estado_cursos()

        elif opcion == "6":
            facultad.mostrar_estado_estudiantes()

        elif opcion == "7":
            print("Programa terminado.")
            break

        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()
