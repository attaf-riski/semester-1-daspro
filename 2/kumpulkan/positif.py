# Nama file : positif.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 4 September 2021
# Deskripsi : Menerima sebuah bilangan bulat dan bernilai benar jika bilangan tersebut positif.

# Definisi dan spesifikasi
# is_positif : integer --> boolean
#   is_positif(x) akan menghasilkan nilai benar / True apabila x positif(x >= 0)

# Realisasi
def is_positif(x):
    return x >= 0

# Aplikasi
print(is_positif(1)) # hasilnya True
print(is_positif(0)) # hasilnya True
print(is_positif(-1)) # hasilnya False
