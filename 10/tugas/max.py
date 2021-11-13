# Nama File : max.py
# Deksripsi : menghasilkan sebuah nilai maksimum dalam sebuah List of List
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 11 November 2021

# DEFINISI DAN SPESIFIKASI
# max: List of list tidak kosong --> integer 
#   { max(S)  menghasilkan nilai elemen (atom) yang maksimum dari S }

# REALISASI
from modal import *

def max(S):
    if is_empty(S): # basis 0
        return 0
    else:
        if is_atom(first_list(S)):
            return max2(first_list(S),max(tail_list(S)))
        else: #list
            return max2(max(first_list(S)),max(tail_list(S)))

# APLIKASI
print(max([1,2,3,4,[4,5,100],6,7,8,9,90]))
print(max([10,[4,5]]))