# Nama File : 7.aritmatic.py
# Deskripsi : Mencari jumlah total nilai pada deret geometri sampai suku tertentu
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal 24 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# geo: integer > 0 --> integer
#   {geo(n): Menghasilkan jumlah total/sum dari deret geometri dari suku pertama hingga suku ke-n
#    Rumus: Un = 1*3ˆn-1
#    geo(n) = geo(n-1) + (1*3ˆn-1)}

# REALISASI
def geo(n):
    if n == 1: #basis 1
        return 1
    else:
        return geo(n-1) + (1*3**(n-1))

# APLIKASI
print("===Program Start===")
print(geo(2))
print(geo(3))
print(geo(4))
print(geo(5))
print("===Program End, Thanks===")

