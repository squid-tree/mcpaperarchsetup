storedbackup = """
import os
import re
import subprocess
from datetime import datetime

if os.geteuid() != 0:
    print("Must be run as root")
    exit()

def sortervalue(e):
    regex = r'\d+'
    matches = re.findall(regex,e)
    result = ''.join(matches)
    return result
timedate = datetime.now().strftime('%c')

backupspath = str("/usr/share/mcbackupsoftware/backups")
newbackuppath = str("%s%s" % (backupspath, timedate)) 

blacklist = list()

operation = subprocess.run((str('ls %s' % backupspath)), stdout=subprocess.PIPE, shell=True)
backupscontents = list(operation.stdout.decode().split('\n'))#.sort(key=sorter).reverse() # The contents of the backups folder as a list 
backupscontents.sort(key=sortervalue) # Youngest last!

while("" in backupscontents):
    backupscontents.remove("")

if backupscontents != None:                             # Creation of removal blacklist
    for i in range(len(backupscontents) - 4):
        blacklist.append(backupscontents[i])

if len(blacklist) >= 1:
    for i in blacklist:
        os.system(str('sudo rm -r %s\'%s\'' % (backupspath, i)))

os.system("sudo cp -r /opt/minecraft/ %s" % newbackuppath)
"""
