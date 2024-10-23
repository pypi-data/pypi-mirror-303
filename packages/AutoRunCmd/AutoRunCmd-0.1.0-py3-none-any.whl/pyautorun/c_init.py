from textPlay.colors import *
import time
import os

from autoruncmd.constants import *

def createConfig(name):
    created = False
    if not name:
        if checkPath(".pyscripts"):
            try:
                with open(".pyscripts", "w") as f:
                    f.write(f"# Line Of Configuration (LOC) file = .pyscripts [{time.ctime()}]\n")

            except FileNotFoundError:
                FileNotFound()
        else:
                print(f"{RED}Config file not overwritten{RESET} @ {BLUE}.pyscripts{RESET}")
                exit()

    else:
        if checkPath(name):
            try:
                with open(name, "w") as f:
                    f.write(f"# Line Of Configuration (LOC) file = {name} [{time.ctime()}]\n")

            except FileNotFoundError:
                FileNotFound()

        else:
            print(f"{RED}Config file not created{RESET} @ {BLUE}{name}{RESET}")
            exit()

    print(f"{GREEN}Config file created{RESET} @ {BLUE}{os.getcwd()}{RESET} \nUse: {MAGENTA}pyauto run{RESET}")
    print("To run the script")