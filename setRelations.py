#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 18:48:17 2021

@author: danielaesparza jenniferhdzmtz

"""
import variables as v
from colorama import Back,Fore,Style,init

def relationsLoop():
    instructions()
    #BANNER de sumatoria y producto
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" -----------------------------------------------------------------------------------------------")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|                                          |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|               RESULTADOS                 |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|                                          |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(\__/) ||  ")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(•ㅅ•) ||   ")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"/ 　 づ     ")
    dominio()
    codominio()
    reflexiva()
    simetria()
    transitividad()
    funcion()

def instructions(): #Función que muestra las instrucciones y pide los valores al usuario
    #BANNER de la opción de menú solicitada
    print(Fore.MAGENTA+Style.BRIGHT+"  , __       _                                _                     ______                                           ")
    print(Fore.MAGENTA+Style.BRIGHT+" /|/  \     | |          o                   | |    o             /(_) |                         o                   ")
    print(Fore.MAGENTA+Style.BRIGHT+"  |___/  _  | |  __, _|_     __   _  _    ,  | |         _   ,   /    _|_         _  _    __ _|_     __   _  _    ,  ")
    print(Fore.MAGENTA+Style.BRIGHT+"  | \   |/  |/  /  |  |  |  /  \_/ |/ |  / \_|/ \   |  |/ \_/ \_/    / | ||   |  / |/ |  /    |  |  /  \_/ |/ |  / \_")
    print(Fore.MAGENTA+Style.BRIGHT+"  |  \_/|__/|__/\_/|_/|_/|_/\__/   |  |_/ \/ |   |_/|_/|__/  \//    (_/    \_/|_/  |  |_/\___/|_/|_/\__/   |  |_/ \/ ")
    print(Fore.MAGENTA+Style.BRIGHT+"                                                      /|                                                             ")
    print(Fore.MAGENTA+Style.BRIGHT+"                                                      \|                                                             ")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" -----------------------------------------------------------------------------------------------")
         

    #BANNER que muestra las instrucciones para el ingreso de los valores
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| Bienvenido a la calculadora de relaciones y sucesiones para determinar |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| sus propiedades, su dominio y su codominio.                            |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|                                                                        |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|                                                                        |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 1. Ingresa la cantidad de parejas ordenadas a revisar                  |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 2. Ingresa la X de la pareja                                           |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 3. Ingresa la Y de la pareja                                           |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 4. Observa la información analizada                                    |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|                                                                        |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(\__/) ||                                                (\__/) ||")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(•ㅅ•) ||                                                 (•ㅅ•) ||")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"/ 　 づ                                                   / 　 づ\n")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" -----------------------------------------------------------------------------------------------")

    v.pairsQuantity=int(input("Cantidad de parejas ordenadas:")) #Ingreso de la cantidad de parejas ordenadas
    
    for i in range(v.pairsQuantity):
        v.x=int(input("X:"))
        v.xCoords.append(v.x)
        v.y=int(input("Y:"))
        v.yCoords.append(v.y) 
    
def dominio():
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")
    for i in v.xCoords:
        if i not in v.dominio:
            v.dominio.append(i)
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Dominio X")
    v.dominio.sort()
    print(v.dominio)
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")

    

def codominio():
    for i in v.yCoords:
        if i not in v.codominio:
            v.codominio.append(i)
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Codominio Y")
    v.codominio.sort()
    print(v.codominio)
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")

    
def reflexiva():
    contador=len(v.dominio)
    for i in range(len(v.xCoords)):
        if v.yCoords[i]==v.xCoords[i]:
            contador=contador-1
    if contador==0:
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Reflexividad: SI")
    else:
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Reflexividad: NO")  
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")


def simetria():
    revision=False
    noSimetrico=False
    for i in range(len(v.xCoords)):
        for j in range(len(v.yCoords)):
            if (v.xCoords[i]==v.yCoords[j]) and (v.yCoords[i]==v.xCoords[j]):
                revision=True
        if revision==False:
            print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Simetria: NO")
            noSimetrico=True
            break
        revision=False
    if (noSimetrico==False):
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Simetria: SI")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")



def transitividad():
    revision=False
    noTransitivo=False
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Transitividad")
    for i in range(v.pairsQuantity):
        x=v.xCoords[i]
        y=v.yCoords[i]
        for j in range(v.pairsQuantity):
            if (v.xCoords[j]==y):
                z=v.yCoords[j]
                for k in range(v.pairsQuantity):
                    if (v.xCoords[k]==x) and (v.yCoords[k]==z):
                        revision=True
                if revision==False:
                    print("Falta [",x,",",z,"]")
                    noTransitivo=True
                    break
                revision=False
    if (noTransitivo==False):
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Transitividad: SI")
    else:
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Por tanto transitividad: NO")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")


def funcion():
    noFuncion=False
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Funcion")
    for i in range(v.pairsQuantity):
        for j in range(v.pairsQuantity):
            if (v.xCoords[i]==v.xCoords[j]) and (v.yCoords[i]!=v.yCoords[j]):
                noFuncion=True
                if (v.noFuncionX!=v.xCoords[i])and v.noFuncionX!=1000:
                    print("Para X =",v.noFuncionX," Y=",v.noFuncionY)
                    v.noFuncionY=[]
                if v.yCoords[i] not in v.noFuncionY:
                    v.noFuncionY.append(v.yCoords[i])
                if v.yCoords[j] not in v.noFuncionY:
                    v.noFuncionY.append(v.yCoords[j])
                v.noFuncionX=v.xCoords[i]

    if (noFuncion==False):
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Funcion: SI")
    else:
        print("Para X =",v.noFuncionX," Y=",v.noFuncionY) 
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Por tanto función: NO")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")


        
                