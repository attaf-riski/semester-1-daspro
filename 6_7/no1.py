# Nama File : no1.py
# Nama Pembuat File : Attaf Riski Putra Ramadhan
# Tanggal Pembuatan : 8 Oktober 2021
# Deskripsi : Mencari ekuivalen dalam bentuk desimal dari bentuk pecahan campuran 

# DEFINISI DAN SPESIFIKASI
# PC_To_Des: integer, integer >= 0, integer > 0 --> real
#   {PC_To_Des(bil,n,d) Menghasilkan nilai desimal dari pecahan campuran, pecahan campuran dibentuk dari <bil,n,d>:
#    Jika bil >= 0 maka (bil * d + n)/d,
#    Jika bil < 0 maka (bil * d - n)/d}

# REALISASI
def pc_to_des(bil,n,d):
    if bil >= 0:
        return (bil*d + n)/d
    else:
        return (bil*d - n)/d

# APLIKASI
print("\n===WELCOME IN PECAHAN CAMPURAN TO DESIMAL===\n")
print("Nilai desimal dari pecahan campuran <2,1,2> adalah: {}".format(pc_to_des(2,1,2)))
print("Nilai desimal dari pecahan campuran <-2,1,2> adalah: {}".format(pc_to_des(-2,1,2)))
print("\n===THANKS===\n")