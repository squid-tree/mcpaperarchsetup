from modules.scripts import projectmodules
from modules.scripts.config import *

if not projectmodules.confirminput("Are you sure you want to uninstall the server?"):
    print("Quitting")
    quit()
print("Backup will be saved to %s/backupsmc" % homedirectory)
print("Saving Backup ...")
os.system(str("sudo cp --parents /opt/minecraft/mcserver %s/backupsmc" % homedirectory))
print("Backup saved")
print("Uninstalling ...")
projectmodules.cleanupinstall()
projectmodules.cleanupbuild()
