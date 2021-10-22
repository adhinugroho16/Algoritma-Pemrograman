#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 13:35:48 2021
@author: Surgery Adhi Nugroho
NIM : 065002100015
"""

bulan = 1 - 12

hitung = False

print ("Progam menghitung bulan")
while (not hitung):
    print("-1 untuk menghentikan Progam")
    bulan = int(input("Masukkan bulan 1 - 12  : "))
    tahun = int(input("Masukkan tahun : "))

if(bulan >= 13 or bulan <= -2 or bulan == 0):
    print("Progam error atau bulan tidak ada dalam kalender")
elif(bulan == 1 or 3 or 5 or 7 or 8 or 10 or 12 ):
    print("Jumlah hari dalam bulan",bulan , "pada tahun" ,tahun ," adalah 31 hari" )
elif(bulan == 4 or 6 or 9 or 11 ):
    print("Jumlah hari dalam" ,bulan , "pada tahun" ,tahun ,"adalah 30 hari")
elif(bulan == 2 and tahun % 4 == 0):
    print("Jumlah hari dalam bulan" ,bulan ,"pada tahun" ,tahun ,"adalah 29 hari")
else:
    print("Jumlah hari dalam bulan" ,bulan ,"pada tahun" ,tahun ,"adalah 28 hari")
