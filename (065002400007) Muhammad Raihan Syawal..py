# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 22:01:05 2024

@author: Administrator
"""

# Dapatkan panjang dan lebar ruangan dari pengguna
panjang = float(input("Masukkan panjang ruangan: "))
lebar = float(input("Masukkan lebar ruangan: "))

# Dapatkan satuan pengukuran dari pengguna
satuan = input("Masukkan satuan pengukuran (meter atau inci): ")

# Hitung luas
luas = panjang * lebar

# Konversi luas ke inci persegi jika satuan adalah meter
if satuan.lower() == "meter":
    luas_inci = luas * 1550
    print(f"Luas ruangan adalah {luas} meter persegi atau {luas_inci} inci persegi.")
else:
    print(f"Luas ruangan adalah {luas} inci persegi.")