from dominio.excepciones import EcoTechError

try:
    conexion = sqlite3.connect("db/ecotech.db")
    return conexion

except sqlite3.Error as e:
    raise EcoTechError(f"Error de conexión a la base de datos: {e}")