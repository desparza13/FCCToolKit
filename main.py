#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 13:58:58 2021

@author: danielaesparza
"""
import variables as v
import setUp as su
import tables as t
import operations as op
from colorama import Back,Fore,Style,init
init(autoreset=True)

print(Fore.BLUE+" ██████████     █████████   ██████   █████ ██████   █████ ██████████ ███████████  ")
print(Fore.BLUE+"░░███░░░░███   ███░░░░░███ ░░██████ ░░███ ░░██████ ░░███ ░░███░░░░░█░░███░░░░░███ ")
print(Fore.BLUE+" ░███   ░░███ ░███    ░███  ░███░███ ░███  ░███░███ ░███  ░███  █ ░  ░███    ░███ ")
print(Fore.BLUE+" ░███    ░███ ░███████████  ░███░░███░███  ░███░░███░███  ░██████    ░██████████  ")
print(Fore.BLUE+" ░███    ░███ ░███░░░░░███  ░███ ░░██████  ░███ ░░██████  ░███░░█    ░███░░░░░███ ")
print(Fore.BLUE+" ░███    ███  ░███    ░███  ░███  ░░█████  ░███  ░░█████  ░███ ░   █ ░███    ░███ ")
print(Fore.BLUE+" ██████████   █████   █████ █████  ░░█████ █████  ░░█████ ██████████ █████   █████")
print(Fore.BLUE+"░░░░░░░░░░   ░░░░░   ░░░░░ ░░░░░    ░░░░░ ░░░░░    ░░░░░ ░░░░░░░░░░ ░░░░░   ░░░░░ ")

print(Fore.MAGENTA+Style.BRIGHT+"                      _                 _    _                                                      ")
print(Fore.MAGENTA+Style.BRIGHT+"                     | |               | |  | |                                                      ")
print(Fore.MAGENTA+Style.BRIGHT+" _|_  ,_         _|_ | |      _|_  __, | |  | |  _     __,  _   _  _    _   ,_    __, _|_  __   ,_   ")
print(Fore.MAGENTA+Style.BRIGHT+"  |  /  |  |   |  |  |/ \      |  /  | |/ \_|/  |/    /  | |/  / |/ |  |/  /  |  /  |  |  /  \_/  |  ")
print(Fore.MAGENTA+Style.BRIGHT+"  |_/   |_/ \_/|_/|_/|   |_/   |_/\_/|_/\_/ |__/|__/  \_/|/|__/  |  |_/|__/   |_/\_/|_/|_/\__/    |_/")
print(Fore.MAGENTA+Style.BRIGHT+"                                                        /|                                           ")
print(Fore.MAGENTA+Style.BRIGHT+"                                                        \|                                           ")

print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")
print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| REGLAS:                                                                |")
print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 1.Usa premisas de P a Z                                                |")
print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 2.Usa solo mayúsculas para las variables                               |")
print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 3.Introduce entre parentesis las premisas, separando todo con espacios.|")
print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 4.Separa el operador con su espacio también                            |")
print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 5.Los operadores aceptados son: v, ^, ->, <-> y ~                      |")
print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 6.Ingresa SALIR para salir                                                 |")
print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| Ejemplo: ( p ^ q )                                                     |")
print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")
print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(\__/) ||")
print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(•ㅅ•) ||")
print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"/ 　 づ")

v.proposition=""
while(v.proposition!="SALIR"):
    v.proposition=input(">>")
    v.arguments=v.proposition.split(' ')
    t.createTable(v.arguments)
    su.findParentheses(v.arguments)
    t.orderTable(v.tableValues)
    

    
