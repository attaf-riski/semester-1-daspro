# Nama File : 6.mul3.py
# Deskripsi : Mengalikan sebuah bilangan dengan nilai 3 menggunakan rekursif
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal 24 Oktober 2021


# DEFINISI DAN SPESIFIKASI
# mul3: 2 integer --> integer
#   {mul3(x): mengalikan 3 dengan x,
#     jika x > 0 : 3 * x = x(-1) + 3
#     jika x < 0 : 3 * x = x(+1) - 3 }

# REALISASI
def mul3(x):
    if x == 0: #basis 0
        return 0
    else: #x != 0
        if x > 0 :
            return mul3(x-1) + 3
        else: # x < 0
            return mul3(x+1) - 3

# APLIKASI
print("===Program Start===")
print(mul3(1))
print(mul3(2))
print(mul3(3))
print(mul3(-4))
print("===Program End, Thanks===")