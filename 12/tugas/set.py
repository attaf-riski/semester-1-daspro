# NAMA FILE : set.py 
# DESKRIPSI : type bentukan set
# PEMBUAT : Attaf Riski Putra Ramadhan
# TANGGAL : 4 Dec 2021

from list import *
# DEFINISI TYPE
# {Set adalah List dengan tambahan syarat bahwa tidak ada elemen yang sama } 
#   { Semua konstruktor, selektor dan fungsi pada List berlaku untuk Himpunan } 

# DEFINISI DAN SPESIFIKASI OPERASI TERHADAP HIMPUNAN
# Rember : elemen, list   →  list 
#   { Rember (x,L)  menghapus sebuah elemen bernilai x dari list  } 
#   { list yang baru berkurang SATU elemennya yaitu yang bernilai e } 
#   { List kosong tetap menjadi list kosong }
# REALISASI (dalam python)
def Rember(x,L):
    if IsEmpty(L):
        return L
    else:
        if not (x == FirstElmt(L)):
            return Konso(FirstElmt(L),Rember(x,Tail(L)))
        else:
            return Tail(L)

