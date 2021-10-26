# Nama File : fac_v2.py
# Deskripsi : Menghitung faktorial dari sebuah bilangan integer secara rekursif
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 21 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# fac: integer >= 0 --> integer > 0
#   {fac(n) = n! sesuai dengan definisi rekursif faktorial, versi 2 dengan basis = 0}

# REALISASI
# Realisasi dengan definisi faktorial fac(n) = n! dimana
# Jika n = 0 : n! = 1
# Jika n > 0 : n! = n * (n-1)!

def fac(n):
    if n == 0: #basis 0
        return 1
    else:
        return n * fac(n-1)

# APLIKASI
print("===Program Start===")
print(fac(0))
print(fac(1))
print(fac(3))
print(fac(6))
print("===Program End, Thanks===")