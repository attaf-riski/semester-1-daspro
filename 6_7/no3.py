# Nama File : no3.py
# Nama Pembuat File : Attaf Riski Putra Ramadhan
# Tanggal Pembuatan : 08 Oktober 2021
# Deskripsi : Membuat type bentukan square untuk sebuah segi empat yang terdiri atas dua elemen


# DEFINISI TYPE
# type point: <x: real,y: real>
#   {<x,y> adalah sebuah point, dengan x adalah absis, y adalah ordinat }

# type square: <top: point,bottom: point>
#   {<top,down> adalah sebuah segi empat yang terdiri atas dua elemn, yaitu top dan bottom yang masing-masing bertipe point.
#    . Elemen top adalah titik atas diagonal, sedangkan bottom adalah titik bawah diagonal.}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePoint: 2 real --> point
#   {MakePoint(x,y) membentuk sebuah point, dengan x sebagai absis dan y sebagai ordinat.}
# REALISASI (dalam python)
def make_point(x,y):
    return [x,y]

# MakeSquare: 2 point --> square
#   {MakeSquare(top,bottom) membentuk sebuah square, dengan top sebagai titik diagonal atas dan bottom sebagi titik diagonal bawah.}
# REALISASI (dalam python)
def make_square(top,bottom):
    return [top,bottom]

# DEFINISI DAN SPESIFIKASI SELEKTOR UNTUK POINT
# Absis: point --> real
#   {Absis(P) Memberikan Absis point p}
# REALISASI (dalam python)
def absis(p):
    return p[0]

# Ordinat: point --> real
#   {Ordinat(P) memberikan Ordinat point P}
# REALISASI (dalam python)
def ordinat(p):
    return p[1]

# DEFINISI DAN SPESIFIKASI SELEKTOR UNTUK SQUARE
# Top: square --> point
#   {Top(S) Menghasilkan titik atas diagonal Square S}
# REALISASI (dalam python)
def top(s):
    return s[0]

# Bottom: square --> point
#   {Bottom(S) Menghasilkan titik bawah diagonal Square S}
# REALISASI (dalam python)
def bottom(s):
    return s[1]

# DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI UNTUK SQUARE
# GetPanjang: square --> integer > 0
#   {GetPanjang(s): Mengembalikan panjang dari square S, hasilnya berupa integer positif}
# REALISASI (dalam python)
def get_panjang(s):
    return absis(top(s)) - absis(bottom(s))

# GetLebar: square --> integer > 0
#   {GetLebar(s): Mengembalikan lebar dari square S, hasilnya berupa integer positif.}
# REALISASI (dalam python)
def get_lebar(s):
    return ordinat(top(s)) - ordinat(bottom(s))

# GetLuas: square --> integer
#   {GetLuas(S): Mengembalikan luas dari sebuah square S}
# REALISASI (dalam python)
def get_luas(s):
    return get_lebar(s) * get_panjang(s)

# APLIKASI 
print("\n===WELCOME TO TYPE BENTUKAN SQUARE===\n")
print("Terdefinisi square dengan titik diagonal atas  <3,2> dan titik diagonal bawah <-2,-1>")
print("Maka panjang square adalah: {}".format(get_panjang(make_square(make_point(3,2),make_point(-2,-1)))))
print("Lebarnya adalah: {}".format(get_lebar(make_square(make_point(3,2),make_point(-2,-1)))))
print("Maka luas square tersebut adalah: {}".format(get_luas(make_square(make_point(3,2),make_point(-2,-1)))))
print("\n===THANKS===\n")
