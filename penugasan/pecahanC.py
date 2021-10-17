# Nama File : pecahanC.py
# Nama Pembuat File: Fa'iq Rinda Maulana
# Tanggal Pembuatan File : 7 Oktober 2021
# Deskripsi : Membentuk type bentukan pecahan campuran sebagai tugas matkul daspro

# DEFINISI TYPE
# pecahan: <n:integer >= 0 ,d:integer > 0 >
#   {<n,d> merupakan sebuah pecahan biasa, dengan n sebagai pembilang(numerator) dan d sebagai
#   penyebut(denumerator), n bilangan bulat positif dan d bilangan natural.}

# pecahanc : <bil:integer , n:integer >= 0 ,d:integer > 0 >
#   {<bil,n,d> adalah pecahan campuran, dengan bil sebagai bilangan, n sebagai pembilang(numerator) dan d sebagai penyebut(denumerator), bil merupakan bilangan bulat, n bilangan bulat positif dan d bilangan natural. }

# DEFINISI DAN SPESIFIKASI SELEKTOR
# pemb : pecahan --> integer
#   {pemb(P) memberikan numerator pembilang n dari pecahan biasa tersebut}
def pemb(P):
    return P[0]

# peny : pecahan --> integer
#   {peny(p)memberikan denumerator penyebut d dari pecahan biasa tersebut}
def peny(P):
    return P[1]

# bil : pecahanc --> integer
#   {bil(P) memberikan bilangan bil dari pecahan campuran tersebut}
def bil(P):
    return P[0]
    
# pemb_c : pecahanc --> integer
#   {pemb_c(P) memberikan numerator pembilang n dari pecahan campuran tersebut}
def pemb_c(P):
    return P[1]

# peny_c : pecahanc --> integer
#   {peny_c(P) memberikan denumerator penyebut d dari pecahan campuran tersebut}
def peny_c(P):
    return P[2]

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# make_pecahan : integer>=0, integer>0 --> pecahan
#   {make_pecahan (n,d) membentuk sebuah pecahan biasa dari pembilang n dan penyebut d, dengan n dan y adalah integer }
def make_pecahan(n,d):
    return [n,d]

# make_pecahan_c : integer, integer>=0, integer>0 --> pecahanc
#   {make_pecahan_c(bil,n,d) membentuk sebuah pecahn campuran dari bilangan bil, pembilag n, dan penyebut d, dengan bil, n, dan d adalah integer}
def make_pecahan_c(bil,n,d):
    return [bil,n,d]


# DEFINISI DAN SPESIFIKASI OPERATOR
# konversi_pecahan : pecahanc --> pecahan
#   {konversi_pecahan(P) mengubah pecahan campuran P ke tipe pecahan biasa}
def konversi_pecahan(P):
    if bil(P) >= 0:
        return make_pecahan(bil(P) * peny_c(P) + pemb_c(P), peny_c(P))
    else:
        return make_pecahan(bil(P) * peny_c(P) - pemb_c(P), peny_c(P))

# konversi_real : pecahanc --> real
#   {konversi_real(P) mengubah pecahan campuran P ke bilanagn desimal}
def konversi_real(P):
    return pemb(konversi_pecahan(P)) / peny(konversi_pecahan(P))

