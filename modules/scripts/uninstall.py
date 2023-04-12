from modules.scripts import projectmodules
from modules.scripts.config import *

homedirc = homedirectory

if not projectmodules.confirminput("Are you sure you want to uninstall the server?"):
    print("Quitting")
    quit()
print("Backup will be saved to %s/backupsmc" % homedirc)
print("Saving Backup ...")
os.system(str("mkdir %s/backupsmc" % homedirectory))
os.system(str("sudo cp /opt/minecraft/mcserver %s/backupsmc" % homedirc))
print("Backup saved")
print("Uninstalling ...")
projectmodules.cleanupinstall()
projectmodules.cleanupbuild()
