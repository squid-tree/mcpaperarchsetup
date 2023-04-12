import os 
import subprocess
from modules.scripts import projectmodules
from modules.scripts.config import *

print("Installing ...")
print("Please ensure all configs have been filled")

# Testing Stage
#print('Checking if current user is called: %s' % user)
#if os.getlogin() != str('%s' % user):
#    print("Error: user must be called %s, this will cause errors otherwise", user)
#    quit()

homedirectoryc=homedirectory

print('\n')
print("------Verification------")

print("Checking config (manually ensure this is correct also, the script isn't perfect)")
if False in projectmodules.configchecker():
    print("Configurations missing, Quitting")
    quit()
else:
    print("Configs seem to be in place! (Again, double check)")

print("Checking dependencies")
packages = str(subprocess.check_output(['pacman', '-Qq']))

if not projectmodules.isin(packages,dependencies):
    print("There is a dependancy missing, do you have the following dependencies?")
    print(dependencies)
    quit()
else:
    print('All dependencies seem to be installed, make sure by checking below')
    print(dependencies)

#gitstatus = str(subprocess.Popen(['gh', 'auth', 'status']))
#print("What gitstatus says: %s" % gitstatus)
               #if 'are not logged into any' in gitstatus:
               #print("Error: You haven't authenticated git")
               #quit()
               #else:
               #print("Git seems to be authenticated!")

#if projectmodules.confirminput("Would you like to authenticate github to continue?"):
#    os.system("gh auth login")
#else:
#    print("Quit program")
#    quit()

if not projectmodules.confirminput("Are you sure you wish to continue?"):
    print("Quit program")
    quit()

# Starting Stage
print('\n')
print("------Building------")
if not projectmodules.confirminput("This is now the building stage, where the files will be downloaded in the home directory. Would you like to continue?"):
    print("Quitting, only completed verification stage, no changes were made")

if projectmodules.confirminput("Create a new user named minecraft?"):
    print("Adding user: minecraft")
    os.system('sudo useradd -r -m -U -d /opt/minecraft -s /bin/bash minecraft')
else:
    projectmodules.cleanupbuild()

#if projectmodules.confirminput("Clone the git repo in home?"):
#    os.system('git clone %s %s' % (ghserverurl, str('%s/mcserver' % homedirectory)))
#else:
#    projectmodules.cleanupbuild()

if projectmodules.confirminput('Wget this jar link? (Y/n): %s ' % jarlink):
    os.system('sudo mkdir -p %s/mcserver/paperdirectory' % homedirectoryc)
    os.system('sudo wget %s -P %s' % (jarlink, str('%s/mcserver/paperdirectory' % homedirectoryc)))
    print("Link was wgeted")
else:
    projectmodules.cleanupbuild()

print("\n")
print("------Installation------")    
if not projectmodules.confirminput("This is now the installation stage, where the server will be installed into the system. Continue?"):
    projectmodules.cleanupbuild()

if projectmodules.confirminput("Install mcserver to it's directory?"):
    print("Installing mcserver ...")
    projectmodules.os.system('sudo cp -r %s/mcserver /opt/minecraft/' % homedirectoryc)
else:
    projectmodules.cleanupbuild()

if projectmodules.confirminput("Install the startmc service?"):
    os.system('sudo touch /etc/systemd/system/startmc.service')
    os.system('sudo sh -c \'echo \"%s\" >> /etc/systemd/system/startmc.service\'' % mcserviceconfig)
else:
    projectmodules.cleanupinstall()
    projectmodules.cleanupbuild()

if projectmodules.confirminput("Enable startmc service?"):
    print("Enabling startmc.service ...")
    os.system('sudo systemctl daemon-reload')
    os.system('sudo systemctl enable startmc.service')
else:
    projectmodules.cleanupinstall()
    projectmodules.cleanupbuild()

print('\n')
print('All done! The server will start upon reboot, or if you would like to start the server now, execute the command: systemctl start startmc.service')
