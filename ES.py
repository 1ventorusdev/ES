# import
from colorama import*

import os
import time
import socket
import random
import uuid
import platform
import psutil
import shutil
import ssl
import urllib.request
import datetime
import string
import glob
import wmi


# affichage
BANNER =("""
 ######## ##     ## ######## ########   ######   ######## ##    ##  ######  ##    ## 
 ##       ###   ### ##       ##     ## ##    ##  ##       ###   ## ##    ##  ##  ##  
 ##       #### #### ##       ##     ## ##        ##       ####  ## ##         ####   
 ######   ## ### ## ######   ########  ##   #### ######   ## ## ## ##          ##    
 ##       ##     ## ##       ##   ##   ##    ##  ##       ##  #### ##          ##    
 ##       ##     ## ##       ##    ##  ##    ##  ##       ##   ### ##    ##    ##    
 ######## ##     ## ######## ##     ##  ######   ######## ##    ##  ######     ##    
  ######  ##    ##  ######  ######## ######## ##     ##                              
 ##    ##  ##  ##  ##    ##    ##    ##       ###   ###                              
 ##         ####   ##          ##    ##       #### ####                              
  ######     ##     ######     ##    ######   ## ### ##                              
       ##    ##          ##    ##    ##       ##     ##                              
 ##    ##    ##    ##    ##    ##    ##       ##     ##                              
  ######     ##     ######     ##    ######## ##     ##                              
 """)

BANNER2 =("""
  ____>>>ES/<<<____________________________________________________
 |       toutes les commandes d'info du cmd fonctionnent !         |
 |                                                                 |
 | parametre : affiche les paramètres                              |
 | IPinfo : donne toute les info ip de la machine                  |
 | MACinfo : donne toute les info MAC de la machine                |
 | aide : affiche plus de commande                                 |
 | clear : même fonction que 'cls' mais garde l'interface          |
 | save : sauvegarde les paramètres actuel                         |
 | load : charge les dernier paramètre sauvegardé                  |
 | close : ferme le système de sécurité d'urgence                  |
 |_________________________________________________________________|
 """)

aide_admin = ("""
  ____>>>ES/aide<<<________________________________________________________
 |           toute les commandes d'info du cmd fonctionnent !              |
 |                                                                         |
 | parametre : affiche les paramètres                                      |
 | chat : permet de discuter avec soi même                                 |
 | IPinfo : donne toute les info ip de la machine                          |
 | MACinfo : donne toute les info MAC de la machine                        |
 | os : donne le systeme d'exploitation (os) de la machine                 |
 | info sys : donne les info sur le systeme physique                       |
 | defend no : désactive windows defender                                  |
 | defend yes : active windows defender                                    |
 | internet : verifie la connexion internet                                |
 | hostname / hn : donne le nom de la machine                              |
 | ipconfig : donne les info sur le materiel                               |
 | chdir : permet de se deplacer dans un répertoire précis                 |
 | curl ipinfo.io : donne l'adrese ip public                               |  
 | clear : même fonction que 'cls' mais garde l'interface                  |
 | ch 'chemin' : se déplace au chemin indiqué                              |
 | ch/ : revient a la racine du disque                                     |
 | ch.. : revient au dossier précedent                                     |
 | save : sauvegarde les paramètres actuel                                 |
 | load : charge les dernier paramètre sauvegardé                          |
 | credits : affiche les credits ainsi que la version de toolbox           |
 | close : ferme le cmd personnalisé                                       |
 |_________________________________________________________________________| 
 """)

aide_user = ("""
  ____>>>ES/aide<<<________________________________________________________
 |           toute les commandes d'info du cmd fonctionnent !              |
 |                                                                         |
 | parametre : affiche les paramètres                                      |
 | chat : permet de discuter avec soi même                                 |
 | IPinfo : donne toute les info ip de la machine                          |
 | MACinfo : donne toute les info MAC de la machine                        |
 | os : donne le systeme d'exploitation (os) de la machine                 |
 | info sys : donne les info sur le systeme physique                       |
 | internet : verifie la connexion internet                                |
 | hostname / hn : donne le nom de la machine                              |
 | ipconfig : donne les info sur le materiel                               |
 | chdir : permet de se deplacer dans un répertoire précis                 |
 | curl ipinfo.io : donne l'adrese ip public                               |  
 | clear : même fonction que 'cls' mais garde l'interface                  |
 | ch 'chemin' : se déplace au chemin indiqué                              |
 | ch/ : revient a la racine du disque                                     |
 | ch.. : revient au dossier précedent                                     |
 | save : sauvegarde les paramètres actuel                                 |
 | load : charge les dernier paramètre sauvegardé                          |
 | credits : affiche les credits ainsi que la version de toolbox           |
 | close : ferme le cmd personnalisé                                       |
 |_________________________________________________________________________| 
 """)

gen_parameters_admin=("""
  ____>>>ES/paramètres<<<__________________________________________________
 |                                                                         |
 | couleur : modifie la couleur                                            |
 | commande : accede au parametre des commandes                            |
 | info : donne les toute les info de ES                                   |
 | user : permet de gerer les utilisateur de ES ainsi que leur donnée      |
 | maj : met à jour ES                                                     |
 | logs : permet de modifier le mot de passe du compte                     |
 | view log : affiche les rapport de log si le mode dev est activé         |
 | admin : permet d'activer ou de désactiver le mode administrateur        |
 | close : retourne dans ES                                                |
 |_________________________________________________________________________|
 """)

gen_parameters_user=("""
  ____>>>ES/paramètres<<<__________________________________________________
 |                                                                         |
 | couleur : modifie la couleur                                            |
 | commande : accede au parametre des commandes                            |
 | info : donne les toute les info de ES                                   |
 | maj : met à jour ES                                                     |
 | logs : permet de modifier le mot de passe du compte                     |
 | view log : affiche les rapport de log si le mode dev est activé         |
 | admin : permet d'activer ou de désactiver le mode administrateur        |
 | dev : permet d'activer ou de désactiver le mode developpeur             |
 | close : retourne dans ES                                                |
 |_________________________________________________________________________|
 """)

command_sys=("""
  ____>>>ES/paramètres/commande<<<_________________________________________
 |                                                                         |
 | couleur com (cc) : modifie la couleur          (non fonctionnel)        |
 | couleur text (ct): modifie la couleur          (non fonctionnel)        |
 | linux : modifie le texte de commande pour celui de linux                |
 | win : modifie le texte de commande pour celui de windows                |
 | defaut : modifie le texte de commande pour celui par défaut de ES       |
 | close : retourne au parametre generaux                                  |
 |_________________________________________________________________________|
 """)

