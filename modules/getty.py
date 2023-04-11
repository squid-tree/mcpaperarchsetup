from modules.scripts.config import *
import os
print("Setting up getty autologin")

configstring=str("""[Service]
ExecStart=
ExecStart=-/sbin/agetty -o '-p -f -- "\\"u' --noclear --autologin %s %I $TERM""" % user)

os.system("sudo -C \'echo %s >> /etc/systemd/system/getty@tty1.service.d/autologin.conf\'")

print("Getty login has been setup")
