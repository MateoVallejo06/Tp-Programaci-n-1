from log import registrar_log
from archivos import (
    ARCHIVO_NOTAS,
    ARCHIVO_MATERIAS,
    ARCHIVO_ESTUDIANTES
)

def contar_lineas_recursivo(f):
    """Cuenta cuántas líneas tiene un archivo usando recursividad."""
    linea = f.readline()
    if not linea:
        return 0
    return 1 + contar_lineas_recursivo(f)

def generar_promedios_anuales(usuario):
    """Calcula y guarda el promedio anual de cada alumno"""
    try:
        
        promedios_por_legajo = {}
        
        f = open(ARCHIVO_NOTAS, "r")
        f.readline()  
        linea = f.readline()
        while linea:
            partes = linea.strip().split(",")
            if len(partes) >= 6:
                legajo = partes[0]
                notas = [int(x) for x in partes[2:]]
                promedio = sum(notas) / len(notas)
                
                if legajo not in promedios_por_legajo:
                    promedios_por_legajo[legajo] = []
                promedios_por_legajo[legajo].append(promedio)
            linea = f.readline()
        f.close()
        
    
        fout = open(ARCHIVO_PROMEDIOS_ANUALES, "w")
        fout.write("legajo,nombre,apellido,año,division,promedio\n")
        
        fin = open(ARCHIVO_ESTUDIANTES, "r")
        fin.readline()  
        linea = fin.readline()
        while linea:
            legajo, nombre, apellido, año, division = linea.strip().split(",")
            
            if legajo in promedios_por_legajo:
                notas = promedios_por_legajo[legajo]
                prom_final = round(sum(notas) / len(notas), 2)
                fout.write(f"{legajo},{nombre},{apellido},{año},{division},{prom_final}\n")
                
                del promedios_por_legajo[legajo]
            
            linea = fin.readline()
        fin.close()
        with open(ARCHIVO_NOTAS, "r") as f:
            next(f)  # salteamos encabezado
            total = contar_lineas_recursivo(f)  
            print(f"Total de registros procesados: {total}")
        fout.close()

        print("Archivo 'promediosAnuales.csv' generado correctamente.")
        registrar_log(usuario, "Generó promedios anuales")

    except FileNotFoundError:
        print("Primero debe generar los archivos de entrada: ")
        print("Plan de estudios (opcion 4) - Cargar notas (opción 5)")
    except ValueError as e:
        print("Error de formato:", e)
    except IOError:
        print("Error de entrada/salida")


def generar_promedio_por_materia(usuario):
    """Calcula el promedio general de una materia"""
    resultado = None
    
    try:
        nombre_materia = None
        codigo = ""
        
        while nombre_materia is None:
            codigo = input("Código de materia: ").strip()
            
            f = open(ARCHIVO_MATERIAS, "r")
            f.readline()
            linea = f.readline()
            while linea:
                cod, nombre, año = linea.strip().split(",")
                if cod == codigo:
                    nombre_materia = nombre
                    break
                linea = f.readline()
            f.close()
            
            if nombre_materia is None:
                print("Código no encontrado. Intente nuevamente.")


        notas_materia = []
        f = open(ARCHIVO_NOTAS, "r")
        f.readline()
        linea = f.readline()
        while linea:
            partes = linea.strip().split(",")
            if partes[1] == codigo:
                notas = [int(x) for x in partes[2:]]
                prom = sum(notas) / len(notas)
                notas_materia.append(prom)
            linea = f.readline()
        f.close()

        if notas_materia:
            prom_general = round(sum(notas_materia) / len(notas_materia), 2)

            f = open(ARCHIVO_PROMEDIOS_MATERIA, "a")
            f.write(f"{codigo},{nombre_materia},{prom_general}\n")
            f.close()

            print(f"Promedio general de {nombre_materia}: {prom_general}")
            registrar_log(usuario, f"Promedio de materia {nombre_materia}")
            resultado = True
        else:
            print("No hay notas para esa materia.")
            resultado = False

    except FileNotFoundError:
        print("Debe generar primero los archivos de entrada: ")
        print("Plan de estudios (opción 4) - Cargar notas (Opción 5)")
        resultado = False
    except ValueError as e:
        print(f"Error de formato: {e}")
        resultado = False
    except IOError as e:
        print(f"Error de entrada/salida: {e}")
        resultado = False
    except KeyboardInterrupt:
        print("Operación cancelada por el usuario.")
        resultado = False
    
    return resultado
        
def mostrar_notas_maxmin():
    try:
        codigo = input("Código de materia: ").strip()
        f = open(ARCHIVO_NOTAS, "r")
        f.readline()
        notas_totales = []
        linea = f.readline()
        while linea:
            partes = linea.strip().split(",")
            if partes[1] == codigo:
                notas = [int(x) for x in partes[2:]]
                notas_totales.extend(notas)
            linea = f.readline()
        f.close()

        if notas_totales:
            print("Nota más baja:", min(notas_totales))
            print("Nota más alta:", max(notas_totales))
        else:
            print("No hay notas para esa materia.")
    except FileNotFoundError:
        print("Debe generar primero los archivos de entrada: ")
        print("Plan de estudios (opción 4) - Cargar notas (opción 5)")
        
        
ARCHIVO_PROMEDIOS_ANUALES = "promediosAnuales.csv"
ARCHIVO_PROMEDIOS_MATERIA = "promedioPorMateria.csv"
