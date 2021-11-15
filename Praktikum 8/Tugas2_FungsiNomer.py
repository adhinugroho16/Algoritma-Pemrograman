# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 12:40:15 2021

@author: Surgery Adhi Nugroho
NIM: 065002100015
"""

bil = False

def ordinal_number(ordinal):
    if ordinal in [10,11,12,13]:
        print(ordinal,"th")
    else:
        angka = ordinal % 10
        if angka==1:
           print(ordinal,"st")
        elif angka==2:
            print(ordinal,"nd")
        elif angka==3:
            print(ordinal,"rd")
        else:
            print(ordinal,"th")
            
while (not bil):
    print("Masukkan 0 untuk menghentikan program")
    ordinal = int(input("Masukan Angka: "))
    
    if ordinal == 0:
        bil = True
        print("Terimakasih sudah menggunakan program ini")
    else:
        ordinal_number(ordinal)
