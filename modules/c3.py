#! /usr/bin/python3
# _Programa : wolf-wep_
# _Version :1.0_
# _Creador : Gabriel Romero_
# _Contacto : gabrielromero0499@gmail.com_
# _Apodo : Wolf-Saiko_

#################################################################
#                                                               #
# -*- ENCODING: UTF-8 -*-                                       #
# Este script es software libre. Puede redistribuirlo y/o       #
# modificar-lo bajo los términos de la Licencia Pública General #
# de GNU según es publicada por la Free Software Foundation,    #
# bien de la versión 3 de dicha Licencia o bien (según su       #
# elección) de cualquier versión posterior.                     #
#                                                               #
# Si usted hace alguna modificación en esta aplicación,         #
# deberá siempre mencionar al autor original de la misma.       #
#                                                               #
# Autor: Script creado por Wolf-Saiko                           #
#                                                               #
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