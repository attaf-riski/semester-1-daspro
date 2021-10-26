# Nama File : is_inverse.py
# Deskripsi : Mengecek apakah benar suatu list merupakan kebalikan suatu list yang lain
# Nama : Attaf Riski Putra Ramaadhan
# Tanggal : 25 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# first_element: list != [] --> element
#   {first_elemen(L): Menghasilkan elemen pertama dari list L}

# last_element: list != [] --> element
#   {last_element(L): Menghasilkan elemen terakhir dari list L}

# is_empty: list --> boolean
#   {is_empty(L): benar apabila list kosong. }

# tail: list --> list
#   {tail(L): menghasilkan list tanpa elemen pertama list L, bisa kosong}

# head: list --> list
#   {head(L): menghasilkan list tanpa elemen terakhir list L, bisa kosong}

# nb_element: list --> integer
#   {nb_element(L): Menghasilkan banyaknya elemen list L}

# is_inverse: list,list --> boolean
#   {is_inverse(L1,L2): benar apabila L2 merupakan inverse dari L1}

# is_inverse_v2: list,list --> boolean
#   {is_inverse(L1,L2): benar apabila L2 merupakan inverse dari L1, menggunakan fungsi antara}

# inverse: list --> list
#   {inverse(L): Menghasilkan list berupa inverse dari list L}

# is_equal: list,list --> boolean
#   {is_equal(L1,L2): benar apabila list L1 sama dengan list L2, baik berupa jumlah elemen maupun urutan elemen}

# konso: elemen,list --> list
#   {konso(e,L): menambahkan elemen e pada awal list L}

# konsi: list,elemen --> list
#   {konsi(e,L): menambahkan elemen e pada akhir list L} 

# REALISASI 
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

def head(L):
    return L[:-1]

def tail(L):
    return L[1:]

def is_empty(L):
    return L == []

def nb_elemen(L):
    if is_empty(L):
        return 0
    else:
        return 1 + nb_elemen(tail(L))

def is_inverse(L1,L2):
    if nb_elemen(L1) == nb_elemen(L2):
        if is_empty(L1) and is_empty(L2): # basis 0
            return True
        else: # rekurens
            #pada diktat dihilangkan elemen pertama dan terakhir
            return first_element(L1) == last_element(L2) and is_inverse(tail(L1),head(L2))
    else: #salah bila jumlah elemen tidak sama
        return False

def is_equal(L1,L2):
    if nb_elemen(L1) == nb_elemen(L2):
        if is_empty(L1) and is_empty(L2): # basis 0
            return True
        else: #rekurens
            return first_element(L1) == first_element(L2) and is_equal(tail(L1),tail(L2))
    else: #panjang tidak sama
        return False

def konso(e,L):
    return [e] + L

def konsi(L,e):
    return L + [e]

def inverse(L):
    if is_empty(L):#basis 0
        return []
    else:#rekurens #konso
        #return konso(last_element(L),inverse(head(L)))
        return konsi(inverse(tail(L)),first_element(L))

def is_inverse_v2(L1,L2):
    return is_equal(L1,inverse(L2))

# APLIKASI
print("V1")
print(is_inverse([1,2,3,4,5,6],[6,5,4,3,2,1]))
print("V2")
print(is_inverse_v2([1,2,3,4,5,6],[6,5,4,3,2,1]))