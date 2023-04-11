# Setup ufw
    # Enable ports 25565 and 22
# Setup Ssh with {user} 
# Set Getty Up
# Install Dependencies
# Install server 
print("Welcome")
print("This script will set up your minecraft server")
print("It will set up ufw (firewall), ssh for the current user, autologin, any dependencies and install the server")
print("\n")

from modules import depends
from modules import ufwsetup
from modules import getty
from modules import sshsetup
from modules import installer
from modules import saveinstall
