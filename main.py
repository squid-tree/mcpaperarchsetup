import getpass
userc = list(getpass.getuser()).copy()
user = ''.join(userc)
del getpass

import os 
scrdirectoryc = list(os.path.dirname(os.path.realpath(__file__))).copy()
scrdirectory = ''.join(scrdirectoryc)
del os

x=input("Installing or uninstalling? (i/u)")

if x == "i":
    exec(open(str("%s/superinstaller.py" % scrdirectory)).read())
elif x == "u":
    exec(open(str("%s/uninstaller.py" % scrdirectory)).read())
    quit()
else:
    print("Invalid option")
    quit()
