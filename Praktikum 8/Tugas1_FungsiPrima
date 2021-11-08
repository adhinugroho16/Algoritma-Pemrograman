# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:38:52 2021

@author: Surgery Adhi Nugroho
NIM: 065002100015
"""

def cekbilangan(bil):
    if bil == 1:
        print(f"bilangan dari {bil} adalah bilangan prima")
    elif bil == 2:
        print(f"bilangan dari {bil} adalah bukan bilangan prima")
    else:
        global x 
        for x in range(2, bil):
            if bil%x==0:
                stat = 0 
                break
            else: 
                stat = 1 
        cekstat(stat)

def cekstat(stat):
    if stat == 0:
        print(f"bilangan dari {bil} adalah bukan bilangan prima")
        print(f"{x} kali {bil//x} = {bil}")
    else:
        print(f"{bil} adalah bilangan prima")

x = 1
while x == 1:                    
    bil = int(input("Masukkan bilangan : "))
    cekbilangan(bil)                 
bil = int(input("Masukkan bilangan : "))
cekbilangan(bil)
