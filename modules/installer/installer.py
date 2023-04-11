import os
import sys

print("----------------------------------")
print("Welcome to the mcserver installer!")
print("----------------------------------")
print("\n")
if len(sys.argv) == 2:
    if sys.argv[1] == "--install":
        print("\n")
        from scripts import build
    if sys.argv[1] == "--uninstall":
        print("\n")
        from scripts import uninstall
else:
    print("\n")
    print("Options: ")
    print("--install, install the server")
    print("--uninstall, uninstall the server")
