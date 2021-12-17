# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 09:31:38 2021

@author: Surgery Adhi Nugroho
NIM: 065002100015
"""
import panda as pd
df = pd.read_csv("Negara.csv")
mean = df.groupby(["Benua"]).mean()
std = df.groupby(["Benua"]).std()
print(df)
print(mean)
print(std)
