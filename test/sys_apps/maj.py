import os
import ssl
import socket
import urllib.request

def parentdir():
    try:
        parent_directory = os.path.normpath(os.path.join(os.getcwd(), ".."))
        os.chdir(parent_directory)
    except Exception as e:
        print(f"Erreur lors du changement de répertoire : {e}")

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

def fetch_file(url, filename):
    urllib.request.urlretrieve(url, filename)

def list_users():
    locat=os.getcwd()
    os.chdir("user")
    items = os.listdir()
    users = [item for item in items if os.path.isdir(item)]

    os.chdir(locat)
    return users

def maj():
   
    parentdir()
    parentdir()
    os.remove("launcher.py")
    os.remove("ES.py")
    if os.path.exists("ES_setup.py"):
        os.remove("ES_setup.py")
    os.remove("version.ver")
    os.chdir("test")
    os.chdir("sys_apps")
    os.remove("cmd.py")
    os.remove("store.py")
    os.remove("file_manager.py")
    os.remove("task_manager.py")
    os.remove("maj.py")
    if os.path.exists("maj_suite.py"):
        os.remove("maj_suite.py")
    fetch_file("https://raw.githubusercontent.com/1ventorusdev/ES/main/test/sys_apps/maj_suite.py", "maj_suite.py")

if connected:
    maj()
    os.system("python maj_suite.py")
else:
    print("vous n'étes pas connecté")