o
from dominio.empleado import Empleado
from dominio.departamento import Departamento

def main():
    dep = Departamento("Operaciones")
    ana = Empleado("12345678-9", "Ana Rojas", "2024-03-01", 950_000)
    dep.agregar_empleado(ana)

    print(dep)
    print(ana)
    print(f"Horas registradas: {ana.total_horas()}")

if __name__ == "__main__":
    main()