apps=("""
  ____>>>ES/apps<<<________________________________________________________
 |                                    |                                    |
 | outils :                           | microsoft :                        |
 |      -toolbox                      |      -powerpoint                   |
 |      -cmd                          |      -word                         |
 |      -file manager (fm)            |      -excel                        |
 |      -task manager (tm)            |                                    |
 |      -store                        |                                    |
 |                                    |                                    |
 | apps :                             | jeux :                             |
 |      -                             |       -life evol                   |
 |      -                             |       -nuclear ingenior (ni)       |
 |      -                             |       -                            |
 |_________________________________________________________________________|
 
 """)

cred=("""
 credits : 
  conception : 1ventorus

 merci de me contacter pour plus d'info au adresse mail suivante
    personnel :
      1ventorus@gmail.com
    
    professionel :
      x.storm.group@gmail.com

 """)

with open("version.txt", "r") as offline_data:
        data_version=offline_data.read()
        version=data_version.splitlines()

        offline_version=version[0]

new=(
 """version actuel de ES :\n"""
 f"""   {offline_version}\n\n"""
 
 """dernier ajout :\n"""
 """   -modification système de rapport log\n"""
 """   -correction de bug\n"""
 """   -ajout de la commande : hostname\n"""
 """   -ajout de l'NUS(New User System)\n"""
 """   -ajout de la batterie sur la commande linux\n"""
 )

# variable d'environnement
system = platform.system()
if system=="Windows":
    clear="cls"
elif system =="Linux":
    clear ="clear"
else:
    clear ="erreur"

with open("user.txt", "r") as datafile:
    data = datafile.read()
    usersave = data.splitlines()
    user = usersave[0]

with open(os.path.join(user, "system", "admin.txt"), "r") as data_save:
    data_admin = data_save.read()
    savelist = data_admin.splitlines()
    admin = savelist[0]
    devmode = savelist[1]

host = socket.gethostname()
couleur = Fore.GREEN
command_colors = Fore.CYAN
text_colors = Fore.BLUE

def get_battery_percentage():
    battery = psutil.sensors_battery()
    if battery is not None:
        return battery.percent
    else:
        return None

def get_battery_voltage():
    c = wmi.WMI()
    battery_info = c.Win32_Battery()[0]
    if battery_info is not None:
        try:
            voltage_str = battery_info.DesignVoltage
            voltage_int = int(voltage_str)  # Convertir en nombre entier
            voltage = voltage_int / 1000  # Convertir en volts
            return voltage
        except ValueError:
            return None
    else:
        return None

def get_battery_details():
    battery = psutil.sensors_battery()
    if battery is not None:
        status = "Plugged in" if battery.power_plugged else "Not plugged in"
        percent = battery.percent
        voltage = get_battery_voltage()
        remaining_seconds = battery.secsleft if battery.secsleft != -1 else None
        if remaining_seconds is not None:
            days = remaining_seconds // (24 * 3600)
            remaining_seconds %= (24 * 3600)
            hours = remaining_seconds // 3600
            remaining_seconds %= 3600
            minutes = remaining_seconds // 60
            seconds = remaining_seconds % 60
            remaining_time = f"{days}:{hours:02d}:{minutes:02d}:{seconds:02d}"
        else:
            remaining_time = "Calculating..."
        return {
            "status": status,
            "percent": percent,
            "voltage": voltage,
            "remaining_time": remaining_time
        }
    else:
        return None
    
def battery_details():
    battery_info = get_battery_details()
    if battery_info is not None:
        print(f"status de la batterie: {Fore.RED}{battery_info['status']}{couleur}")
        print(f"pourcentage de batterie: {Fore.RED}{battery_info['percent']}%{couleur}")
        print(f"Voltage: {Fore.RED}{battery_info['voltage']} mV{couleur}")
        print(f"temps d'activité: {Fore.RED}{battery_info['remaining_time']}{couleur}")
    else:
        print("Unable to retrieve battery information.")

def linux_command_admin():
    percentage = get_battery_percentage()
    if percentage is not None:
        linux_command = (
            f"{command_colors}┌─[{text_colors}ES {offline_version}{command_colors}]─[{text_colors}administrator system{command_colors}]─[{text_colors}{user}{command_colors}]─[{text_colors}~{command_colors}]\n"
            f"{command_colors}└──╼[{text_colors}Battery: {percentage}%{command_colors}]$>>>{text_colors} "
        )
    else:
        linux_command = (
            f"{command_colors}┌─[{text_colors}ES {offline_version}{command_colors}]─[{text_colors}administrator system{command_colors}]─[{text_colors}{user}{command_colors}]─[{text_colors}~{command_colors}]\n"
            f"{command_colors}└──╼[{text_colors}Battery: N/A{command_colors}]$>>>{text_colors} "
        )
    return linux_command

def linux_command_user():
    percentage = get_battery_percentage()
    if percentage is not None:
        linux_command = (
            f"{command_colors}┌─[{text_colors}ES {offline_version}{command_colors}]─[{text_colors}user system{command_colors}]─[{text_colors}{user}{command_colors}]─[{text_colors}~{command_colors}]\n"
            f"{command_colors}└──╼[{text_colors}Battery: {percentage}%{command_colors}]$>>>{text_colors} "
        )
    else:
        linux_command = (
            f"{command_colors}┌─[{text_colors}ES {offline_version}{command_colors}]─[{text_colors}user system{command_colors}]─[{text_colors}{user}{command_colors}]─[{text_colors}~{command_colors}]\n"
            f"{command_colors}└──╼[{text_colors}Battery: N/A{command_colors}]$>>>{text_colors} "
        )
    return linux_command
"""
linux_command_admin = (
    f"{command_colors}┌─[{text_colors}ES {offline_version}{command_colors}]─[{text_colors}administrator system{command_colors}]─[{text_colors}{user}{command_colors}]─[{text_colors}~{command_colors}]\n"
    f"{command_colors}└──╼[{text_colors}★{command_colors}]$>>>{text_colors} ")
linux_command_user = (
    f"{command_colors}┌─[{text_colors}ES {offline_version}{command_colors}]─[{text_colors}user system{command_colors}]─[{text_colors}{user}{command_colors}]─[{text_colors}~{command_colors}]\n"
    f"{command_colors}└──╼[{text_colors}★{command_colors}]$>>>{text_colors} ")"""
win_command=text_colors + os.getcwd() + command_colors + ">>>" + text_colors       # os.getcwd() permet d'obtenir la position sous format str 
location=os.getcwd()

if admin=="admin":
    def linux_command():
        return linux_command_admin()
    aide = aide_admin
    gen_parameters = gen_parameters_admin
    autorise = "administrateur"
elif admin=="user":
    def linux_command():
        return linux_command_user()
    aide = aide_user
    gen_parameters = gen_parameters_user
    autorise = "utilisateur"

if devmode=="yes":
    session_log="yes"
    devmode_fr="développeur"
elif devmode=="no":
    session_log="no"
    devmode_fr="non développeur"

