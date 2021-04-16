#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 14:40:50 2021

@author: danielaesparza jenniferhdzmtz
"""

import variables as v
from colorama import Back,Fore,Style,init

def sucesionsLoop():#Ciclo de la calculadora de sucesiones
    while(v.endSuccessions==False): #Mientras el usuario no escoja salir
    
        #BANNER de la opción de menú solicitada
         print(Fore.MAGENTA+Style.BRIGHT+"                                                                 _               _                      ")
         print(Fore.MAGENTA+Style.BRIGHT+"   ()                          o                                | |             | |                     ")
         print(Fore.MAGENTA+Style.BRIGHT+"   /\         __   __   _   ,      __   _  _    ,     __   __,  | |  __         | |  __, _|_  __   ,_   ")
         print(Fore.MAGENTA+Style.BRIGHT+"  /  \|   |  /    /    |/  / \_|  /  \_/ |/ |  / \_  /    /  |  |/  /    |   |  |/  /  |  |  /  \_/  |  ")
         print(Fore.MAGENTA+Style.BRIGHT+" /(__/ \_/|_/\___/\___/|__/ \/ |_/\__/   |  |_/ \/   \___/\_/|_/|__/\___/ \_/|_/|__/\_/|_/|_/\__/    |_/")
         print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" -----------------------------------------------------------------------------------------------")
         
         instructions() #Función que muestra las instrucciones y pide los valores al usuario
         print("-----------------------------------------------------------------------------------------------")
         print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------")
         print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|                                          |")
         print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|         CÁLCULO DE TERMINOS              |")
         print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|                                          |")
         print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------")
         print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(\__/) ||  ")
         print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(•ㅅ•) ||   ")
         print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"/ 　 づ     ")
         calculate(v.limInferior,v.limSuperior) #Función recursiva que muestro los términos, realiza la suma y el producto
         
         #BANNER para preguntar si quiere salir
         print(Back.WHITE + Fore.BLACK + Style.BRIGHT + " ------------------------------------------------------------------------")
         print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "| Ingresa SALIR para salir                                               |")
         print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "| Si desea seguir en Sets Calculator ingrese algo diferente              |")
         print(Back.WHITE + Fore.BLACK + Style.BRIGHT + " ------------------------------------------------------------------------")
         print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "(\_/) ||                                               (\_/) ||")
         print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "(•ㅅ•) ||                                                (•ㅅ•) ||")
         print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "/ 　 づ                                                  / 　 づ ")
         
         #preguntar si se desea salir de la calculadora
         end=input(">>")
         if(end=="SALIR"):
             v.endSuccessions = True

     
def instructions(): #Función que muestra las instrucciones y pide los valores al usuario
    #BANNER que muestra las instrucciones para el ingreso de los valores
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| Bienvenido a la calculadora de sucesiones, vamos a calcular los        |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| elementos desde el límite inferior (m) hasta el limite superior (n) de |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| una fórmula que ingreses                                               |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|                                                                        |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| Al ingresar la fórmula:                                                |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 1. Utiliza X como variable                                             |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"| 2. Utiliza los siguientes operadores:                                  |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|     Suma: +                                                            |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|     Resta: -                                                           |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|     Producto: *                                                        |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|     Potencia: **                                                       |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|     División: /                                                        |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|                                                                        |")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------------------------------------")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(\__/) ||                                                (\__/) ||")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(•ㅅ•) ||                                                 (•ㅅ•) ||")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"/ 　 づ                                                   / 　 づ\n")
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" -----------------------------------------------------------------------------------------------")
    
    print(Back.LIGHTMAGENTA_EX+Fore.BLACK+Style.BRIGHT+"Límite inferior:")
    v.limInferior=int(input()) #Ingreso del límite inferior de la sucesión
    
    print(Back.LIGHTMAGENTA_EX+Fore.BLACK+Style.BRIGHT+"Límite superior:")
    v.limSuperior=int(input()) #Ingreso del límite superior de la sucesión
    
    print(Back.LIGHTMAGENTA_EX+Fore.BLACK+Style.BRIGHT+"Fórmula:")
    v.formula=input() #Ingreso de la función o término general de la sucesión
    
    v.suma=0 #Resetear el valor de la suma para que no afecten los resultados de la sucesion anterior
    v.producto=1 #Resetear el valor de la multiplicación para que no afecten los resultados de la sucesion anterior
    


def calculate(inicio,fin): #Función recursiva que calcula los términos, la suma y la multiplicación
    #ALGORITMO GENERAL cada término entramos aqui
    x=inicio #establecemos el valor de la variable para utilizarlo en la fórmula
    nuevoTermino=eval(v.formula) #evaluamos ese valor en la fórmula
    v.suma=v.suma+nuevoTermino #lo añadimos a la suma
    v.producto=v.producto*nuevoTermino #lo multiplicamos por la multiplicación acumulada
    print("Término",x,":\t",nuevoTermino) #imprimimos el ttérmino
    
    #CONDICION DE SALIDA
    if(inicio==fin): #si estamos en el ultimo término
        #BANNER de sumatoria y producto
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" -----------------------------------------------------------------------------------------------")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|                                          |")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|         SUMATORIA Y PRODUCTO             |")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"|                                          |")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+" ------------------------------------------")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(\__/) ||  ")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"(•ㅅ•) ||   ")
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"/ 　 づ     ")
        #Imprimimos la suma y el producto
        print(Fore.MAGENTA+Style.BRIGHT+"Suma:",v.suma,"\n")
        print(Fore.MAGENTA+Style.BRIGHT+"Producto:",v.producto,"\n")
        print(Fore.MAGENTA+Style.BRIGHT+Back.WHITE+Fore.BLACK+Style.BRIGHT+" -----------------------------------------------------------------------------------------------")
        #no hacemos otra llamada a la función, términamos
        
    #LLAMADA RECURSIVA
    else:
        calculate(inicio+1,fin) #vuelvo a llamar la variable para que haga lo mismo pero con el siguiente término
        

        
        
    
    