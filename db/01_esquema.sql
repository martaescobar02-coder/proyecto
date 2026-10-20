

CREATE TABLE departamento (
    id_depto INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    gerente TEXT NOT NULL
);

CREATE TABLE empleado (
    id_empleado INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    direccion TEXT,
    telefono TEXT,
    correo TEXT,
    fecha_inicio_contrato TEXT,
    salario REAL,
    id_depto INTEGER,
    FOREIGN KEY (id_depto) REFERENCES departamento(id_depto)
);

CREATE TABLE proyecto (
    id_proyecto INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    fecha_inicio TEXT
);

CREATE TABLE registro_tiempo (
    id_registro INTEGER PRIMARY KEY,
    fecha TEXT NOT NULL,
    horas_trabajadas INTEGER NOT NULL,
    descripcion_tarea TEXT,
    id_empleado INTEGER,
    id_proyecto INTEGER,
    FOREIGN KEY (id_empleado) REFERENCES empleado(id_empleado),
    FOREIGN KEY (id_proyecto) REFERENCES proyecto(id_proyecto)
);
