# Nama File : make_intersect.py
# Deskripsi : Menghasilkan set hasil dari intersect 2 buah set
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 3 November 2021

# DEFINISI DAN SPESIFIKASI
# is_empty: List --> boolean
#   {is_empty(L): benar apabila List kosong. }

# konso : elemen, List  --> List 
#   {konso(e,L): menghasilkan sebuah List dari e dan L, dengan e sebagai  elemen pertama e 
#   :   e o L --> L'}

# first_elmnt: List (tidak kosong ) --> element
#   {first_elmnt(L): Menghasilkan elemen pertama dari List L}

# tail: List --> List
#   {tail(L): menghasilkan List tanpa elemen pertama List L, bisa kosong}

# is_member: List (tidak kosong ),elemen --> boolean
#   {is_member(L,e): benar apabila e adalah anggota dari list L}

# make_set(L) : list --> set 
#   {membuat sebuah set dari sebuah list} 
#   {yaitu membuang semua kemunculan yang lebih dari satu kali} 
#   {List kosong tetap menjadi list kosong }

# make_intersect  : 2 set --> set 
#   {make_intersect(H1,H2): membuat  interseksi  H1  dengan  H2  :  yaitu  set  baru  dengan  anggota  
#    elemen yang merupakan anggota H1 dan juga anggota H2 }

# REALISASI
def is_empty(L):
    return L == []

def konso(e,L):
    if is_empty(L):
        return [e]
    else:
        return [e] + L

def first_elmnt(L):
    return L[0]

def tail(L):
    return L[1:]

def is_member(e,L):
    if is_empty(L): # basis 0
        return False
    else:
        if first_elmnt(L) == e:
            return True
        else:#rekurens
            return False or is_member(e,tail(L))

def make_set(L):
    if is_empty(L):#basis 0
        return []
    else:
        if is_member(first_elmnt(L),tail(L)): #skip
            return make_set(tail(L))
        else:#rekurens
            return konso(first_elmnt(L),make_set(tail(L)))

def make_intersect(H1,H2):
    if is_empty(H1) or is_empty(H2): #basis 0
        return []
    else:
        if is_member(first_elmnt(H1),H2) :
            return konso(first_elmnt(H1),make_intersect(tail(H1),H2))
        else: #rekurens
            return make_intersect(tail(H1),H2)

# APLIKASI
print(make_intersect(make_set([1,2,2,3,4,5,5]),make_set([4,4,5,5,6,7,8,9,9,10])))
print(make_intersect(make_set([]),make_set([4,4,5,5,6,7,8,9,9,10])))
print(make_intersect(make_set(["ayam","kambing","sapi"]),make_set(["kambing"])))