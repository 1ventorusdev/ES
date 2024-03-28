from colorama import*
import os
import platform
import psutil
import shutil

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

storage_used_bar_color=Fore.GREEN + Style.BRIGHT
storage_no_used_bar_color=Fore.RED + Style.BRIGHT
font_color=Style.RESET_ALL + couleur

os.chdir(locat)

def convert_bytes(num, suffix='o'):
    for unit in [' ', ' K', ' M', ' G', ' T', ' P', ' E', ' Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def get_disk_space_info(drive):
    total, used, free = shutil.disk_usage(drive)
    total_size_str = convert_bytes(total, 'o')
    used_size_str = convert_bytes(used, 'o')
    return total_size_str, used_size_str, free

def list_all_disks():
    partitions = psutil.disk_partitions(all=True)
    disks = [partition.device for partition in partitions]
    return disks

def list_files(path='.'):
    file_list = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        size = os.path.getsize(item_path) if os.path.isfile(item_path) else 0
        size_str = convert_bytes(size)
        file_list.append((item, size_str))
    return file_list



def print_file_manager():
    drivers = list_all_disks()

    if not drivers:
        print("Aucun disque disponible.")
    else:
        for driver in drivers:
            total_size_str, used_size_str, free = get_disk_space_info(driver)

            total_size = float(total_size_str.split()[0])
            used_size = float(used_size_str.split()[0])

            percentage_used = int((used_size / total_size) * 100)
            bar_length = 50
            progress = int(bar_length * percentage_used / 100)
            
            bar = '[' + f'{storage_used_bar_color}/{font_color}' * progress + f'{storage_no_used_bar_color}/{font_color}' * (bar_length - progress) + f'] {percentage_used}%  {used_size_str} / {total_size_str}'
            print(f"Disque {driver} {bar}")

    print("\nListe des fichiers et dossiers dans '", direct, "' :")
    files = list_files()
    for file, size in files:
        print(f"- {file:<50} {size}")

def hall():
    print(couleur)
    os.system(clear)
    print("pour se deplacer faire 'ch' au lieu de 'cd'")
    print("pour supprimer un fichier ou un dossier faire 'rm' puis son nom")
    print()
    print("les nom ayant 0o sont des dossiers")
    print()
    print_file_manager()
    print()

os.chdir(cd)
direct = cd
hall()
while True:
    print(direct)
    command = input(command_colors + entry)

    if command == "close":
        os.system(clear)
        break

    elif command == "clear":
        hall()

    elif command == "ch..":
        hall()
        try:
            parent_directory = os.path.normpath(os.path.join(os.getcwd(), ".."))
            os.chdir(parent_directory)
            direct = os.getcwd()
            hall()
        except Exception as e:
            print(f"Erreur lors du changement de répertoire : {e}")

    elif command == "ch/":
        hall()
        try:
            # Obtient la racine du disque
            root_directory = os.path.abspath(os.sep)
            os.chdir(root_directory)
            direct = os.getcwd()
            hall()
        except Exception as e:
            print(f"Erreur lors du changement de répertoire : {e}")

    elif command.startswith("ch"):
        hall()
        _, path = command.split(" ", 1)
        path = path.strip()

        try:
            os.chdir(path)
            direct = os.getcwd()
            hall()
        except FileNotFoundError:
            print(f"Le répertoire '{path}' n'existe pas.")
        except Exception as e:
            print(f"Erreur lors du changement de répertoire : {e}")

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
            print(f"Erreur lors de la suppression de {path}: {e}")

    elif command == command:
        hall()
        print("\n>>> " + command + "\n")
        os.system(command)
