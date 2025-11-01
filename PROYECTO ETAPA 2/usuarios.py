ARCHIVO_USUARIOS = "usuarios.csv"

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
        print(f"Error al acceder al archivo: {e}")
    
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