from dominio.persona import Persona
from dominio.empleado import Empleado
from infraestructura.conexion import obtener_conexion
#tupla > objeto
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


# Crear objeto
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

persona = Persona(
    "11111111-1",
    "Juan Perez"
)
objetos = [persona, empleado]

for obj in objetos:
    print(obj.mostrar_datos())



print(empleado.nombre)
print(empleado.mostrar_salario())

# Conexión
conexion = obtener_conexion()

if conexion:
    print("Conexión exitosa")

    # Validaciones
    nombre = empleado.nombre
    salario = empleado.salario

    if nombre == "":
        print("Error: nombre vacío")

    elif salario <= 0:
        print("Error: salario inválido")

    else:
        print("Datos válidos")

        cursor = conexion.cursor()

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

        # Cerrar conexión
        conexion.close()
