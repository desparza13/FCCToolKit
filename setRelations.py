#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 18:48:17 2021

@author: danielaesparza jenniferhdzmtz

"""
import variables as v
from colorama import Back,Fore,Style,init

def relationsLoop():
    while(v.endFuncion== False):
        instructions() #Función que muestra las instrucciones para el ingreso de datos y hace el ingreso de los mismos
        #BANNER que anuncia los resultados
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" -----------------------------------------------------------------------------------------------")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|                                          |")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|               RESULTADOS                 |")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|                                          |")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(\__/) ||  ")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(•ㅅ•) ||   ")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"/ 　 づ     ")
        dominio() #Calcula y muestra el dominio
        codominio() #Calcula y muestra el codominio
        reflexiva() #Determina si es o no reflexiva
        simetria() #Determina si es o no simétrica
        transitividad() #Determina si es o no transitiva y de no serlo muestra que valor falta para que lo sea
        funcion() #Determina si es o no una función y de no serlo muestra que valores de y tiene cada x que tiene más de uno

        print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "|  Escriba SALIR si desea salir, si desea seguir escriba algo diferente                                   |")

        end = input(">>")
        if (end == "SALIR"):
            v.endFuncion = True

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
    
    for i in range(v.pairsQuantity): #Por cada pareja ordenada solicitar su X y su Y
        v.x=int(input("X:"))
        v.xCoords.append(v.x)
        v.y=int(input("Y:"))
        v.yCoords.append(v.y) 
    
def dominio(): #Calcula y muestra el dominio (Valores de X en las parejas ordenadas)
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")
    for i in v.xCoords: #Revisa cada x de las parejas
        if i not in v.dominio: #Si esa coordenada en X no está repetida
            v.dominio.append(i) #Añadirla al dominio
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Dominio X")
    v.dominio.sort() #Ordenar de menor a mayor los valores
    print(v.dominio) #Mostrarlos
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")

    

def codominio(): #Calcula y muestra el codominio (Valores de Y en las parejas ordenadas)
    for i in v.yCoords: #Revisa cada y de las parejas
        if i not in v.codominio: #Si esa coordenada en Y no está repetida
            v.codominio.append(i) #Añadirla al codominio
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Codominio Y")
    v.codominio.sort() #Ordenar de menor a mayor los valores
    print(v.codominio) #Mostrarlos
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")

    
def reflexiva(): #Determina si es o no reflexiva
    contador=len(v.dominio) #Si fuera reflexiva debería tener la misma cantidad de elementos
    for i in range(len(v.xCoords)): #A lo largo de los pares ordenados
        if v.yCoords[i]==v.xCoords[i]: #Si encuentro el par reflexivo
            contador=contador-1 #Lo resto
    if contador==0: #Si había la misma cantidad de reflexivos que la que debería haber 
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Reflexividad: SI") #La función es reflexiva
    else: #Si no
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Reflexividad: NO") #No es reflexiva
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")


def simetria(): #Determina si es o no simétrica
    revision=False
    noSimetrico=False
    for i in range(len(v.xCoords)): # Por cada par
        for j in range(len(v.yCoords)): #Comparo con el resto de pares
            if (v.xCoords[i]==v.yCoords[j]) and (v.yCoords[i]==v.xCoords[j]): # Si (X1,Y1)==(Y2,X2)
                revision=True #Entonces encontré su elemento simetrico
        if revision==False: #Si acabo el for y no lo encontre la funcion ya no es simetrica
            print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Simetria: NO") #Digo que no es simetrico
            noSimetrico=True
            break
        revision=False
    if (noSimetrico==False): #Si nunca me faltó un simetrico
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Simetria: SI") #Decir que es simetrico
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")



def transitividad(): #Determina si es o no transitiva y de no serlo muestra que valor falta para que lo sea
    revision=False
    noTransitivo=False
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Transitividad")
    for i in range(v.pairsQuantity): # Por cada par
        x=v.xCoords[i] #Consigo x
        y=v.yCoords[i] #Consigo y
        for j in range(v.pairsQuantity): #Comparo con el resto de pares
            if (v.xCoords[j]==y): #Si hay y,z
                z=v.yCoords[j]
                for k in range(v.pairsQuantity):
                    if (v.xCoords[k]==x) and (v.yCoords[k]==z): #Si hay x,z
                        revision=True #Es transitivo
                if revision==False: #Si no no es transitivo
                    print("Falta [",x,",",z,"]") #Muestro el x,z faltante
                    noTransitivo=True
                    break
                revision=False
    if (noTransitivo==False):
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Transitividad: SI") #Digo es transitivo
    else:
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Por tanto transitividad: NO") #Digo no es transitivo
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")


def funcion():
    noFuncion=False
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Funcion")
    for i in range(v.pairsQuantity): #Por cada par 
        for j in range(v.pairsQuantity): #Busco si encuentro otros y
            if (v.xCoords[i]==v.xCoords[j]) and (v.yCoords[i]!=v.yCoords[j]):
                noFuncion=True
                if (v.noFuncionX!=v.xCoords[i])and v.noFuncionX!=1000:
                    print("Para X =",v.noFuncionX," Y=",v.noFuncionY) #Si hay mas de uno muestro cuantas y hay para esa x
                    v.noFuncionY=[] #Restauro las y para las siguientes x
                if v.yCoords[i] not in v.noFuncionY: #Añado las y para mostrarlas
                    v.noFuncionY.append(v.yCoords[i])
                if v.yCoords[j] not in v.noFuncionY:
                    v.noFuncionY.append(v.yCoords[j])
                v.noFuncionX=v.xCoords[i]

    if (noFuncion==False): #Si nunca encontre mas de una y para cada x
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Funcion: SI") #Digo que es función
    else:
        print("Para X =",v.noFuncionX," Y=",v.noFuncionY) 
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"Por tanto función: NO") #Digo que es relación y no función
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")


        
                