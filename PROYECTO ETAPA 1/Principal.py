"""Proyecto etapa 1"""

import Funciones

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

# Función para listar alumnos que desaprobaron 3 materias
def listar_alumnos_desaprobados_3_materias(nombres, notas):
    print("\nAlumnos que desaprobaron 3 materias:")
    encontrados = False
    for i in range(len(notas)):
        desaprobadas = sum(1 for nota in notas[i] if nota < 7)
        if desaprobadas == 3:
            print(f"{nombres[i]} - Materias desaprobadas: {desaprobadas}")
            encontrados = True
    if not encontrados:
        print("No hay alumnos que hayan desaprobado exactamente 3 materias.")

# Función principal
def main(curso):
    materias_cargadas = ["Filosofía", "Sociología", "Historia", "Geografía", "Ciudadanía"]
    legajos = []
    nombres = []
    notas = []
    alumnos = Funciones.cargar_alumnos()
    m = [[0]*7 for i in range(alumnos)]
    seguir = 1


    while len(legajos) < alumnos and seguir == 1:
        legajo = Funciones.pedir_legajo(legajos)
        if legajo == 99:
            seguir = 0
        else:
            nombre = Funciones.pedir_nombre()
            notas_por_alumno = Funciones.materia_notas(materias_cargadas)
            m[len(legajos)] [0] = legajo
            m[len(legajos)] [1] = nombre
            for j in range (len((notas_por_alumno))):
                m[len(legajos)] [2+j] = notas_por_alumno[j]


            legajos.append(legajo)
            nombres.append(nombre)
            notas.append(notas_por_alumno)

        
    Funciones.matriz_completa(m,alumnos,7,curso,materias_cargadas)
    Funciones.mostrar_estadisticas_notas(notas)
    Funciones.alumnos_notas(nombres, notas, materias_cargadas, 10)
    Funciones.alumnos_notas(nombres, notas, materias_cargadas, 6)
    Funciones.mostrar_top_promedios(nombres, notas)
    Funciones.aprobados_aplazados_materias(nombres, notas, materias_cargadas)
    listar_alumnos_desaprobados_3_materias(nombres, notas)



print(msj)
if __name__ == "__main__":
    curso = Funciones.cargar_curso()
    while curso != "Finalizar":
        main(curso)
        curso = Funciones.cargar_curso()
    print("Programa finalizado, Gracias por usar SIGE.")

