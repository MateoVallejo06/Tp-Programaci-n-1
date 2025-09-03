"""Funciones proyecto etapa 1"""

import random

def cargar_curso():
    texto = input("ingrese el nombre del curso: ")
    return texto


def pedir_numero():
    legajo = int(input("Número de legajo (>=1000, 99 para terminar): "))
    return legajo

#Comprueba que el legajo no exista
def existe_legajo(lista, legajo):
    for i in range(len(lista)):
        if lista[i] == legajo:
            return 1
    return 0


def pedir_legajo(lista):
    numero = pedir_numero()
    while (numero != 99 and numero < 1000) or existe_legajo(lista, numero) == 1:
        print("El numero de legajo no es válido o ya fue cargado. ")
        numero = pedir_numero()
    return numero


def pedir_nombre():
    nombre = input("Ingrese el nombre y apellido del alumno: ")
    return nombre


def materia_opcion(opcion):
    print("""Materias disponibles:
    1) Filosofía
    2) Sociología
    3) Historia
    4) Geografía
    5) Ciudadanía""")
    opcion=int(input("Ingrese el número de la materia (1-5): "))
    while opcion <1 or opcion >5:
        opcion=int(input("Opción no valida, Ingrese el número de la materia (1-5): "))
    if opcion == 1:
        return "Filosofía"
    if opcion == 2:
        return "Sociología"
    if opcion == 3:
        return "Historia"
    if opcion == 4:
        return "Geografía"
    return "Ciudadanía"

#La nota se asigna de forma aleatoria
def nota_random():
    return random.randint(1, 10)

# Función principal
def main():
    curso = cargar_curso()
    legajos = []
    nombres = []
    apellidos = []
    materias = []
    notas = []
    seguir = 1
    while len(legajos) < 40 and seguir == 1:
        legajo = pedir_legajo(legajos)
        if legajo == 99:
            seguir = 0
            print("Programa finalizado, Gracias por usar SIGE.")
        else:
            nombre = pedir_nombre()
            materia = materia_opcion(0)  # esta función pide y valida adentro
            nota = nota_random()
            print("Nota asignada:", nota)

            legajos.append(legajo)
            nombres.append(nombre)
            materias.append(materia)
            notas.append(nota)
