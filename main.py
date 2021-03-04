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


print("                      _                 _    _                                                      ")
print("                     | |               | |  | |                                                      ")
print(" _|_  ,_         _|_ | |      _|_  __, | |  | |  _     __,  _   _  _    _   ,_    __, _|_  __   ,_   ")
print("  |  /  |  |   |  |  |/ \      |  /  | |/ \_|/  |/    /  | |/  / |/ |  |/  /  |  /  |  |  /  \_/  |  ")
print("  |_/   |_/ \_/|_/|_/|   |_/   |_/\_/|_/\_/ |__/|__/  \_/|/|__/  |  |_/|__/   |_/\_/|_/|_/\__/    |_/")
print("                                                        /|                                           ")
print("                                                        \|                                           ")
v.proposition=input(">>")
v.arguments=v.proposition.split(' ')
t.createTable(v.arguments)
su.findParentheses(v.arguments)
t.orderTable(v.tableValues)

    
