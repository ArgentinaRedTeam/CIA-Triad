# -*- coding: utf-8 -*-
"""
cifrado.py - Tu guardián criptográfico personal, cortesía de Red Team Argentina.
Porque la seguridad no tiene por qué ser aburrida. 😉

Este script te permite cifrar y descifrar archivos con facilidad, manteniendo tus secretos a salvo de miradas indiscretas.

Copyright (c) 2024 Red Team Argentina. Todos los derechos reservados.
"""

from cryptography.fernet import Fernet

def generar_clave():
    """
    ¡Forjando la llave maestra! 🗝️

    Genera una clave de cifrado ultrasecreta y la guarda en 'clave.key'.
    """
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)

def cargar_clave():
    """
    ¡Abriendo el cofre del tesoro! 🎁

    Recupera la clave de cifrado del archivo 'clave.key'.
    """
    return open("clave.key", "rb").read()

def cifrar(archivo, clave):
    """
    ¡Encriptando como un agente secreto! 🕵️‍♀️

    Transforma el contenido del archivo en un galimatías indescifrable.
    """
    f = Fernet(clave)
    with open(archivo, "rb") as file:
        datos_originales = file.read()
    datos_cifrados = f.encrypt(datos_originales)
    with open(archivo, "wb") as file:
        file.write(datos_cifrados)

def descifrar(archivo, clave):
    """
    ¡Descifrando el código secreto! 🔓

    Revela el contenido original del archivo a partir del galimatías.
    """
    f = Fernet(clave)
    with open(archivo, "rb") as file:
        datos_cifrados = file.read()
    datos_originales = f.decrypt(datos_cifrados)
    with open(archivo, "wb") as file:
        file.write(datos_originales)

def main():
    """
    ¡El centro de control de la misión! 🚀

    Gestiona las operaciones de cifrado y descifrado.
    """
    import argparse

    parser = argparse.ArgumentParser(description="Cifrar o descifrar un archivo.")
    parser.add_argument("archivo", help="El archivo a proteger.")
    parser.add_argument(
        "-g",
        "--generar_clave",
        action="store_true",
        help="Generar una nueva clave de cifrado.",
    )
    parser.add_argument(
        "-d",
        "--descifrar",
        action="store_true",
        help="Descifrar el archivo (por defecto, se cifra).",
    )
    args = parser.parse_args()

    if args.generar_clave:
        generar_clave()
        print("¡Clave generada y lista para la acción!")

    clave = cargar_clave()

    if args.descifrar:
        descifrar(args.archivo, clave)
        print("¡Archivo descifrado! ¡Misión cumplida!")
    else:
        cifrar(args.archivo, clave)
        print("¡Archivo cifrado! ¡Nadie podrá leer tus secretos!")

if __name__ == "__main__":
    main()
