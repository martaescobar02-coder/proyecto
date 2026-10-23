class EcoTechError(Exception):
    """Excepción base para errores del sistema EcoTech."""
    pass


class RutDuplicadoError(EcoTechError):
    """Se lanza cuando se intenta registrar un empleado con un RUT existente."""
    pass


class SueldoInvalidoError(EcoTechError, ValueError):
    """Se lanza cuando el sueldo no cumple las restricciones laborales."""
    pass