# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 19:41:24 2021

@author: Surgery Adhi Nugroho
NIM: 065002100015
"""
class OOP:
    def __init__(self,nama,nilai):
        self.nama = nama
        self.nilai = nilai
                
    def printtampil(self):
        print('Nama: ',self.nama,'\nNilai: ',str(self.nilai))
        
y = False 

while (not y ):
    try:    
        print("==== Progam OOP ====")
        print("1.Mendeklarasikan Objek")
        print("2.Menampilkan Objek")        
        print("3.Merubah Nilai Objek")
        print("4.Menghapus Objek")
        print("5.Keluar dari Program")
        print("")
        pilih = int(input("Masukkan pilihan angka(1/2/3/4/5): "))
        if pilih == 5:
            y = True
            print("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.")
        
        elif pilih == 1:
            nama = input('Masukkan namamu: ')
            nilai = input('Masukkan nilaimu: ')
            cetak = OOP(nama, nilai)
            print("Data Berhasil Ditambahkan\n")
            
        elif pilih == 2:
            cetak = OOP(nama, nilai)
            cetak.printtampil()
            print('\n')
            
        elif pilih == 3:
            rubah = input('Apa yang ingin diubah(nama/nilai): ')
            if rubah == 'nama':
                nama = input('Masukkan nama: ')
                print('Data Nama Berhasil Dirubah\n')
            if rubah == 'nilai':
                nilai = input('Masukkan nilai: ')
                print('Data Nilai Berhasil Dirubah\n')
        
        elif pilih ==4:
            print('Data berhasil dihapus\n')
            nama = ''
            nilai = ''
        
        else :
            print ("Progam tidak berjalan/masukkan data dengan tepat ! ")
            print("")
            
    except ValueError:
        print("Masukkan pilihan dengan benar!!\n")
