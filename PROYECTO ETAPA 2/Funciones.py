import random
from faker import Faker


ARCHIVO_USUARIOS = "usuarios.txt"
ARCHIVO_ESTUDIANTES = "estudiantes.csv"
ARCHIVO_MATERIAS = "materias.csv"
ARCHIVO_NOTAS = "notas.csv"

def crear_archivo_usuarios():
    """Crea el archivo de usuarios si no existe con usuarios por defecto"""
    try:
        f = open(ARCHIVO_USUARIOS, 'r')
        f.close()
    except IOError:
        f = open(ARCHIVO_USUARIOS, 'w')
        f.write("profesor,pass123\n")
        f.write("secretario,admin456\n")
        f.close()
        print("Archivo de usuarios creado")

def login():
    """Maneja el proceso de login del usuario"""
    intentos = 3
    usuario_valido = None
    
    while intentos > 0 and usuario_valido is None:
        try:
            print("\n--- LOGIN ---")
            usuario = input("Usuario: ").strip()
            contrasena = input("Contraseña: ").strip()
            
            if validar_datos(usuario, contrasena) == True:
                usuario_valido = usuario
            else:
                intentos -= 1
                if intentos > 0:
                    print(f"Ingreso incorrecto. Te quedan {intentos} intento(s).")
                else:
                    print("Te quedaste sin intentos.")
                    
        except KeyboardInterrupt as e:
            print(f"Error durante el login: {e}")
            intentos -= 1
    
    return usuario_valido

def validar_datos(usuario, contraseña):
    """Valida las credenciales del usuario contra el archivo"""
    resultado = False
    try:
        f = open(ARCHIVO_USUARIOS, 'r')
        linea = f.readline()
        while linea and not resultado:
            linea = linea.strip()
            if linea:
                partes = linea.split(',')
                if len(partes) == 2:
                    usr, pwd = partes[0].strip(), partes[1].strip()
                    if usr == usuario and pwd == contraseña:
                        resultado = True
            linea = f.readline()
        f.close()
    except IOError:
        print(f"Error: No se encontró el archivo {ARCHIVO_USUARIOS}")
        resultado = False
    return resultado

def listar_usuarios():
    """Lista todos los usuarios registrados (sin contraseñas)"""
    usuarios = []
    try:
        f = open(ARCHIVO_USUARIOS, 'r')
        linea = f.readline()
        while linea:
            linea = linea.strip()
            if linea:
                partes = linea.split(',')
                if len(partes) >= 1:
                    usuarios.append(partes[0].strip())
            linea = f.readline()
        f.close()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ARCHIVO_USUARIOS}")
    except IOError as e:
        print(f"Error de lectura: {e}")
    
    return usuarios


def alta_usuario():
    """Registra un nuevo usuario en el sistema"""
    resultado = False
    try:
        print("\n" + "="*50)
        print("ALTA DE USUARIO")
        print("="*50)
        
        nuevo_usuario = input("Nuevo usuario: ").strip()
        
        if nuevo_usuario in listar_usuarios():
            print("El usuario ya existe.")
        elif not nuevo_usuario:
            print("El nombre de usuario no puede estar vacío.")
        else:
            nueva_contrasena = input("Contraseña: ").strip()
            
            if not nueva_contrasena:
                print("La contraseña no puede estar vacía.")
            else:
                f = open(ARCHIVO_USUARIOS, 'a')
                f.write(f"{nuevo_usuario},{nueva_contrasena}\n")
                f.close()
                print(f"Usuario '{nuevo_usuario}' registrado.")
                resultado = True
        
    except IOError as e:
        print(f"❌ Error al acceder al archivo: {e}")
    
    return resultado

