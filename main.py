#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 13:58:58 2021

@author: danielaesparza
"""
import variables as v
import setUp as su
import tables as t
import operations as op
from colorama import Back,Fore,Style,init
import programSetUp as psu
import setUpSets as sus
init(autoreset=True)

psu.menu()
print(v.menuChoice)
if(v.menuChoice==1):
    print("No F")
    su.truthTableLoop()
elif(v.menuChoice==2):
    sus.setsLoop()





    
