import os
import socket
import nmap
import platform
from colorama import *


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
    f"{command_colors}┌─[{text_colors}contact 0.10.1{command_colors}]─[{text_colors}administrator system{command_colors}]─[{text_colors}~{command_colors}]\n"
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

font_color=Style.RESET_ALL + couleur

os.chdir(locat)


MESSAGE_DIR = os.path.join("contact", "messages")
SEND_DIR = os.path.join("contact", "send")

# Fonction pour détecter les noms d'hôtes connectés au même réseau
def detect_local_hosts():
    local_hosts = set()

    try:
        # Créez un scanner nmap
        scanner = nmap.PortScanner()

        # Obtenez l'adresse IP de l'interface réseau active
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        test_ip = s.getsockname()[0]
        s.close()

        # Utilisez nmap pour scanner les hôtes sur le réseau
        scanner.scan(hosts=f"{test_ip}/24", arguments="-n -sP")

        # Parcourez les hôtes découverts et récupérez leur nom d'hôte
        for host in scanner.all_hosts():
            try:
                hostnames = scanner[host]['hostnames']
                if len(hostnames) > 0:
                    hostname = hostnames[0]['name']
                    local_hosts.add(hostname)
            except KeyError:
                pass

    except Exception as e:
        print("Erreur lors de la détection des hôtes locaux :", e)

    return local_hosts


# Fonction pour envoyer un message à un hôte
def send_message_to_host(host, message):
    filename = os.path.join(SEND_DIR, host)
    with open(filename, "a") as file:
        file.write(message + "\n")

# Fonction pour vérifier et envoyer les messages en attente
def check_and_send_messages():
    for filename in os.listdir(SEND_DIR):
        host = filename.split(".")[0]  # Supprime l'extension .txt
        if host in local_hosts:
            with open(os.path.join(SEND_DIR, filename)) as file:
                messages = file.readlines()
                for message in messages:
                    # Envoyer le message à l'hôte
                    pass  # À implémenter selon vos besoins
            os.remove(os.path.join(SEND_DIR, filename))

# Fonction pour gérer le chat avec un hôte
def chat_with_host(host):
    while True:
        message = input("Votre message (ou 'close' pour quitter ou 'contacts' pour afficher la liste des contacts) : ")
        if message.lower() == "close":
            break
        elif message.lower() == "contacts":
            print("Liste des contacts : ", local_hosts)
        else:
            send_message_to_host(host, message)

# Main
if __name__ == "__main__":
    print(couleur)
    os.system(clear)
    if not os.path.exists(MESSAGE_DIR):
        os.makedirs(MESSAGE_DIR)
    if not os.path.exists(SEND_DIR):
        os.makedirs(SEND_DIR)

    while True:
        # Détecter les noms d'hôtes connectés au même réseau
        local_hosts = detect_local_hosts()

        # Vérifier et envoyer les messages en attente
        check_and_send_messages()

        # Boucle pour chaque hôte trouvé
        for host in local_hosts:
            print(host)
        
        send_to = input(entry)
        os.system(clear)
        if send_to == "close":
            print(Style.RESET_ALL)
            os.system(clear)
            break
        for host in local_hosts:
            if send_to == host:
                print(f"Connected host: {host}")
                # Commencer le chat avec cet hôte
                chat_with_host(host)
            else:
                pass