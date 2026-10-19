from dominio.persona import Persona

class Empleado(Persona):

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

        super().__init__(
            nombre,
            direccion,
            telefono,
            correo
        )

        self.id_empleado = id_empleado
        self.fecha_inicio_contrato = fecha_inicio_contrato
        self.salario = salario