# add_p : pecahanc --> pecahanc
#   {add_p(P1,P2) menjumlahkan pecahan campurang P1 dengan pecahan campuran P2}
def add_p(P1,P2):
    return make_pecahan_c(((pemb(konversi_pecahan(P1)) * peny(konversi_pecahan(P2))) + (pemb(konversi_pecahan(P2)) * peny(konversi_pecahan(P1)))) // (peny(konversi_pecahan(P2)) * peny(konversi_pecahan(P1))),((pemb(konversi_pecahan(P1)) * peny(konversi_pecahan(P2))) + (pemb(konversi_pecahan(P2)) * peny(konversi_pecahan(P1)))) % (peny(konversi_pecahan(P2)) * peny(konversi_pecahan(P1))), (peny(konversi_pecahan(P2)) * peny(konversi_pecahan(P1))))



# sub_p : pecahanc --> pecahanc
#   {sub_p(P1,P2) mengurangkan pecahan campuran P1 dengan pecahan camuran P2}
# (2,4,5) dan (1,2,4)
def sub_p(P1,P2):
    return make_pecahan_c(((pemb(konversi_pecahan(P1)) * peny(konversi_pecahan(P2))) - (pemb(konversi_pecahan(P2)) * peny(konversi_pecahan(P1)))) // (peny(konversi_pecahan(P2)) * peny(konversi_pecahan(P1))),((pemb(konversi_pecahan(P1)) * peny(konversi_pecahan(P2))) - (pemb(konversi_pecahan(P2)) * peny(konversi_pecahan(P1)))) % (peny(konversi_pecahan(P2)) * peny(konversi_pecahan(P1))), (peny(konversi_pecahan(P2)) * peny(konversi_pecahan(P1))))

def sub():
    return make_pecahan_c(-13//5,-13%5,5)

# div_p : pecahanc --> pecahanc
#   {div_p(P1,P2) membagi pecahan campuran P1 dengan pecahan campuran P2}
def div_p(P1,P2):
    return make_pecahan_c(((pemb(konversi_pecahan(P1)) * peny(konversi_pecahan(P2))) // (pemb(konversi_pecahan(P2)) * peny(konversi_pecahan(P1)))),((pemb(konversi_pecahan(P1)) * peny(konversi_pecahan(P2))) % (pemb(konversi_pecahan(P2)) * peny(konversi_pecahan(P1)))),(pemb(konversi_pecahan(P2)) * peny(konversi_pecahan(P1))))



# mul_p : pecahanc --> pecahanc
#   {mul_p(P1,P2) mengalikan pecahan campuran P1 dengan pecahan campuran P2}
def mul_p(P1,P2):
    return make_pecahan_c(((pemb(konversi_pecahan(P1)) * pemb(konversi_pecahan(P2))) // (peny(konversi_pecahan(P1)) * peny(konversi_pecahan(P2)))),((pemb(konversi_pecahan(P1)) * pemb(konversi_pecahan(P2))) % (peny(konversi_pecahan(P1)) * peny(konversi_pecahan(P2)))),(peny(konversi_pecahan(P1)) * peny(konversi_pecahan(P2))))



# DEFINISI DAN SPESIFIKASI PREDIKAT
# is_eq_p : 2 pecahanc --> boolean
#   {is_eq_p(P1,P2) membandingkan apakah P1 sama dengan P2}
def is_eq_p(P1,P2):
    return konversi_real(P1) == konversi_real(P2)


# is_lt_p : 2 pecahanc --> boolean
#    {is_lt_p(P1,P2) membandingkan apakah P1 lebih kecil dari P2}
def is_lt_p(P1,P2):
    return konversi_real(P1) < konversi_real(P2)



# is_gt_p : 2 pecahanc --> boolean
#   {is_gt_p(P1,P2) membandingkan apakah P1 lebih besar dari P2}
def is_gt_p(P1,P2):
    return konversi_real(P1) > konversi_real(P2)

# APLIKASI

print("\n===SELAMAT DATANG DI PROGRAM TYPE BENTUKAN PECAHAN CAMPURAN===\n")

print("\n===SESI OPERATOR===\n")
print("Konversi dari [1,2,4] ke pecahan biasa adalah {}/{}".format(pemb(konversi_pecahan(make_pecahan_c(1,2,4))),peny(konversi_pecahan(make_pecahan_c(1,2,4)))))
print("Konversi dari [1,2,4] ke bilangan desimal adalah {}".format(konversi_real(make_pecahan_c(-1,2,4))))
print("Penjumlahan pecahan campuran (1 2/4) dengan pecahan campuran (2 4/5) adalah   ({} {}/{})".format(bil(add_p(make_pecahan_c(1,2,4),make_pecahan_c(2,4,5))),pemb_c(add_p(make_pecahan_c(1,2,4),make_pecahan_c(2,4,5))),peny_c(add_p(make_pecahan_c(1,2,4),make_pecahan_c(2,4,5)))))
print("Pengurangan pecahan campuran (2 4/5) dengan pecahan campuran (1 2/4) adalah   ({} {}/{})".format(bil(sub_p(make_pecahan_c(1,2,4),make_pecahan_c(2,4,5))),pemb_c(sub_p(make_pecahan_c(1,2,4),make_pecahan_c(2,4,5))),peny_c(sub_p(make_pecahan_c(1,2,4),make_pecahan_c(2,4,5)))))
print("Pembagian pecahan campuran (1 2/4) dengan pecahan campuran (2 4/5) adalah   ({} {}/{})".format(bil(div_p(make_pecahan_c(1,2,4),make_pecahan_c(2,4,5))),pemb_c(div_p(make_pecahan_c(1,2,4),make_pecahan_c(2,4,5))),peny_c(div_p(make_pecahan_c(1,2,4),make_pecahan_c(2,4,5)))))
print("Perkalian pecahan campuran (1 2/4) dengan pecahan campuran (2 4/5) adalah   ({} {}/{})".format(bil(mul_p(make_pecahan_c(1,2,4),make_pecahan_c(2,4,5))),pemb_c(mul_p(make_pecahan_c(1,2,4),make_pecahan_c(2,4,5))),peny_c(mul_p(make_pecahan_c(1,2,4),make_pecahan_c(2,4,5)))))

print("\n===SESI PREDIKAT===\n")
print ("Apakah pecahan 1 sama dengan pecahan 2? : {}" .format (is_eq_p(make_pecahan_c(1,2,4), make_pecahan_c(1,2,4))))
print ("Apakah pecahan 1 kurang dari pecahan 2? : {}" .format (is_lt_p(make_pecahan_c(0,2,4), make_pecahan_c(1,2,4))))
print ("Apakah pecahan 1 lebih dari pecahan 2? : {}" .format (is_gt_p(make_pecahan_c(5,2,4), make_pecahan_c(1,2,4))))

print ("\n======= PROGRAM BERHASIL DIJALANKAN =======\n")

print ("============== TERIMA  KASIH ==============")