def baja_usuario():
    """Elimina un usuario del sistema"""
    resultado = False
    try:
        print("\n" + "="*50)
        print("BAJA DE USUARIO")
        print("="*50)
        
        usuarios_actuales = listar_usuarios()
        
        if not usuarios_actuales:
            print("No hay usuarios en el sistema.")
        else:
            print("\nUsuarios disponibles:")
            for usuario in usuarios_actuales:
                print(f"  - {usuario}")
            
            usuario_eliminar = input("\nUsuario a eliminar: ").strip()
            
            if usuario_eliminar not in usuarios_actuales:
                print("El usuario no existe.")
            else:

                f_lectura = open(ARCHIVO_USUARIOS, 'rt')
                lineas_filtradas = []
                
                linea = f_lectura.readline()
                while linea:
                    partes = linea.split(',')
                    if len(partes) > 0:
                        usuario_linea = partes[0]
                        if usuario_linea != usuario_eliminar:
                            lineas_filtradas.append(linea)
                    else:
                        lineas_filtradas.append(linea)
                    
                    linea = f_lectura.readline()
                
                f_lectura.close()
                
                f_escritura = open(ARCHIVO_USUARIOS, 'w')
                for linea in lineas_filtradas:
                    f_escritura.write(linea)
                
                f_escritura.close()
                
                print(f"Usuario '{usuario_eliminar}' eliminado exitosamente.")
                resultado = True
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo necesario")
    except IOError as e:
        print(f"Error al modificar archivo: {e}")
    
    return resultado

def modificar_contrasena():
    """Modifica la contraseña de un usuario existente"""
    resultado = False
    try:
        print("\n" + "="*50)
        print("MODIFICACIÓN DE CONTRASEÑA")
        print("="*50)
        
        usuarios_actuales = listar_usuarios()
        
        if not usuarios_actuales:
            print("No hay usuarios en el sistema.")
        else:
            print("\nUsuarios disponibles:")
            for usuario in usuarios_actuales:
                print(f"  - {usuario}")
            
            usuario_modificar = input("\nUsuario: ").strip()
            
            if usuario_modificar not in usuarios_actuales:
                print("El usuario no existe.")
            else:
                contrasena_actual = input("Contraseña actual: ").strip()
                
                if not validar_datos(usuario_modificar, contrasena_actual):
                    print("Contraseña actual incorrecta.")
                else:
                    nueva_contrasena = input("Nueva contraseña: ").strip()
                    
                    if not nueva_contrasena:
                        print("La contraseña no puede estar vacía.")
                    else:
                        f_lectura = open(ARCHIVO_USUARIOS, 'r')
                        lineas_modificadas = []
                        
                        linea = f_lectura.readline()
                        while linea:
                            partes = linea.split(',')
                            if len(partes) > 0:
                                usuario_linea = partes[0]
                                if usuario_linea == usuario_modificar:
                                    lineas_modificadas.append(f"{usuario_modificar},{nueva_contrasena}\n")
                                else:
                                    lineas_modificadas.append(linea)
                            else:
                                lineas_modificadas.append(linea)
                            
                            linea = f_lectura.readline()
                        
                        f_lectura.close()
                        
                        f_escritura = open(ARCHIVO_USUARIOS, 'w')
                        for linea in lineas_modificadas:
                            f_escritura.write(linea)
                        
                        f_escritura.close()
                        
                        print(f"Contraseña de '{usuario_modificar}' modificada exitosamente.")
                        resultado = True
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo necesario")
    except IOError as e:
        print(f"Error de entrada/salida: {e}")

    return resultado

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
                        continuar_año == False
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

def menu_principal(usuario):
    """Muestra el menú principal del sistema"""
    
    opciones = {
        "1": alta_usuario,
        "2": baja_usuario,
        "3": modificar_contrasena,
        "4": cargar_materias,
        "5": cargar_notas,
        "6": lambda: cargar_asistencia(usuario),
        "7": lambda: generar_promedios_anuales(usuario),
        "8": lambda: generar_promedio_por_materia(usuario),
        "9": mostrar_notas_maxmin
    }
    
    continuar = True
    
    while continuar:
        try:
            print("\n" + "="*60)
            print(f"MENÚ PRINCIPAL - Usuario: {usuario}")
            print("="*60)
            print("1. Alta de usuario")
            print("2. Baja de usuario")
            print("3. Modificación de contraseña")
            print("4. Cargar plan de estudios")
            print("5. Cargar notas")
            print("6. Cargar asistencia")
            print("7. Generar promedios anuales por alumno")
            print("8. Generar promedios anuales por materia")
            print("9. Mostrar nota más baja y más alta por materia")
            print("0. Salir")
            print("="*60)
            
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == "0":
                print("\nCerrando sesión...")
                continuar = False
            elif opcion in opciones:
                opciones[opcion]()
            else:
                print("Opción inválida. Intente nuevamente.")
                
        except ValueError as e:
            print(f"Error de valor: {e}")
        except KeyboardInterrupt:
            print("Interrupción detectada. Cerrando sesión...")
            continuar = False
            
