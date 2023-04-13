import os 

#setting working directory
scrdirectoryc = list(os.path.dirname(os.path.realpath(__file__))).copy()
scrdirectory = ''.join(scrdirectoryc)

#setting user variable
import getpass
userc = list(getpass.getuser()).copy()
user = ''.join(userc)
del getpass
os.system(str("echo %s > %s/modules/scripts/user.txt" % (user, scrdirectory)))

del os

x=input("Installing or uninstalling? (i/u)")

if x == "i":
    #setting mcrcon password
    import os 
    passwordtemp = input("Enter desired mcrcon password: ")
    if input("Confirm mcrcon password: ") != passwordtemp:
        quit()
    else:
        os.system(str("echo %s > %s/modules/scripts/rcpassword.txt" % (passwordtemp, scrdirectory)))
        print("Mcrcon password set!")
    del os

    exec(open(str("%s/superinstaller.py" % scrdirectory)).read())
    print("Cleaning temp files")
    os.system(str("sudo rm %s/modules/scripts/user.txt" % scrdirectory))
    os.system(str("sudo rm %s/modules/scriptsbackup/temp.txt" % scrdirectory))
    os.system(str("sudo rm %s/modules/scripts/rcpassword.txt" % scrdirectory))
    quit()
elif x == "u":
    exec(open(str("%s/uninstaller.py" % scrdirectory)).read())
    quit()
else:
    print("Invalid option")
    quit()
