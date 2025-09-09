"""Funciones proyecto etapa 1"""

import random

def cargar_curso():
    texto = input("ingrese el nombre del curso o Finalizar para salir: ").title() 
    return texto


def cargar_alumnos():
    cantidad = int(input("Ingrese la cantidad de alumnos a cargar: "))
    while cantidad < 1:
        print("Cantidad no válida. Intente nuevamente.")
        cantidad = int(input("Ingrese la cantidad de alumnos a cargar: "))
    return cantidad


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


# Devuelve una lista con notas aleatorias por cada materia, mostrando resultados
def materia_notas(lista_materias):
    lista_notas = []
    print("\nNotas asignadas:")
    for i in range(len(lista_materias)):
        nota = random.randint(1, 10)
        lista_notas.append(nota)
        print(f"{lista_materias[i]}: {nota}")
    return lista_notas

#Matriz y promedios
def matriz_completa(mat,cf,cc,cur,materias):
    print(f"LISTADO DE NOTAS CUATRIMESTRALES - CURSO: {cur}")
    print("-"*100)                                 
    print(f"{'Legajo':<10}{'Nombre y Apellido':<25}{'Filosofía':<15}{'Sociología':<15}{'Historia':<15}{'Geografía':<15}{'Ciudadanía':<15}")
    not_por_mat = [0] * (cc - 2)
    for i in range(cf):
        print(f"{mat[i][0]:<10}", end="")
        print(f"{mat[i][1]:<25}", end="")
        for j in range(2, cc):
            nota = mat[i][j]
            not_por_mat[j-2] += nota
            print(f"{nota:<15}", end="")
        print("\n")
    print("-"*100)
    print(f"{'Promedios':<35}")
    for t in range(len(materias)):
        prom = not_por_mat[t]/cf
        print(f"{materias[t]}: {prom:.2f}", end="   ")
    print("\n")



# Muestra cantidad y porcentaje de aprobados, desaprobados y aplazados
def mostrar_estadisticas_notas(notas):
    total_notas = 0
    aprobados = 0
    desaprobados = 0
    aplazados = 0

    for i in notas:
        for nota in i:
            total_notas += 1
            if nota >= 7:
                aprobados += 1
            elif 5 <= nota <= 6:
                desaprobados += 1
            else:
                aplazados += 1

    print("\n--- Estadísticas de las Notas ---")
    print(f"Aprobados (7 o más): {aprobados} ({aprobados / total_notas:.2%})")
    print(f"Desaprobados (5-6): {desaprobados} ({desaprobados / total_notas:.2%})")
    print(f"Aplazados (<=4): {aplazados} ({aplazados / total_notas:.2%})")


# Muestra alumnos con 10 y con 6
def alumnos_notas(nombres, notas, materias, valor_buscado):
    print(f"\nAlumnos con nota {valor_buscado}:")
    for i in range(len(notas)):
        materias_nota = []
        for j in range(len(notas[i])):
            if notas[i][j] == valor_buscado:
                materias_nota.append(materias[j])
        if len(materias_nota) > 0:
            print(nombres[i])
            for materia in materias_nota:
                print(" ->", materia)


# Top 3 alumnos con notas más altas y más bajas
def mostrar_top_promedios(nombres, notas, n=3):
    promedios = []
    for i in range(len(nombres)):
        promedio = sum(notas[i]) / len(notas[i])   
        promedios.append((promedio, nombres[i]))

    # se ordena de mayor a menor
    promedios.sort(key=lambda x: x[0], reverse=True)

    # slicing para mejores y peores
    top_mejores = promedios[:n]           
    top_peores  = promedios[-n:][::-1]   

    print(f"\n--- Top {n} Mejores promedios (todas las materias) ---")
    for promedio, nombre in top_mejores:
        print(f"{nombre} -> Promedio: {promedio:.2f}")

    print(f"\n--- Top {n} Peores promedios (todas las materias) ---")
    for promedio, nombre in top_peores:
        print(f"{nombre} -> Promedio: {promedio:.2f}")


def buscar_indice_materia(materias, nombre_materia):
    for i in range(len(materias)):
        if materias[i] == nombre_materia:
            return i


# Muestra cantidad de aprobados en Sociología y aplazados en Historia
def aprobados_aplazados_materias(nombres, notas, materias):
    aprobados_sociologia = 0
    aplazados_historia = 0

    indice_sociologia = buscar_indice_materia(materias, "Sociología")
    indice_historia = buscar_indice_materia(materias, "Historia")

    for i in range(len(notas)):
        if notas[i][indice_sociologia] >= 7:
            aprobados_sociologia += 1
        if notas[i][indice_historia] <= 4:
            aplazados_historia += 1

    print(f"\nAprobados en Sociología: {aprobados_sociologia}")
    print(f"Aplazados en Historia: {aplazados_historia}")
    
    
    # Función para listar alumnos que desaprobaron 3 materias
def listar_alumnos_desaprobados_3_materias(lista_nombres, lista_notas):
    print("\nAlumnos que desaprobaron 3 materias:")
    encontrados = False
    for i in range(len(lista_notas)):
        desaprobadas = sum(1 for nota in lista_notas[i] if nota < 7)
        if desaprobadas == 3:
            print(f"{lista_nombres[i]} - Materias desaprobadas: {desaprobadas}")
            encontrados = True
    if not encontrados:
        print("No hay alumnos que hayan desaprobado exactamente 3 materias.")
