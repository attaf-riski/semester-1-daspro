# Nama File : 2.mul.py
# Deskripsi : Mengalikan dua buah bilangan dengan metode fungsi rekursif
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal 24 Oktober 2021


# DEFINISI DAN SPESIFIKASI
# mul: 2 integer --> integer
#   {mul(x,y): mengalikan x dengan y,
#     jika y > 0 : x * y = x + x * y(-1)
#     jika y < 0 : x * y = x - x * y(+1) }

# REALISASI
def mul(x,y):
    if y == 0: #basis 0
        return 0
    else: #y != 0
        if y > 0 :
            return mul(x,y-1) + x
        else: # y < 0
            return mul(x,y+1) - x

# APLIKASI
print("===Program Start===")
print(mul(6,7))
print(mul(10,-10))
print(mul(-7,10))
print(mul(-5,-5)) 
print("===Program End, Thanks===")