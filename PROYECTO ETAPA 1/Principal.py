"""Proyecto etapa 1"""

import FuncionesSige


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
    curso = FuncionesSige.cargar_curso()
    legajos = []
    nombres = []
    apellidos = []
    materias = []
    notas = []
    seguir = 1
    while len(legajos) < 40 and seguir == 1:
        legajo = FuncionesSige.pedir_legajo(legajos)
        if legajo == 99:
            seguir = 0
            print("Programa finalizado, Gracias por usar SIGE.")
        else:
            nombre = FuncionesSige.pedir_nombre()
            materia = FuncionesSige.materia_opcion(0)
            nota = FuncionesSige.nota_random()
            print("Nota asignada:", nota)

            legajos.append(legajo)
            nombres.append(nombre)
            materias.append(materia)
            notas.append(nota)


print(msj)
if __name__ == "__main__":
    main()
