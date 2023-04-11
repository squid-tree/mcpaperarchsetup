from modules.scriptsbackup.backup import *
from modules.scripts.config import *
from modules.scripts.projectmodules import *
print("Installing Mcserverbackup")

print("Creating backup script... ")
os.system('sudo mkdir /usr/share/mcbackupsoftware')
os.system('sudo touch /usr/share/mcbackupsoftware/backup.py')
os.system('sudo sh -c \'echo \"%s\" >> /usr/share/mcbackupsoftware/backup.py\'' % storedbackup)

print("Setting script up to run daily ...")
backupbscr="""#!/bin/bash
/usr/bin/python3 /usr/share/mcbackupsoftware/backup.py"""
os.system('sudo touch /usr/share/mcbackupsoftware/mcserverbackup.sh')
os.system(str('sudo bash -c \'echo \"%s\" >> /usr/share/mcbackupsoftware/mcserverbackup.sh\'' % backupbscr))
os.system(str('sudo ln -sf /usr/share/mcbackupsoftware/mcserverbackup.sh /etc/cron.daily/mcserverbackup.sh'))

print("Setting up backup script binary at /usr/bin/mcserverbackup ...")
os.system(str('sudo ln -sf /usr/share/mcbackupsoftware/mcserverbackup.sh /usr/bin/mcserverbackup'))

print("Creating storage for backups at /usr/share/mcbackupsoftware/backups ...")
os.system('sudo mkdir /usr/share/mcbackupsoftware/backups')
