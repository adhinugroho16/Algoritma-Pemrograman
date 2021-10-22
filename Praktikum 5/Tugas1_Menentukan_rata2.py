# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 13:18:10 2021
@author: Surgery Adhi Nugroho
NIM: 065002100015
"""

n = '0'
jumlah = 0
lanjut = 0

while (n != "") :
    n = str(input("Masukkan nilai :  "))
    lanjut = lanjut + 1
    if (n == ''):
        break ;
    elif (n== 'A'):
        print ("nilai = 4.00")
        jumlah += 4.00
    elif (n == 'A-'):
        print ("nilai = 3.75")
        jumlah += 3.75
    elif (n== 'B+'):
        print ("nilai = 3.50")
        jumlah += 3.50
    elif (n == 'B'):
        print ("nilai = 3.00")
        jumlah += 3.00
    elif (n== 'B-'):
        print ("nilai = 2.75")
        jumlah += 2.75
    elif (n == "C+"):
        print ("nilai = 2.50")
        jumlah += 2.50
    elif (n == "C"):
        print ("nilai = 2.00")
        jumlah += 2.00
    elif (n == "C-"):
        print ("nilai = 1.75")
        jumlah += 1.75
    elif (n == "D"):
        print ("nilai = 1.50")
        jumlah += 1.50
    elif (n == "E"):
        print ("nilai = 1.25")
        jumlah += 1.25
    else :
        lanjut = lanjut-1
        print ("error atau masukkan nilai yang benar :")
if (lanjut ==1):
        print ("rata ratanya adalah 0")
else :
        avg  = jumlah/(lanjut-1)
        print ("rata ratanya adalah :", avg)
