#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:48:30 2021

@author: danielaesparza jenniferhernandez
"""

import variables as v
import setUps as su
from colorama import Back,Fore,Style,init
init(autoreset=True)
#-------------------------------------------------------------------------------------------------------
def createTable(expressions): #Genera la tabla
    exp={}
    expressionsQuantity=0
    for expression in expressions: #Por cada argumento
        if expression in v.expressions and not (expression in exp): #Si no existe anteriormente
            expressionsQuantity=expressionsQuantity+1 #Aumento nuestro contador de argumentos
            exp[expression]='' #Creo su elemento con su llave en el diccionario pero vacio

    exp={}
    v.rows = 2**expressionsQuantity #La cantidad de filas es 2^cantidad de premisas
    i= -1
    for expression in expressions:
        if expression in v.expressions and not (expression in exp):
            exp[expression]=''
            i=i+1
            notExp=False #Indica que asumimos de entrada que el argumento es positivo
            notExpression="~"+expression
            if(len(expression))==2: #Si la longitud es dos el ~ y la variable que niega, es negativo, uno es variable, mas de dos es ya una operacion
                notExpression=expression[1:2] #Tomo solo la variable sin el signo
                notExp=True #Digo que es expresión negativa
            v.truthTable[expression]=[] #Creo el elemento con su llave
            v.truthTable[notExpression]=[]
            divisor=2 ** (i+1)
            chunk=v.rows/divisor #calcula cada cuanto va True y cada cuanto False, p. ejemplo en la primer variable va de 1 en 1
            nextChunk=chunk 
            addValue=True
        
            for j in range(v.rows): #se repite hasta llenar la columna de la variable
                if j==nextChunk:
                    nextChunk=nextChunk+chunk #Aumenta la cantidad, ejemplo, en la variable uno cambia de 1 en 1, en la segunda de 2 en 2, en la tercera de 4 en 4
                    addValue=not addValue #Hace que pase a ser el contrario
                if notExp==True: # Si era negativo va en inversa, empieza con false termina con true
                    v.truthTable[notExpression].insert(j,addValue)
                    v.truthTable[expression].insert(j,not addValue)
                else: #Empieza con True termina con False
                    v.truthTable[expression].insert(j,addValue)
                    v.truthTable[notExpression].insert(j,not addValue)

#-------------------------------------------------------------------------------------------------------

def printTable(table): #Imprime la tabla con guiones y separadores para mayor legibilidad
    headers=""
    for i in table:
        headers=headers+"|     "+i+"    |"
    dividers=""
    for i in range(len(headers)): #Imprime los encabezados de las columnas (argumentos y variables)
        dividers=dividers+"-"
    print(Back.MAGENTA+Style.BRIGHT+Fore.WHITE+dividers)
    print(Back.MAGENTA+Style.BRIGHT+Fore.WHITE+headers)
    print(Back.MAGENTA+Style.BRIGHT+Fore.WHITE+dividers)
    
    printing=""
    for i in range(v.rows): #Llena la tabla imprimiendo los valores de True o False
        for j,k in table.items():
            if k[i]==True:
                printing=printing+"| True"+v.separator[0:len(j)+5-1]+"|"
            else:
                printing=printing+"| False"+v.separator[0:len(j)+4-1]+"|"
        print(printing)
        printing=""
    print(Back.MAGENTA+Style.BRIGHT+Fore.WHITE+dividers,"\n") #Cierra la tabla
#-------------------------------------------------------------------------------------------------------
def orderTable(table): #Ordena la tabla poniendo primero variables positivas, luego variables negativas, finalmente los argumentos con operacion
    positiveTable={}
    negativeTable={}
    operationsTable={}
    finalTable={}
    for exp in table.keys():
        if exp in v.expressions:
            if len(exp)==2:
                contrary=exp[1:2]
                negativeTable[exp]=v.truthTable[exp]
                positiveTable[exp]=v.truthTable[contrary]
            else:
                positiveTable[exp]=v.truthTable[exp]
        else:
            operationsTable[exp]=table[exp]
    for key, value in positiveTable.items():
        finalTable[key]=value
    for key, value in negativeTable.items():
        finalTable[key]=value
    for key, value in operationsTable.items():
        finalTable[key]=value
    printTable(finalTable)
#-------------------------------------------------------------------------------------------------------



                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
            
                