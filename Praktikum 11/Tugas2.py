# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 16:38:22 2021

@author: Surgery Adhi Nugroho
NIM: 065002100015
"""

class bubbleSort:
	
	def __init__(self, number):
		self.number = number
		self.length = len(number)
        
	def __str__(self):
		return ", ".join([str(x) for x in self.number])
    
	def Rekursif(self, n = None):
		if n is None:
			n = self.length
		if n == 1:
			return
        
		for a in range(n - 1):
			if self.number[a] > self.number[a + 1]:
				self.number[a], self.number[a + 1] = self.number[a + 1], self.number[a]
		self.Rekursif(n - 1)

def main():
	number = [4,1,3,-2,8,9,5]
	print('List Sebelum disorting:\n',number)
	sort = bubbleSort(number)
	sort.Rekursif()
	print("List yang sudah disorting:\n",sort)
    
if __name__ == "__main__":
	main()
