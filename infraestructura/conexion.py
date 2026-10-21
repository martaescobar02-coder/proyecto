import sqlite3

def obtener_conexion():
    try:
        conexion = sqlite3.connect("db/ecotech.db")
        return conexion

    except sqlite3.Error as e:
        print("Error de conexión:", e)
        return None