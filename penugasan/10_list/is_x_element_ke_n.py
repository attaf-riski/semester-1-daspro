# Nama File : is_x_element_ke_n.py
# Deskripsi : Memeriksa apakah suatu elemen adalah elemen ke-n dari list sebuah list
# Nama : Attaf Riski Putra Ramaadhan
# Tanggal : 25 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# is_x_element_ke_n: element,integer > 0, list --> boolean
#   {is_x_element_ke_n(x,n,L): Menghasilkan benar apabila x adalah elemen ke-n list L,
#    n > 0, dan n <= banyaknya elemen list, false jika tidak}

# is_x_element_ke_n_v2: element,integer > 0, list --> boolean
#   {is_x_element_ke_n(x,n,L): Menghasilkan benar apabila x adalah elemen ke-n list L,
#    n > 0, dan n <= banyaknya elemen list, false jika tidak, menggunakan bantuan fungsi elemen_ke_n()}

# elemen_ke_n: integer>0, list != [] --> element
#   {elemen_ke_n(n,L): menghasilkan elemen ke-n list L, n > 0, dan n <= banyaknya elemen list }

# first_element: list != [] --> element
#   {first_elemen(L): Menghasilkan elemen pertama dari list L}

# last_element: list != [] --> element
#   {last_element(L): Menghasilkan elemen terakhir dari list L}

# is_empty: list --> boolean
#   {is_empty(L): benar apabila list kosong. }

# is_member: list != [],elemen --> boolean
#   {is_member(L,e): benar apabila e adalah anggota dari list L, menggunakan konsi}

# nb_element: list --> integer
#   {nb_element(L): Menghasilkan banyaknya elemen list L}

# prec: integer --> integer
#   {prec(n): Mengembalikan nilai n-1}

# tail: list --> list
#   {tail(L): menghasilkan list tanpa elemen pertama list L, bisa kosong}

# head: list --> list
#   {head(L): menghasilkan list tanpa elemen terakhir list L, bisa kosong}

# REALISASI (dengan konso)(dengan python)
def is_empty(L):
    return L == []

def is_member(L,e):
    #konsi
    if is_empty(L):
        return False
    elif last_element(L) == e: 
        return True
    else:
        return False or is_member(head(L),e)

def head(L):
    return L[:-1]

def tail(L):
    return L[1:]

def nb_element(L):
    if is_empty(L):
        return 0
    else:
        return 1 + nb_element(tail(L))

def first_element(L):
    if not is_empty(L):
        return L[0]
    else:
        return 

def last_element(L):
    if not is_empty(L):
        return L[-1]
    else:
        return 

def prec(n):
    return n-1 

def elemen_ke_n(n,L):
    if is_empty(L) or n > nb_element(L) or n < 1:
        return 
    elif n == 1:#basis 1
        return first_element(L)
    else:
        return elemen_ke_n(prec(n),tail(L))

def is_x_element_ke_n(x,n,L):
    if is_empty(L) or not is_member(L,x) or n < 1 or n > nb_element(L):
        return False
    elif n == 1 and x == first_element(L): #basis 1
        return True
    else:
        return False or is_x_element_ke_n(x,prec(n),tail(L))

# REALISASI (dengan fungsi elemen_ke_n()) (dengan python)
def is_x_element_ke_n_v2(x,n,L):
    if is_empty(L) or not is_member(L,x) or n < 1 or n > nb_element(L):
        return False
    else:
        return elemen_ke_n(n,L) == x


# APLIKASI
print("V1")
print(is_x_element_ke_n('b',2,['a','b','c','d','e']))
print(is_x_element_ke_n('c',4,['a','b','c','d','e']))
print(is_x_element_ke_n('c',6,['a','b','c','d','e']))
print(is_x_element_ke_n('z',2,['a','b','c','d','e']))
print(is_x_element_ke_n('e',5,['a','b','c','d','e']))
print("V2")
print(is_x_element_ke_n_v2('b',2,['a','b','c','d','e']))
print(is_x_element_ke_n_v2('c',4,['a','b','c','d','e']))
print(is_x_element_ke_n_v2('c',6,['a','b','c','d','e']))
print(is_x_element_ke_n_v2('z',2,['a','b','c','d','e']))
print(is_x_element_ke_n_v2('e',5,['a','b','c','d','e']))