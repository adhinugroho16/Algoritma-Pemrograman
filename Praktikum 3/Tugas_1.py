# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:34:41 2021

@author: Surgery Adhi Nugroho
@NIM: 065002100015
Praktikum 3
"""
A = float(input('Masukan sisi A :  '))
B = float(input('Masukan sisi B :  '))
C = float(input('Masukan sisi C :  '))

if(A == B == C):
    print('ini adalah segitiga sama sisi')
elif((A == B) or (B == C) or (C == A)):
     print('ini adalah segitiga sama kaki')
elif((A + B <=C) or (A + C <= B) or (B + C <= A)):
    print('ini bukan termasuk segitiga')
else:
    print('ini adalah segitiga sembarang')     
     
    
    
