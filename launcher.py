from colorama import *
import hashlib
import os
import time
import getpass
import shutil
import platform

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

system = platform.system()
if system == "Windows":
    clear = "cls"
elif system == "Linux":
    clear = "clear"
else:
    clear = "erreur"

couleur = Fore.GREEN
command_colors = Fore.RED
local = os.getcwd()

def hall():
    os.system(clear)
    print(couleur + BANNER)        

def create_user_directory(user, password):
    local1 = os.getcwd()
    user_path = os.path.join(local1, user)

    if not os.path.exists(user_path):
        with open("new.txt", "w+"):
            pass

        os.mkdir(user_path)


        # Créer les répertoires system, programs, games et tool
        os.mkdir(os.path.join(user_path, "system"))

        # Écrire les informations de connexion dans logs.txt
        with open(os.path.join(user_path, "system", "logs.txt"), "w+") as logs:
            password_hached = hash_password(password)
            logs.write(password_hached)
        print("Logs.txt créé avec succès.")
        with open(os.path.join(user_path, "system", "admin.txt"), "w+") as admin:
            admin.write("user" + "\n" + "no")
        print("admin.txt créé avec succès.")
        with open(os.path.join(user_path, "system", "save_config.txt"), "w+") as save:
            save.write("lin\n"+ "vert\n"+ "rouge\n"+ "bleu\n")
        print("save_config.txt créé avec succès.")
        os.system("python ES.py")

def list_users():
    # Obtenir la liste des éléments dans le répertoire actuel
    items = os.listdir()

    # Filtrer les dossiers (utilisateurs)
    users = [item for item in items if os.path.isdir(item)]

    return users

def print_users():
    print("Utilisateurs disponibles:")
    users = list_users()

    for user in users:
        if user == "test":
            pass
        else:
            print(f"- {user}")

def launch():
    load = 1
    if load != 5:
        load =+ 1
        os.system(clear)
        print("chargement")
        time.sleep(0.5)
        os.system(clear)
        print("chargement.")
        time.sleep(0.5)
        os.system(clear)
        print("chargement..")
        time.sleep(0.5)
        os.system(clear)
        print("chargement...")
        time.sleep(0.5)
    load = -4

def loading():
    launch()
    os.system(clear)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_hash, provided_password):
    return stored_hash == hash_password(provided_password)

def close():
    load3 = 1
    if load3 != 5:
        load =+ 1
        os.system(clear)
        print("fermeture")
        time.sleep(0.5)
        os.system(clear)
        print("fermeture.")
        time.sleep(0.5)
        os.system(clear)
        print("fermeture..")
        time.sleep(0.5)
        os.system(clear)
        print("fermeture...")
        time.sleep(0.5)
    load3 = -4

def closing():
    close()
    print(Style.RESET_ALL)
    close()
    os.system(clear)

loading()
with open("etat.dta", "w+") as dta:
    dta.write("launching")
print(couleur)

hall()
while True:
    with open("etat.dta", "r") as dta:
        data = dta.read()
    if data == "exit":
        break

    os.chdir(local)
    print("entrez votre nom d'utilisateur ou close pour quitter")
    print("si l'utilisateur entré n'existe pas il en créera un nouveau")
    print("pour supprimer un utilisateur faite rm puis son nom")
    print_users()
    print("- i : mode invité")
    print()
    user = input(command_colors + ">>>")
    print(couleur)
    os.system(clear)
    if user == "close":
        break

    with open("user.dta", "w+") as data:
            userdata=user
            data.write(userdata)
    
    if user == "invite" or user == "i":
        hall()
        password = "invite"
        create_user_directory(user, password)
        os.chdir(user)
        os.system("python ES.py")
        os.chdir("..")
        shutil.rmtree(user)
        hall()

    elif user.startswith("rm"):
        hall()
        _, path = user.split(" ", 1)
        path = path.strip()

        if path=="test":
            print(Fore.LIGHTRED_EX + "impossible de supprimer un dossier système")
            print(couleur)
        else:
            try:
                shutil.rmtree(path)
                print(f"{path} supprimé")
                hall()
            except FileNotFoundError:
                print(f"L'utilisateur '{path}' n'existe pas.")
            except Exception as e:
                print(f"Erreur lors de la suppression de {e}")

    else:
        hall()
        print("entrez votre mot de passe")
        print()
        password = getpass.getpass(command_colors + ">>>")
        print(couleur)
        create_user_directory(user, password)
        with open(os.path.join(user, "system","logs.txt"), "r") as file:
            info = file.read()
            password_data = info.splitlines()
            pass_save = password_data[0]
            
        
        if verify_password(pass_save, password):
            os.system("python ES.py")
            hall()
        else:
            hall()
            print(Fore.RED + "mauvais mot de passe")
            print(couleur)
closing()
os.system(clear)
print("au revoir !")
time.sleep(2)
os.system(clear)