import os
import sys
import shutil


def crear_carpetas (sufijo, cantidad):
    """
    Crea N número de carpetas
    """
    for i in range(cantidad):
        os.mkdir(f"{sufijo}{i}")
        print(f"Creando carpeta {sufijo}{i}")


def borrar_carpeta(ruta):
    
    if os.path.isdir(ruta):

        os.rmdir(ruta)  # Borra carpeta vacia
    
    #else:
    #   raise ValueError("file {} is not a file or dir.".format(ruta))
