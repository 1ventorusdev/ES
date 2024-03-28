#!/usr/bin/env python

import os
import ssl
import socket
import platform
import urllib.request

BANNER=("""
'########::'######::::::'######::'########::'#######::'########::'########:
 ##.....::'##... ##::::'##... ##:... ##..::'##.... ##: ##.... ##: ##.....::
 ##::::::: ##:::..::::: ##:::..::::: ##:::: ##:::: ##: ##:::: ##: ##:::::::
 ######:::. ######:::::. ######::::: ##:::: ##:::: ##: ########:: ######:::
 ##...:::::..... ##:::::..... ##:::: ##:::: ##:::: ##: ##.. ##::: ##...::::
 ##:::::::'##::: ##::::'##::: ##:::: ##:::: ##:::: ##: ##::. ##:: ##:::::::
 ########:. ######:::::. ######::::: ##::::. #######:: ##:::. ##: ########:
........:::......:::::::......::::::..::::::.......:::..:::::..::........::
""")

APPS=("""
  ____>>>ES/apps<<<________________________________________________________
 |                                    |                                    |
 | outils :                           | microsoft :                        |
 |      -toolbox                      |     -                              |
 |      -                             |     -                              |
 |      -                             |     -                              |
 |      -                             |     -                              |
 |                                    |                                    |
 | apps :                             | jeux :                             |
 |      -                             |      -life evol                    |
 |      -                             |      -nuclear ingenior             |
 |      -                             |      -                             |
 |      -                             |      -                             |
 |      -                             |      -                             |
 |      -                             |      -                             |
 |      -                             |      -                             |
 |      -                             |      -                             |
 |_________________________________________________________________________|
""")

system = platform.system()
if system=="Windows":
    clear="cls"
elif system =="Linux":
    clear ="clear"
else:
    clear ="erreur"

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

def hall():
    os.system(clear)
    print(BANNER)
    if connected:
        print("Le PC est connecté à Internet. 🌐")
        if ssl_version:
            print("La connexion est sécurisée avec la version:", ssl_version)
        else:
            print("La connexion n'est pas sécurisée. 🌐❌")
        print(APPS)
    else:
        print("Le PC n'est pas connecté à Internet. ❌")
        print("connectez vous et relancer store")

def fetch_file(url, filename):
    urllib.request.urlretrieve(url, filename)

with open("save_local.txt", "r") as local:
    locat=local.read()
    loc=locat.splitlines()
    cd=loc[0]



hall()
while True:
    app=input(">>>")

    if app=="toolbox":
        os.chdir(cd)
        hall()
        if os.path.exists(r"programs\tool\toolbox\toolbox_setup.py"):
            print("vous possédez déja l'application")
        else:
            if connected: 
                os.chdir(r"programs\tool")   
                fetch_file("https://raw.githubusercontent.com/1ventorus/toolbox/main/toolbox_setup.py", "toolbox_setup.py")
            else:
                print("Le PC n'est pas connecté à Internet. ❌")

    elif app=="life evol":
        os.chdir(cd)
        hall()
        if os.path.exists(r"programs\games\life_evol_setup.py"):
            print("vous possédez déja l'application")
        else:
            if connected: 
                os.chdir(r"programs\games")       
                fetch_file("https://raw.githubusercontent.com/1ventorus/life_evol/main/life_evol_setup.py", "life_evol_setup.py")
            else:
                print("Le PC n'est pas connecté à Internet. ❌")

    elif app=="nuclear ingenior":
        os.chdir(cd)
        hall()
        if os.path.exists(r"programs\games\nuclear_ingenior_setup.py"):
            print("vous possédez déja l'application")
        else:
            if connected: 
                os.chdir(r"programs\games")   
                fetch_file("https://raw.githubusercontent.com/1ventorus/life_evol/main/nuclear_setup.py", "life_evol_setup.py")
            else:
                print("Le PC n'est pas connecté à Internet. ❌")

    elif app=="close":
        break

    