import sys 
from pathlib import Path
from colorama import Fore, Style, init
init()

if len(sys.argv) < 2:
    print("Please provide a directory path")
    sys.exit()

path = Path(sys.argv[1])

if not path.exists():
    print("Directory does not exist")
    sys.exit()

if not path.is_dir():
    print("Path is not a directory")
    sys.exit()

def print_tree(folder, indent=0):
    for item in folder.iterdir():

        if item.is_dir():
            print("    " * indent + Fore.BLUE + "📂 " + item.name + Style.RESET_ALL)
            print_tree(item, indent + 1)
        elif item.is_file():
            print("    " * indent + Fore.GREEN + "📜 " + item.name + Style.RESET_ALL)

print_tree(path)
