import os
import shutil
from datetime import datetime

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

ruta_archivo_original = os.path.join(directorio_actual, "FichaAlumnos.db")
nombre_carpeta = "Documents/DBD"
nombre_archivo_copia = cadena_hora + ".db"
ruta_carpeta_copia = os.path.join(os.path.expanduser("~"), nombre_carpeta)
ruta_archivo_copia = os.path.join(ruta_carpeta_copia, nombre_archivo_copia)

crear_copia_archivo(ruta_archivo_original, ruta_archivo_copia)
