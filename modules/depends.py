import os
print("Installing dependencies")
os.system('sudo pacman -S openssh git github-cli ufw cronie wget yay')
os.system('yay -S mcrcon')
