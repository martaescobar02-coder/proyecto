class Persona:
    def __init__(self, rut, nombre):
        self.rut = rut
        self.nombre = nombre

    def mostrar_datos(self):
        return f"RUT: {self.rut} - Nombre: {self.nombre}"