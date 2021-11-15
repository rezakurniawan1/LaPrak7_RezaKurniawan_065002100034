# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 08:35:13 2021

@author: RezaKurniawan
"""

vokal = ['a', 'e', 'i', 'o', 'u']
konsonan = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

def vocal_konsonan(string):
	total_vokal, total_konsonan = 0, 0
	for x in vokal:
		total_vokal += string.count(x)
	for x in konsonan:
		total_konsonan += string.count(x)
	print(f"Jumlah huruf vokal adalah {total_vokal}")
	print(f"Jumlah huruf konsonan adalah {total_konsonan}")
		
string = input("Masukkan kalimat: ")
vocal_konsonan(string)
