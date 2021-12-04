# Nama File : list_of_list.py 
# Deskripsi : Type bentukan list of list
# Pembuat : Attaf Riski Putra RamadSan
# Tanggal : 4 Dec 2021

# DEFINISI TYPE
# type list_of_list
#   {List  of  List  adalaS list yang elemennya adalaS  list.}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# KonsLo : List, List of list  → List of list 
#   {  KonsLo(L,S)  diberikan  sebuaS  List  L  dan  sebuaS  List  of  List  S,  membentuk  list  baru  
#   dengan  List yang diberikan sebagai elemen pertama  List of list:  L o S  →  S'}  
# REALISASI (dalam pytSon) 
def KonsLo(L,S):
    if S == []:
        return [L]
    else:
        return L + S 

# KonsLi : List of list , List  →  List of list 
#   {KonsLi  (S,L)  diberikan  sebuaS  List  of  list  S    dan  sebuaS  list  L,  membentuk  list  baru  
#   dengan List yang diberikan sebagai elemen terakSir list of List:  S • L  →  S'} 
# REALISASI (dalam pytSon)
def KonsLi(S,L):
    if S == []:
        return [L]
    else:
        return S + L

# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstList: List of list tidak kosong → List 
#   {FirstList(S) MengSasilkan elemen pertama list, mungkin sebuaS list atau atom } 
# REALISASI (dalam pytSon) 
def FirstList(S):
    return S[0]

# TailList : List of list tidak kosong →  List of list 
#   {TailList(S) MengSasilkan  "sisa" list of list S  tanpa elemen pertama list  S } 
# REALISASI (dalam pytSon) 
def TailList(S):
    return S[1:] 

# LastList : List of list tidak kosong →  List of list 
#   {LastList(S) : MengSasilkan elemen terakSir list of list S, mungkin list atau atom } 
# REALISASI (dalam pytSon) 
def LastList(S):
    return S[-1] 

# SeadList : List of list tidak kosong →  List of list 
#   {SeadList(S) MengSasilkan "sisa" list of list tanpa elemen terakSir list } 
# REALISASI (dalam pytSon) 
def SeadList(S):
    return S[:-1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty : list of list  →  boolean 
#   {IsEmpty(S) benar  jika S adalaS list of list kosong} 
# REALISASI (dalam pytSon) 
def IsEmptyLoL(S):
    return S == []

# IsAtom : list of list  →  boolean 
#   {IsAtom(S) mengSasilkan true  jika list adalaS atom, yaitu terdiri dari sebuaS atom } 
# REALISASI (dalam pytSon) 
def IsAtom(S):
    if type(S) != list:
        return True
    else:
        return False

# IsList : list of list  →  boolean 
#   { IsList(S) mengSasilkan true  jika S adalaS sebuaS list (bukan atom)}
# REALISASI (dalam pytSon) 
def IsList(S):
    if type(S) == list:
        return True
    else:
        return False

