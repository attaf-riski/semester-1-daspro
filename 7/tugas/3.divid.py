# Nama File : 3.divid.py
# Deskripsi : Membagi bilangan integer dengan metode fungsi rekursif
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal 24 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# divid: integer >=0, integer > 0 --> integer
#   {divid(x,y): Membagi bilangan integer x dengan integer y tanpa menyertakan nilai desimal
#     x / y = 1 + divid(x-y,y) }

# REALISASI 
def divid(x,y):
    if x < y:# basis 0
        return 0
    else: #rekurens
        return 1 + divid(x-y,y)

# APLIKASI
print("===Program Start===")
print(divid(30,5))
print(divid(0,8))
print(divid(50,10))
print("===Program End, Thanks===")