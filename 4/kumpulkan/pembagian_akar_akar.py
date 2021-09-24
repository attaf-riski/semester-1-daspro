# Nama file : pembagian_akar_akar.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 19 September 2021
# Deskripsi : Menghitung hasil pembagian akar-akar suatu persamaan dengan cara akar lebih besar dibagi akar yang kecil.


# DESKRIPSI DAN SPESIFIKASI
# max_2 : 2 integer -> integer
#   max_2(a,b) menghasilkan nilai terbesar dari a dan b

# min_2 : 2 integer -> integer
#   min_2(a,b) menghasilkan nilai terbesar dari a dan b 

# akar_1 : 3 integer -> real
#   akar_1(a,b,c) akan mencari akar dari persamaan ax^2 + bx + c = 0 dengan rumus abc dengan tanda positif

# akar_2 : 3 integer -> real
#   akar_2(a,b,c) akan mencari akar dari persamaan ax^2 + bx + c = 0 dengan rumus abc dengan tanda negatif

# pembagian_akar : 3 integer --> real
# pembagian_akar(a,b,c) menghasilkan nilai pembagian dari akar terbesar dibagi akar terkecil dari persamaan kuadrat
#    ax^2 + bx + c = 0. Akar-akar bisa ditemukan menggunakan rumus abc.

# REALISASI
import math # untuk menggunakan fungsi math.sqrt()

def max_2(a,b) :
    return a if a >= b else b
    
def min_2(a,b) :
    return a if a <= b else b

def akar_1(a,b,c):
    return (-b + math.sqrt(b*b-4*a*c)) / (2*a)

def akar_2(a,b,c):
    return (-b - math.sqrt(b*b-4*a*c)) / (2*a)

def pembagian_akar(a,b,c):
    return max_2(akar_1(a,b,c),akar_2(a,b,c)) / min_2(akar_1(a,b,c),akar_2(a,b,c))

# APLIKASI
print(pembagian_akar(1,4,-21)) # Hasilnya adalah -0,428...
print(pembagian_akar(1,-7,12)) # Hasilnya adalah 1,333...






    













    
