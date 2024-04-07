from colorama import*

import os
import platform



couleur = Fore.GREEN
command_colors = Fore.CYAN
text_colors = Fore.BLUE

os.chdir("..")
os.chdir("..")
direct = os.getcwd()
with open("version.ver", "r") as offline_data:
        data_version=offline_data.read()
        version=data_version.splitlines()

        offline_version=version[0]

with open("user.dta", "r") as datafile:
    data = datafile.read()
    usersave = data.splitlines()
    user = usersave[0]

linux_command = (
    f"{command_colors}┌─[{text_colors}CMD {offline_version}{command_colors}]─[{text_colors}administrator system{command_colors}]─[{text_colors}~{command_colors}]\n"
    f"{command_colors}└──╼[{text_colors}★{command_colors}]$>>>{text_colors} ")
win_command=text_colors + os.getcwd() + command_colors + ">>>" + text_colors 

system = platform.system()
if system == "Windows":
    clear = "cls"
    directory = "dir"
    ver = (f"windows version {offline_version}")
elif system == "Linux":
    clear = "clear"
    directory = "ls"
    ver = (f"linux version {offline_version}")
else:
    clear = "erreur"
    
if os.path.exists(os.path.join(user, "system", "save_config.txt")):
    with open(os.path.join(user, "system", "save_config.txt"), "r") as file:
        info = file.read()
        savelist = info.splitlines()
        entry_save = savelist[0]
        couleur_save = savelist[1]


        if entry_save == ">>>":
            entry = ">>>"

        elif entry_save == "lin":
            entry = linux_command

        elif entry_save == "win":
            entry = win_command

                    
        if couleur_save == "jaune":
            couleur = Fore.YELLOW
                        
        elif couleur_save == "vert":
            couleur = Fore.GREEN

        elif couleur_save == "blanc":
            couleur = Fore.WHITE

        elif couleur_save == "bleu":
            couleur = Fore.BLUE

        elif couleur_save == "majenta":
            couleur = Fore.MAGENTA

        elif couleur_save == "rouge":
            couleur = Fore.RED

        elif couleur_save == "cyan":
            couleur = Fore.CYAN

        elif couleur_save == "violet":
            couleur = Fore.MAGENTA + Style.DIM

        elif couleur_save == "rose":
            couleur = Fore.MAGENTA + Style.BRIGHT
            
else:
    entry = linux_command
    couleur = Fore.GREEN

def hall():
    os.system(clear)
    print(couleur)
    print(ver)
    print("x-storm software")

os.chdir(direct)
hall()
while True:
    command = input(command_colors + entry)

    if command == "close":
        os.system(clear)
        break

    elif command == "ch..":
        hall()
        try:
            parent_directory = os.path.normpath(os.path.join(os.getcwd(), ".."))
            os.chdir(parent_directory)
            hall()
        except Exception as e:
            print(f"Erreur lors du changement de répertoire : {e}")

    elif command == "ch/":
        hall()
        try:
            # Obtient la racine du disque
            root_directory = os.path.abspath(os.sep)
            os.chdir(root_directory)
            hall()
        except Exception as e:
            print(f"Erreur lors du changement de répertoire : {e}")

    elif command.startswith("ch"):
        hall()
        _, path = command.split(" ", 1)
        path = path.strip()

        try:
            os.chdir(path)
            print(f"Changement de répertoire vers : {path}")
            hall()
        except FileNotFoundError:
            print(f"Le répertoire '{path}' n'existe pas")

    elif command.startswith("rm"):
        hall()
        _, path = command.split(" ", 1)
        path = path.strip()

        try:
            os.remove(path)
            print(f"{path} supprimé")
            hall()
        except FileNotFoundError:
            print(f"Le fichier '{path}' n'existe pas.")
        except Exception as e:
            print(f"Erreur lors de la suppression de {e}")

    else:
        hall()
        print("\n>>> " + command + "\n")
        os.system(command)