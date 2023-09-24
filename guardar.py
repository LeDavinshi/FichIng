import os
import shutil
from datetime import datetime
from pathlib import Path
import crearCarpeta

#guarda una copia de seguridad del archivo principal de la base de datos.

directorio_actual = os.getcwd()
print(directorio_actual)
fecha_actual = datetime.today()
cadena_hora = str(fecha_actual.strftime('%d %m %Y %H %M'))

def crear_copia_archivo(ruta_original, ruta_copia):
    try:
        with open(ruta_original, 'rb') as file_original:
            with open(ruta_copia, 'wb') as file_copia:
                shutil.copyfileobj(file_original, file_copia)
        print("Copia de archivo creada exitosamente.")
    except IsADirectoryError:
        print("La ruta especificada es un directorio.")

# Ejemplo de 
crearCarpeta
ruta_archivo_original = os.path.join(directorio_actual, "FichaAlumnos.db")
print(ruta_archivo_original)
nombre_carpeta = "Documents/DBD"
nombre_archivo_copia = cadena_hora + ".db"
ruta_carpeta_copia = Path.home() / nombre_carpeta
ruta_archivo_copia = ruta_carpeta_copia / nombre_archivo_copia
print (ruta_carpeta_copia)


crear_copia_archivo(ruta_archivo_original, str(ruta_archivo_copia))
