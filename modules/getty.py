from modules.scripts.config import *
import os

def literaljoiner(l):
    string=str()
    for i in range(len(l)):
        string += r'{}'.format(str("%s" % l[i]).replace('\n', '\\n'))

print("Setting up getty autologin")


configstring=list([r"[Service]", "\n", r"ExecStart=", "\n", r"ExecStart=-/sbin/agetty -o '-p -f -- ", r"\\\\\\\\u", r"' ", r"--noclear --autologin ", r'{}'.format(str("%s" % user)), " %%I \$TERM"])


configstring = literaljoiner(configstring)

print("Setting up getty directory ... ")

os.system(str('sudo mkdir -p /etc/systemd/system/getty@tty.service.d'))

print("Installing getty script")

os.system(str('sudo bash -c \"printf \"%s\" > %s"' % (configstring, str('/etc/systemd/system/getty@tty1.service.d/autologin.conf'))))

print("Getty login has been setup")
