import os
from pathlib import Path
from datetime import datetime

def eliminar_archivos_antiguos_en_carpeta(ruta_carpeta):
    fecha_actual = datetime.now()
    archivos=os.listdir(ruta_carpeta)
    size=len(archivos)
    for archivo in archivos:
        size-=1
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        if os.path.isfile(ruta_archivo) and size>=5:
            fecha_creacion = datetime.fromtimestamp(os.path.getctime(ruta_archivo))
            tiempo_transcurrido = fecha_actual - fecha_creacion

            if tiempo_transcurrido.days >= 15:
                try:
                    os.remove(ruta_archivo)
                    print(f"Archivo '{archivo}' eliminado exitosamente.")
                except FileNotFoundError:
                    print(f"El archivo '{archivo}' no existe.")
            else:
                print(f"El archivo '{archivo}' no cumple el criterio de eliminación.")

# Ejemplo de uso
ruta_carpeta = Path.home() / "Documents/DBD"
eliminar_archivos_antiguos_en_carpeta(ruta_carpeta)
