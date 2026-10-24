from dominio.persona import Persona
from dominio.empleado import Empleado
from infraestructura.conexion import obtener_conexion


# Tupla -> Objeto
def fila_a_empleado(fila):
    return Empleado(
        fila[0],
        fila[1],
        fila[2],
        fila[3],
        fila[4],
        fila[5],
        fila[6],
        fila[7]
    )


# Crear objeto Empleado
empleado = Empleado(
    1,
    "12345678-9",
    "Ana Rojas",
    "Los Carrera 123",
    "987654321",
    "ana@correo.cl",
    "2024-03-01",
    950000
)

# Crear objeto Persona
persona = Persona(
    "11111111-1",
    "Juan Perez"
)

# Polimorfismo
objetos = [persona, empleado]

for obj in objetos:
    print(obj.mostrar_datos())

print(empleado.nombre)
print(empleado.mostrar_salario())


# Conexión
conexion = obtener_conexion()

if conexion:
    print("Conexión exitosa")

    cursor = conexion.cursor()

    # Validaciones
    nombre = empleado.nombre
    salario = empleado.salario

    if nombre == "":
        print("Error: nombre vacío")

    elif salario <= 0:
        print("Error: salario inválido")

    else:
        print("Datos válidos")

    try:

        # CREATE
        cursor.execute("""
        INSERT INTO empleado
        (nombre, direccion, telefono, correo,
        fecha_inicio_contrato, salario, id_depto)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            empleado.nombre,
            empleado.direccion,
            empleado.telefono,
            empleado.correo,
            empleado.fecha_inicio_contrato,
            empleado.salario,
            1
        ))

        conexion.commit()
        print("Empleado agregado")

        # READ
        cursor.execute("SELECT * FROM empleado")

        empleados = cursor.fetchall()

        for emp in empleados:
            print(emp)

        # UPDATE
        cursor.execute("""
        UPDATE empleado
        SET salario = ?
        WHERE id_empleado = ?
        """,
        (1000000, 1))

        conexion.commit()
        print("Empleado actualizado")

        # DELETE
        cursor.execute("""
        DELETE FROM empleado
        WHERE id_empleado = ?
        """,
        (1,))

        conexion.commit()
        print("Empleado eliminado")

    except Exception as e:
        conexion.rollback()
        print("Error durante la transacción:", e)

    finally:
        conexion.close()
        print("Conexión cerrada")