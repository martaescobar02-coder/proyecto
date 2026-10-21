class Departamento:

    def __init__(self, id_depto, nombre, gerente):
        self.id_depto = id_depto
        self.nombre = nombre
        self.gerente = gerente
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def cantidad_empleados(self):
        return len(self.empleados)
        