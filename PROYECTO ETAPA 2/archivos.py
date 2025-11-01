from faker import Faker 
import random 
from log import registrar_log

def generar_estudiantes():
    """Genera archivo CSV con datos aleatorios de estudiantes"""
    resultado = False
    try:
        print("\n" + "="*50)
        print("GENERANDO ARCHIVO: estudiantes.csv")
        print("="*50)
        
        cantidad = 0
        while cantidad < 10 or cantidad > 100:
            try:
                cantidad = int(input("Cantidad de estudiantes a generar (10-100): "))
                if cantidad < 10 or cantidad > 100:
                    print("Debe ser un número entre 10 y 100.")
            except ValueError:
                print("Debe ingresar un número válido.")

        fake = Faker('es_ES')
        
        años = [1, 2, 3, 4, 5]
        divisiones = ["A", "B", "C"]
        
        f = open(ARCHIVO_ESTUDIANTES, 'w')
        f.write("legajo,nombre,apellido,año,division\n")
        
        for i in range(1, cantidad + 1):
            legajo = 1000 + i
            nombre = fake.first_name()
            apellido = fake.last_name()
            
            año = años[random.randint(0, len(años) - 1)]
            division = divisiones[random.randint(0, len(divisiones) - 1)]
            
            f.write(f"{legajo},{nombre},{apellido},{año},{division}\n")
        
        f.close()
        
        print(f"Archivo '{ARCHIVO_ESTUDIANTES}' generado con {cantidad} estudiantes.")
        resultado = True
        
    except IOError as e:
        print(f"Error de escritura: {e}")
    
    return resultado

def cargar_materias():
    """Genera archivo CSV con datos de materias ingresadas"""
    resultado = False
    try:
        print("\n" + "="*50)
        print("GENERANDO ARCHIVO: materias.csv")
        print("="*50)
        
        print("Generando archivo de estudiantes")
        estudiantes_generados = generar_estudiantes()
          
        if estudiantes_generados:
            print("Ingrese las materias para cada año (ingresar 1 por línea o deje vacío para terminar el año)")

        materias_por_año = {}

        for año in range(1,6):
            print(f"--AÑO  {año} --")
            materias = []
            continuar_año = True
            while continuar_año:
                materia = input(f"Materia {len(materias)+1} (o Enter para terminar el año {año}): ").strip()
        
                if materia == "":
                    if len(materias) == 0:
                        print("Debe ingresar al menos una materia por año.")
                    else:
                        continuar_año = False
                else:
                    materias.append(materia)
                    print(f"Agregada: {materia}")
            
            materias_por_año[año] = materias
            print(f"Total de materias para año {año}: {len(materias)}")


        f = open(ARCHIVO_MATERIAS, 'w')
        f.write("codigo,nombre,año\n")
        
        codigo = 100
        total_materias = 0
        for año in materias_por_año:
            materias = materias_por_año[año]
            for materia in materias:
                f.write(f"{codigo},{materia},{año}\n")
                codigo += 1
                total_materias += 1
        
        f.close()
        
        print(f"Archivo '{ARCHIVO_MATERIAS}' generado con {total_materias} materias.")
        resultado = True
        
    except IOError as e:
        print(f"Error de escritura: {e}")
    
    return resultado

def cargar_notas():
    """Genera archivo CSV con 4 notas ingresadas manualmente por alumno y materia"""
    resultado = False
    
    try:
        print("\n" + "="*50)
        print("GENERANDO ARCHIVO: notas.csv")
        print("="*50)
        
        f_notas = open(ARCHIVO_NOTAS, 'w')
        f_notas.write("legajo,codigo,nota1,nota2,nota3,nota4\n")
        f_notas.close()
        
        continuar = True
        contador = 0
        
        while continuar:
            print("\n" + "-"*50)
            
            legajo_valido = None
            año_alumno = None
            
            while legajo_valido is None:
                legajo = input("Ingrese legajo del estudiante (o '0' para terminar): ").strip()
                
                if legajo == "0":
                    continuar = False
                    break
                
                f = open(ARCHIVO_ESTUDIANTES, 'r')
                f.readline() 
                linea = f.readline()
                encontrado = False
                
                while linea and not encontrado:
                    partes = linea.strip().split(',')
                    if len(partes) >= 4 and partes[0] == legajo:
                        legajo_valido = legajo
                        año_alumno = int(partes[3])
                        encontrado = True
                    linea = f.readline()
                f.close()
                
                if legajo_valido is None and legajo != "0":
                    print(f"Legajo '{legajo}' no encontrado. Intente nuevamente.")
            
            if not continuar:
                break
            
            codigo_valido = None
            nombre_materia = None
            
            while codigo_valido is None:
                codigo = input(f"Ingrese código de materia para legajo {legajo_valido}: ").strip()
                
                f = open(ARCHIVO_MATERIAS, 'r')
                f.readline() 
                linea = f.readline()
                encontrado = False
                
                while linea and not encontrado:
                    partes = linea.strip().split(',')
                    if len(partes) >= 3 and partes[0] == codigo:
                        año_materia = int(partes[2])
                        
                        if año_materia == año_alumno:
                            codigo_valido = codigo
                            nombre_materia = partes[1]
                            encontrado = True
                        else:
                            print(f"La materia '{partes[1]}' es de año {año_materia}, pero el alumno está en año {año_alumno}.")
                            break
                    linea = f.readline()
                f.close()
                
                if codigo_valido is None:
                    if not encontrado:
                        print(f"Código '{codigo}' no encontrado. Intente nuevamente.")
            
            print(f"\nIngrese las 4 notas para {nombre_materia} (legajo {legajo_valido}):")
            notas = []
            
            for i in range(1, 5):
                nota_valida = False
                while not nota_valida:
                    try:
                        nota = int(input(f"  Nota {i} (1-10): "))
                        if 1 <= nota <= 10:
                            notas.append(nota)
                            nota_valida = True
                        else:
                            print("Error, la nota debe estar entre 1 y 10.")
                    except ValueError:
                        print("Error, Debe ingresar un número válido.")
            
            f_notas = open(ARCHIVO_NOTAS, 'a')
            f_notas.write(f"{legajo_valido},{codigo_valido},{notas[0]},{notas[1]},{notas[2]},{notas[3]}\n")
            f_notas.close()
            
            contador += 1
            print(f"Notas guardadas correctamente. Total de registros: {contador}")
        
        if contador > 0:
            print(f"Archivo '{ARCHIVO_NOTAS}' generado con {contador} registros.")
            resultado = True
        else:
            print("No se ingresaron notas.")
        
    except FileNotFoundError as e:
        print(f"Error: No se encontró un archivo necesario.")
        print("Debe generar primero los archivos de estudiantes y materias.")
    except ValueError as e:
        print(f"Error de formato: {e}")
    except IOError as e:
        print(f"Error de entrada/salida: {e}")
    except KeyboardInterrupt:
        print("Operación cancelada por el usuario.")
    
    return resultado

