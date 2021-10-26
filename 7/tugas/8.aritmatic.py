# Nama File : 8.aritmatic.py
# Deskripsi : Mencari jumlah total nilai pada deret aritmatika sampai suku tertentu
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal 24 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# arith: integer > 0 --> integer
#   {arith(n): Menghasilkan jumlah dari U1 sampai Un. 
#    Dimana rumus : Un = 3 + (n-1)3
#    arith(n) = arith(n-1) + (3+(n-1)3)

# REALISASI
def arith(n):
    if n == 1: #basis 1
        return 3
    else:
        return arith(n-1) + (3+(n-1)*3)

# APLIKASI
print("===Program Start===")
print(arith(2))
print(arith(3))
print(arith(4))
print(arith(5))
print("===Program End, Thanks===")

