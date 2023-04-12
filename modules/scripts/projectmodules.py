import os
import subprocess
from modules.scripts.config import *

homedirectory = homedirectory

def configchecker():
    tests = [None] * 4
    # Check jar link
    if "https://api.papermc.io/v2/projects/paper/versions/" in jarlink:
        tests[0] = True
    else:
        tests[0] = False
    # Check jar version
    if "paper-" in jarversion and ".jar" in jarversion and jarversion in jarlink:
        tests[1] = True
    else:
        tests[1] = False
    # Check ram
    if int(ram) == '':
        tests[2] = False
    else:
        tests[2] = True
#    # Check gh url
#    if 'https://github.com/' in ghserverurl:
#        tests[3] = True
#    else:
#        tests[3] = False
    return tests

def falseortrue(s):
    if s == "y" or s == "Y" or s == '':
        return True
    else:
        return False

def isin(l,d):
    for i in range(len(d)):
        if d[i] not in l:
            return False
    return True

def confirminput(s):
    return falseortrue(input('%s (Y/n) ' % s))

def cleanupbuild():
    print("Cleaning Build:")
    os.system('sudo killall -u minecraft')
    os.system('sudo userdel -r minecraft')
    os.system('rm -r %s/mcserver' % homedirectory)
    print("Build was cleaned succesfully")
    quit()

def cleanupinstall():
    print("Uninstalling server from it's directory")
    os.system('sudo rm -rf /opt/minecraft/mcserver')
    print("Removing startmc service")
    os.system('sudo systemctl stop startmc.service')
    os.system('sudo systemctl disable startmc.service')
    os.system('sudo rm /etc/systemd/system/startmc.service')