# NUS
if os.path.exists("new.txt"):
    os.system(clear)
    print(BANNER)
    print("voici le processus de creation de compte")
    print("définissez votre type de compte : admin/user")
    new_type = input(">>>")
    if new_type == "admin":
        def linux_command():
            return linux_command_admin()
        aide = aide_admin
        gen_parameters = gen_parameters_admin
        autorise = "administrateur"
        with open(os.path.join(user, "system", "admin.txt"), "w") as data_new:
            data_new.write("admin" + "\n")
    else:
        def linux_command():
            return linux_command_user()
        aide = aide_user
        gen_parameters = gen_parameters_user
        autorise = "utilisateur"
        with open(os.path.join(user, "system", "admin.txt"), "w") as data_new:
            data_new.write("user" + "\n")

    print("activer le mode developpeur (système de log activé): o/n")
    new_dev = input(">>>")
    if new_dev=="o":
        session_log="yes"
        devmode_fr="développeur"
        with open(os.path.join(user, "system", "admin.txt"), "a") as data_new:
            data_new.write("yes" + "\n")
    elif new_dev=="n":
        session_log="no"
        devmode_fr="non développeur"
        with open(os.path.join(user, "system", "admin.txt"), "a") as data_new:
            data_new.write("no" + "\n")

    os.system(clear)
    print("bienvenue dans votre session, afin de finir le guide")
    while True:
        print("entrez la commande 'aide' elle affichera un menu contenant toute les commande disponible")
        test_command = input(">>>")
        if test_command == "aide":
            os.system(clear)
            print(BANNER)
            print(aide)
            end_new = input("faite entrer pour entrer dans votre session...")
            os.remove("new.txt")
            break
        else:
            os.system(clear)
            print("recommencez")

else:
    pass


# fonction complex
def save_config():
    with open(os.path.join(user, "system", "save_config.txt"), "w+") as fichier:
        if entry_com == "win":
            entry_save = "win"

        elif entry_com == "lin":
            entry_save = "lin"

        elif entry_com == "defaut":
            entry_save = ">>>"


        if couleur == Fore.YELLOW:
            couleur_save = "jaune"
            
        elif couleur == Fore.GREEN:
            couleur_save = "vert"

        elif couleur == Fore.WHITE:
            couleur_save = "blanc"

        elif couleur == Fore.BLUE:
            couleur_save = "bleu"

        elif couleur == Fore.MAGENTA:
            couleur_save = "magenta"

        elif couleur == Fore.RED:
            couleur_save = "rouge"

        elif couleur == Fore.CYAN:
            couleur_save = "cyan"

        elif couleur == Fore.MAGENTA + Style.DIM:
            couleur_save = "violet"

        elif couleur == Fore.MAGENTA + Style.BRIGHT:
            couleur_save = "rose"

        
        if command_colors == Fore.YELLOW:
            command_colors_save = "jaune"
            
        elif command_colors == Fore.GREEN:
            command_colors_save = "vert"

        elif command_colors == Fore.WHITE:
            command_colors_save = "blanc"

        elif command_colors == Fore.BLUE:
            command_colors_save = "bleu"

        elif command_colors == Fore.MAGENTA:
            command_colors_save = "magenta"

        elif command_colors == Fore.RED:
            command_colors_save = "rouge"

        elif command_colors == Fore.CYAN:
            command_colors_save = "cyan"

        elif command_colors == Fore.MAGENTA + Style.DIM:
            command_colors_save = "violet"

        elif command_colors == Fore.MAGENTA + Style.BRIGHT:
            command_colors_save = "rose"


        if text_colors == Fore.YELLOW:
            text_colors_save = "jaune"
            
        elif text_colors == Fore.GREEN:
            text_colors_save = "vert"

        elif text_colors == Fore.WHITE:
            text_colors_save = "blanc"

        elif text_colors == Fore.BLUE:
            text_colors_save = "bleu"

        elif text_colors == Fore.MAGENTA:
            text_colors_save = "magenta"

        elif text_colors == Fore.RED:
            text_colors_save = "rouge"

        elif text_colors == Fore.CYAN:
            text_colors_save = "cyan"

        elif text_colors == Fore.MAGENTA + Style.DIM:
            text_colors_save = "violet"

        elif text_colors == Fore.MAGENTA + Style.BRIGHT:
            text_colors_save = "rose"

        fichier.write(entry_save+"\n"+couleur_save+"\n"+command_colors_save+"\n"+text_colors_save)
        fichier.close()

# Définir les valeurs des paramètres
command = "created"
control = "created"
color = "created"
command_system = "created"
com_color = "created"
text_color = "created"
password = "created"
admin_user = "created"
chat = "created"
session_part = "none"
new_session = "yes"

def generer_suite_aleatoire(min_value, max_value, longueur_suite):
    # Générer une ou deux lettres aléatoires
    prefixe = ''.join(random.choices(string.ascii_uppercase, k=random.randint(1, 2)))

    # Générer la suite de nombres aléatoires
    suite_numerique = [random.randint(min_value, max_value) for _ in range(longueur_suite)]

    # Combiner le préfixe et la suite numérique
    suite_complete = prefixe + ''.join(map(str, suite_numerique))

    return suite_complete

def create_session_log(session_start_time, **kwargs):
    global session_part  # Déclarer la variable comme globale
    global new_session

    # Créer un répertoire pour stocker les fichiers de journalisation
    log_directory = os.path.join(location, user, "system", "session_logs")
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    min_value = 10
    max_value = 99
    if session_part == "none":
        # Utiliser la nouvelle fonction pour générer la suite aléatoire
        session_part = generer_suite_aleatoire(min_value, max_value, 1)
    else:
        number_random = session_part

    session_number = session_start_time.strftime('%d %m %Y') + f'-{session_part}'
    log_filename = f"session {session_number}.log"
    log_filepath = os.path.join(log_directory, log_filename)

    # Charger les anciennes valeurs
    try:
        with open(log_filepath, "r") as old_log_file:
            old_log_lines = old_log_file.readlines()
        old_values = {}
        for line in old_log_lines[1:]:  # Ignorer la première ligne (Session started)
            parts = line.split(": ")
            if len(parts) == 2:
                variable, value = parts[0].strip(), parts[1].strip()
                old_values[variable] = value
    except FileNotFoundError:
        old_values = {}

    # Comparer les nouvelles valeurs avec les anciennes et sauvegarder uniquement celles qui ont changé
    with open(log_filepath, "a") as log_file:
        if "status" in kwargs:
            status = kwargs.pop("status")
            log_file.write(f"[{session_start_time.strftime('%H:%M:%S')} {session_start_time.strftime('%m/%d/%Y')}] {status}\n")
        else:
            if new_session=="yes":
                log_file.write(f"[{session_start_time.strftime('%H:%M:%S')} {session_start_time.strftime('%m/%d/%Y')}] Session created\n")
                new_session="no"
            else:
                pass

        for variable, value in kwargs.items():
            if variable not in old_values or old_values[variable] != value:
                log_file.write(f"[{session_start_time.strftime('%H:%M:%S')}] {variable}: {value}\n")
                old_values[variable] = value  # Mettre à jour la valeur dans le dictionnaire des anciennes valeurs

    return log_filepath

