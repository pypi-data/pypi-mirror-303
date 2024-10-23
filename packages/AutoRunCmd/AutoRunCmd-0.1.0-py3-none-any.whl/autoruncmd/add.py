from textPlay.colors import *
import os

from autoruncmd.constants import *

def addtoScript(config, header, script):
    found_header = False
    if "=" not in script:
        print(f"SyntaxError: No '=' in script name \nUsage: {MAGENTA}pyauto add -c <config_file> -h <header_name> -s '<script_name>=<script_to_run>'{RESET}")
        exit()
    else:
        print(f"Config file: {config}")
        try:
            with open(config, "r") as f:
                lines = f.readlines()
                lines = [x for x in lines if x != "" or x != "\n"]
                for i, line in enumerate(lines):
                    line = line.strip().replace("\n", "")
                    if header in line:
                        found_header = True
                        if checkHeader(line, i):
                            lines.insert(i + 1, f"{script}\n")
                            with open(config, "w") as f:
                                f.writelines(lines)
                            print(f"Added command: {MAGENTA}{header}.{script.split('=')[0]}={script.split('=')[1]}{RESET}") 
                            print(f"{GREEN}Script added{RESET} @ {BLUE}{config}{RESET} \n\nUse: {MAGENTA}pyauto run{RESET}")
                            print("To run the script")
                            break
                else:
                    with open(config, "a") as f:
                        f.write(f"\n[py.{header}]\n{script}\n")
                    print(f"Added command: {MAGENTA}{header}.{script.split('=')[0]}={script.split('=')[1]}{RESET}")
                    print(f"{GREEN}New header and script added{RESET} @ {BLUE}{config}{RESET} \n\nUse: {MAGENTA}pyauto run{RESET}")
                    print("To run the script")
                    found_header = True

                if not found_header :
                    print(f"{RED}Header '{header}' not found{RESET} @ {BLUE}{config}{RESET}")

        except FileNotFoundError:
            FileNotFound()