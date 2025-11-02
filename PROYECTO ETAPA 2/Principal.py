import archivos
import log
import reportes
import usuarios
import menu

def main():
    """Función principal del programa"""
    try:
        print("\n" + "="*60)
        print("SISTEMA DE GESTIÓN EDUCATIVA")
        print("="*60)
        
        usuarios.crear_archivo_usuarios()
        
        usuario_actual = usuarios.login()
        
        if usuario_actual:
            print(f"Bienvenido/a, {usuario_actual}!")

            menu.menu_principal(usuario_actual)
        else:
            print("Acceso denegado. Cerrando el sistema...")
    
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"\nError inesperado: {e}")
    finally:
        print("\n" + "="*60)
        print("¡Gracias por usar el sistema!")
        print("="*60)


if __name__ == "__main__":
    main()
