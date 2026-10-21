import sqlite3

conexion = sqlite3.connect("db/ecotech.db")

with open("db/01_esquema.sql", "r", encoding="utf-8") as archivo:
    sql = archivo.read()

conexion.executescript(sql)

conexion.commit()
conexion.close()

print("Tablas creadas correctamente")