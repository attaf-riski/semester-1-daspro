# Nama File : rember*.py
# Deksripsi : Menghapus suatu elemen di keseluruhan List of List
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 11 November 2021

# DEFINISI DAN SPESIFIKASI
# rember: elemen, List of list --> List of list 
#   { rember(a,S)  menghapus sebuah elemen bernilai a dari semua list S }

# REALISASI
from modal import *

def rember(a,S):
    if is_empty(S):
        return S
    else:
        if is_list(first_list(S)):
            return konslo(rember(a,first_list(S)),rember(a,tail_list(S)))
        else:#atom
            if first_list(S) == a: #skip
                return rember(a,tail_list(S))
            else:
                return konslo(first_list(S),rember(a,tail_list(S)))

# APLIKASI
print(rember(1,[1,2,[1,2],4,5]))
print(rember(4,[]))
