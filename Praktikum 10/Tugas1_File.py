#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 09:06:38 2021

@author: Surgery Adhi Nugroho
NIM: 065002100015
"""
def fungsidata (biodata):
    file = open ('Biodata.txt','w')
    file.write(biodata)
    file.close()
    
def write ():
    file = open ('Biodata.txt', 'r')
    text = file.read()
    print(text)
    file.close
    
nama = input ('Nama: ')
usia = input ('Usia: ')
alamat = input ('Alamat: ')
email = input ('Email: ')
pengajar = input ('Dosen Walimu: ')
biodata = 'Nama: {}\nUsia: {}\nAlamat: {}\nEmail: {}\nPengajar: {}'.format(nama,usia,alamat,email,pengajar)
print('')
print('Biodata Anda')
print('===================')
fungsidata(biodata)
write()
