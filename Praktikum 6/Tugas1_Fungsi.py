# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:38:39 2021

@author: Surgery Adhi Nugroho
NIM : 065002100015
Praktikum 6
"""
print("Progam menghitung nilai dan rata rata ")
print("Nilai terdiri dari A,A-,B+,B,C+,C,C-")
print("Tekan ENTER untuk menghitung rata rata")

def nilai_siswa ():
    jumlah = 0    
    ulang = 1
    nomor = 0
    while ulang == 1:
        nomor += 1
        n = str(input('Masukkan nilai : '))
        if n == '': 
            nomor -= 1
            ulang = 0
        else:
            if n == 'A': 
                jumlah += float(4)
                nilai = '4'
            elif n == 'A-':
                jumlah += float(3.75)
                nilai = '3,75'
            elif n == 'B+':
                jumlah += float(3.50)
                nilai = '3,5'
            elif n == 'B':
                jumlah += float(3.00)
                nilai = '3'
            elif n == 'B-':
                jumlah += float(2.75)
                nilai = '2,75'
            elif n == 'C+':
                jumlah += float(2.50)
                nilai = '2,5'
            elif n == 'C':
                jumlah += float(2.00)
                nilai = '2'
            elif n == 'C-':
                jumlah += float(1.75)
                nilai = '1,75'
            else:
                print('data infalid')
                nomor -= 1
                nilai = '0'
            print(f"nilai ke-{nomor} = {nilai}")
    rata2 = jumlah / nomor
    return rata2

print("rata rata nilai adalah", nilai_siswa())
