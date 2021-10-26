# Nama File : 4.divid_v2.py
# Deskripsi : Menghasilkan pecahan campuran dengan pembagian rekurens
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 26 Oktober 2021

# DEFINISI TYPE
# pecahan_c : <bil:integer , n:integer >= 0 ,d:integer > 0 >
#   {<bil,n,d> adalah pecahan campuran, dengan bil sebagai bilangan, n sebagai pembilang(numerator) dan d sebagai penyebut(denumerator), bil merupakan bilangan bulat, n bilangan bulat positif dan d bilangan natural. }

# DEFINISI DAN SPESIFIKASI SELEKTOR
# bil : pecahan_c --> integer
#   {bil(P) memberikan bilangan bil dari pecahan campuran tersebut}
def bil(P):
    return P[0]
    
# pemb_c : pecahan_c --> integer
#   {pemb_c(P) memberikan numerator pembilang n dari pecahan campuran tersebut}
def pemb_c(P):
    return P[1]

# peny_c : pecahan_c --> integer
#   {peny_c(P) memberikan denumerator penyebut d dari pecahan campuran tersebut}
def peny_c(P):
    return P[2]

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# make_pecahan_c : integer, integer>=0, integer>0 --> pecahan_c
#   {make_pecahan_c(bil,n,d) membentuk sebuah pecahn campuran dari bilangan bil, pembilag n, dan penyebut d, dengan bil, n, dan d adalah integer}
def make_pecahan_c(bil,n,d):
    return [bil,n,d]

# =================================================
# modulo: integer >=0,integer > 0 --> integer
#   {modulo(x,y): Mencari modulo dari x dibagi y
#     x / y = modulo(x-y,y) }
# REALISASI(dalam python)
def modulo(x,y):
    if x < y:# basis 0
        return x
    else: #rekurens 
        return modulo(x-y,y)

# div: integer >=0,integer > 0 --> integer
#   {div(x,y): Mencari jumlah x dibagi y, dibulatkan
#     x / y = 1 + div(x-y,y) }
# REALISASI(dalam python)
def div(x,y):
    if x < y:# basis 0
        return 0
    else: #rekurens
        return 1 + div(x-y,y)

# bagi_to_pecahan: integer >=0,integer > 0 --> pecahan_c
#   {bagi_to_pecahan(x,y): menghasilkan pecahan c dan akan dicari bil,numerator,denumerator dari x dan y.}
# REALISASI(dalam python)
def bagi_to_pecahan_c(x,y):
    return make_pecahan_c(div(x,y),modulo(x,y),y)

# penampil_pecahan_c: integer >=0,integer > 0 --> string
#   {penampil_pecahan_c(x,y): Membuat pola string untuk menampilkan pecahan c agar lebih terbaca dan menerapkan konsep DRY(don't repeat yourself)}
# REALISASI(dalam python)
def penampil_pecahan_c(x,y):
    return print("{}({}/{})".format(bil(bagi_to_pecahan_c(x,y)),pemb_c(bagi_to_pecahan_c(x,y)),peny_c(bagi_to_pecahan_c(x,y))))

# APLIKASI
print("===Program Start===")
penampil_pecahan_c(30,5)
penampil_pecahan_c(0,8)
penampil_pecahan_c(50,3)
print("===Program End, Thanks===")