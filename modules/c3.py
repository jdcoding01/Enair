#! /usr/bin/python3  
import os
ruta_captura = ("../files/")
ruta_diccionarios = ("../Dictionaries/")


# variables a usar

print ("\n Type the name of the captured file. This should be in the 'files' folder.")
archivo = input ("wifi >> ")
handshake = ruta_captura + archivo

print ("\nIngrese el nombre del diccionario")
diccionario = input ("wifi >> ")
passwords = ruta_diccionarios + diccionario

comando_1 = ("aircrack-ng %s -w %s") % (handshake, passwords)

os.system (comando_1)
