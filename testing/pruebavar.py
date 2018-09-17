import os
import time

os.chdir("/home/root/enair/modules")

os.system ("sudo sh script.sh")
file = open("interfaces.txt", "r")
variablesW = (file.readlines())
print ("First variable\n")

print (variablesW)

command = ("airmon-ng start %s" %(variablesW))
os.system (command)
os.system ("clear")
print ("Waiting...")
time.sleep (3)

os.system ("rm -rf interfaces.txt")
os.system ("touch mini")
os.system ("sudo sh script.sh")

print ("Second variable\n")

print (variablesW)

command_2 = ("airmon-ng stop %s" %(variablesW))
os.system (command_2)
