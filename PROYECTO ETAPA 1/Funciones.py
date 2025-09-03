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
    nombre = input("Ingrese el nombre y apellido del alumno: ").title()
    return nombre


#Pide y valida la materia
def materia_opcion(lista):
    print("""Materias disponibles:
    1) Filosofía
    2) Sociología
    3) Historia
    4) Geografía
    5) Ciudadanía""")
    opcion=int(input("Ingrese el número de la materia (1-5): "))
    while opcion <1 or opcion >5:
        opcion=int(input("Opción no valida, Ingrese el número de la materia (1-5): "))
    return lista[opcion-1]

#La nota se asigna de forma aleatoria
def nota_random():
    return random.randint(1, 10)
