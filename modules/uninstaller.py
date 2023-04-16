from modules.scripts import projectmodules
from modules.scripts.config import *
import time

scrdirectoryc = list(os.path.dirname(os.path.realpath(__file__))).copy()
scrdirectory1 = ''.join(scrdirectoryc)

if os.geteuid() == 0:
    print("ERROR: Cannot be run as root")
    quit()

homedircopy = homedirectory

print("UNINSTALLER \n")
if not projectmodules.confirminput("Would you like to continue?"):
    print("Quiting program ...")
    quit()

print("Stopping mcserver ...")
os.system("sudo systemctl stop startmc")
time.sleep(4)

# mcserverbackup
print("Uninstalling backup software and saving backups in home")
os.system(str('sudo cp -r /usr/share/mcbackupsoftware/backups %s/' % homedircopy))
os.system('sudo rm -rf /usr/bin/mcserverbackup')
os.system('sudo rm -rf /etc/cron.daily/mcserverbackup.sh')
os.system('sudo rm -rf /usr/mcbackupsoftware')

# saveinstall
#print("Uninstalling the mcserverinstaller script from home")
#os.system(str('rm -rf %s/mcserverinstaller' % homedircopy))

# Install script 
print("Uninstalling mcserver, most recent backup will be saved to backupsmc in home")
from modules.scripts import uninstall

print("Removing temp files")
os.system(str("sudo rm %s/modules/scripts/user.txt" % scrdirectory1))
os.system(str("sudo rm %s/modules/scriptsbackup/temp.txt" % scrdirectory1))
os.system(str("sudo rm %s/modules/scripts/rcpassword.txt" % scrdirectory1))

print("Uninstalling mcconsole")
os.system('sudo rm /usr/bin/mcconsole')
os.system('sudo rm -rf /usr/share/mcconsole')

print("Everything uninstalled! Dependencies and services have been left as is, besides startmc.service which was deleted and disabled")
