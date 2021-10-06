# بسم الله الرحمن الرحيم
# Nama file : pecahan.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 26 September 2021
# Deskripsi : Membuat type bentukan pecahan dilengkapi realisasi konstruktor dan selektor. Program ini adalah realisasi dari diktat pemrograman fungsional halaman 38



# DEFINISI TYPE

# type pecahan : <n:integer >= 0, d:integer >0>
#   {<n:integer >=0, d:integer > 0> adalah sebuah pecahan, dengan n sebagai pembilang(numerator) dan d sebagai penyebut(denumerator). Penyebut tidak boleh nol.}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR

# MakePecahan : integer >= 0,integer 0>0 --> pecahan
#   {MakePecahan(n,d) membentuk sebuah pecahan dari pembilang n dan penyebut d, dengan n dan y integer}
# REALISASI (dalam python)
def make_pecahan(n,d):
    return [n,d]

#BEFORE
#class Pecahan:
#    def __init__(self,n,d):
#        self.n = n
#        self.d = d

# DEFINISI DAN SPESIFIKASI SELEKTOR

# pemb: pecahan --> integer
#   {pemb(P) memberikan pembilang(numerator) dari pecahan P}
# REALISASI (dalam python)
def pemb(P):
    return P[0]

# peny: pecahan --> integer
#   {pecahan(P) memberikan penyebut(denumerator) dari pecahan P}
# REALISASI (dalam python)
def peny(P):
    return P[1]

# DEFINISI DAN FUNGSI PREDIKAT
# {Operator Relasional Pecahan}

# IsEqF?: 2 pecahan --> boolean
#   {IsEqF?(P1,P2) benar jika P1 = P2. Membandingkan apakah dua buah pecahan sama nilainya: n1/d2 = n2/d2}
# REALISASI (dalam python)
def is_eq_f(P1,P2):
    return (pemb(P1)/peny(P1) ==  pemb(P2)/peny(P2))

# IsLtF?: 2 pecahan --> boolean
#   {IsLtF(P1,P2) benar jika P1 < P2. Membandingkan dua buah pecahan, apakah P1 kurang dari P2: n1/d1 < n2/d2}
# REALISASI (dalam python)
def is_lt_f(P1,P2):
    return (pemb(P1)/peny(P1) <  pemb(P2)/peny(P2))

# IsGtF?: 2 pecahan --> boolean
#   {IsGtF(P1,P2)benar jika P1 > P2. Membandingkan nilai dua buah pecahan, apakah P1 lebih dari P2: n1/d1 > n2/d2}
# REALISASI (dalam python)
def is_gt_f(P1,P2):
    return (pemb(P1)/peny(P1) >  pemb(P2)/peny(P2))

# DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI LAIN TERHADAP POINT
# { Operator aritmatika Pecahan }

# AddF: 2 pecahan --> pecahan
#   {AddF(P1,P2) Menambahkan dua buah pecahan P1 dan P2: n1/d1 + n2/d2 = (n1*d2 + n2*d1)/d1*d2 }
# REALISASI (dalam python)
def add_f(P1,P2):
   return make_pecahan((pemb(P1)*peny(P2)) + (pemb(P2)*peny(P1)),peny(P1) * peny(P2))

# SubF: 2 pecahan --> pecahan
#    {SubF(P1,P2) Mengurangkan dua buah pecahan P1 dan P2: n1/d1 - n2/d2 = (n1*d2 + n2*d1)/d1*d2}
# REALISASI (dalam python)
def sub_f(P1,P2):
   return make_pecahan((pemb(P1)*peny(P2)) - (pemb(P2)*peny(P1)),peny(P1) * peny(P2))

# MulF: 2 pecahan --> pecahan
#   {MulF(P1,P2) Mengalikan dua buah pecahan P1 dan P2: n1/d1 * n2/d2 = (n1 * n2) / (d1 * d2)}
# REALISASI (dalam python)
def mul_f(P1,P2):
    return make_pecahan(pemb(P1) * pemb(P2),peny(P1) * peny(P2))

# DivF: 2 pecahan --> pecahan
#   {DivF(P1,P2) Membagi dua buah pecahan P1 dan P2: (n1/d1) / (n2/d2) = (n1*d2) / (n2*d1)}
# REALISASI (dalam python)
def div_f(P1,P2):
    return make_pecahan(pemb(P1) * peny(P2),pemb(P2) * peny(P1))

# RealF: 2 pecahan --> real
#   {RealF(P) Menuliskan bilangan pecahan dalam notasi desimal}
# REALISASI (dalam python)
def real_f(P):
    return pemb(P) / peny(P)

# APLIKASI
print("\n=====SELAMAT DATANG DI PROGRAM TIPE BENTUKAN Pecahan=====\n")
print("Pecahan 1 terbentuk dengan nilai: {0}/{1}".format(pemb(make_pecahan(1,5)),peny(make_pecahan(1,5))))
print("Pecahan 2 terbentuk dengan nilai: {0}/{1}".format(pemb(make_pecahan(3,5)),peny(make_pecahan(3,5))))

print("\n==SESI OPERASI ARITMATIKA PECAHAN==\n")
print("Apakah Pecahan 1 sama dengan (==) Pecahan 2?: {}".format(is_eq_f(make_pecahan(1,5),make_pecahan(3,5))))
print("Apakah Pecahan 1 kurang dari (<=) Pecahan 2?: {}".format(is_lt_f(make_pecahan(1,5),make_pecahan(3,5))))
print("Apakah Pecahan 1 lebih dari (>=) Pecahan 2?: {}".format(is_gt_f(make_pecahan(1,5),make_pecahan(3,5))))

print("\n==SESI OPERASI RELASIONAL PECAHAN==\n")
print("Kita ingat kembali bahwa Pecahan 1 adalah: {0}/{1}".format(pemb(make_pecahan(1,5)),peny(make_pecahan(1,5))))
print("Dan Kita ingat kembali bahwa Pecahan 2 adalah: {0}/{1}".format(pemb(make_pecahan(3,5)),peny(make_pecahan(3,5))))
Pecahan_buffer = add_f(make_pecahan(1,5),make_pecahan(3,5))
print("Pecahan 1 + Pecahan 2 = {}/{}".format(pemb(Pecahan_buffer),peny(Pecahan_buffer)))
Pecahan_buffer = sub_f(make_pecahan(1,5),make_pecahan(3,5))
print("Pecahan 1 - Pecahan 2 = {}/{}".format(pemb(Pecahan_buffer),peny(Pecahan_buffer)))
Pecahan_buffer = mul_f(make_pecahan(1,5),make_pecahan(3,5))
print("Pecahan 1 * Pecahan 2 = {}/{}".format(pemb(Pecahan_buffer),peny(Pecahan_buffer)))
Pecahan_buffer = div_f(make_pecahan(1,5),make_pecahan(3,5))
print("Pecahan 1 / Pecahan 2 = {}/{}".format(pemb(Pecahan_buffer),peny(Pecahan_buffer)))
print("Bentuk desimal Pecahan 1 adalah = {}".format(real_f(make_pecahan(1,5))))
print("Bentuk desimal Pecahan 2 adalah = {}".format(real_f(make_pecahan(3,5))))
                   
print("\n=====PROGRAM BERAKHIR,TERIMAKASIH=====")









