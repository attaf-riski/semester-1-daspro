# Nama File : plus.py
# Deskripsi : penjumlahan dua bilangan bulat
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 21 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# plus: 2 integer > 0 --> integer > 0
#   {plus(x,y): menjumlahkan x dan y
#    plus(x,y) = x + y
#              = x + 1 + y(-1)}

# REALISASI
def plus(x,y):
    if y == 0: #basis 0
        return x
    else: #rekurens
        return 1 + plus(x,y-1)

# APLIKASI
print("===Program Start===")
print(plus(4,0))
print(plus(4,1))
print(plus(5,5))
print("===Program End, Thanks===")
