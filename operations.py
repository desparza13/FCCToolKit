#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:07:18 2021

@author: danielaesparza jenniferhernandez
"""
import variables as v
import setUps as su
import tables as t
#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
def logicAnd(arg1,arg2): #Regresa los valores de una operación Y a partir de dos valores
    if (arg1==True) and (arg2==True): #Solo regresa verdad si ambos lo son 
        return True
    else: #Cualquier otra combinación regresa un falso
        return False
#-------------------------------------------------------------------------------------------------------    
def logicOr(arg1,arg2): #Regresa los valores de una operación O a partir de dos valores
    if (arg1==False) and (arg2==False): #Solo regresa falso si ambos lo son
        return False
    else: #Cualquier otra combinación regresa verdadero
        return True
#-------------------------------------------------------------------------------------------------------    
def logicConditional(arg1,arg2): #Regresa los valores de una operación CONDICIONAL a partir de dos valores
    if (arg1==True)and(arg2==False): #Solo regresa Falso si el primero es True y el segundo False
        return False
    else: #Cualquier otra combinación regresa verdadero
        return True
#-------------------------------------------------------------------------------------------------------
def logicBiconditional(arg1, arg2): #Regresa los valores de una operación BICONDICIONAL a partir de dos valores
    if (arg1==True) and (arg2==False):
        return False
    elif (arg1==False) and (arg2==True):
        return False
    else: #Solo regresa verdadero si ambas son iguales
        return True
    
#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------   
def executeOperation(table, operator, arg1, arg2): #Ejecuta la operación indicada por el operador entre los argumentos que reciba y lo guarda en la tabla
    newPos = arg1+operator+arg2
    table[newPos]=[]
    for i, j in zip(table[arg1],table[arg2]):
        result=""
        if operator=="^":
            result=logicAnd(i, j)
        if operator=="v":
            result=logicOr(i, j)
        if operator=="->":
            result=logicConditional(i, j)
        if operator=="<->":
            result=logicBiconditional(i, j)
        table[newPos].append(result)
    return [newPos, table]
#-------------------------------------------------------------------------------------------------------
def evaluate(exps=[], var=-1): #Evalua las operaciones, necesita la ayuda de la ejecución de operación, marca el ritmo y hace que se operen todas las columnas como deben con recursividad
    if not exps:
        exps=v.variables['v'+str(v.variable-1)]
    argument2=""
    connector=""
    for exp in exps:
        if len(exp) == 2 and exp[0:1]=='v':
            newArgument=v.variables[exp]
            v.argument=''
            return evaluate(newArgument,exp)
        if (exp in v.expressions) or (exp in v.truthTable):
            v.tableValues[exp]=v.truthTable[exp]
            if v.argument == "":
                v.argument=exp
            elif exp!=v.argument:
                argument2=exp
                if v.argument==argument2:
                    v.argument=0
        if exp in v.connectors:
            connector=exp
        if (connector != "") and (v.argument!="") and (argument2!= ""):
            v.values=executeOperation(v.tableValues, connector, v.argument, argument2)
            v.argument=v.values[0]
            v.tableValues=v.values[1]
            connector=""
            argument2=""
            su.renameExpressions(var,v.argument)

#------------------------------------------------------------------------------------------------------- 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
            

