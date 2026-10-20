class Empleado:
    def __init__(
        self,
        id_empleado,
        nombre,
        direccion,
        telefono,
        correo,
        fecha_inicio_contrato,
        salario
    ):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fecha_inicio_contrato = fecha_inicio_contrato
        self.salario = salario