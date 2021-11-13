# Nama File : is_eq_S.py
# Deksripsi : Mengecek apakah elemen adalah member dari suatu List of List
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 11 November 2021

# DEFINISI DAN SPESIFIKASI
# is_member_S  : elemen, List of list --> boolean 
#   { is_member_S(A,S)  true jika A adalah anggota S } 

# REALISASI
from modal import *

def is_member_S(A,S):
    if is_empty(S):
        return False
    else:
        if is_atom(A):
            if A == first_list(S):
                return True
            else: #aljabar boolean
                return is_member_S(A,tail_list(S))
        elif is_list(A):
            if is_member(A,S):
                return True
            else: #aljabar boolean
                return is_member_S(A,tail_list(S))
        else:#bukan atom bukan List
            return False

# APLIKASI
print(is_member_S([1],[[-4,-3],-2,[1]]))
print(is_member_S(10,[6,7,8,4,1,0]))