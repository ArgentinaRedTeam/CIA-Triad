# -*- coding: utf-8 -*-
"""
suma_verificacion.py - Tu detector de intrusos digital, cortesía de Red Team Argentina.
Porque la integridad de tus datos es tan importante como un buen mate. 🧉

Este script te permite generar y verificar sumas de verificación (hashes) de tus archivos,
para asegurarte de que nadie los haya alterado a tus espaldas.

Copyright (c) 2024 Red Team Argentina. Todos los derechos reservados.
"""

import hashlib

def generar_hash(archivo, algoritmo="sha256"):
    """
    ¡Calculando la huella digital de tu archivo! 👣

    Genera una suma de verificación (hash) del archivo especificado utilizando el algoritmo elegido.
    """
    try:
        hash_objeto = hashlib.new(algoritmo)
        with open(archivo, "rb") as f:
            for bloque in iter(lambda: f.read(4096), b""):
                hash_objeto.update(bloque)
        return hash_objeto.hexdigest()
    except FileNotFoundError:
        print(f"¡Error! No encuentro el archivo '{archivo}'.")
        return None

def verificar_hash(archivo, hash_esperado, algoritmo="sha256"):
    """
    ¡Comparando huellas dactilares! 🔍

    Verifica si la suma de verificación del archivo coincide con el hash esperado.
    """
    hash_calculado = generar_hash(archivo, algoritmo)
    if hash_calculado == hash_esperado:
        print("¡Integridad verificada! El archivo no ha sido modificado.")
        return True
    else:
        print("¡Alerta! El archivo ha sido modificado o dañado.")
        return False

def main():
    """
    ¡El sheriff de la integridad de datos! 🤠

    Gestiona la generación y verificación de sumas de verificación.
    """
    import argparse

    parser = argparse.ArgumentParser(description="Generar o verificar la suma de verificación de un archivo.")
    parser.add_argument("archivo", help="El archivo a procesar.")
    parser.add_argument(
        "-v",
        "--verificar",
        metavar="HASH",
        help="Verificar si la suma de verificación coincide con el valor HASH.",
    )
    parser.add_argument(
        "-a",
        "--algoritmo",
        default="sha256",
        choices=["sha256", "md5"],
        help="Algoritmo de hash a utilizar (por defecto: sha256).",
    )
    args = parser.parse_args()

    if args.verificar:
        verificar_hash(args.archivo, args.verificar, args.algoritmo)
    else:
        hash_generado = generar_hash(args.archivo, args.algoritmo)
        if hash_generado:
            print(f"Suma de verificación ({args.algoritmo}): {hash_generado}")

if __name__ == "__main__":
    main()
