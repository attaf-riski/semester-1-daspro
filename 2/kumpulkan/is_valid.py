# Nama file : is_valid.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 4 September 2021
# Deskripsi : Menerima sebuah besaran integer, dan menentukan apakah bilangan tersebut valid.
#               Bilangan disebut valid jika nilainya kurang dari 5 atau lebih dari 500. Jadi bilangan di antara 5 dan 500 tidak valid.

# Definisi dan spesifikasi
# is_valid : integer --> boolean
#   is_valid(x) akan menghasilkan nilai benar / True apabila x bernilai kurang dari 5 atau lebih dari 500. Bilangan selain itu akan False.

# Realisasi
def is_valid(x):
    return x < 5 or x > 500

# Aplikasi
print(is_valid(5)) # hasilnya False
print(is_valid(0)) # hasilnya True
print(is_valid(500)) # hasilnya False
print(is_valid(6000)) # hasilnya True
