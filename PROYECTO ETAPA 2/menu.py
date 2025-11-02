import archivos
import Principal
import reportes
import usuarios
import log

def menu_principal(usuario):
    """Muestra el menú principal del sistema"""
    
    opciones = {
        "1": lambda: usuarios.alta_usuario(usuario),
        "2": lambda: usuarios.baja_usuario(usuario),
        "3": lambda: usuarios.modificar_contrasena(usuario),
        "4": lambda: archivos.cargar_materias(usuario),
        "5": lambda: archivos.cargar_notas(usuario),
        "6": lambda: archivos.cargar_asistencia(usuario),
        "7": lambda: reportes.generar_promedios_anuales(usuario),
        "8": lambda: reportes.generar_promedio_por_materia(usuario),
        "9": lambda: reportes.mostrar_notas_maxmin(usuario)
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
        except EOFError:
            print("\nError: entrada inesperada")
            continuar = False
        except KeyboardInterrupt:
            print("\n\nInterrupción detectada. Cerrando sesión...")
            continuar = False