# Nama file : point.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 24 September 2021
# Deskripsi : Membuat tipe bentukan point beserta konstruktor dan selektornya

from math import sqrt
from pangkat2 import fx2

# DEFINISI TYPE
# type point : <x:real, x:real>
#   {<x,y> adalah sebuah point, dengan x adalah absis dan y adalah ordinat}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePoint : 2 real --> point
#   {MakePoint(x,y) membentuk sebuah point dari a dan b dengan a sebagai absis dan b sebagai ordinat}
# REALISASI (dalam python)
class Point:
    def __init__(self,a,b):
        self.x = a
        self.y = b

# DEFINISI DAN SPESIFIKASI SELEKTOR
# absis: point --> real
#   {absis(P) memberikan absis point P}
# REALISASI (dalam python)
def absis(P):
    return P.x

# ordinat: point --> real
#   {ordinat(P) memberikan ordinat point P}
# REALISASI (dalam python)
def ordinat(P):
    return P.y

# DEFINISI DAN FUNGSI PREDIKAT
# IsOrigin?: point --> boolean
#   {IsOrigin?(P) benar jika P adalah titik origin <0,0>
# REALISASI (dalam python)
def is_origin(P):
    return absis(P) == 0 and ordinat(P) == 0

# DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI LAIN TERHADAP POINT
# jarak: 2 point --> real
#   {jarak(P1,P2) menghitung jarak antara 2 point P1 dan P2}
# REALISASI (dalam python)
def jarak(P1,P2):
    return sqrt( fx2(absis(P1) - absis(P2)) + fx2(ordinat(P1) - ordinat(P2)) )

# jarak0: 2 point --> real
#   {jarak0(P) menghitung jarak antara point P dengan titik origin <0,0>}
# REALISASI (dalam python)
def jarak_0(P):
    return sqrt( fx2(absis(P)) + fx2(ordinat(P)) )

# kuadran: point --> integer
#   {kuadran(P) mengembalikan kuadran dimana point P berada, dengan syarat P bukan titik <0,0>, tidak terletak di sumbu X maupun Y}
# REALISASI (dalam python)
def kuadran(P):
    if (absis(P) > 0) and (ordinat(P) > 0):
        return 1
    elif (absis(P) < 0) and (ordinat(P) > 0):
        return 2
    elif (absis(P) < 0) and (ordinat(P) < 0):
        return 3
    elif (absis(P) > 0) and (ordinat(P) < 0):
        return 4
    
# APLIKASI
print("=====SELAMAT DATANG DI PROGRAM TIPE BENTUKAN POINT/Titik=====\n")
Titik_1 = Point(3,9)
print("Titik_1 terbentuk dengan:")
print("Absis dari Titik_1 adalah: {0} dan Ordinat dari Titik_1 adalah: {1}".format(absis(Titik_1),ordinat(Titik_1)))
print("Apakah Titik_1 origin? {0}".format(is_origin(Titik_1)))
print("Jarak Titik_1 ke origin adalah: {0}".format(jarak_0(Titik_1)))
print("Kuadran dari Titik_1 adalah: {0}".format(kuadran(Titik_1)))

Titik_2 = Point(2,4)
print("\nTitik_2 terbentuk dengan:")
print("Absis dari Titik_2 adalah: {0} dan Ordinat dari Titik_2 adalah: {1}".format(absis(Titik_2),ordinat(Titik_2)))
print("Apakah Titik_2 origin? {0}".format(is_origin(Titik_2)))
print("Jarak Titik_2 ke origin adalah: {0}".format(jarak_0(Titik_2)))
print("Kuadran dari Titik_2 adalah: {0}".format(kuadran(Titik_2)))

print("\nJarak antara Titik_1 dan Titik_2 adalah: {0}".format(jarak(Titik_1,Titik_2)))
print("\n=====PROGRAM BERAKHIR, TERIMAKASIH=====")









