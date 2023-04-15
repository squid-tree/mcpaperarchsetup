import os 

password = input("Mcrcon password: ")
command = str()

print("Console, type q to quit")
while command != 'q':
    command=input("> ")
    os.system(str('mcrcon -H 127.0.0.1 -P 25575 -p %s %s' % (password, command)))
