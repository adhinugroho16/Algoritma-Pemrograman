# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 13:08:22 2021

@author: Surgery Adhi Nugroho
NIM: 065002100015
"""
import math

a = float(input("Berapa nilai A =  "))
b = float(input("Berapa nilai B =  "))
c = float(input("Berapa nilai C =  "))

nd = (b**2)-(4*a*c)
if(a==0):
    print("ini bukan sebuah persamaan kuadrat")
elif(nd==0):
    x1 = (-b/(2*a))
    print("persamaan kuadrat dari",a ,"x^2 +",b ,"x +",c )
    print("determinan dari =",nd)
    print("ini termasuk akar kembar")
    print("Akar",(x1))
elif(nd>0):
    x1 = (-b+(math.sqrt(nd)))/(2*a)
    x2 = (-b-(math.sqrt(nd)))/(2*a)
    print("persamaan kuadrat dari",a ,"x^2 +",b ,"x +",c )
    print("determinan dari =",nd)
    print("akarnya berbeda")
    print("Akar dari x1 dan x2 =  ",x1 ,x2)
elif(nd<0):
    print("persamaan kuadrat dari",a ,"x^2 +",b ,"x +",c )
    print("determinan dari =",nd)
    print("termasuk akar intejer")
    print(-b,"+akar",nd )
    print(-b,"-akar",nd )   
print("Terima Kasih")
    
