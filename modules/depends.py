import os
print("Installing dependencies")
depends = ['openssh','git','github-cli','ufw','cronie','jdk-openjdk']
for i in depends:
    if i not in os.popen("pacman -Qq").read():
        os.system(str('pacman -S %s' % i))
    else:
        print(str('Dependency %s is installed, skipping install' % i))
os.system('sudo pacman -S openssh git github-cli ufw cronie wget jdk-openjdk')
held=os.popen('pacman -Qq').read()
if 'yay' not in held:
    print("yay must be installed first")
    quit()
yaydeps=["mcrcon"]

print("Yay is installed, checking yay dependencies")
for i in yaydeps:
    if i not in os.popen('pacman -Qq').read():
        os.system(str('yay -S %s') % i)
    else:
        print(str('Dependency %s is installed, skipping install' % i))
