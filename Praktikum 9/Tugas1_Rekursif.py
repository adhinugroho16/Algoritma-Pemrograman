# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 13:23:36 2021

@author: Surgery Adhi Nugroho
NIM: 065002100015
"""
jumlah = 0
angka = 0
bil = 1

def penjumlahan(jumlah = 0,angka = 0,bil = 1):
    if (angka<=0):
        return 0
    else :
       jumlah=int(input("Masukan Bilangan ke-"+ str(bil) +":"))
       if (angka==1):
           return jumlah
       else:
           bil+=1
           return jumlah + penjumlahan(jumlah, angka-1,bil)
    
total=int(input("Masukan Jumlah: "))
hasil=penjumlahan(angka=total)
print("Hasil dari penjumlahan adalah:"+ str(hasil))
