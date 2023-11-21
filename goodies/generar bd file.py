import sqlite3

#ESTO CREA LA BASE DE DATOS PERO ES MUY RUDIMENTARIO, DEBERÍA IMPLEMENTAR UN SOLO CODIGO
#QUE GENERE UNA NUEVA BASE DESDE 0 EN CASO DE QUE ESTA SE ELIMINE

def crear_basedatos_desde_sql(sql_file, db_file):
    # Leer el contenido del archivo SQL
    with open(sql_file, 'r') as file:
        sql_script = file.read()

    # Conectar a la base de datos
    conexion = sqlite3.connect(db_file)
    cursor = conexion.cursor()

    # Ejecutar el script SQL para crear las tablas y definir la estructura de la base de datos
    cursor.executescript(sql_script)

    # Confirmar los cambios en la base de datos
    conexion.commit()

    # Cerrar la conexión a la base de datos
    conexion.close()

# Ejemplo de uso
archivo_sql = 'FichaAlumnos.sql'
archivo_db = 'FichaAlumnos.db'
crear_basedatos_desde_sql(archivo_sql, archivo_db)