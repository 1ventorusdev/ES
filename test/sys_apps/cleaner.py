#!/usr/bin/env python
from colorama import*
import os
import random
import string
import datetime
import shutil
import psutil

storage_used_bar_color=Fore.GREEN + Style.BRIGHT
storage_no_used_bar_color=Fore.RED + Style.BRIGHT
font_color=Style.RESET_ALL

def generer_suite_aleatoire(min_value, max_value, longueur_suite):
    # Générer une ou deux lettres aléatoires
    prefixe = ''.join(random.choices(string.ascii_uppercase, k=random.randint(1, 2)))

    # Générer la suite de nombres aléatoires
    suite_numerique = [random.randint(min_value, max_value) for _ in range(longueur_suite)]

    # Combiner le préfixe et la suite numérique
    suite_complete = prefixe + ''.join(map(str, suite_numerique))

    return suite_complete

def filenames(session_start_time):
    global filename
    random_nbr = generer_suite_aleatoire(1, 10, 4)
    filename = session_start_time.strftime('%d %m %Y ') + random_nbr + ".txt"

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

def print_storage_bar():
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


try:
    os.system("cls")
    print_storage_bar()
    while True:
        print("lancer le nettoyage disque o/n")
        cleaning=input(">>>")

        if cleaning=="o":
            os.system("cleanmgr /sagerun:65535")
            os.system("del /S /F /Q %temp%")
            os.system(r"del /S /F /Q %windir%\Temp")
            os.system("cls")
            print_storage_bar()
            print(f"{Fore.CYAN}! nettoyage effectué !{font_color}")
        elif cleaning=="n":
            os.system("cls")
            break

    os.system("exit")

except Exception as e:
    error_message = f"session closed because an error occurred: {str(e)}"
    print(e)
    while True:
        if os.path.exists("cleaner_report_bug"):
            session_start_time = datetime.datetime.now()
            filenames(session_start_time)
            with open(os.path.join("cleaner_report_bug", filename), "w+") as bug:
                bug.write(error_message)
            break
        else:
            os.mkdir("cleaner_report_bug")
    os.system("exit")