# Nama File : is_member_LS.py
# Deksripsi : Mengecek apakah List adalah member dari suatu List of List
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 11 November 2021

# DEFINISI DAN SPESIFIKASI
# is_member_LS  : List, List of list  → boolean 
#   {is_member_LS(L,S)  true jika L adalah anggota S }

# REALISASI
from modal import *

def is_member_LS(L,S):
    if is_empty(L) and is_empty(S):
        return True
    elif not is_empty(L) and is_empty(S):
        return False
    elif is_empty(L) and not is_empty(S):
        return False
    else: # not empty(L) and not empty(S)
        if is_atom(first_list(S)): #skip
            return is_member_LS(L,tail_list(S))
        else: #list
            if is_equal(L,first_list(S)):
                return True
            else: #skip
                return is_member_LS(L,tail_list(S))

# APLIKASI
print(is_member_LS([1,2],[1,2,[1,2]]))
print(is_member_LS([1,2],[1,2]))