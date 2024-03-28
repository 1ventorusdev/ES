from colorama import*
import os
import platform
import psutil

system = platform.system()
if system == "Windows":
    clear = "cls"
    directory = "dir"
elif system == "Linux":
    clear = "clear"
    directory = "ls"
else:
    clear = "erreur"
direct = os.getcwd()

couleur = Fore.GREEN
command_colors = Fore.CYAN
text_colors = Fore.BLUE

with open("save_local.txt", "r") as local:
    locat = local.read()
    loc = locat.splitlines()
    cd = loc[0]
locat = os.getcwd()
os.chdir(cd)

with open("version.txt", "r") as offline_data:
        data_version=offline_data.read()
        version=data_version.splitlines()

        offline_version=version[0]

with open("user.txt", "r") as datafile:
    data = datafile.read()
    usersave = data.splitlines()
    user = usersave[0]

linux_command = (
    f"{command_colors}┌─[{text_colors}file manager 0.10.3{command_colors}]─[{text_colors}administrator system{command_colors}]─[{text_colors}~{command_colors}]\n"
    f"{command_colors}└──╼[{text_colors}★{command_colors}]$>>>{text_colors} ")
win_command=text_colors + os.getcwd() + command_colors + ">>>" + text_colors 
    
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

os.chdir(locat)

def display_running_processes():
    print("Liste des processus en cours d'exécution:")
    print("=========================================")
    for process in psutil.process_iter(['name', 'cpu_percent', 'memory_percent']):
        print(f"Nom: {process.info['name']}, CPU: {process.info['cpu_percent']}%, Mémoire: {process.info['memory_percent']}%")

def hall():
    os.system(clear)
    print(couleur)
    display_running_processes()
    print("commande :")
    print("   -close : ferme task manager")
    print("   -clear : recharge l'affichage de task manager")

os.chdir(cd)
hall()
while True:
    print(direct)
    command = input(command_colors + entry)

    if command=="clear":
        hall()

    elif command=="close":
        os.system(clear)
        break

    else:
        hall()
        print("je n'ai pas compris")

# generate a system for kill selected taskp