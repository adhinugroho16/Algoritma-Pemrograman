#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 10:46:42 2021

@author : Surgery Adhi Nugroho
NIM : 065002100015 
Progam perhitungan tiket
"""

n = '0'

jumlah = 0


while (n != ''):
    a = float(input("masukkan umur : "))

    if (a == 0):
        break ;

    elif (a <=2):
        print ("gratis")
        jumlah +=0
        print ("total harga tiket kamu : ", jumlah,"dollar")

    elif (a >= 3) and (a <=12):
        print ("harga tiket sebesar = 14.00 dollar ")
        jumlah += 14.00
        print ("total harga tiket kamu : ", jumlah,"dollar")

    elif (a >= 65):
        print ("harga tiket sebesar = 18.00 dollar")
        jumlah += 18.00
        print ("total harga tiket kamu : ", jumlah,"dollar")

    else :
        print ("harga tiket sebesar = 23.00 dollar ")
        jumlah += 23.00
        print ("total harga tiket kamu : ", jumlah,"dollar")

uang = float(input("masukkan jumlah uang berapa : "))
if (uang < jumlah):
     print ("uang kurang,kamu harus membayar sebesar :  ", jumlah,"dollar")
elif (uang >= jumlah):
    print ("kembalian", uang - jumlah,"dollar")
