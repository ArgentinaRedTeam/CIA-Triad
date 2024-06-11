# -*- coding: utf-8 -*-
"""
backup_script.py - Tu salvavidas digital, cortesía de Red Team Argentina.
Porque perder datos es más triste que un asado sin chimichurri. 🥹

Este script te permite hacer copias de seguridad de tus archivos importantes,
para que puedas dormir tranquilo sabiendo que tus recuerdos están a salvo.

Copyright (c) 2024 Red Team Argentina. Todos los derechos reservados.
"""

import os
import shutil
from datetime import datetime

def hacer_backup(origen, destino):
    """
    ¡Clonando tus archivos como un mago! 🪄

    Copia el archivo o directorio especificado en 'origen' a la ubicación 'destino'.
    """
    try:
        if os.path.isfile(origen):
            shutil.copy2(origen, destino)  # Copia con metadatos (fecha, permisos)
            print(f"¡Archivo '{origen}' respaldado con éxito!")
        elif os.path.isdir(origen):
            nombre_backup = os.path.basename(origen) + "_" + datetime.now().strftime("%Y%m%d-%H%M%S")
            destino_final = os.path.join(destino, nombre_backup)
            shutil.copytree(origen, destino_final)
            print(f"¡Directorio '{origen}' respaldado con éxito en '{destino_final}'!")
        else:
            print(f"¡Alerta! '{origen}' no es un archivo ni un directorio válido.")
    except PermissionError:
        print(f"¡Uy! No tengo permiso para acceder a '{origen}'.")
    except Exception as e:
        print(f"¡Error inesperado! {e}")

def main():
    """
    ¡El capitán del barco de los backups! ⛵

    Configura y ejecuta las copias de seguridad.
    """
    import argparse

    parser = argparse.ArgumentParser(description="Realizar copias de seguridad de archivos o directorios.")
    parser.add_argument("origen", help="Archivo o directorio a respaldar.")
    parser.add_argument("destino", help="Directorio donde se guardará la copia de seguridad.")
    args = parser.parse_args()

    hacer_backup(args.origen, args.destino)

if __name__ == "__main__":
    main()
