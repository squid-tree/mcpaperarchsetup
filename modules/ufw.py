import os

print("Setting up UFW to allow ports 25565 and 22")

os.system('sudo ufw enable')
os.system('sudo ufw allow 25565')
os.system('sudo ufw allow 22')
