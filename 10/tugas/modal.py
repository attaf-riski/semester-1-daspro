# Nama File : modal.py
# Deksripsi : daftar fungsi-fungsi yang sering dipakai di List of List
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 11 November 2021

# DEFINISI DAN SPESIFIKASI
# is_atom : list of list  -->  boolean 
#   {is_atom(S) menghasilkan true  jika list adalah atom, yaitu terdiri dari sebuah atom } 

# is_list : list of list  -->  boolean 
#   { is_atom(S) menghasilkan true  jika S adalah sebuah list (bukan atom)} 

# is_empty : list of list  -->  boolean 
#   {is_empty(S) benar  jika S adalah list of list kosong} 

# konslo : List, List of list  --> List of list 
#   {  konslo(L,S)  diberikan  sebuah  List  L  dan  sebuah  List  of  List  S,  membentuk  list  baru  
#   dengan  List yang diberikan sebagai elemen pertama  List of list:  L o S  -->  S'}  
 
# konsli : List of list , List  -->  List of list 
#   {konsli  (S,L)  diberikan  sebuah  List  of  list  S    dan  sebuah  list  L,  membentuk  list  baru  
#   dengan List yang diberikan sebagai elemen terakhir list of List:  S • L  -->  S'}  

# first_list: List of list tidak kosong --> List 
#   {first_list(S) Menghasilkan elemen pertama list, mungkin sebuah list atau atom } 
 
# tail_list : List of list tidak kosong -->  List of list 
#   {tail_list(S) Menghasilkan  "sisa" list of list S  tanpa elemen pertama list  S } 
 
# last_list : List of list tidak kosong -->  List of list 
#   {last_list(S) : Menghasilkan elemen terakhir list of list S, mungkin list atau atom } 
 
# head_list : List of list tidak kosong -->  List of list 
#   {head_list(S) Menghasilkan "sisa" list of list tanpa elemen terakhir list } 

# is_member: elemen, List  --> boolean 
#   {is_member(X,L) adalah benar jika X adalah elemen list L } 

# is_equal : 2 List --> boolean 
#   {is_equal(L1,L2)  benar    jika  semua  elemen  list  L1  sama  dengan  L2:  sama  urutan  dan  
#    sama nilainya } 

# max2: 2 integer --> integer 
#   {max2(a,b) menghasilkan nilai maksimum a dan b } 

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

def is_member(e,L):
    if is_empty(L):
        return False
    else:
        if first_list(L) == e :
            return True
        else:
            return is_member(e,tail_list(L))

def is_equal(L1,L2):
    if is_empty(L1) and is_empty(L2):
            return True
    elif first_list(L1) == first_list(L2):
        return is_equal(tail_list(L1),tail_list(L2))
    else:
        return False

def max2(a,b):
    if a>=b:
        return a
    else: #a<b
        return b
