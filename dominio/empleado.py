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

        # Encapsulamiento
        self.salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor):
        if valor <= 0:
            raise ValueError("El salario debe ser mayor a 0")
        self.__salario = valor

    def mostrar_salario(self):
        return self.salario

    def mostrar_datos(self):
        return f"Empleado: {self.nombre} - Salario: {self.salario}"