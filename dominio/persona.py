from infraestructura.conexion import obtener_conexion, ErrorDeConexion

try:
    with obtener_conexion() as conn:
        conn.execute(
            "INSERT INTO persona (rut, nombre) VALUES (?, ?)",
            ("12345678-9", "Ana Rojas"),
        )
    print("✅ Registro insertado correctamente.")
except ErrorDeConexion as e:
    print(f"⚠️ No se pudo insertar: {e}")

# Ahora leemos lo que hay en la tabla
with obtener_conexion() as conn:
    filas = conn.execute("SELECT rut, nombre FROM persona").fetchall()
    for fila in filas:
        print(fila)

