"""Proyecto etapa 1"""

import Funciones
import random

msj="""
------------------------------------------------
Bienvenido a SIGE.
(Sistema Interno de Gestión de Evaluaciones)

Este programa te permite:
- Cargar un curso
- Cargar alumnos con su legajo y nombre
- Asignar materias y notas
- Visualizar listado completo con promedios
- Consultar aprobados, desaprobados y aplazados
- Identificar la nota más alta y más baja
- Buscar alumnos por legajo
------------------------------------------------
"""

# Función principal
def main():
    mats_cargadas = ["Filosofía", "Sociología", "Historia", "Geografía", "Ciudadanía"]
    curso = Funciones.cargar_curso()
    legajos = []
    nombres = []
    apellidos = []
    materias = []
    notas = []
    seguir = 1
    while len(legajos) < 40 and seguir == 1:
        legajo = Funciones.pedir_legajo(legajos)
        if legajo == 99:
            seguir = 0
            print("Programa finalizado, Gracias por usar SIGE.")
        else:
            nombre = Funciones.pedir_nombre()
            materia = Funciones.materia_opcion(mats_cargadas)
            nota = Funciones.nota_random()
            print("Nota asignada:", nota)

            legajos.append(legajo)
            nombres.append(nombre)
            materias.append(materia)
            notas.append(nota)


print(msj)
if __name__ == "__main__":
    main()
