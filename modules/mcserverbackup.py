import os
from modules.scriptsbackup import *
from modules.scripts.config import *
from modules.scripts.projectmodules import *

pwd = os.path.realpath(os.path.dirname(__file__))
backupdirpy = str('%s/scriptsbackup/backup.txt' % pwd)

print("Installing Mcserverbackup")

print("Enabling cron ...")
os.system('sudo systemctl --now enable cronie.service')

print("Creating backup script... ")
os.system('sudo mkdir /usr/share/mcbackupsoftware')
os.system('sudo touch /usr/share/mcbackupsoftware/backup.py')
os.system(str('sudo cp %s /usr/share/mcbackupsoftware/backup.py' % backupdirpy))

print("Setting script up to run daily ...")
os.system('sudo touch /usr/share/mcbackupsoftware/mcserverbackup.sh')
#os.system(str('sudo bash -c \'printf \"%%s\" \"%s\" > /usr/share/mcbackupsoftware/mcserverbackup.sh\'' % backupbscr))
os.system(str('sudo cp %s/scriptsbackup/shellbackup.txt /usr/share/mcbackupsoftware/mcserverbackup.sh' % pwd ))
os.system('sudo chmod +x /usr/share/mcbackupsoftware/mcserverbackup.sh')
os.system(str('sudo ln -sf /usr/share/mcbackupsoftware/mcserverbackup.sh /etc/cron.daily/mcserverbackup.sh'))

print("Setting up backup script binary at /usr/bin/mcserverbackup ...")
os.system(str('sudo ln -sf /usr/share/mcbackupsoftware/mcserverbackup.sh /usr/bin/mcserverbackup'))

print("Creating storage for backups at /usr/share/mcbackupsoftware/backups ...")
os.system('sudo mkdir /usr/share/mcbackupsoftware/backups')
