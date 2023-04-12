from modules.scripts.config import *
import modules.scripts.projectmodules
import copy

if os.geteuid() == 0:
    print("ERROR: Cannot be run as root")
    quit()

print("UNINSTALLER \n")
if not projectmodules.confirminput("Would you like to continue?"):
    print("Quiting program ...")
    quit()

homedircopy = homedirectory


print("homedircopy", homedircopy)

# mcserverbackup
print("Uninstalling backup software and saving backups in home")
os.system(str('sudo cp /usr/share/mcbackupsoftware/backups %s/' % homedircopy))
os.system('sudo rm -rf /usr/bin/mcserverbackup')
os.system('sudo rm -rf /etc/cron.daily/mcserverbackup.sh')
os.system('sudo rm -rf /usr/mcbackupsoftware')

# saveinstall
print("Uninstalling the mcserverinstaller script from home")
os.system(str('sudo rm -rf %s/mcserverinstaller' % homedircopy))

# Install script 
print("Uninstalling mcserver, most recent backup will be saved to backupsmc in home")
from modules.scripts import uninstall

print("Everything uninstalled! Dependencies and services have been left as is, besides startmc.service which was deleted and disabled")
