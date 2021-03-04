#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:14:06 2021

@author: danielaesparza jenniferhernandez
"""

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
