def registrar_log(usuario, accion):
    """Agrega una línea al log"""
    try:
        linea = f"Usuario: {usuario} - Acción: {accion}\n"
        f = open(ARCHIVO_LOG, "a")
        f.write(linea)
        f.close()
    except:
        print("Error al escribir en el log.")




ARCHIVO_LOG = "log.txt"