def create_log(log):
    if session_log == "yes":
        session_start_time = datetime.datetime.now()
        create_session_log(session_start_time, log=log)
    elif session_log == "no":
        pass

def save_local():
    cd=os.getcwd()
    with open(os.path.join(user, "sys_apps", "save_local.txt"), "w+") as local:
        local.write(cd)
        local.close()


def hall():
    os.system(clear)
    print(couleur + BANNER)
    print(couleur + BANNER2)
    if not entry_com == "win":
        print("vous êtes acutellement sur le disque :\n")
        os.system("cd")
    else:
        pass
    print()

def General_Parameters():
    os.system(clear)
    print(couleur + BANNER)
    print(couleur + gen_parameters)
    print()

def Command_Parameters():
    os.system(clear)
    print(couleur + BANNER)
    print(couleur + command_sys)
    print()


def fetch_file(url, filename):
    urllib.request.urlretrieve(url, filename)


def create_user_directory(new_user, password):
    local1 = os.getcwd()
    user_path = os.path.join(local1, new_user)
    print("salut")

    if not os.path.exists(user_path):
        os.mkdir(user_path)

        # Créer le répertoire sys_apps et copier les fichiers de référence
        sys_apps_path = os.path.join(user_path, "sys_apps")
        os.mkdir(sys_apps_path)
        shutil.copy(os.path.join(local1, "test", "sys_apps", "cmd.py"), sys_apps_path)
        print("cmd.py copié avec succès.")
        shutil.copy(os.path.join(local1, "test", "sys_apps", "store.py"), sys_apps_path)
        print("store.py copié avec succès.")
        shutil.copy(os.path.join(local1, "test", "sys_apps", "file_manager.py"), sys_apps_path)
        print("file_manager.py copié avec succès.")
        shutil.copy(os.path.join(local1, "test", "sys_apps", "task_manager.py"), sys_apps_path)
        print("task_manager.py copié avec succès.")
        shutil.copy(os.path.join(local1, "test", "sys_apps", "maj.py"), sys_apps_path)
        print("maj.py copié avec succès.")

        # Créer les répertoires system, programs, games et tool
        os.mkdir(os.path.join(user_path, "system"))
        os.mkdir(os.path.join(user_path, "programs"))
        os.mkdir(os.path.join(user_path, "programs", "games"))
        os.mkdir(os.path.join(user_path, "programs", "tool"))

        # Écrire les informations de connexion dans logs.txt
        with open(os.path.join(user_path, "system", "logs.txt"), "w+") as logs:
            logs.write(password)
        print("Logs.txt créé avec succès.")
        with open(os.path.join(user_path, "system", "admin.txt"), "w+") as admin:
            admin.write("user" + "\n" + "no")
        print("admin.txt créé avec succès.")
        with open(os.path.join(user_path, "system", "save_config.txt"), "w+") as save:
            save.write("lin\n"+ "vert\n"+ "rouge\n"+ "bleu\n")
        print("save_config.txt créé avec succès.")

def check_internet_connection():
    try:
        socket.create_connection(("www.google.com", 443))
        context = ssl.create_default_context()
        with socket.create_connection(("www.google.com", 443)) as sock:
            with context.wrap_socket(sock, server_hostname="www.google.com") as ssock:
                return True, ssock.version()
    except OSError:
        return False, None
    
def verif_version():
    """
    try:
        local=os.getcwd()
        os.chdir(location)
        fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/version.txt", "online_version.txt")
        with open("online_version.txt", "r") as online_data:
            data_online_version=online_data.read()
            version_online=data_online_version.splitlines()
            online_version=version_online[0]
        os.remove("online_version.txt")
    except Exception as e:
        online_version = "0.10.5"
        error_message = f"an error occurred: {e}"
        session_start_time = datetime.datetime.now()
        if devmode=="yes":
            create_session_log(session_start_time, status=error_message)"""

    online_version = "0.10.5"
    if online_version==offline_version:
        print("votre système est à jour")
        print("version possedé : ", Fore.RED, offline_version, couleur)

    else:
        print("votre version n'est pas la meme que celle qui est en ligne")
        print("version possedé : ", Fore.RED, offline_version, couleur)
        print("version en ligne : ", Fore.RED, online_version, couleur)
        print("faite une mise a jour si votre version est inferieur a la version en ligne")
        print("sinon vous bénéficier sûrement d'une version de test")


def list_users():
    # Obtenir la liste des éléments dans le répertoire actuel
    items = os.listdir()

    # Filtrer les dossiers (utilisateurs)
    users = [item for item in items if os.path.isdir(item)]

    return users

def print_users():
    print(couleur)
    os.system(clear)
    print(BANNER)
    print("  ____>>>ES/paramètres/user<<<_____________________________________________")
    print(" | Utilisateurs disponibles:                                               |")
    users = list_users()

    if not users:
        print(" | Aucun utilisateur trouvé.                                               |")
    else:
        for user in users:
            print(f" | - {user}")
    print(" |_________________________________________________________________________|")
    print()

def list_files_with_creation_dates():
    # Get a list of all files in the directory
    logs_data = [f for f in os.listdir(os.path.join(user, "system", "session_logs")) if os.path.isfile(os.path.join(os.path.join(user, "system", "session_logs"), f))]

    # Print header
    print(f"{'fichier': <40}{'date de creation'}")

    # Iterate over each file and print its name and creation date
    for log in logs_data:
        file_path = os.path.join(os.path.join(user, "system", "session_logs"), log)
        creation_time = os.path.getctime(file_path)
        creation_date = datetime.datetime.fromtimestamp(creation_time).strftime('%d-%m-%Y %H:%M:%S')

        print(f"{log: <40}{creation_date}")
    print()

def delete_all_files():
    # Get a list of all files in the directory
    files = [f for f in os.listdir(os.path.join(user, "system", "session_logs")) if os.path.isfile(os.path.join(os.path.join(user, "system", "session_logs"), f))]

    # Delete each file in the directory
    for file in files:
        file_path = os.path.join(os.path.join(user, "system", "session_logs"), file)
        try:
            os.remove(file_path)
            print(f"File '{file}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting file '{file}': {e}")
    print()

def openlogfile(id):
    # Définir le chemin du répertoire des journaux de session
    user_directory = os.path.join(location, user, "system", "session_logs")

    # Utiliser glob pour trouver le fichier correspondant au modèle
    pattern = f"*-{id}.txt"
    nametag = f"{id}.txt"
    matching_files = glob.glob(os.path.join(user_directory, pattern))

    if not matching_files:
        pattern = f"*-{id}.log"
        nametag = f"{id}.log"
        matching_files = glob.glob(os.path.join(user_directory, pattern))

        if not matching_files:
            os.system(clear)
            print(BANNER)
            list_files_with_creation_dates()
            print(f"Aucun fichier correspondant à l'ID '{id}' n'a été trouvé.")
            return

    # Prendre le premier fichier correspondant (ou vous pouvez gérer plusieurs fichiers si nécessaire)
    file_path = matching_files[0]

    # Ouvrir et lire le contenu du fichier
    with open(file_path, 'r') as file:
        content = file.read()
        os.system(clear)
        print(BANNER)
        print(f"Contenu de log de la session avec l'id '{nametag}':\n\n{content}\n")

