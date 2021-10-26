# Nama File : 7.integer.py
# Deskripsi : Mencari jumlah total nilai pada deret integer dari 1 hingga nilai tertentu
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal 24 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# integ: integer > 0 --> integer
#   {integ(n): Menghasilkan total jumlah/sum dari integer 1 hingga integer n
#    integ(n) = integ(n-1) + n
#             = integ(n-2) + n-1 + n

# REALISASI
def integ(n):
    if n == 1: #basis1
        return 1
    else:
        return integ(n-1) + n

# APLIKASI
print("===Program Start===")
print(integ(1))
print(integ(2))
print(integ(3))
print(integ(4))
print(integ(5))
print("===Program End, Thanks===")