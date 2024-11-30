import os
import sys
import subprocess
import getpass
import socket
import readline
from colorama import Fore, Back, Style, init

init(autoreset=True)

def terminal():
    history_file = "command_history.txt"

    if os.path.exists(history_file):
        readline.read_history_file(history_file)

    while True:
        current_path = os.getcwd()
        print(Fore.BLUE + "┃", Fore.BLACK + Back.BLUE + f" 🖴 {current_path}" + Back.RESET + Fore.BLUE + "", Fore.RESET + Back.RESET, end=" ")
        command = input()

        if command.lower() == "exit":
            break
        elif command.strip() == "":
            print(" ")
            continue
        else:
            readline.add_history(command)

            if command.startswith("cd "):
                try:
                    path = command[3:].strip()
                    os.chdir(path)
                except Exception:
                    print(Fore.RED + " ✘ " + Style.RESET_ALL, end="")
                continue
            else:
                try:
                    result = subprocess.run(command, shell=True, text=True)
                    if result.stdout:
                        print(" ", result.stdout.strip())
                    if result.stderr:
                        print(Fore.RED + " ✘ " + Style.RESET_ALL, end="")
                except Exception:
                    print(Fore.RED + " ✘ " + Style.RESET_ALL, end="")

    readline.write_history_file(history_file)

if __name__ == "__main__":
    terminal()