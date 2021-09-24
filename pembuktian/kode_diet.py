# Nama file : kode_diet.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 22 September 2021
# Deskripsi : kode diet

# Definisi dan Spesifikasi


# Realisasi
def kode_diet(bb,jk):
    if jk <= 1000 :
        return "DC" + str(jk) + "B" + str(bb)
    elif jk > 1000 and jk < 2000:
        return "DL" + str(jk) + "B" + str(bb)
    elif jk > 2000:
        return "DS" + str(jk) + "B" + str(bb)
    

# Aplikasi
print(kode_diet(60,1500))
print(kode_diet(50,900))
print(kode_diet(70,2500))
