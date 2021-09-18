# Nama file : is_an_A.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 4 September 2021
# Deskripsi : Menerima sebuah karakter dan bernilai benar jika karakter tersebut adalah huruf 'A'

# Definisi dan spesifikasi
# is_an_A : character --> boolean
#   is_an_A(c) akan menghasilkan nilai benar / True apabila c adalah karakter(huruf) 'A'

# Realisasi
def is_an_A(c):
    return c == 'A'

# Aplikasi
print(is_an_A('a')) # hasilnya False
print(is_an_A('A')) # hasilnya True
print(is_an_A('z')) # hasilnya False
