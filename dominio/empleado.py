from dominio.persona import Persona

class Empleado(Persona):

    def __init__(
        self,
        id_empleado,
        rut,
        nombre,
        direccion,
        telefono,
        correo,
        fecha_inicio_contrato,
        salario
    ):

        super().__init__(rut, nombre)

        self.id_empleado = id_empleado
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fecha_inicio_contrato = fecha_inicio_contrato
        self.salario = salario

    def mostrar_salario(self):
        return self.salario