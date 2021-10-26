# Nama File : fac_v3.py
# Deskripsi : Menghitung faktorial dari sebuah bilangan integer secara rekursif (INI ADALAH CONTOH YANG SALAH)
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 21 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# fac: integer > 0 --> integer > 0
#   {fac(n) = n! sesuai dengan definisi rekursif faktorial versi 3, yaitu RUMUS BENAR TAPI PROGRAM SALAH}

# REALISASI
# Realisasi dengan definisi faktorial fac(n) = n! dimana
# Jika n = 1 : n! = 1
# Jika n > 1 : n! =  (n+1)! / (n+1)

def fac(n):
    if n == 1: #basis 1
        return 1
    else:
        return fac(n+1) / (n + 1)

# APLIKASI
print("===Program Start===")
print(fac(1))
print(fac(3))
print(fac(5))
print("===Program End, Thanks===")