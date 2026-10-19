from dominio.empleado import Empleado
from dominio.departamento import Departamento

def main():

    empleado1 = Empleado(
        1,
        "elena avalor",
        "San Pedro",
        "987654321",
        "elena@correo.cl",
        850000
    )

    departamento_ti = Departamento("Tecnología")

    departamento_ti.empleados.append(empleado1)

    print(f"Departamento: {departamento_ti.nombre}")
    print(f"Empleado: {empleado1.nombre}")

if __name__ == "__main__":
    main()