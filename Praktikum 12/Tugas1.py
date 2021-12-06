# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:30:15 2021

@author: Surgery Adhi Nugroho
NIM: 065002100015
"""
class mahasiswa:
    jumlah = 0
    def __init__(self,nama,nim,tahun):
        self.nama=nama
        self.nim=nim
        self.tahun=tahun
        mahasiswa.jumlah+=1
    
    def printmahasiswa(self):
        print('Nama: '+ self.nama + '\nNIM : '+ str(self.nim) + '\nAngkatan: '+ str(self.tahun))

nama=input("Masukkan namamu : ")
nim=str(input("Masukkan NIM kamu : "))
tahun=str(input("Masukkan tahun angkatanmu : "))

x = mahasiswa(nama,nim,tahun)
x.printmahasiswa()

print('Total mahasiswa: ',mahasiswa.jumlah)
