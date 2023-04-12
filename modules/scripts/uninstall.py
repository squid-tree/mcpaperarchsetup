from modules.scripts import projectmodules
from modules.scripts.config import *

homedirc = list(homedirectory)
homedirc = homedirc.copy()
homedirc = ''.join(homedirc)

if not projectmodules.confirminput("Are you sure you want to uninstall the server?"):
    print("Quitting")
    quit()
print("Backup will be saved to %s/backupsmc" % homedirc)
print("Saving Backup ...")
os.system(str("sudo cp --parents /opt/minecraft/mcserver %s/backupsmc" % homedircy))
print("Backup saved")
print("Uninstalling ...")
projectmodules.cleanupinstall()
projectmodules.cleanupbuild()
