#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:48:30 2021

@author: danielaesparza jenniferhernandez
"""

import variables as v
import setUp as su
from colorama import Back,Fore,Style,init
init(autoreset=True)
#-------------------------------------------------------------------------------------------------------
def createTable(expressions):
    exp={}
    expressionsQuantity=0
    for expression in expressions:
        if expression in v.expressions and not (expression in exp):
            expressionsQuantity=expressionsQuantity+1
            exp[expression]=''

    exp={}
    v.rows = 2**expressionsQuantity 
    i= -1
    for expression in expressions:
        if expression in v.expressions and not (expression in exp):
            exp[expression]=''
            i=i+1
            notExp=False
            notExpression="~"+expression
            if(len(expression))==2:
                notExpression=expression[1:2]
                notExp=True
            v.truthTable[expression]=[]
            v.truthTable[notExpression]=[]
            divisor=2 ** (i+1)
            chunk=v.rows/divisor
            nextChunk=chunk
            addValue=True
        
            for j in range(v.rows):
                if j==nextChunk:
                    nextChunk=nextChunk+chunk
                    addValue=not addValue
                if notExp==True:
                    v.truthTable[notExpression].insert(j,addValue)
                    v.truthTable[expression].insert(j,not addValue)
                else:
                    v.truthTable[expression].insert(j,addValue)
                    v.truthTable[notExpression].insert(j,not addValue)

#-------------------------------------------------------------------------------------------------------

def printTable(table):
    headers=""
    for i in table:
        headers=headers+"|     "+i+"    |"
    dividers=""
    for i in range(len(headers)):
        dividers=dividers+"-"
    print(Back.MAGENTA+Style.BRIGHT+Fore.WHITE+dividers)
    print(Back.MAGENTA+Style.BRIGHT+Fore.WHITE+headers)
    print(Back.MAGENTA+Style.BRIGHT+Fore.WHITE+dividers)
    
    printing=""
    for i in range(v.rows):
        for j,k in table.items():
            if k[i]==True:
                printing=printing+"| True"+v.separator[0:len(j)+5-1]+"|"
            else:
                printing=printing+"| False"+v.separator[0:len(j)+4-1]+"|"
        print(printing)
        printing=""
    print(Back.MAGENTA+Style.BRIGHT+Fore.WHITE+dividers,"\n")
#-------------------------------------------------------------------------------------------------------
def orderTable(table):
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







    
                
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
            
                