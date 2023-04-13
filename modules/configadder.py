from modules.scripts.config import *
import os

print("Configruing mcrcon...")
pwd = ''.join(list(os.path.realpath(os.path.dirname(__file__))).copy()).strip()

storagedir=str("%s/mcconfigstxt/mcrcon.txt" % pwd)
tempdir=str("%s/mcconfigstxt/temp.txt" % pwd)
targetdir=str("/opt/minecraft/mcserver/server.properties")

os.system(str("rm %s" % tempdir))
os.system(str("touch %s" % tempdir))

with open(storagedir, 'r') as file:
    copytty = file.read().strip()

copytty = copytty.splitlines()

copytty[42] = str('rcon.password=%s' % rcpassword)
copytty[12] = str('enable-rcon=true')
copytty='\n'.join(copytty)
    
temp_object = open(tempdir, "a")
temp_object.write(str(copytty))
temp_object.close()

os.system(str("sudo cp %s %s" % (tempdir,targetdir)))

os.system(str("rm %s" % tempdir))

print("Agreeing to EULA...")
eulatarget="/opt/minecraft/mcserver/eula.txt"
eulastorage=str("%s/mcconfigstxt/eula.txt" % pwd)
os.system(str("sudo cp %s %s" % (eulastorage ,eulatarget)))
