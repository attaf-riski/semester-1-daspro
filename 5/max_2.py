# Nama file : max_2.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 18 September 2021
# Deskripsi : menentukan nilai maksimum dari 2 bilangan integer

# DEFINISI DAN SPESIFIKASI
# max_2 : 2 integer --> integer
#   max_2(a,b) menentukan nilai maksimum dari 2 bilangan integer a dan b

# REALISASI
def max_2(a,b) :
    return (a if a >= b else b)

# APLIKASI
print(max_2(4,9)) # Hasilnya 9
print(max_2(100,-20)) # Hasilnya 100
print(max_2(10,10)) # Hasilnya 10