def disable_windows_defender():
    os.system("powershell -command Set-MpPreference -DisableRealtimeMonitoring 1")

def enable_windows_defender():
    os.system("powershell -command Set-MpPreference -DisableRealtimeMonitoring 0")

def get_ipv4_address():
    # Obtention de l'adresse IPv4
    ip = socket.gethostbyname(socket.gethostname())
    return ip

def get_ipv6_address():
    # Obtention de l'adresse IPv6
    ip = [l for l in ([ip for ip in socket.getaddrinfo(socket.gethostname(), None) if ':' in ip[4][0]]) if l]
    return ip[0][4][0] if ip else None

def get_mac_address():
    # Obtention de l'adresse MAC
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1])
    return mac


def get_system_info():
    system_info = {
        "Système d'exploitation": platform.system(),
        "Nom de la machine": platform.node(),
        "Nom de version": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processeur": platform.processor(),
    }

    print("Informations générales du système:")
    for key, value in system_info.items():
        print(f"{key}: {Fore.RED}{value}{couleur}")
    print("\n")

    print("Informations sur la mémoire:")
    memory_info = psutil.virtual_memory()
    print(f"Mémoire totale: {Fore.RED}{memory_info.total / (1024 ** 3):.2f} GB{couleur}")
    print(f"Mémoire utilisée: {Fore.RED}{memory_info.used / (1024 ** 3):.2f} GB{couleur}")
    print("\n")

    print("Informations sur le processeur:")
    print(f"Modèle du processeur: {Fore.RED}{platform.processor()}{couleur}")
    print(f"Nombre de cœurs physiques: {Fore.RED}{psutil.cpu_count(logical=False)}{couleur}")
    print(f"Nombre de threads logiques: {Fore.RED}{psutil.cpu_count(logical=True)}{couleur}")
    print(f"Utilisation du processeur: {Fore.RED}{psutil.cpu_percent()}%{couleur}")
    print("\n")

    print("Informations sur les disques:")
    disk_info = psutil.disk_partitions()
    for disk in disk_info:
        print(f"Disque {Fore.RED}{disk.device}:{couleur}")
        print(f"  Type: {Fore.RED}{disk.fstype}{couleur}")
        print(f"  Espace total: {Fore.RED}{psutil.disk_usage(disk.device).total / (1024 ** 3):.2f} GB{couleur}")
        print(f"  Espace utilisé: {Fore.RED}{psutil.disk_usage(disk.device).used / (1024 ** 3):.2f} GB{couleur}")
    print("\n")

    # Ajout des informations sur le GPU
    print("Informations sur le GPU:")
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        if gpus:
            for gpu in gpus:
                print(f"GPU: {Fore.RED}{gpu.name}{couleur}")
                print(f"  Utilisation: {Fore.RED}{gpu.load * 100}%{couleur}")
                print(f"  Mémoire disponible: {Fore.RED}{gpu.memoryFree} MB{couleur}")
                print(f"  Température: {Fore.RED}{gpu.temperature} °C{couleur}")
        else:
            print(Fore.RED, "Aucun GPU trouvé.", couleur)
    except ImportError:
        print("Le module GPUtil n'est pas installé. Impossible d'obtenir les informations sur le GPU.")


# variable d'association
ipv4 =get_ipv4_address()
ipv6 =get_ipv6_address()
mac_adress =get_mac_address()
connected, ssl_version = check_internet_connection()

