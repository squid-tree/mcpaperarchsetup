import getpass
import modules.scripts.projectmodules
userc = list(getpass.getuser())).copy()
user = ''.join(userc)

x=input("Installing or uninstalling? (i/u)")
if x == "i":
    import superinstaller
elif x == "u":
    import uninstaller
else:
    print("Invalid option")
    quit()
