# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 14:28:15 2021

@author: Surgery Adhi Nugroho
NIM: 065002100015
"""
print("Rekursif perpangkatan")

def pangkat(bil,power):
    if (bil == 0):
        return 0
    elif (bil == 1):
        return 1
    
    else:
        
        if (power <= 0):
            min = 1 / (bil * pangkat(bil,power -1))
            return min
        elif (power == 0):
            return 1
        elif (power == 1):
            return bil
        elif (power >= 1):
            return bil * pangkat (bil,power - 1)
        else:
            print("Progam error atau masukkan data dengan benar")
            
def mulai(bilangan = 0,bil_pangkat = 0):
    print("Progam pemangkatan rekursif ")
    bilangan = int(input("Masukkan bilangan : "))
    bil_pangkat = int(input("Masukkan pangkat : "))
    jumlah = pangkat(bil = bilangan,power = bil_pangkat)
    print("Hasil dari",bilangan,'pangkat',bil_pangkat,'adalah',jumlah)
    input_ulang()
    
def input_ulang():
    print("Masukkan YA atau TIDAK untuk menjalankan progam berikutnya")
    print("Masukkan input sesuai kriteria atau progam tidak akan berjalan selanjutnya")
    ulang = input("YA / TIDAK : ")
    if ulang == 'YA':
        mulai()
    elif ulang == 'TIDAK':
        print("Terima Kasih sudah menggunakan program ini")
    else:
        input_ulang()
        
mulai()
    
            
     
