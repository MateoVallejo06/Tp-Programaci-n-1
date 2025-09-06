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

# Función principal
def main():
    materias_cargadas = ["Filosofía", "Sociología", "Historia", "Geografía", "Ciudadanía"]
    curso = Funciones.cargar_curso()
    legajos = []
    nombres = []
    notas = []
    alumnos = Funciones.cargar_alumnos()
    m = [[0]*7 for i in range(alumnos)]
    seguir = 1
    cont = 0

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

        cont += 1
    Funciones.matriz_completa(m,alumnos,7,curso,materias_cargadas)
    Funciones.mostrar_estadisticas_notas(notas)
    Funciones.alumnos_notas(nombres, notas, materias_cargadas, 10)
    Funciones.alumnos_notas(nombres, notas, materias_cargadas, 6)
    Funciones.mostrar_top_promedios(nombres, notas)
    Funciones.aprobados_aplazados_materias(nombres, notas, materias_cargadas)



print(msj)
if __name__ == "__main__":
    main()
    print("Programa finalizado, Gracias por usar SIGE.")
print(msj)
if __name__ == "__main__":
    main()

