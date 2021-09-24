# Nama file : absolut.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 18 September 2021
# Deskripsi : menentukan nilai absolut dari sebuah bilangan integer

# DEFINISI DAN SPESIFIKASI
# absolut : integer --> integer > 0
#   absolut(x) menentukan nilai absolut dari sebuah bilangan integer x

# REALISASI
def absolut(x):
    return (x if x>0 else 0 if x==0 else -x)

# APLIKASI
print(absolut(10)) # Hasilnya 10
print(absolut(0)) # Hasilnya 0
print(absolut(-10)) # Hasilnya 10
