#crear carpeta en una ruta dada
import os
from pathlib import Path

def crear_carpeta_si_no_existe(ruta_carpeta):
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
        print("Carpeta creada exitosamente.")
    else:
        print("La carpeta ya existe.")

# Ejemplo de uso
nombre_carpeta = Path.home() / "Documents/DBD"
ruta_carpeta = os.path.join(os.getcwd(), nombre_carpeta)

crear_carpeta_si_no_existe(ruta_carpeta)