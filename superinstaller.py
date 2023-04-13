# Setup ufw
    # Enable ports 25565 and 22
# Setup Ssh with {user} 
# Set Getty Up
# Install Dependencies
# Install server 
import os
print("Welcome")
print("This script will set up your minecraft server")
print("It will set up ufw (firewall), ssh for the current user, autologin, any dependencies, backup software and install the server")
print("\n")

if os.geteuid() == 0:
    print("ERROR: Cannot be run as root")
    quit()

del os 

if input("HAVE YOU FILLED OUT THE CONFIG (y/n)") != 'y':
    quit()
if input("DOUBLE CONFIRM, type fully (yes/no)") != 'yes':
    quit()

from modules import depends
from modules import ufw
from modules import getty
from modules import sshsetup
from modules import installer
from modules import saveinstall
from modules import mcserverbackup
from modules import configadder

print("\n\n\n\n\n\n")
print("ALL DONE!!!!")
print("For your next steps: agree to the eula, configure the server and reboot!")
