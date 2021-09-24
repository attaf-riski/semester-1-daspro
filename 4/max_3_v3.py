# Nama file : max_3_v1.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 18 September 2021
# Deskripsi : menentukan nilai maksimum dari 3 bilangan integer

# DEFINISI DAN SPESIFIKASI
# max_3 : 3 integer --> integer
#   max_3(a,b, c) menentukan nilai maksimum dari 3 bilangan integer yang
#       berlainan a, b, dan c, menggunakan ekspresi kondisional versi 3

# REALISASI
def max_3(a,b, c) :
    if a>b :
        if a>c :
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c

# APLIKASI
print(max_3(12, 7, 5)) # Hasilnya 12
print(max_3(4,9,-10)) # Hasilnya 9
print(max_3(100,-20,300)) # Hasilnya 300
