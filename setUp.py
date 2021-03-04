#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 17:21:16 2021

@author: danielaesparza jenniferhernandez
"""
import variables as v
import operations as op
import tables as t
#-------------------------------------------------------------------------------------------------------
def findFirst (proposition, letterToSearch): #Regresa la posición de la primera ocurrencia de un caractér
    for i in range (len(proposition)): #Recorre la proposición
        if (proposition[i] == letterToSearch): #Si la encuentra
            return i #regresa la posición
    return -1 #regresa -1 si nunca aparece ese caracter en la proposición
#-------------------------------------------------------------------------------------------------------

def findLast (proposition, letterToSearch): #Regresa la posición de la última ocurrencia de un caracter
    for i in range (len(proposition)): #Recorre la proposición
        if (proposition[i]==letterToSearch): #Si lo encuentra
            if ((i+1) > len(proposition)): #Si era el último carácter de la proposición
                return i #era la última ocurrencia
            search = findLast(proposition[i+1:len(proposition)], letterToSearch) #guardo el resultado de la busqueda
            if (search==-1): #si da menos uno quiere decir que ya no encontró otro después, el pasado era el último
                return i #regreso el indice pasado
            else:
                findLast(proposition[i+1:len(proposition)], letterToSearch) #si lo volvi a encontrar repito el proceso hasta si encontrar el ULTIMO
    return -1

#-------------------------------------------------------------------------------------------------------

def findParentheses (proposition):
    openP=-1
    closeP=-1
    parenthesesUndone=0
    parenthesesCheck=0
    for i in range(len(proposition)):
        if (proposition[i]==')'): #Si encuentro un parentesis que cierra resto uno al contador de pares porque está completo
            parenthesesUndone=parenthesesUndone-1
            closeP=i #Guardo la posicion donde cierro
        if (proposition[i]=='('): #Si encuentro un parentesis que abra sumo uno al contador de pares incompletos porque todavía no encuentro su cierre
            parenthesesUndone=parenthesesUndone+1
            openP=i #Guardo la posicion donde abro
        if (parenthesesUndone < parenthesesCheck):
            exp = proposition[openP+1:closeP] #extraes lo que está dentro de los parentesis
            oldProp=saveOperation(exp)
            
            if (closeP== len(proposition)-1):
                newProposition = proposition[0:openP] + [oldProp]
            if (openP==0):
                newProposition = [oldProp] + proposition[closeP+1:len(proposition)]
            if (openP!=0 and closeP != len(proposition)-1):
                newProposition = proposition[0:openP]+[oldProp]+proposition[closeP:len(proposition)]
            if (findFirst(newProposition, '(')!=-1):
                findParentheses(newProposition)
            else:
                saveOperation(newProposition)
                op.evaluate()
                return
        parenthesesCheck=parenthesesUndone
            
                
#-------------------------------------------------------------------------------------------------------
    
def eliminateParentheses (proposition):
    openP=findLast(proposition, '(')
    newProposition=proposition[openP+1:len(proposition)]
    closeP=openP+findFirst(newProposition, ')')+1
    auxiliar=proposition[openP+1:closeP]
    var=saveOperation(auxiliar)
    
    argument=proposition[0:openP]
    argument.append(var)
    newProposition=proposition[closeP+1:len(proposition)]
    argument=argument+newProposition
    if findFirst(argument, '(') != -1:
        eliminateParentheses(argument)
    else:
        saveOperation(argument)
        op.evaluate()

#-------------------------------------------------------------------------------------------------------
def renameExpressions(var,exp):
    if(len(v.variables)==1):
        op.evaluate(v.variables,var)
    for key, values in v.variables.items():
        for i in values:
            if i==var:
                pos=v.variables[key].index(i)
                v.truthTable[exp]=v.tableValues[exp]
                v.variables[key][pos]=exp
                op.evaluate(v.variables[key],key)
                return
#-------------------------------------------------------------------------------------------------------            
def saveOperation(op):
    var='v'+str(v.variable)
    v.variables[var]=op
    v.variable=v.variable+1
    return var
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
            