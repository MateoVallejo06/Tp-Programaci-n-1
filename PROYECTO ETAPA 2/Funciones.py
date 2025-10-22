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
        print(f"❌ Error de escritura: {e}")
    
    return resultado

def generar_materias():
    """Genera archivo CSV con datos de materias"""
    resultado = False
    try:
        print("\n" + "="*50)
        print("GENERANDO ARCHIVO: materias.csv")
        print("="*50)
        
        materias_por_año = {
            1: ["Matemática I", "Lengua I", "Historia I", "Ciencias Naturales I", "Inglés I"],
            2: ["Matemática II", "Lengua II", "Historia II", "Física I", "Inglés II"],
            3: ["Matemática III", "Literatura I", "Geografía I", "Química I", "Inglés III"],
            4: ["Matemática IV", "Literatura II", "Geografía II", "Química II", "Biología I"],
            5: ["Análisis Matemático", "Filosofía", "Educación Cívica", "Biología II", "Inglés IV"]
        }
        
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
        print(f"❌ Error de escritura: {e}")
    
    return resultado

def generar_notas():
    """Genera archivo CSV con 4 notas aleatorias por alumno"""
    resultado = False
    estudiantes = []
    materias = []
    error_encontrado = False
    
    try:
        print("\n" + "="*50)
        print("GENERANDO ARCHIVO: notas.csv")
        print("="*50)
        
        f = open(ARCHIVO_ESTUDIANTES, 'r')
        encabezado = f.readline()  
        linea = f.readline()
        while linea:
            linea = linea.strip()
            if linea:
                partes = linea.split(',')
                if len(partes) >= 4:
                    estudiantes.append({
                        'legajo': partes[0],
                        'año': int(partes[3])
                    })
            linea = f.readline()
        f.close()
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ARCHIVO_ESTUDIANTES}'.")
        print("Debe generar primero el archivo de estudiantes.")
        error_encontrado = True
    except ValueError:
        print(f"Error: Formato inválido en el archivo de estudiantes")
        error_encontrado = True
    except IOError as e:
        print(f"❌ Error de entrada/salida: {e}")
        error_encontrado = True
    else:
        try:
            f = open(ARCHIVO_MATERIAS, 'r')
            encabezado = f.readline() 
            linea = f.readline()
            while linea:
                linea = linea.strip()
                if linea:
                    partes = linea.split(',')
                    if len(partes) >= 3:
                        materias.append({
                            'codigo': partes[0],
                            'año': int(partes[2])
                        })
                linea = f.readline()
            f.close()
            
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{ARCHIVO_MATERIAS}'.")
            print("Debe generar primero el archivo de materias.")
            error_encontrado = True
        except ValueError:
            print(f"❌ Error: Formato inválido en el archivo de materias")
            error_encontrado = True
        except IOError as e:
            print(f"❌ Error de entrada/salida: {e}")
            error_encontrado = True
        else:
            if not estudiantes:
                print("No hay estudiantes para generar notas.")
            elif not materias:
                print("No hay materias para generar notas.")
            else:
                try:
                    f = open(ARCHIVO_NOTAS, 'w')
                    f.write("legajo,codigo,nota1,nota2,nota3,nota4\n")
                    
                    contador = 0
                    for estudiante in estudiantes:
                        for materia in materias:
                            if materia['año'] == estudiante['año']:
                                nota1 = random.randint(1, 10)
                                nota2 = random.randint(1, 10)
                                nota3 = random.randint(1, 10)
                                nota4 = random.randint(1, 10)
                                
                                f.write(f"{estudiante['legajo']},{materia['codigo']},{nota1},{nota2},{nota3},{nota4}\n")
                                contador += 1
                    
                    f.close()
                    
                    print(f"Archivo '{ARCHIVO_NOTAS}' generado con {contador} registros (4 notas por alumno).")
                    resultado = True
                    
                except IOError as e:
                    print(f"❌ Error de entrada/salida: {e}")

    return resultado

def generar_archivos():
    """Genera los 3 archivos de entrada en secuencia"""
    print("\n" + "="*60)
    print("GENERACIÓN DE ARCHIVOS DE ENTRADA")
    print("="*60)
    
    if generar_estudiantes():
        if generar_materias():
            generar_notas()
        else:
            print("\nNo se pudo continuar con la generación de notas.")
    else:
        print("\nNo se pudieron generar los archivos.")

def menu_principal(usuario):
    """Muestra el menú principal del sistema"""
    continuar = True
    
    while continuar:
        try:
            print("\n" + "="*60)
            print(f"MENÚ PRINCIPAL - Usuario: {usuario}")
            print("="*60)
            print("1. Alta de usuario")
            print("2. Baja de usuario")
            print("3. Modificación de contraseña")
            print("4. Generar archivos de entrada")
            print("5. Generar archivo de estudiantes")
            print("6. Generar archivo de materias")
            print("7. Generar archivo de notas")
            print("0. Salir")
            print("="*60)
            
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == "1":
                alta_usuario()
            elif opcion == "2":
                baja_usuario()
            elif opcion == "3":
                modificar_contrasena()
            elif opcion == "4":
                generar_archivos()
            elif opcion == "5":
                generar_estudiantes()
            elif opcion == "6":
                generar_materias()
            elif opcion == "7":
                generar_notas()
            elif opcion == "0":
                print("\nCerrando sesión...")
                continuar = False
            else:
                print("Opción inválida. Intente nuevamente.")
                
        except ValueError as e:
            print(f"❌ Error de valor: {e}")
        except KeyboardInterrupt:
            print("\n\nInterrupción detectada. Cerrando sesión...")
            continuar = False