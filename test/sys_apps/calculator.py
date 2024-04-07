#!/usr/bin/env python

import os
import platform

BANNER=("""
              ______            ______      _____              
 ____________ ___  /_________  ____  /_____ __  /______________
 _  ___/  __ `/_  /_  ___/  / / /_  /_  __ `/  __/  __ \_  ___/
 / /__ / /_/ /_  / / /__ / /_/ /_  / / /_/ // /_ / /_/ /  /    
 \___/ \__,_/ /_/  \___/ \__,_/ /_/  \__,_/ \__/ \____//_/  
 """)

Help=("""
entrez un calcul tels que :
 x : *
 - : -
 + : +
 puissance : ** x (x le nombre de la puissance)
 division : /

 """)

system = platform.system()
if system=="Windows":
    clear="cls"
elif system =="Linux":
    clear ="clear"
else:
    clear ="erreur"

def hall():
    os.system(clear)
    print(BANNER)
    print(Help)

hall()
while True:
    calcul=input(">>>")

    if calcul=="close":    
        break
    else: 
        hall() 
        calcul_base = calcul  
        calcul = calcul.split()
        if calcul[1] == "+":
            result = int(calcul[0]) + int(calcul[2])
        elif calcul[1] == "*":
            result = int(calcul[0]) * int(calcul[2])
        elif calcul[1] == "-":
            result = int(calcul[0]) - int(calcul[2])
        elif calcul[1] == "/":
            result = int(calcul[0]) / int(calcul[2])
        elif calcul[1] == "**":
            result = int(calcul[0]) **int(calcul[2])
        print(calcul_base, " = ", result)