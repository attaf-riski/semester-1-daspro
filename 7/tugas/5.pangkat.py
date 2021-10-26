# Nama File : 5.pangkat.py
# Deskripsi : Mencari pangkat dari suatu bilangan integer dengan metode rekursif
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 24 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# pangkat: integer, integer >= 0 --> integer
#   {pangkat(x,y): Menghasilkan pangkat y dari x}

# REALISASI
def pangkat(x,y):
    if y == 0: #basis 0
        return 1
    else:
        return x * pangkat(x,y-1)
    
# APLIKASI
print("===Program Start===")
print(pangkat(2,2))
print(pangkat(-5,3))
print(pangkat(10,2))
print(pangkat(3,0))
print("===Program End, Thanks===")
