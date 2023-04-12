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
    import superinstaller
elif x == "u":
    import uninstaller
else:
    print("Invalid option")
    quit()