def cargar_asistencia(usuario):
    """Permite registrar o modificar asistencia"""
    
    try:
        # Validar que existan los archivos necesarios
        try:
            f_test = open(ARCHIVO_MATERIAS, "r")
            f_test.close()
            f_test = open(ARCHIVO_ESTUDIANTES, "r")
            f_test.close()
            archivos_existen = True
        except FileNotFoundError:
            print("Debe generar primero el plan de estudios (opción 4).")
            archivos_existen = False
        
        if archivos_existen:
            continuar = True
            contador = 0
            
            while continuar:
                print("\n" + "-"*50)
                
                codigo_valido = None
                while codigo_valido is None:
                    codigo = input("Código de materia (o '0' para salir): ").strip()
                    
                    if codigo == "0":
                        continuar = False
                        break
                    
                    f = open(ARCHIVO_MATERIAS, "r")
                    f.readline()  
                    linea = f.readline()
                    encontrado = False
                    
                    while linea and not encontrado:
                        partes = linea.strip().split(",")
                        if len(partes) >= 3 and partes[0] == codigo:
                            codigo_valido = codigo
                            encontrado = True
                        linea = f.readline()
                    f.close()
                    
                    if codigo_valido is None and codigo != "0":
                        print(f"Código de materia '{codigo}' no encontrado. Intente nuevamente.")
                
                if not continuar:
                    break
                
                legajo_valido = None
                while legajo_valido is None:
                    legajo = input("Legajo del alumno: ").strip()
                    
                    f = open(ARCHIVO_ESTUDIANTES, "r")
                    f.readline()  
                    linea = f.readline()
                    encontrado = False
                    
                    while linea and not encontrado:
                        partes = linea.strip().split(",")
                        if len(partes) >= 1 and partes[0] == legajo:
                            legajo_valido = legajo
                            encontrado = True
                        linea = f.readline()
                    f.close()
                    
                    if legajo_valido is None:
                        print(f"Legajo '{legajo}' no encontrado. Intente nuevamente.")
                
                porcentaje_valido = False
                while not porcentaje_valido:
                    porcentaje = input("Porcentaje de asistencia (0-100): ").strip()
                    
                    if not porcentaje.replace(".", "", 1).isdigit():
                        print("Debe ingresar un número válido.")
                    else:
                        porcentaje_float = float(porcentaje)
                        if porcentaje_float < 0 or porcentaje_float > 100:
                            print("Debe estar entre 0 y 100.")
                        else:
                            porcentaje_valido = True
                
                registros = []
                actualizado = False
                try:
                    f = open(ARCHIVO_ASISTENCIA, "r")
                    linea = f.readline()
                    while linea:
                        partes = linea.strip().split(",")
                        if len(partes) == 3:
                            if partes[0] == codigo_valido and partes[1] == legajo_valido:
                                partes[2] = porcentaje
                                actualizado = True
                            registros.append(",".join(partes))
                        linea = f.readline()
                    f.close()
                except FileNotFoundError:
                    pass
                
                if not actualizado:
                    registros.append(f"{codigo_valido},{legajo_valido},{porcentaje}")
                

                f = open(ARCHIVO_ASISTENCIA, "w")
                for r in registros:
                    f.write(r + "\n")
                f.close()
                
                contador += 1
                print(f"Asistencia registrada correctamente. Total de registros: {contador}")
                registrar_log(usuario, f"Asistencia materia {codigo_valido}, legajo {legajo_valido}")
            
            if contador > 0:
                print(f"Se registraron {contador} asistencias en total.")
            else:
                print("No se registraron asistencias.")

    except ValueError as e:
        print(f"Error de formato: {e}")
    except IOError as e:
        print(f"Error de entrada/salida: {e}")
    except KeyboardInterrupt:
        print("Operación cancelada.") 
        
ARCHIVO_ESTUDIANTES = "estudiantes.csv"
ARCHIVO_MATERIAS = "materias.csv"
ARCHIVO_NOTAS = "notas.csv"
ARCHIVO_ASISTENCIA = "asistenciaPorMateria.csv"