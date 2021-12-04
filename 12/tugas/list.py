# Nama File : list.py
# Deskripsi : Tipe list
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 4 Dec 2021

# DEFINISI DAN SPESIFIKASI TYPE
    # {Konstruktor menambahkan elemen di awal, notasi prefix } 
# type  List  : [ ], atau [e o List] 
    # {Konstruktor menambahkan elemen di akhir, notasi postfix } 
# type  List  : [ ] atau [List • e] 
    # {List adalah  sekumpulan elemen list yang bertype sama : }

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
#Konso : elemen, List  → List 
    #{Konso(e,L): menghasilkan  sebuah list dari e dan L,  dengan e sebagai  elemen pertama e 
    #:   e o L → L'} 
# REALISASI (dalam python)
def Konso(e,L):
    if L == []:
        return [e]
    else:
        return [e] + L
 
#Kons• : List, elemen  →  List 
    #{  Kons(L,e):    menghasilkan  sebuah  list    dari  L  dan  e,  dengan  e  sebagai  elemen  terakhir  
    #list :  L •  e → L'} 
# REALISASI (dalam python)
def Konsi(L,e):
    if L == []:
        return [e]
    else:
        return L + [e]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt: List tidak kosong  →  elemen 
#   {FirstElmt(L) Menghasilkan elemen pertama list L } 
# REALISASI (dalam python)
def FirstElmt(L):
    return L[0]
 
# Tail : List tidak kosong →  List 
#   {Tail(L) : Menghasilkan  list tanpa elemen pertama list L, mungkin kosong } 
# REALISASI (dalam python)
def Tail(L):
    return L[1:]

# LastElmt : List tidak kosong →  elemen 
#   {LastElmt(L) : Menghasilkan elemen terakhir list L } 
# REALISASI (dalam python)
def LastElmt(L):
    return L[-1]

# Head : List tidak kosong → List 
#   {Head(L) : Menghasilkan  list tanpa elemen terakhir list L,  mungkin kosong} 
# REALISASI (dalam python)
def Head(L):
    return L[:-1]

#DEFINISI DAN SPESIFIKASI PREDIKAT
# {Basis 0 } 
# IsEmpty : List   → boolean 
#   {IsEmpty(L)  benar jika list kosong }
# REALISASI (dalam python)
def IsEmpty(L):
    return L == []

# NbElmt(L): List -> integer
#   {NbElmt(L) menjumlah elemen }
# REALISASI (dalam python)
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))

# IsOneElmt:  List of integer →  boolean 
#   {IsOneElmt (X,L) adalah benar jika teks hanya mempunyai satu elemen }
# REALISASI (dalam python)
def IsOneElmt(L):
    return NbElmt(L) == 1

# Union: 2 List -> List
#   {Union(S1,S2) menghasilkan list penggabungan kedua buah input}
# REALISASI (dalam python)
def Union(S1,S2):
    if IsEmpty(S1):
        return S2
    elif IsEmpty(S2):
        return S1
    elif IsEmpty(S1) and IsEmpty(S2):
        return []
    else:
        return Konso(FirstElmt(S1),Union(Tail(S1),S2))