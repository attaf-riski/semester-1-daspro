# Nama File : 10.aritmatic_v2.py
# Deskripsi : Mencari jumlah total nilai pada deret aritmatika tingkat 3 sampai suku tertentu
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal 24 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# arith_v2: integer > 0 --> integer
#   {arith_v2(n): Menghasilkan jumlah/sum dari semua deret, 
#    Dimana rumus mencari suku n adalah = Un = nˆ2
#    arith_v2(n) =  arith_v2(n-1) + nˆ2}

# REALISASI
def arith_v2(n):
    if n == 1: #basis 1
        return 1
    else: 
        return arith_v2(n-1) + n**2

# APLIKASI
print("===Program Start===")
print(arith_v2(1))
print(arith_v2(2))
print(arith_v2(3))
print(arith_v2(4))
print(arith_v2(5))
print("===Program End, Thanks===")