#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 20:16:55 2021

@author: danielaesparza jenniferhernandez
"""

import variables as v
from colorama import Back,Fore,Style,init

def captureSets(): #Recibe tres conjuntos ingresados por el usuario separados por comas
    var=input("A = ")
    v.a=var.split(",")
    var=input("B = ")
    v.b=var.split(",")
    var=input("C = ")
    v.c=var.split(",")
    print(v.a)
    print(v.b)
    print(v.c)
    
def menuOperations(): #Muestra un banner con las cuatro opciones a escoger (Unión, intersección, diferencia, diferencia simétrica)
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

def options(): #De acuerdo a la opción de operación escogida por el usuario se muestra un nuevo banner con las posibles operaciones a realizar por él, escogerá una ingresando el número de opción
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
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 5.B"+operator+"(A"+operator+"C)                                                              |")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 6.C"+operator+"(A"+operator+"B)                                                              |")

    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|                                                                        |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(\__/) ||                                                (\__/) ||")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(•ㅅ•) ||                                                 (•ㅅ•) ||")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"/ 　 づ                                                   / 　 づ\n")
    v.operation=int(input(">>"))
 
def union(a,b): #Realiza la operación unión entre dos conjuntos
    c=[]
    for i in a: #Recorre todo el primer arreglo de elementos del primer conjunto
        c.append(i) #Añadir el elemento a un nuevo conjunto que será la respuesta
    for i in b: #Checar en el segundo arreglo de elementos del segundo conjunto
        if (i not in c): #Si no está en el nuevo conjunto
            c.append(i) #Lo añades, así evitamos repetidos
    v.newSet=c #Entregar la respuesta
    return c
    
def intersection(a,b): #Realiza la operación intersección entre dos conjuntos
    c=[]
    for i in a: #Recorre todos los elementos del primer conjunto
        if (i in b): #Si el elemento está también en el segundo conjunto
            c.append(i) #Lo añado al conjunto de respuesta que contiene los elementos que coinciden en ambos conjuntos
    v.newSet=c

def difference(a,b): #Realiza la operación diferencia entre dos conjuntos
    c=[]
    for i in a: #Recorre todos los elementos del primer conjunto
        if (i not in b): #Revisa si el elemento está en el conjunto a PERO NO en b
            c.append(i) #Lo añade al nuevo conjunto respuesta
    v.newSet=c
    return c

def symmetricDiff(a,b): #Realiza la operación diferencia simétrica entre dos conjuntos
    c=[]
    d=[]
    e=[]
    d= difference(a,b) #Obtengo A-B
    e=difference(b,a) #Obtengo B-A
    c=union(d,e) #Hago la unión (A-B) U ( B-A)
    v.newSet=c

def operate(): #De acuerdo a la operación a realizar llamo a las funciones con las respectivas variables e imprimo el resultado
    if (v.chosenOperation==1): #UNION
        if (v.operation==1): #Union AUB
            union(v.a, v.b)
            print("AUB =",v.a,"U",v.b)
            print("AUB =",v.newSet)
        elif (v.operation==2): #UNION BUC
            union(v.b,v.c)
            print("BUC =",v.b,"U",v.c)
            print("BUC =",v.newSet)
        elif (v.operation==3): #Union AUC
            union(v.a, v.c)
            print("AUC =",v.a,"U",v.c)
            print("AUC =",v.newSet)
        elif (v.operation==4): #Union AU(BUC)
            union(v.b, v.c)
            union(v.newSet,v.a)
            print("AU(BUC) =",v.a,"U (",v.b,"U",v.c,")")
            print("AU(BUC) =",v.newSet)
        elif (v.operation==5): #Union BU(AUC)
            union(v.a, v.c)
            union(v.b,v.newSet)
            print("BU(AUC) =",v.b,"U (",v.a,"U",v.c,")")
            print("BU(AUC) =",v.newSet)
        elif (v.operation==6): #Union CU(AUB)
            union(v.a, v.b)
            union(v.c,v.newSet)
            print("CU(AUB) =",v.c,"U (",v.a,"U",v.b,")")
            print("CU(AUB) =",v.newSet)
            
    if (v.chosenOperation==2): #Intersección
        if (v.operation==1): #A∩B
            intersection(v.a, v.b)
            print("A∩B =",v.a,"∩",v.b)
            print("A∩B =",v.newSet)
        elif (v.operation==2): #B∩C 
            intersection(v.b, v.c)
            print("B∩C =",v.b,"∩",v.c)
            print("B∩C =",v.newSet)
        elif (v.operation==3): #A∩C
            intersection(v.a, v.c)
            print("A∩C =",v.a,"∩",v.c)
            print("A∩C =",v.newSet)
        elif (v.operation==4): #A∩(B∩C)
            intersection(v.b, v.c)
            intersection(v.newSet,v.a)
            print("A∩(B∩C) =",v.a,"∩ (",v.b,"∩",v.c,")")
            print("A∩(B∩C) =",v.newSet)
        elif (v.operation==5): #B∩(A∩C)
            intersection(v.a, v.c)
            intersection(v.b,v.newSet)
            print("B∩(A∩C) =",v.b,"∩ (",v.a,"∩",v.c,")")
            print("B∩(A∩C) =",v.newSet)
        elif (v.operation==6): #C∩(A∩B)
            intersection(v.a, v.c)
            intersection(v.b,v.newSet)
            print("C∩(A∩B) =",v.c,"∩ (",v.a,"∩",v.b,")")
            print("C∩(A∩B) =",v.newSet)
    
    if (v.chosenOperation==3): #Diferencia
        if (v.operation==1): #A-B
            difference(v.a,v.b)
            print("A-B =",v.a,"-",v.b)
            print("A-B =",v.newSet)
        elif (v.operation==2): #B-C
            difference(v.b,v.c)
            print("B-C =",v.b,"-",v.c)
            print("B-C =",v.newSet)
        elif (v.operation==3): #A-C
            difference(v.a, v.c)
            print("A-C =",v.a,"-",v.c)
            print("A-C =",v.newSet)
    
    if (v.chosenOperation==4): #Diferencia simétrica
        if (v.operation==1): #AΔB
            symmetricDiff(v.a,v.b)
            print("AΔB =",v.a,"Δ",v.b)
            print("AΔB =",v.newSet)
        elif (v.operation==2): #BΔC
            symmetricDiff(v.b,v.c)
            print("BΔC =",v.b,"Δ",v.c)
            print("BΔC =",v.newSet)
        elif (v.operation==3): #AΔC
            symmetricDiff(v.a, v.c)
            print("AΔC =",v.a,"Δ",v.c)
            print("AΔC =",v.newSet)

            
    
def setsLoop(): #Loop principal de la calculadora de conjuntos
    while(v.endCalculator==False): #Mientras el usuario no escoja salir
        #BANNER de bienvenida e instrucciones
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
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"/ 　 づ                                                   / 　 づ ")
        captureSets() #Ingreso de conjuntos
        menuOperations() #Seleccionar operacion
        options()#Seleccionar opcion de variables con operacion
        operate()#Ver resultado
        #Resetear variables
        v.chosenOperation=0
        v.operation=0
        v.newSet=[]
        #BANNER para preguntar si quiere salir
        print(Back.WHITE + Fore.BLACK + Style.BRIGHT + " ------------------------------------------------------------------------")
        print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "| Ingresa SALIR para salir                                               |")
        print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "| Si desea seguir en Sets Calculator ingrese algo diferente              |")
        print(Back.WHITE + Fore.BLACK + Style.BRIGHT + " ------------------------------------------------------------------------")
        print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "(\_/) ||                                               (\_/) ||")
        print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "(•ㅅ•) ||                                                (•ㅅ•) ||")
        print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "/ 　 づ                                                  / 　 づ ")
        
        end=input(">>")
        if(end=="SALIR"):
            v.endCalculator = True
        

    

