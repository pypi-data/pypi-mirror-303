from textPlay.colors import *
import os

def FileNotFound():
    print(f"{RED}File not found{RESET} \nUse: {MAGENTA}pyauto init{RESET}")
    print("To create a config file")
    exit()

def checkHeader(line, index)-> bool:          
    if line[-1] == "]\n" or line[-1] == "]":
        return True
    else:
        print(f"SyntaxError: No closing bracket @ line {index} \n{line} \n{'~'*(len(line))}^")
        exit()

def checkPath(name):
    if os.path.exists(name):
        print(f"{RED}Config file already exists{RESET} @ {BLUE}{name}{RESET}")
        rewrite = input(f"Do you want to rewrite {name}? (y/n) ").lower()
        if rewrite == "y" or rewrite == "yes":
            return True
        elif rewrite == "n" or rewrite == "no":
            return False
        else:
            return False
    else:
        return True