import os
import ssl
import socket
import platform
import urllib.request
import hashlib

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
  ┌─┐┌─┐┌┬┐┬ ┬┌─┐
  └─┐├┤  │ │ │├─┘
  └─┘└─┘ ┴ └─┘┴  
 """)

system = platform.system()
if system=="Windows":
    clear="cls"
elif system =="Linux":
    clear ="clear"
else:
    clear ="erreur"

Help = ("""
 installer emergency system : 
 suivez les consignes et tout se passera bien
 toolbox s'installe au meme emplacement que ES_setup
 avec tout les requierments

""")

def fetch_file(url, filename):
    urllib.request.urlretrieve(url, filename)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_internet_connection():
    try:
        socket.create_connection(("www.google.com", 443))
        context = ssl.create_default_context()
        with socket.create_connection(("www.google.com", 443)) as sock:
            with context.wrap_socket(sock, server_hostname="www.google.com") as ssock:
                return True, ssock.version()
    except OSError:
        return False, None
connected, ssl_version = check_internet_connection()

def install():
    locat = os.getcwd()

    fetch_file("https://raw.githubusercontent.com/1ventorusdev/ES/main/launcher.py", "launcher.py")
    fetch_file("https://raw.githubusercontent.com/1ventorusdev/ES/main/ES.py", "ES.py")
    fetch_file("https://raw.githubusercontent.com/1ventorusdev/ES/main/version.ver", "version.ver")
    os.system("pip install colorama")
    os.system("pip install psutil")
    os.system("pip install wmi")
    os.mkdir("test")
    sys_apps_dir = os.path.join("test", "sys_apps")
    os.mkdir(sys_apps_dir)
    os.chdir(sys_apps_dir)
    fetch_file("https://raw.githubusercontent.com/1ventorusdev/ES/main/test/sys_apps/cmd.py", "cmd.py")
    fetch_file("https://raw.githubusercontent.com/1ventorusdev/ES/main/test/sys_apps/store.py", "store.py")
    fetch_file("https://raw.githubusercontent.com/1ventorusdev/ES/main/test/sys_apps/file_manager.py", "file_manager.py")
    fetch_file("https://raw.githubusercontent.com/1ventorusdev/ES/main/test/sys_apps/task_manager.py", "task_manager.py")
    fetch_file("https://raw.githubusercontent.com/1ventorusdev/ES/main/test/sys_apps/maj.py", "maj.py")
    os.chdir(os.path.join(locat, "test"))
    system_dir = os.path.join("system")
    os.mkdir(system_dir)
    os.chdir(system_dir)
    with open("logs.txt", "w+") as data:
        data.write(hash_password("test"))

    with open("admin.txt", "w+") as data:
        data.write("admin"+"\n"+"yes")

    with open("save_config.txt", "w+") as save:
            save.write("lin\n"+ "cyan\n"+ "cyan\n"+ "bleu\n")

    os.chdir(os.path.join(locat, "test"))
    programs_dir = os.path.join("programs")
    os.mkdir(programs_dir)
    games_dir = os.path.join(programs_dir, "games")
    os.mkdir(games_dir)
    tool_dir = os.path.join(programs_dir, "tool")
    os.mkdir(tool_dir)
    os.chdir(locat)
    print("installation terminé")
    print("vous pouvez fermer l'installateur et lancer ES a l'endroit où vous l'avez enregistré dans le dossier ES")



def hall():
    os.system(clear)
    print(BANNER)
    print(Help)
    print("lancer l'installation de ES o/n ou y/n ou close pour fermer l'installateur")

hall()
while True:
    launch=input(">>>")

    if launch=="o" or launch=="y":
        hall()
        while True:
            location = input("entrez le chemin souhaitez d'installation (defaut : à cette position dans le dossier ES): ")
            if location == "":
                os.mkdir("ES")
                os.chdir("ES")
                break
            else:
                try:
                    os.chdir(location)
                    os.mkdir("ES")
                    os.chdir("ES")
                    break
                except FileNotFoundError:
                    print("il semble que ce chemin d'acces n'existe pas")
        if not os.path.exists("test"):
            if connected:
                install()
            else:
                print("vous n'étes pas connecté")
        else:
            print("vous posséder déjà ES")
    elif launch=="n" or launch=="close":
        os.system(clear)
        break
