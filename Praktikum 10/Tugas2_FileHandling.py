#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 10:35:58 2021

@author: Surgery Adhi Nugroho
NIM: 065002100015
"""
def nulis (data):
    file=open(NamaFile+".txt","w")
    file.write(data)
    file.close()
def baca ():
    file=open(NamaFile+".txt","r")
    text=file.read()
    print(text)
    file.close()
def nambah(data):
    file = open(NamaFile+'.txt', 'a')
    file.write(data)
    file.close()

a = True
while(a == True):
    print("===== program file handling =====")
    print("1. Membaca dan menulis file")
    print("2. Membaca File")
    print("3. Menambahkan Text pada file")
    print("4. Keluar dari program")
    answer = int(input("masukan angka pilihan kamu(1/2/3/4) : "))
    if answer == 1:
        NamaFile=input("Masukan nama file : ")
        Namamu=input("Masukan namamu : ")
        Nim=int(input("Masukan NIM kamu : "))
        Tahun=int(input("Masukan tahun angkatanmu : "))
        print("File Berhasil Dibuat")
        print("")
        print("")
        data=("\nNamamu:{}\nNim:{}\nAngkatan:{}").format(Namamu,Nim,Tahun)
        nulis(data)
    elif answer == 2:
        NamaFile=input("Masukan nama file : ")
        baca()
        print("")
        print("")
    elif answer == 3:
        NamaFile=input("Masukan nama file : ")
        sahabat=input("Masukan nama sahabatmu : ")
        tambahan=input("Masukan catatan tambahan kamu: ")
        data=("\nNama Sahabat:{}\nCatatan:{}").format(sahabat,tambahan)
        nambah(data)
    elif answer == 4:
        a = False
        print("terimaksih sudah menggunakan program saya")
