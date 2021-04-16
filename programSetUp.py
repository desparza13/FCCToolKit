#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 20:06:12 2021

@author: danielaesparza jenniferhernandez
"""
import variables as v
from colorama import Back,Fore,Style,init

def menu():
    print(Fore.BLUE+" ██████████     █████████   ██████   █████ ██████   █████ ██████████ ███████████  ")
    print(Fore.BLUE+"░░███░░░░███   ███░░░░░███ ░░██████ ░░███ ░░██████ ░░███ ░░███░░░░░█░░███░░░░░███ ")
    print(Fore.BLUE+" ░███   ░░███ ░███    ░███  ░███░███ ░███  ░███░███ ░███  ░███  █ ░  ░███    ░███ ")
    print(Fore.BLUE+" ░███    ░███ ░███████████  ░███░░███░███  ░███░░███░███  ░██████    ░██████████  ")
    print(Fore.BLUE+" ░███    ░███ ░███░░░░░███  ░███ ░░██████  ░███ ░░██████  ░███░░█    ░███░░░░░███ ")
    print(Fore.BLUE+" ░███    ███  ░███    ░███  ░███  ░░█████  ░███  ░░█████  ░███ ░   █ ░███    ░███ ")
    print(Fore.BLUE+" ██████████   █████   █████ █████  ░░█████ █████  ░░█████ ██████████ █████   █████")
    print(Fore.BLUE+"░░░░░░░░░░   ░░░░░   ░░░░░ ░░░░░    ░░░░░ ░░░░░    ░░░░░ ░░░░░░░░░░ ░░░░░   ░░░░░ ")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| Escoge la opción que quieres usar:                                     |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|                                                                        |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 1.Generador de tablas de verdad                                        |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 2.Calculadora de conjuntos                                             |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 3.Sucesiones                                                           |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|                                                                        |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(\__/) ||                                                (\__/) ||")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(•ㅅ•) ||                                                 (•ㅅ•) ||")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"/ 　 づ                                                   / 　 づ")
    
    v.menuChoice=int(input(">>"))