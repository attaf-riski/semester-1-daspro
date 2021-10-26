# Nama File : 1.min.py
# Deskripsi : pengurangan dua bilangan bulat menggunakan fungsi rekursif
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 23 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# min: 2 integer --> integer
#   {min(x,y): dimana x akan dikurangi y
#    jika y > 0 : x-y = x - y
#                     = x - y(-1) - 1 
#                     = x - y(-2) - 1 - 1
#    jika y < 0 : x-y = x - (-y)
#                     = x - (-y(+1)) - (-1)
#                     = x - (-y(+2)) - (-1) - (-1)

# REALISASI
#loncat 2 agar dicacah per dua
def min(x,y):
    if y == 0: #basis 0
        return x
    else: # y != 0
        if y>0:
            if y%2 == 0:
                return min(x,y-2) - 2 
            else: #y%2 = 1
                return min(x,y-1) - 1 
        else: # y < 0
            if y%2 == 0:
                return min(x,y+2) - -2
            else: #y%2 = 1
                return min(x,y+1) - -1 

# APLIKASI
print("===Program Start===")
print(min(7,9)) #-2
print(min(-7,9)) #-16 
print(min(7,-9)) #16
print(min(-7,-9)) #2
print("===Program End, Thanks===")