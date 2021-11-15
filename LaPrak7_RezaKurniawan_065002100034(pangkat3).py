# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 07:23:20 2021

@author: RezaKurniawan
"""
print('PROGRAM PENGECEKAN BILANGAN')
def pertama(angka):
	return angka ** 3
	
def kedua(angka):
	if angka % 3 == 0:
		return pertama(angka)
	return False

angka = int(input("Masukkan bilangan: "))
output = kedua(angka)
print(f"Hasil: {output}")
