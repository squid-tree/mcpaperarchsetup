from modules.scripts.config import *
import os

pwd = ''.join(list(os.path.realpath(os.path.dirname(__file__))).copy()).strip()

#creation of temp
ttydir=str("%s/scriptsbackup/tty.txt" % pwd)
tempdir=str("%s/scriptsbackup/temp.txt" % pwd)

os.system(str("rm %s" % tempdir)
os.system(str("touch %s" % tempdir)

# Taking of tty.txt and writing to temp
with open(ttydir, 'r') as file:
    copytty = file.read()
    
temp_object = open(tempdir, "a")
temp_object.write(str(copytty))
temp_object.write(str(" %s" % user))
temp_object.write(str(r" %I $TERM"))
temp_object.close()

print("Setting up getty directory ... ")

os.system(str('sudo mkdir -p /etc/systemd/system/getty@tty1.service.d'))

print("Installing getty script")

os.system(str("sudo cp %s /etc/systemd/system/getty@tty1.service.d/autologin.conf" % tempdir)) 

print("Getty login has been setup")
