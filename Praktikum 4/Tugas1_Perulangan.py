#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 13:45:49 2021

@author: Surgery Adhi Nugroho
NIM: 065002100015
"""
n = int(input("Masukan angka =  "))
for i in range (n,0,-1):
    for j in range (1,i+1):
        print(i,end='')
    print()
