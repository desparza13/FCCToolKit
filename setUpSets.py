#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 20:16:55 2021

@author: danielaesparza jenniferhernandez
"""

import variables as v
from colorama import Back,Fore,Style,init

def captureSets():
    var=input("A = ")
    v.a=var.split(",")
    var=input("B = ")
    v.b=var.split(",")
    var=input("C = ")
    v.c=var.split(",")
    print(v.a)
    print(v.b)
    print(v.c)
    
def menuOperations():
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| Escoge la operación que quieres usar:                                  |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|                                                                        |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 1.Unión                                                                |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 2.Intersección                                                         |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 3.Diferencia                                                           |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 4.Diferencia simétrica                                                 |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|                                                                        |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(\__/) ||                                                (\__/) ||")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(•ㅅ•) ||                                                 (•ㅅ•) ||")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"/ 　 づ                                                   / 　 づ\n")
    v.chosenOperation=int(input(">>"))

def options():
    if (v.chosenOperation==1):
        operator="U"
    elif (v.chosenOperation==2):
        operator="∩"
    elif (v.chosenOperation==3):
        operator="-"
    elif (v.chosenOperation==4):
        operator="Δ"
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| Escoge la operación a resolver:                                        |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|                                                                        |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 1.A"+operator+"B                                                                  |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 2.B"+operator+"C                                                                  |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 3.A"+operator+"C                                                                  |")
    if(v.chosenOperation==1 or v.chosenOperation==2):
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 4.A"+operator+"(B"+operator+"C)                                                              |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|                                                                        |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(\__/) ||                                                (\__/) ||")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(•ㅅ•) ||                                                 (•ㅅ•) ||")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"/ 　 づ                                                   / 　 づ\n")
    v.operation=int(input(">>"))
 
def union(a,b):
    c=[]
    for i in a:
        c.append(i)
    for i in b:
        if (i not in c):
            c.append(i)
    v.newSet=c
    return c
    
def intersection(a,b):
    c=[]
    for i in a:
        if (i in b):
            c.append(i)
    v.newSet=c

def difference(a,b):
    c=[]
    for i in a:
        if (i not in b):
            c.append(i)
    v.newSet=c
    return c

def symmetricDiff(a,b):
    c=[]
    d=[]
    e=[]
    d= difference(a,b)
    print(d)
    e=difference(b,a)
    print(e)
    c=union(d,e)
    v.newSet=c

def operate():
    if (v.chosenOperation==1):
        if (v.operation==1):
            union(v.a, v.b)
            print("AUB =",v.a,"U",v.b)
            print("AUB =",v.newSet)
        elif (v.operation==2):
            union(v.b,v.c)
            print("BUC =",v.b,"U",v.c)
            print("BUC =",v.newSet)
        elif (v.operation==3):
            union(v.a, v.c)
            print("AUC =",v.a,"U",v.c)
            print("AUC =",v.newSet)
        elif (v.operation==4):
            union(v.b, v.c)
            union(v.newSet,v.a)
            print("AU(BUC) =",v.a,"U (",v.b,"U",v.c,")")
            print("AU(BUC) =",v.newSet)
            
    if (v.chosenOperation==2):
        if (v.operation==1):
            intersection(v.a, v.b)
            print("A∩B =",v.a,"∩",v.b)
            print("A∩B =",v.newSet)
        elif (v.operation==2):
            intersection(v.b, v.c)
            print("B∩C =",v.b,"∩",v.c)
            print("B∩C =",v.newSet)
        elif (v.operation==3):
            intersection(v.a, v.c)
            print("A∩C =",v.a,"∩",v.c)
            print("A∩C =",v.newSet)
        elif (v.operation==4):
            intersection(v.b, v.c)
            intersection(v.newSet,v.a)
            print("A∩(B∩C) =",v.a,"∩ (",v.b,"∩",v.c,")")
            print("A∩(B∩C) =",v.newSet)
    
    if (v.chosenOperation==3):
        if (v.operation==1):
            difference(v.a,v.b)
            print("A-B =",v.a,"-",v.b)
            print("A-B =",v.newSet)
        elif (v.operation==2):
            difference(v.b,v.c)
            print("B-C =",v.b,"-",v.c)
            print("B-C =",v.newSet)
        elif (v.operation==3):
            difference(v.a, v.c)
            print("A-C =",v.a,"-",v.c)
            print("A-C =",v.newSet)
    
    if (v.chosenOperation==4):
        if (v.operation==1):
            symmetricDiff(v.a,v.b)
            print("AΔB =",v.a,"Δ",v.b)
            print("AΔB =",v.newSet)
        elif (v.operation==2):
            symmetricDiff(v.b,v.c)
            print("BΔC =",v.b,"Δ",v.c)
            print("BΔC =",v.newSet)
        elif (v.operation==3):
            symmetricDiff(v.a, v.c)
            print("AΔC =",v.a,"Δ",v.c)
            print("AΔC =",v.newSet)

            
    
def setsLoop():
        print(Fore.MAGENTA+Style.BRIGHT+"                              _               _                      ")
        print(Fore.MAGENTA+Style.BRIGHT+"                             | |             | |                     ")
        print(Fore.MAGENTA+Style.BRIGHT+"  ,   _ _|_  ,     __   __,  | |  __         | |  __, _|_  __   ,_   ")
        print(Fore.MAGENTA+Style.BRIGHT+" / \_|/  |  / \_  /    /  |  |/  /    |   |  |/  /  |  |  /  \_/  |  ")
        print(Fore.MAGENTA+Style.BRIGHT+"  \/ |__/|_/ \/   \___/\_/|_/|__/\___/ \_/|_/|__/\_/|_/|_/\__/    |_/")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| Inserta los elementos alfanuméricos de cada conjunto separados por     |")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| comas. SIN ESPACIOS                                                    |")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| Ejemplo:                                                               |")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| A= 1,2,3,4,5,6,7,8                                                     |")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| B= a,5,hola,jenny,7,conejo                                             |")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(\__/) ||                                                (\__/) ||")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(•ㅅ•) ||                                                 (•ㅅ•) ||")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"/ 　 づ                                                   / 　 づ \n")
        captureSets()
        menuOperations()
        options()
        operate()
        v.chosenOperation=0
        v.operation=0
        v.newSet=[]
        

    

