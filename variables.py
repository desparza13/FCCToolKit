#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:14:06 2021

@author: danielaesparza jenniferhernandez
"""
#--------------GENERAL--------------------------------------------------------
menuChoice=1
#--------------GENERADOR DE TABLAS DE VERDAD----------------------------------
expressions={"P":[], "Q":[], "R":[], "S":[], "T":[], "U":[], "V":[], "W":[], "X":[], "Y":[], "Z":[]
,"~P":[], "~Q":[], "~R":[], "~S":[], "~T":[], "~U":[], "~V":[], "~W":[], "~X":[], "~Y":[], "~Z":[]}

connectors={"^":0, "v":1, "->":2, "<->":3} 

variable=0
variables={}

values={}
tableValues={}

separator= "                                             "

rows=0
truthTable={}
finalsTable={}
finalTable={}
argument=""


proposition = ""
arguments=""
#------------------------------------------------------------------------------
#------------------CALCULADORA DE CONJUNTOS------------------------------------

a=0
b=0
c=0
chosenOperation=0
operation=0
newSet=[]
endCalculator=False
#------------------------------------------------------------------------------
#------------------CALCULADORA DE SUCESIONES------------------------------------
limInferior=0
limSuperior=0
formula=""
elementos=[]
suma=0
producto=1
endSuccessions=False
#------------------------------------------------------------------------------
#-------------------RELACIONES Y FUNCIONES-------------------------------------
pairsQuantity=1
xCoords=[]
yCoords=[]
dominio=[]
codominio=[]
x=0
y=0
noFuncionY=[]
noFuncionX=1000