ARCHIVO_ASISTENCIA = "asistenciaPorMateria.csv"
ARCHIVO_PROMEDIOS_ANUALES = "promediosAnuales.csv"
ARCHIVO_PROMEDIOS_MATERIA = "promedioPorMateria.csv"
ARCHIVO_LOG = "log.txt"


def registrar_log(usuario, accion):
    """Agrega una línea al log"""
    try:
        linea = f"Usuario: {usuario} - Acción: {accion}\n"
        f = open(ARCHIVO_LOG, "a")
        f.write(linea)
        f.close()
    except:
        print("Error al escribir en el log.")


def cargar_asistencia(usuario):
    """Permite registrar o modificar asistencia"""
    ejecutado = False
    
    try:
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
            codigo = input("Código de materia: ").strip()
            legajo = input("Legajo del alumno: ").strip()
            porcentaje = input("Porcentaje de asistencia (0-100): ").strip()

            if not porcentaje.replace(".", "", 1).isdigit():
                print("Debe ingresar un número válido.")
            else:
                porcentaje = float(porcentaje)
                if porcentaje < 0 or porcentaje > 100:
                    print("Debe estar entre 0 y 100.")
                else:
                    registros = []
                    actualizado = False
                    try:
                        f = open(ARCHIVO_ASISTENCIA, "r")
                        linea = f.readline()
                        while linea:
                            partes = linea.strip().split(",")
                            if len(partes) == 3:
                                if partes[0] == codigo and partes[1] == legajo:
                                    partes[2] = str(porcentaje)
                                    actualizado = True
                                registros.append(",".join(partes))
                            linea = f.readline()
                        f.close()
                    except FileNotFoundError:
                        pass

                    if not actualizado:
                        registros.append(f"{codigo},{legajo},{porcentaje}")

                    f = open(ARCHIVO_ASISTENCIA, "w")
                    for r in registros:
                        f.write(r + "\n")
                    f.close()

                    print("Asistencia registrada correctamente.")
                    registrar_log(usuario, f"Asistencia materia {codigo}, legajo {legajo}")
                    ejecutado = True

    except IOError as e:
        print(f"Error de entrada/salida: {e}")
    except KeyboardInterrupt:
        print("Operación cancelada.")



def generar_promedios_anuales(usuario):
    """Calcula y guarda el promedio anual de cada alumno"""
    try:
        estudiantes = {}
        f = open(ARCHIVO_ESTUDIANTES, "r")
        f.readline()
        linea = f.readline()
        while linea:
            legajo, nombre, apellido, año, division = linea.strip().split(",")
            estudiantes[legajo] = {"nombre": nombre, "apellido": apellido,
                                   "año": año, "division": division, "notas": []}
            linea = f.readline()
        f.close()

        f = open(ARCHIVO_NOTAS, "r")
        f.readline()
        linea = f.readline()
        while linea:
            partes = linea.strip().split(",")
            if len(partes) >= 6:
                legajo = partes[0]
                notas = [int(x) for x in partes[2:]]
                promedio = sum(notas) / len(notas)
                if legajo in estudiantes:
                    estudiantes[legajo]["notas"].append(promedio)
            linea = f.readline()
        f.close()

        f = open(ARCHIVO_PROMEDIOS_ANUALES, "w")
        f.write("legajo,nombre,apellido,año,division,promedio\n")
        for legajo, datos in estudiantes.items():
            if datos["notas"]:
                prom_final = round(sum(datos["notas"]) / len(datos["notas"]), 2)
                f.write(f"{legajo},{datos['nombre']},{datos['apellido']},{datos['año']},{datos['division']},{prom_final}\n")
        f.close()

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
