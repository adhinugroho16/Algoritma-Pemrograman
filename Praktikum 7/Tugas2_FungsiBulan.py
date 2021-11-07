@author: Surgery Adhi Nugroho
NIM: 065002100015
"""

def variable (bulan = 0, tahun= 0, z = 0):
    while  (bulan >-3) :
        bulan += bulan 
        bulan= int(input("Masukan bulan dalam bilangan 1 - 12 : "))
        tahun = int(input("Masukan tahun :  "))
        if (bulan >= 13) or (bulan <= 0) and not (bulan == -1) :
            print ("Progam error atau masukan nilai yang benar ")
            print ("Masukan -1 pada nilai untuk menghentikan progam ")
        
        elif (bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12):
            print ("Jumlah hari dalam bulan",bulan , "pada tahun" ,tahun ," adalah 31 hari ")
            print ("Masukan -1 pada nilai untuk menghentikan progam ")
        elif (bulan == 2):
            
            if (tahun %4 == 0) and (bulan == 2) :
                print ("Jumlah hari dalam bulan" ,bulan ,"pada tahun" ,tahun ,"adalah 29 hari")
                print ("Masukan -1 pada nilai untuk menghentikan progam ")
            else : 
                print("Jumlah hari dalam bulan" ,bulan ,"pada tahun" ,tahun ,"adalah 28 hari")
                print ("Masukan -1 pada nilai untuk menghentikan progam ")
        elif (bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11 ) :
            print ("Jumlah hari dalam" ,bulan , "pada tahun" ,tahun ,"adalah 30 hari")
            print ("Masukan -1 pada nilai untuk menghentikan progam ")
        if (bulan == -1):
           return (bulan) 
       

variable ()  
print ("program berhenti")