try:
    # initialisation
    if session_log=="yes":
        session_start_time = datetime.datetime.now()
        log_filepath = create_session_log(session_start_time)
    elif session_log=="no":
        pass

    if os.path.exists(os.path.join(user, "system", "save_config.txt")):
        with open(os.path.join(user, "system", "save_config.txt"), "r") as file:
            info = file.read()
            savelist = info.splitlines()
            entry_save = savelist[0]
            couleur_save = savelist[1]
            command_colors_save = savelist[2]
            text_colors_save = savelist[3]

            if entry_save == ">>>":
                def entry():
                    return ">>>"
                entry_com = ">>>"

            elif entry_save == "lin":
                def entry():
                    return linux_command()
                entry_com = "lin"

            elif entry_save == "win":
                def entry():
                    return win_command
                entry_com = "win"

                        
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

                        
            if command_colors_save == "jaune":
                command_colors = Fore.YELLOW
                            
            elif command_colors_save == "vert":
                command_colors = Fore.GREEN

            elif command_colors_save == "blanc":
                command_colors = Fore.WHITE

            elif command_colors_save == "bleu":
                command_colors = Fore.BLUE

            elif command_colors_save == "majenta":
                command_colors = Fore.MAGENTA

            elif command_colors_save == "rouge":
                command_colors = Fore.RED

            elif command_colors_save == "cyan":
                command_colors = Fore.CYAN

            elif command_colors_save == "violet":
                command_colors = Fore.MAGENTA + Style.DIM

            elif command_colors_save == "rose":
                command_colors = Fore.MAGENTA + Style.BRIGHT

            
            if text_colors_save == "jaune":
                text_colors = Fore.YELLOW
                            
            elif text_colors_save == "vert":
                text_colors = Fore.GREEN

            elif text_colors_save == "blanc":
                text_colors = Fore.WHITE

            elif text_colors_save == "bleu":
                text_colors = Fore.BLUE

            elif text_colors_save == "majenta":
                text_colors = Fore.MAGENTA

            elif text_colors_save == "rouge":
                text_colors = Fore.RED

            elif text_colors_save == "cyan":
                text_colors = Fore.CYAN

            elif text_colors_save == "violet":
                text_colors = Fore.MAGENTA + Style.DIM

            elif text_colors_save == "rose":
                text_colors = Fore.MAGENTA + Style.BRIGHT
            
    local1=os.getcwd()
    hall()
    if connected:
        try:
            local=os.getcwd()
            os.chdir(location)
            fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/version.txt", "online_version.txt")
            with open("online_version.txt", "r") as online_data:
                data_online_version=online_data.read()
                version_online=data_online_version.splitlines()
            
                online_version=version_online[0]
            os.remove("online_version.txt")


            if online_version==offline_version:
                print("votre système est à jour")
                print("version possedé : ", Fore.RED, offline_version, couleur)

            else:
                print("mise a jour disponible !")
        except:
            pass
    else:
        pass
    # programme
    while True:
        command =input(entry())
        create_log(command)


        print(couleur)

    # parametre
        if command =="parametre":
            General_Parameters()
            while True:
                control = input(entry())
                create_log(control)
                # couleur general
                if control == "couleur":
                    General_Parameters()
                    print(couleur +"quelle couleur ? vert/jaune/rouge/majenta/cyan/blanc/bleu/violet/rose")
                    color = input(entry())
                    create_log(color)

                    if color == "jaune":
                        couleur = Fore.YELLOW
                        
                    elif color == "vert":
                        couleur = Fore.GREEN

                    elif color == "blanc":
                        couleur = Fore.WHITE

                    elif color == "bleu":
                        couleur = Fore.BLUE

                    elif color == "majenta":
                        couleur = Fore.MAGENTA

                    elif color == "rouge":
                        couleur = Fore.RED

                    elif color == "cyan":
                        couleur = Fore.CYAN

                    elif color == "violet":
                        couleur = Fore.MAGENTA + Style.DIM

                    elif color == "rose":
                        couleur = Fore.MAGENTA + Style.BRIGHT

                    else:
                        print("Cette couleur ne fonctionne pas")
                    General_Parameters()

    # parametre de l'entré des commande
                elif control=="commande":
                    Command_Parameters()
                    while True:
                        command_system = input(entry())
                        create_log(command_system)
        
        # couleur de commande
                        if command_system == "couleur com" or command_system == "cc":
                            while True:
                                Command_Parameters()
                                print(couleur +"quelle couleur ? vert/jaune/rouge/majenta/cyan/blanc/bleu/violet/rose")
                                com_color = input(entry())
                                create_log(com_color)

                                if com_color == "jaune": 
                                    command_colors = Fore.YELLOW
                                    Command_Parameters()
                                    print("couleur sauvegardé")
                                    break

                                elif com_color == "vert":
                                    command_colors = Fore.GREEN
                                    print("couleur sauvegardé")
                                    break

                                elif com_color == "blanc":
                                    command_colors = Fore.WHITE
                                    Command_Parameters()
                                    print("couleur sauvegardé")
                                    break

                                elif com_color == "bleu":
                                    command_colors = Fore.BLUE
                                    Command_Parameters()
                                    print("couleur sauvegardé")
                                    break

                                elif com_color == "majenta":
                                    command_colors = Fore.MAGENTA
                                    Command_Parameters()
                                    print("couleur sauvegardé")
                                    break

                                elif com_color == "rouge":
                                    command_colors = Fore.RED
                                    Command_Parameters()
                                    print("couleur sauvegardé")
                                    break

                                elif com_color == "cyan":
                                    command_colors = Fore.CYAN
                                    Command_Parameters()
                                    print("couleur sauvegardé")
                                    break
                                    
                                elif com_color == "violet":
                                    command_colors = Fore.MAGENTA + Style.DIM
                                    Command_Parameters()
                                    print("couleur sauvegardé")
                                    break

                                elif com_color == "rose":
                                    command_colors = Fore.MAGENTA + Style.BRIGHT
                                    Command_Parameters()
                                    print("couleur sauvegardé")
                                    break
                                
                                else:
                                    print("Cette couleur ne fonctionne pas")

                            
                        elif command_system == "couleur text" or command_system == "ct":
                            while True:
                                Command_Parameters()
                                print(couleur +"quelle couleur ? vert/jaune/rouge/majenta/cyan/blanc/bleu/violet/rose")
                                text_color = input(entry())
                                create_log(text_color)

                                if text_color == "jaune": 
                                    text_colors = Fore.YELLOW
                                    Command_Parameters()
                                    print("couleur sauvegardé")
                                    break

                                elif text_color == "vert":
                                    print("couleur sauvegardé")
                                    text_colors = Fore.GREEN
                                    print("couleur sauvegardé")
                                    break

                                elif text_color == "blanc":
                                    text_colors = Fore.WHITE
                                    Command_Parameters()
                                    print("couleur sauvegardé")
                                    break

                                elif text_color == "bleu":
                                    text_colors = Fore.BLUE
                                    Command_Parameters()
                                    print("couleur sauvegardé")
                                    break

                                elif text_color == "majenta":
                                    text_colors = Fore.MAGENTA
                                    Command_Parameters()
                                    print("couleur sauvegardé")
                                    break

                                elif text_color == "rouge":
                                    text_colors = Fore.RED
                                    Command_Parameters()
                                    print("couleur sauvegardé")
                                    break

                                elif text_color == "cyan":
                                    text_colors = Fore.CYAN
                                    Command_Parameters()
                                    print("couleur sauvegardé")
                                    break
                                    
                                elif text_color == "violet":
                                    text_colors = Fore.MAGENTA + Style.DIM
                                    Command_Parameters()
                                    print("couleur sauvegardé")
                                    break

                                elif text_color == "rose":
                                    text_colors = Fore.MAGENTA + Style.BRIGHT
                                    Command_Parameters()
                                    print("couleur sauvegardé")
                                    break
                                
                                else:
                                    print("Cette couleur ne fonctionne pas")

        # style visuel commande
                        elif command_system=="linux":
                            def entry():
                                return linux_command()
                            entry_com = "lin"

                        elif command_system=="win":
                            def entry():
                                return win_command
                            entry_com = "win"

                        elif command_system=="defaut":
                            def entry():
                                return ">>> "
                            entry_com = "defaut"

            # retour au parametre généraux
                        elif command_system=="close":
                            General_Parameters()
                            break

                        else:
                            print("veuillez recommencer")
                            time.sleep(2)
                        Command_Parameters()

            # admin info
                elif control=="admin":
                    General_Parameters()
                    with open(os.path.join(user, "system","logs.txt"), "r") as file:
                        info = file.read()
                        password_data = info.splitlines()
                        password_save = password_data[0]
                        pass_save=password_save

                    General_Parameters()
                    print("entrez votre mot de passe")
                    password=input(entry())
                    create_log(password)
                    General_Parameters()
                    if password==pass_save:
                        if admin=="admin":
                            admin="user"
                            def linux_command():
                                return linux_command_user()
                            if entry()==linux_command():
                                def entry():
                                    return linux_command()
                            aide = aide_user
                            gen_parameters = gen_parameters_user
                            autorise = "utilisateur"
                            print("autorisation modifié  en utilisateur")
                            print("vous devez vous reconnecter")
                        elif admin=="user":
                            admin="admin"
                            def linux_command():
                                return linux_command_admin()
                            if entry()==linux_command():
                                def entry():
                                    return linux_command()
                            aide = aide_admin
                            gen_parameters = gen_parameters_admin
                            autorise = "administrateur"
                            print("autorisation modifié en administrateur")
                            print("vous devez vous reconnecter")
                        else:
                            print("impossible d'identifier les authorisation de votre compte")
                        with open(os.path.join(user, "system", "admin.txt"), "w") as admin_modif:
                            admin_modif.write(admin+"\n"+devmode)
                    else:
                        print("erreur de mot de passe")

                elif control=="dev":
                    General_Parameters()
                    if devmode=="yes":
                        devmode="no"
                        devmode_fr="non développeur"
                    elif devmode=="no":
                        devmode="yes"
                        devmode_fr="développeur"
                    else:
                        print("impossible d'identifier les authorisation de votre compte")
                    with open(os.path.join(user, "system", "admin.txt"), "w") as dev_modif:
                        dev_modif.write(admin+"\n"+devmode)


                elif control=="user":
                    print_users()
                    while True:
                        admin_user=input(entry())
                        create_log(admin_user)

                        if admin_user.startswith("rm") and admin=="admin":
                            print_users()
                            _, path = admin_user.split(" ", 1)
                            path = path.strip()

                            if path=="test":
                                print(Fore.LIGHTRED_EX + "impossible de supprimer un dossier système")
                                print(couleur)
                            else:
                                try:
                                    shutil.rmtree(path)
                                    print_users()
                                    print(f"{path} supprimé")
                                except FileNotFoundError:
                                    print(f"L'utilisateur '{path}' n'existe pas.")
                                except Exception as e:
                                    print(f"Erreur lors de la suppression de {e}")

                        elif admin_user.startswith("cr"):
                            print_users()
                            _, path = admin_user.split(" ", 1)
                            new_user = path.strip()

                            if new_user=="test":
                                print(Fore.LIGHTRED_EX + "impossible de créer au même nom qu'un fichier système un dossier système")
                                print(couleur)
                            else:
                                print("entrez un mot de passe")
                                password=input(entry())
                                create_log(password)
                                print(couleur)
                                try:
                                    create_user_directory(new_user, password)
                                except Exception as e:
                                    print(e)
                                print_users()

                        elif admin_user=="clear":
                            print_users()

                        elif admin_user=="close":
                            General_Parameters()
                            break
                        else:
                            print_users()
                            print("recommencer")

                elif control=="view log"and devmode=="yes":
                    print(couleur)
                    os.system(clear)
                    print(BANNER)
                    print("open (id 'ex : NE44') : ouvre le fichier log ayant cette id")
                    print("reset : supprime tout les fichier log")
                    print("clear : recharge l'interface")
                    print("close : retourne au paramètres")
                    print()
                    list_files_with_creation_dates()

                    while True:
                        view_log=input(entry())
                        create_log(view_log)
                        print(couleur)

                        if view_log=="close":
                            General_Parameters()
                            break
                        
                        elif view_log=="reset":
                            os.system(clear)
                            print(BANNER)
                            delete_all_files()
                            list_files_with_creation_dates()

                        elif view_log=="clear":
                            os.system(clear)
                            print(BANNER)
                            list_files_with_creation_dates()

                        elif view_log.startswith("open"):
                            _, path = view_log.split(" ", 1)
                            path = path.strip()

                            if path==path:
                                openlogfile(path)

                        else:
                            print("recommencer")

            # info systeme
                elif control=="info":
                    General_Parameters()
                    print(couleur + new)
                    print("mise a jour :")
                    if connected:
                        verif_version()
                    else:
                        print(Fore.RED, "impossible de verifier si votre version est à jour, verifier si vous etes connecté")
                        print(couleur)

                elif control=="maj":
                    hall()
                    if connected:
                        local=os.getcwd()
                        os.chdir(local1)
                        os.chdir(os.path.join(user, "sys_apps"))
                        os.system("python maj.py")
                        os.chdir(local)
                        hall()
                        print("mise ajour effectué vous pouvez redémarrer ES")
                    else:
                        print("vous n'étes pas connecté")

            # changer le mot de passe
                elif control=="logs":
                    General_Parameters()
                    print("nouveau mot de passe")
                    password=input(entry())
                    create_log(password)
                    with open(os.path.join(user, "system", "logs.txt"), "w+") as logs:
                        logs.write(password)
                        logs.close()
                    General_Parameters()

            # fermeture des parametre
                elif control=="close":
                    hall()
                    save_config()
                    break

        # erreur
                else:
                    print("veuillez recommencer")
                    time.sleep(2)
                    General_Parameters()

    # ip info
        elif command =="IPinfo":
            hall()
            print("ip :\n\n ipv4 : ", ipv4, "\n ipv6 : ", ipv6)

    # mac info
        elif command =="MACinfo":
            hall()
            print("adresse MAC : \n\n", mac_adress)
            print()

            # os info
        elif command =="os":
            hall()
            system_name = os.name
                    
            if system_name == "posix":
                print("système d'exploitation Unix")
                print("cette os correspond a toute les version de linux et macOS")
                unix_version = platform.uname()
                print("Informations sur la version d'Unix :", unix_version)
                    
            elif system_name == "nt":
                print("système d'exploitation Windows")
                windows_version = platform.version()
                print("Version de Windows :", windows_version)
                    
            else:
                print("Système d'exploitation non reconnu.")

            # systeme chat
        elif command =="chat":
            hall()
            while True:
                    
                chat = input(couleur + "que voulez vous dire ? ")
                create_log(chat)


                if chat == chat:
                    hall()
                    print(couleur + chat)

                if chat =="clear":
                    hall()

                if chat =="exit":
                    hall()
                    break

            # info sur le systeme
        elif command =="info sys":
            hall()
            print(f"connecté en tant que '{Fore.RED}{user}{couleur}'")
            print(f"vous avez un compte {Fore.RED}{autorise}{couleur}")
            print(f"vous avez un compte {Fore.RED}{devmode_fr}{couleur}")
            print()
            get_system_info()
            print()
            print("Informations sur la batterie:")
            battery_details()
            print()

            # verification d'internet
        elif command =="internet":
            hall()
            if connected:
                print("Le PC est connecté à Internet. 🌐")
                if ssl_version:
                    print("La connexion est sécurisée avec la version:", ssl_version)
                else:
                    print("La connexion n'est pas sécurisée. 🌐❌")
            else:
                print("Le PC n'est pas connecté à Internet. ❌")

            # windows defender
        elif command=="defend no":
            hall()
            disable_windows_defender()

        elif command=="defend yes":
            hall()
            enable_windows_defender()

            # help
        elif command =="aide":
            os.system(clear)
            print(couleur + BANNER)
            print(couleur + aide)

            # clear
        elif command =="clear":
            hall()

            # systeme d'apps
        elif command =="apps":
            os.system(clear)
            print(BANNER)
            print(apps)

        # extinction systeme
        elif command =="close":
            save_config()
            os.system(clear)
            session_closed_time = datetime.datetime.now()
            break

        elif command =="powerpoint":
            if os.path.exists(os.path.join("C:", "Program Files", "Microsoft Office", "root", "Office16")):
                hall()
                local=os.getcwd()
                os.chdir("C:")
                os.chdir(os.path.join("C:", "Program Files", "Microsoft Office", "root", "Office16"))
                os.system("POWERPNT.EXE")
                os.chdir(local)
                hall()

        elif command =="word":
            if os.path.exists(os.path.join("C:", "Program Files", "Microsoft Office", "root", "Office16")):
                hall()
                local=os.getcwd()
                os.chdir("C:")
                os.chdir(os.path.join("C:", "Program Files", "Microsoft Office", "root", "Office16"))
                os.system("WINWORD.EXE")
                os.chdir(local)
                hall()

        elif command =="excel":
            if os.path.exists(os.path.join("C:", "Program Files", "Microsoft Office", "root", "Office16")):
                hall()
                local=os.getcwd()
                os.chdir("C:")
                os.chdir(os.path.join("C:", "Program Files", "Microsoft Office", "root", "Office16"))
                os.system("EXCEL.EXE")
                os.chdir(local)
                hall()

        elif command =="educadhoc":
            if os.path.exists(os.path.join("E:", "livres", "math", "educadhoc")):
                hall()
                local=os.getcwd()
                os.chdir("E:")
                os.chdir(os.path.join("E:", "livres", "math", "educadhoc"))
                os.system("educadhoc.exe")
                os.chdir(local)
                hall()

        elif command =="cmd":
            hall()
            save_local()
            local=os.getcwd()
            os.chdir(location)
            os.chdir(os.path.join(user, "sys_apps"))
            os.system("python cmd.py")
            os.chdir(local)
            hall()

        elif command =="file manager" or command=="fm":
            hall()
            save_local()
            local=os.getcwd()
            os.chdir(location)
            os.chdir(os.path.join(user, "sys_apps"))
            os.system("python file_manager.py")
            os.chdir(local)
            hall()

        elif command =="task manager" or command=="tm":
            hall()
            save_local()
            local=os.getcwd()
            os.chdir(location)
            os.chdir(os.path.join(user, "sys_apps"))
            os.system("python task_manager.py")
            os.chdir(local)
            hall()

        elif command =="toolbox":
            hall()
            local=os.getcwd()
            os.chdir(location)
            os.chdir(os.path.join(user, "programs", "tool", "toolbox"))
            if os.path.exists(os.path.join(user, "programs", "tool", "toolbox", "toolbox_win.py")):
                os.system("python toolbox_win.py")
            else:
                if os.path.exists(os.path.join(user, "programs", "tool", "toolbox", "toolbox_setup.py")):
                    os.system("python toolbox_setup.py")
                else:
                    print("toolbox n'est pas installé")
            os.chdir(local)
            hall()

        elif command =="life evol":
            hall()
            local=os.getcwd()
            os.chdir(location)
            os.chdir(os.path.join(user, "programs", "games"))
            if os.path.exists(os.path.join(user, "programs", "games", "life_evol.py")):
                os.system("python life_evol.py")
            else:
                if os.path.exists(os.path.join(user, "programs", "games", "life_evol_setup.py")):
                    os.system("python life_evol_setup.py")
                else:
                    print("life evol n'est pas installé")
            os.chdir(local)
            hall()

        elif command =="nuclear ingenior" or command =="ni":
            hall()
            local=os.getcwd()
            os.chdir(location)
            os.chdir(os.path.join(user, "programs", "games", "nuclear_ingenior.py"))
            os.system("python nuclear_ingenior.py")
            os.chdir(local)
            hall()

        elif command =="store":
            save_local()
            hall()
            local=os.getcwd()
            os.chdir(location)
            os.chdir(os.path.join(user, "sys_apps"))
            os.system("python store.py")
            os.chdir(local)
            hall()

            # credits
        elif command =="credits":
            hall()
            print(couleur + cred)
            print("")

            # save des réglages
        elif command =="save":
            save_config()
            hall()
            print("paramètre sauvegardé")

        elif command =="load":
            os.chdir(local1)
            if os.path.exists(os.path.join(user, "system", "save_config.txt")):
                with open(os.path.join(user, "system", "save_config.txt"), "r") as file:
                    info = file.read()
                    savelist = info.splitlines()
                    entry_save = savelist[0]
                    couleur_save = savelist[1]
                    command_colors_save = savelist[2]
                    text_colors_save = savelist[3]

                    if entry_save == ">>>":
                        def entry():
                            return ">>>"

                    elif entry_save == "lin":
                        def entry():
                            return linux_command()

                    elif entry_save == "win":
                        def entry():
                            return win_command

                                
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

                                
                    if command_colors_save == "jaune":
                        command_colors = Fore.YELLOW
                                    
                    elif command_colors_save == "vert":
                        command_colors = Fore.GREEN

                    elif command_colors_save == "blanc":
                        command_colors = Fore.WHITE

                    elif command_colors_save == "bleu":
                        command_colors = Fore.BLUE

                    elif command_colors_save == "majenta":
                        command_colors = Fore.MAGENTA

                    elif command_colors_save == "rouge":
                        command_colors = Fore.RED

                    elif command_colors_save == "cyan":
                        command_colors = Fore.CYAN

                    elif command_colors_save == "violet":
                        command_colors = Fore.MAGENTA + Style.DIM

                    elif command_colors_save == "rose":
                        command_colors = Fore.MAGENTA + Style.BRIGHT

                    
                    if text_colors_save == "jaune":
                        text_colors = Fore.YELLOW
                                    
                    elif text_colors_save == "vert":
                        text_colors = Fore.GREEN

                    elif text_colors_save == "blanc":
                        text_colors = Fore.WHITE

                    elif text_colors_save == "bleu":
                        text_colors = Fore.BLUE

                    elif text_colors_save == "majenta":
                        text_colors = Fore.MAGENTA

                    elif text_colors_save == "rouge":
                        text_colors = Fore.RED

                    elif text_colors_save == "cyan":
                        text_colors = Fore.CYAN

                    elif text_colors_save == "violet":
                        text_colors = Fore.MAGENTA + Style.DIM

                    elif text_colors_save == "rose":
                        text_colors = Fore.MAGENTA + Style.BRIGHT
                        
                hall()
                print("paramètre chargé")
            else:
                hall()
                print("vous n'avez aucune sauvegarde")

            # déplacment dans le pc
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
                print(f"Le répertoire '{path}' n'existe pas.")
            except Exception as e:
                print(f"Erreur lors du changement de répertoire : {e}")

            # hostname
        elif command =="hostname" or command =="hn":
            hall()
            print("nom de la machine : ", Fore.RED, host, couleur)

        elif command =="battery" or command =="bat":
            hall()
            battery_details()
    
            # commande de cmd
        else:
            hall()
            print(command_colors + "\n>>> " + text_colors + command + "\n")
            os.system(command)

except Exception as e:
    # En cas d'erreur, enregistrez un message d'erreur dans le fichier de log
    error_message = f"session closed because an error occurred: {e}"
    session_start_time = datetime.datetime.now()
    if devmode=="yes":
        create_session_log(session_start_time, status=error_message)
        print(error_message)

session_start_time = datetime.datetime.now()
if devmode=="yes":
    create_session_log(session_start_time, status="Session closed")