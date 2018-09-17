#! /usr/bin/python3

# Integra Funciones De:                                         #
#                                                               #
# Python 3                                                      #
# Aircrack-ng                                                   #
# Xterm                                                         #
#                                                               #
# Un saludo                                                     # 
#                                                               #
#################################################################""")

import os

###########################################################
ruta_captura = ("../captura/")
ruta_diccionarios = ("../diccionarios/")
###########################################################

print ("""
__    __   ___   __     ____  __    __ __  ____ __    ___ ____   ___    ___ __ __
 ||    ||  // \\  ||    ||     ||    || || ||    ||   //   || \\ // \\  //   || //
 \\ /\ // ((   )) ||    ||==   \\ /\ // || ||==  ||  ((    ||_// ||=|| ((    ||<< 
  \V/\V/   \\_//  ||__| ||      \V/\V/  || ||    ||   \\__ || \\ || ||  \\__ || \\
                                                                                   
                                Crackear A Fuerza Bruta""")

# variables a usar

print ("\nIngrese el nombre del archivo capturado")
archivo = input ("wifi >> ")
handshake = ruta_captura + archivo

print ("\nIngrese el nombre del diccionario")
diccionario = input ("wifi >> ")
passwords = ruta_diccionarios + diccionario

comando_1 = ("aircrack-ng %s -w %s") % (handshake, passwords)

os.system (comando_1)
