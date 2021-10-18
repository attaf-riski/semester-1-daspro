# Nama File : permutasi_kombinasi.py
# Nama Pembuat File : Attaf Riski Putra Ramadhan
# Tanggal Pembuatan File: 18 Oktober 2021
# Deskripsi File : Membuat fungsi permutasi dan kombinasi dengan bantuan fungsi faktorial-rekursif

# DEFINISI DAN SPESIFIKASI
# FaktorialRekursif: integer>=0 -->  integer>0
#   {FaktorialRekursif(n): Menghasilkan nilai faktorial dari n menggunakan fungsi rekursif.}

# Permutasi: integer >= 0, integer >=0 --> integer>0
#   {Permutasi(n,r): Menghasilkan jumlah cara penyusunan dari nilai yang diberikan dengan memperhatikan urutan objek.
#     n adalah banyaknya objek yang dapat dipilih, r adalah jumlah yang harus dipilih.
#     Dimana n >= r}

# Kombinasi: integer >= 0, integer >=0 --> integer>0
#   {Kombinasi(n,r): Menghasilkan jumlah  cara penyusunan dari nilai yang diberikan tanpa memperhatikan urutan objek.
#    n adalah banyaknya objek yang dapat dipilih, r adalah jumlah yang harus dipilih. 
#    Dimana n >= r}

# REALISASI
def faktorial_rekursif(n):
    if n == 0:
        return 1
    else: # n > 0
        return n * faktorial_rekursif(n - 1)

def permutasi(n,r):
    return faktorial_rekursif(n) // faktorial_rekursif(n - r)

def kombinasi(n,r):
    return faktorial_rekursif(n) // (faktorial_rekursif(r) * faktorial_rekursif(n - r))

# APLIKASI
print("===PROGRAM PERMUTASI & KOMBINASI===")
print(faktorial_rekursif(5)) # adalah 120
print(permutasi(6,2)) # adalah 30
print(kombinasi(6,2)) # adalah 15
print("===TERIMAKASIH===")
