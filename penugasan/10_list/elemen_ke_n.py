# Nama File : elemen_ke_n.py
# Deskripsi : Menghasilkan elemen ke-n dari sebuah list
# Nama : Attaf Riski Putra Ramaadhan
# Tanggal : 25 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# elemen_ke_n: integer>0, list != [] --> element
#   {elemen_ke_n(n,L): menghasilkan elemen ke-n list L, n > 0, dan n <= banyaknya elemen list }

# first_element: list != [] --> element
#   {first_elemen(L): Menghasilkan elemen pertama dari list L}

# is_empty: list --> boolean
#   {is_empty(L): benar apabila list kosong. }

# nb_elemen: list --> integer
#   {nb_elemen(L): Menghasilkan banyaknya elemen list L}

# prec: integer --> integer
#   {prec(n): Mengembalikan nilai n-1}

# tail: list --> list
#   {tail(L): menghasilkan list tanpa elemen pertama list L, bisa kosong}

# REALISASI (dengan konso)(dengan python)
def is_empty(L):
    return L == []

def tail(L):
    return L[1:]

def nb_elemen(L):
    if is_empty(L):
        return 0
    else:
        return 1 + nb_elemen(tail(L))

def first_element(L):
    if not is_empty(L):
        return L[0]
    else:
        return 

def prec(n):
    return n-1 

def elemen_ke_n(n,L):
    if is_empty(L) or n > nb_elemen(L) or n < 1:
        return 
    elif n == 1:#basis 1
        return first_element(L)
    else:
        return elemen_ke_n(prec(n),tail(L))

# APLIKASI
print(elemen_ke_n(1,[1,'2',3.0,4.5,5==5]))
print(elemen_ke_n(2,[1,'2',3.0,4.5,5==5]))
print(elemen_ke_n(3,[1,'2',3.0,4.5,5==5]))
print(elemen_ke_n(4,[1,'2',3.0,4.5,5==5]))
print(elemen_ke_n(5,[1,'2',3.0,4.5,5==5]))