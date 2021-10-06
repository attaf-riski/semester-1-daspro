# Nama File : garis.py
# Nama Pembuat File : Attaf Riski Putra Ramadhan
# Tanggal Pembuatan File : 6 Oktober 2021
# Deskripsi : Membentuk sebuah type bentukan bertipe garis sebagai tugas matkul daspro

from math import sqrt

# DESKRIPSI TYPE
# type point: <x: real, y: real>
#   {<x,y> adalah point, dengan x sebagai absis dan y sebagai ordinat.}

# type garis: <p1: point, p2: point>
#   {<p1,p2> adalah garis, dengan p1 adalah titik awal dan p2 sebagai titik akhir, dengan titik p1 tidak sama dengan titik p2}

# DESKRIPSI KONSTRUKTOR
# MakePoint: 2 real --> point
#   {MakePoint(x,y): membentuk sebuah point dari x dan y, dengan x sebagai absis dan y sebagai ordinat.}
# REALISASI (dalam python)
def make_point(x,y):
    return [x,y]

# MakeGaris: 2 point --> garis
#   {MakeGaris(p1,p2): membentuk sebuah garis yang memiliki titik(point) p1 dan p2.}
# REALISASI (dalam python)
def make_garis(p1,p2):
    return [p1,p2]

# DESKRIPSI SELEKTOR
# Absis: point --> real
#   {Absis(p): Memberikan absis dari point p.}
# REALISASI (dalam python)
def absis(p):
    return p[0]

# Ordinat: point --> real
#   {Ordinat(p): Memberikan ordinat dari point p.}
def ordinat(p):
    return p[1]

# Titik1: garis --> point
#   {Titik1(g): Memberikan titik 1 dari garis g.}
# REALISASI (dalam python)
def titik1(g):
    return g[0]

# Titik2: garis --> point
#   {Titik2(g): Memberikan titik 2 dari garis g.}
# REALISASI (dalam python)
def titik2(g):
    return g[1]

# DEFINISI DAN SPESIFIKASI OPERATOR
# Gradien: garis --> real
#   {Gradient(g): Menghasilkan gradient dari garis g: m = (y2-y1)/(x2-x1).}
# REALISASI (dalam python)
def gradient(g):
    return (ordinat(titik1(g)) - ordinat(titik2(g))) / (absis(titik1(g)) - absis(titik2(g)))

# PanjangGaris: garis --> real
#   {PanjangGaris(g): Menghitung panjang garis g berdasarkan 2 titik yang menjadi komponen garis g: akar dari (y2-y1)^2 + (x2-x1)^2 }
# REALISASI (dalam python)
def panjang_garis(g):
    return sqrt((ordinat(titik1(g)) - ordinat(titik2(g)))**2 + (absis(titik1(g)) - absis(titik2(g)))**2)

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsSejajar?: 2 garis --> boolean
#   {IsSejajar?(g1,g2): Akan bernilai benar apabila g1 sejajar dengan g2, yaitu dengan syarat
#    gradient dari kedua garis tersebut sama: m1 = m2 .}
# REALISASI (dalam python)
def is_sejajar(g1,g2):
    return gradient(g1) == gradient(g2)

# IsTegakLurus?: 2 garis --> boolean
#   {IsTegakLurus?(g1,g2): Akan bernilai benar apabila g1 tegak lurus dengan g2, 
#    yaitu perkalian dari gradient g1 dan g2 sama dengan -1: m1*m2 = -1 .}
# REALISASI (dalam python)
def is_tegak_lurus(g1,g2):
    return (gradient(g1) * gradient(g2)) == -1

# APLIKASI
# titik hasil persamaan garis y = 2x + 1 sejajar dengan titik hasil persamaan y = 2x -6
# titik hasil persamaan garis y = 2x + 1 tegak lurus dengan titik hasil persamaan y = (-0,5)x + 7,5

print("\n=====SELAMAT DATANG DI PROGRAM TYPE BENTUKAN GARIS=====\n")
print("Garis A mempunyai 2 komponen berupa titik yaitu: <{},{}> dan <{},{}>".format(absis(make_point(1,3)),ordinat(make_point(1,3)),absis(make_point(5,11)),ordinat(make_point(5,11))))
print("Garis B mempunyai 2 komponen berupa titik yaitu: <{},{}> dan <{},{}>".format(absis(make_point(1,-4)),ordinat(make_point(1,-4)),absis(make_point(5,-4)),ordinat(make_point(5,-4))))
print("Garis C mempunyai 2 komponen berupa titik yaitu: <{},{}> dan <{},{}>".format(absis(make_point(1,7)),ordinat(make_point(1,7)),absis(make_point(3,6)),ordinat(make_point(3,6))))

print("\n==SESI OPERASI GARIS==\n")
print("Garis A mempunyai gradient: {}".format(gradient(make_garis(make_point(1,3),make_point(5,11)))))
print("Garis B mempunyai gradient: {}".format(gradient(make_garis(make_point(1,-4),make_point(5,4)))))
print("Garis C mempunyai gradient: {}".format(gradient(make_garis(make_point(1,7),make_point(3,6)))))

print("\n==SESI PREDIKAT GARIS==\n")
print("Apakah Garis A sejajar Garis B? {}".format(is_sejajar(make_garis(make_point(1,3),make_point(5,11)),make_garis(make_point(1,-4),make_point(5,4)))))
print("Apakah Garis A sejajar Garis C? {}".format(is_sejajar(make_garis(make_point(1,3),make_point(5,11)),make_garis(make_point(1,7),make_point(3,6)))))
print("Apakah Garis A tegak lurus Garis C? {}".format(is_tegak_lurus(make_garis(make_point(1,3),make_point(5,11)),make_garis(make_point(1,7),make_point(3,6)))))
print("Apakah Garis B tegak lurus Garis C? {}".format(is_tegak_lurus(make_garis(make_point(1,-4),make_point(5,4)),make_garis(make_point(1,7),make_point(3,6)))))

print("\n=====PROGRAM BERAKHIR,TERIMAKASIH=====")
