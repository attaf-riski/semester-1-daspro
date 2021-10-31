# Nama file : tugas_8.py
# Deskripsi : kumpulan dari fungsi-fungsi pada List
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 30 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# first_elmnt: List (tidak kosong ) --> element
#   {first_elemen(L): Menghasilkan elemen pertama dari List L}

# last_elmnt: List (tidak kosong ) --> element
#   {last_element(L): Menghasilkan elemen terakhir dari List L}

# is_empty: List --> boolean
#   {is_empty(L): benar apabila List kosong. }

# is_member: List (tidak kosong ),elemen --> boolean
#   {is_member(L,e): benar apabila e adalah anggota dari List L, menggunakan konsi}

# nb_elmnt: List --> integer
#   {nb_elmnt(L): Menghasilkan banyaknya elemen List L}

# prec: integer --> integer
#   {prec(N): Mengembalikan nilai n-1}

# tail: List --> List
#   {tail(L): menghasilkan List tanpa elemen pertama List L, bisa kosong}

# head: List --> List
#   {head(L): menghasilkan List tanpa elemen terakhir List L, bisa kosong}

# konso : elemen, List  --> List 
#   {konso(e,L): menghasilkan sebuah List dari e dan L, dengan e sebagai  elemen pertama e 
#   :   e o L --> L'}

# elmnt_ke_n: integer>=0, List (tidak kosong ) --> element
#   {elmnt_ke_n(N,L): menghasilkan elemen ke-n List L, n >= 0, dan n <= banyaknya elemen List }

# copy : List  -->  List 
#   { copy(L) : Menghasilkan List yang identik dengan List asal} 

# concat (L1,L2)   : List  --> List 
#   {concat (L1,L2)menghasilkan konkatenasi list L1 dan L2} 

# is_first: elemen, List  (tidak kosong ) --> boolean 
#   {is_first  (e,L) adalah benar jika e adalah elemen pertama  list L } 

# is_last : elemen, List  (tidak kosong ) --> boolean 
#   {is_last  (e,L) adalah benar jika e adalah elemen terakhir  list L }

# is_nb_elemnt (L,N)   : List, integer >=0  -->  integer 
#   {is_nb_elemnt (L,N) true jika banyaknya  elemen  list sama dengan N }

# is_inverse (L1,L2)   : 2 List --> boolean 
#   {is_inverse (L1,L2) true jika L2 adalah list dengan urutan element terbalik dibandingkan L1, 
#    dengan perkataan lain adalah hasil inverse dari L1}

# is_x_element_ke_n: element,integer >= 0, List --> boolean
#   {is_x_element_ke_n(X,N,L): Menghasilkan benar apabila x adalah elemen ke-n List L,
#    n >= 0, dan n <= banyaknya elemen List, false jika tidak}

# REALISASI
def first_elmnt(L):
    if not is_empty(L):
        return L[0]

def last_elmnt(L):
    if not is_empty(L):
        return L[-1]

def is_empty(L):
    return L == []

def is_member(L,e):
    if is_empty(L):
        return False
    elif last_elmnt(L) == e: 
        return True
    else:
        return False or is_member(head(L),e)

def nb_elmnt(L):
    if is_empty(L):
        return 0
    else:
        return 1 + nb_elmnt(tail(L))

def prec(N):
    return N-1 

def tail(L):
    return L[1:]

def head(L):
    return L[:-1]

def konso(e,L):
    if is_empty(L):
        return [e]
    else:
        return [e] + L

def elmnt_ke_n(N,L):
    if not is_empty(L) and N <= nb_elmnt(L) and N >= 0:
        if N == 0:#basis 0
            return first_elmnt(L)
        else:
            return elmnt_ke_n(prec(N),tail(L))

def copy(L):
    if is_empty(L): #basis 0
        return []
    else:
        return konso(first_elmnt(L),copy(tail(L)))
        
def concat(L1,L2):
    if is_empty(L1):#basis 0
        return L2
    else:
        return konso(first_elmnt(L1),concat(tail(L1),L2))

def is_first(e,L):
    if is_empty(L):
        return False
    else:
        return e == L[0]

def is_last(e,L):
    if is_empty(L):
        return False
    else:
        return e == L[-1]

def is_nb_elemnt_n(N,L):
    if N >= 0 and N <= nb_elmnt(L):
        return N == nb_elmnt(L)
    else:
        return False

def is_inverse(L1,L2):
    if is_empty(L1) and is_empty(L2):
       return True
    elif first_elmnt(L1) == last_elmnt(L2) and nb_elmnt(L1) == nb_elmnt(L2):
        return True and is_inverse(tail(L1),head(L2))
    else:
        return False

def is_x_element_ke_n(X,N,L):
    if is_empty(L) or not is_member(L,X) or N < 0 or N > nb_elmnt(L):
        return False
    elif N == 0 and X == first_elmnt(L): #basis 0
        return True
    else:
        return False or is_x_element_ke_n(X,prec(N),tail(L))

# APLIKASI
print("=====Program Started=====")
print("\n*=====Elemen Ke N")
print(elmnt_ke_n(0,[1,2,3,4,5]))
print("\n*=====Copy")
print(copy(["sate","soto","rujak","gudeg"]))
print("\n*=====Concat")
print(concat([1,2,3,4,5],[6,7,8,9,10]))
print("\n*=====Is First?")
print(is_first(1,[1,2,3,4,5]))
print("\n*=====Is Last?")
print(is_last(5,[1,2,3,4,5]))
print("\n*=====Is Nb Element N?")
print(is_nb_elemnt_n(3,[1,2,3]))
print("\n*=====Is Inverse?")
print(is_inverse([1,2,3,4,5],[5,4,3,2,1]))
print("\n*=====Is X Element Ke N?")
print(is_x_element_ke_n(2,1,[1,2,3,4,5]))
print("\n=====Program Finished=====")
