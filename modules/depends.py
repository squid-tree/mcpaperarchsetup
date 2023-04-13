import os
print("Installing dependencies")
os.system('sudo pacman -S openssh git github-cli ufw cronie wget yay')
held=os.popen('pacman -Qq')
if 'yay' not in held:
    print("yay must be installed first")
    quit()
os.system('yay -S mcrcon')
