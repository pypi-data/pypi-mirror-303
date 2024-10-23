import json
import os
from textPlay.colors import *
import time

from autoruncmd.constants import *

# MAIN
error = "Error: "
cmd = []

header_check = False
cmd_line = False
comment = False
token = False
sec_header = False

check_line = []

def runScript(run_cmd, config_file):

    global error
    global cmd

    global header_check
    global cmd_line
    global comment
    global token
    global sec_header
    global check_line


    if not config_file:
        config_file = ".pyscripts"

    print(f"Config file: {config_file}")

    try:
        with open(config_file, "r") as f:
            lines = f.readlines()
            lines = [x for x in lines if x != "" or x != "\n"]

    except FileNotFoundError:
        FileNotFound()

    if not lines[0].startswith(f"# Line Of Configuration (LOC) file = {config_file}"):
        print(f"LOC not found \nWriting to {config_file}")
        loc = f"# Line Of Configuration (LOC) file = {config_file} [{time.ctime()}]\n"
        with open(config_file, "w") as f:
            f.writelines([loc]+lines)

    if not run_cmd:
        run_cmd = input("Header Name: ")
    else:
        print(f"Header Name: {run_cmd}")

    print()

    if "." in run_cmd:
        cmdtoken = run_cmd.split(".")[1]
        head_cmd = f"[py.{run_cmd.split(".")[0]}]"
        run_cmd = run_cmd.split(".")[0]
        token = True


        print(f"Header: {head_cmd}")
        print(f"Command token: {cmdtoken}")

        print()

    for  index, line in enumerate(lines):
        index += 1
        line = line.replace("\n", "")

        if line.startswith("[py."):
            checkHeader(line, index)

        if line.startswith("[") and not line[1:].startswith("py."):
            print(f"Unexpected header found @ line {index}: {line}")
            exit()

        check_line.append(line)

        if line.startswith("[py.") and line[4:-1]==run_cmd and not header_check:
            header_check = checkHeader(line, index)
            print(f"Header found @ line {index}: {line}")
            cmd.append(line)

        elif line.startswith("#"):
            comment = True

        elif line.startswith("[py.") and header_check:
            sec_header = True

        elif "=" in line and header_check and not sec_header:
            cmd_line = True

            if token and line.split("=")[0].strip() == cmdtoken.strip():
                print("Token value:", line.split("=")[1].strip())
                cmd.append(line)

            else:
                cmd.append(line)

    time.sleep(1)

    if not header_check and not token:
        print(f"{error}Header not found:", run_cmd)
    elif not cmd_line and header_check:
        print(f"{error}Command not found")
    elif not cmd_line and not header_check and not comment:
        print(f"{error}Syntax Error @ line {index}")


    cmdstorun = []
    for c in cmd[1:]:
        for i, value in enumerate(c):
            if value == "=" and not token:
                cmdstorun.append(c[i+1:].strip())

            elif token and value == "=" and c.split("=")[0].strip() == cmdtoken.strip():
                cmdstorun.append(c[i+1:].strip())

    time.sleep(1)

    print(f"Number of commands executing: {len(cmdstorun) if len(cmdstorun) >= 1 else 0}")
    print("\nCommands:")

    if len(cmdstorun) > 0:

        for cmds in cmdstorun:
            print(cmds)
        print("\nExecuting Commands...", end="\r")

        for cmds in cmdstorun:
            print(f"\nExecuting: {MAGENTA}{cmds}{RESET}\n")
            os.system(cmds)

    else:
        print("No commands executing")











