# Nama File : is_eq_S.py
# Deksripsi : Mengecek apakah dua buah List of List itu sama
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 11 November 2021

# DEFINISI DAN SPESIFIKASI
# is_eq_S  : 2 List of list --> boolean 
#   {is_eq_S(S1,S2) true jika S1 identik dengan  S2 : semua elemennya sama } 

# REALISASI
# agar lebih ringkas
from modal import *

def is_eq_S(S1,S2):
    if is_empty(S1) and is_empty(S2):
        return True
    elif not is_empty(S1) and is_empty(S2):
        return False
    elif is_empty(S1) and not is_empty(S2):
        return False
    else: #not empty for S1 And not empty for S2
        if is_atom(first_list(S1)) and is_atom(first_list(S2)):
            #sekali ditemukan salah, rekursif berhenti
            if first_list(S1) == first_list(S2):
            #mempersingkat rekursif dengan aljabar boolean: Hk.Idempoten bila True semua, Hk.Identitas bila ada True, Hk.Dominasi bila ada False
                return is_eq_S(tail_list(S1),tail_list(S2)) #skip
            else:# rekursif berhenti karena ketahuan tidak sama
                return False
        elif is_list(first_list(S1)) and is_list(first_list(S2)):
            #sekali ditemukan salah, rekursif berhenti
            if is_eq_S(first_list(S1),first_list(S2)):
                #mempersingkat rekursif dengan aljabar boolean: Hk.Idempoten bila True semua, Hk.Identitas bila ada True, Hk.Dominasi bila ada False
                 return is_eq_S(tail_list(S1),tail_list(S2)) #skip
            else: # rekursif berhenti karena ketahuan tidak sama
                return False  
        else: # rekursif berhenti karena ketahuan tidak sama
            return False

# APLIKASI
print(is_eq_S([1,2,3,[4,5]],[1,2,3,[4,5]]))
print(is_eq_S([1,2,3],[1,2,3,[4,5]]))