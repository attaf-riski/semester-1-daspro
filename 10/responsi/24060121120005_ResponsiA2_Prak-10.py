# Nama File : 24060121120005_ResponsiA2_Prak-10.py
# Deskripsi : Fungsi-fungsi pada List of List
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 11 Agustus 2021

# DEFINISI DAN SPESIFIKASI
# is_atom : list of list  →  boolean 
#   {is_atom(S) menghasilkan true  jika list adalah atom, yaitu terdiri dari sebuah atom } 

# is_list : list of list  →  boolean 
#   { is_atom(S) menghasilkan true  jika S adalah sebuah list (bukan atom)} 

# is_empty : list of list  →  boolean 
#   {is_empty(S) benar  jika S adalah list of list kosong} 

# konslo : List, List of list  → List of list 
#   {  konslo(L,S)  diberikan  sebuah  List  L  dan  sebuah  List  of  List  S,  membentuk  list  baru  
#   dengan  List yang diberikan sebagai elemen pertama  List of list:  L o S  →  S'}  
 
# konsli : List of list , List  →  List of list 
#   {konsli  (S,L)  diberikan  sebuah  List  of  list  S    dan  sebuah  list  L,  membentuk  list  baru  
#   dengan List yang diberikan sebagai elemen terakhir list of List:  S • L  →  S'}  

# first_list: List of list tidak kosong → List 
#   {first_list(S) Menghasilkan elemen pertama list, mungkin sebuah list atau atom } 
 
# tail_list : List of list tidak kosong →  List of list 
#   {tail_list(S) Menghasilkan  "sisa" list of list S  tanpa elemen pertama list  S } 
 
# last_list : List of list tidak kosong →  List of list 
#   {last_list(S) : Menghasilkan elemen terakhir list of list S, mungkin list atau atom } 
 
# head_list : List of list tidak kosong →  List of list 
#   {head_list(S) Menghasilkan "sisa" list of list tanpa elemen terakhir list } 

# is_eq_S  : 2 List of list  → boolean 
#   {is_eq_S (S1,S2 ) true jika S1 identik dengan  S2 : semua elemennya sama }

# REALISASI
def is_atom(S):
    if type(S) != list:
        return True
    else:
        return False

def is_list(S):
    if type(S) == list:
        return True
    else:
        return False

def is_empty(S):
    return S == []

def konslo(L,S):
    if is_empty(L):
        return [L]
    else:
        return [L] + S

def konsli(S,L):
    if is_empty(L):
        return [L]
    else:
        return S + [L]

def first_list(L):
    return L[0]

def tail_list(S):
    return S[1:]

def last_list(S):
    return S[-1]

def head_list(S):
    return S[:-1]

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
print("===PROGRAM STARTED===")

print("\n=||=====>Is Atom?")
print(is_atom([1]))
print(is_atom([1,2]))
print(is_atom([[1,2]]))

print("\n=||=====>Is List?")
print(is_list([1,2,3]))
print(is_list([1,[2,1],3]))
print(is_list([1]))

print("\n=||=====>KonsLo")
print(konslo([1,2,3],[]))
print(konslo([0],[1,2,3]))

print("\n=||=====>KonsLi")
print(konsli([],[1,2,3]))
print(konsli([1,2,3],[4]))

print("\n=||=====>First List")
print(first_list([1,[1,2]]))
print(first_list([[1,3,4],[1,2]]))

print("\n=||=====>Tail List")
print(tail_list([1,[1,2]]))
print(tail_list([[1,3,4],[1,2]]))

print("\n=||=====>Last List")
print(last_list([1,[1,2]]))
print(last_list([[1,3,4],1]))

print("\n=||=====>Head List")
print(head_list([1,[1,2]]))
print(head_list([[1,3,4],1]))

print("\n=||=====>Is Eq S")
print(is_eq_S([1,2,[5,7]],[1,2,[5,7]]))
print(is_eq_S([1,2,[5,7]],[1,2,[5,7]]))

print("\n===PROGRAM FINISHED===")