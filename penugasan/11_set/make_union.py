# Nama File : make_union.py
# Deskripsi : Menghasilkan set hasil dari union 2 buah set
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 3 November 2021

# DEFINISI DAN SPESIFIKASI
# is_empty: List --> boolean
#   {is_empty(L): benar apabila List kosong. }

# konsi : List, elemen --> List 
#   {konsi(L,e):    menghasilkan  sebuah  list    dari  L  dan  e,  dengan  e  sebagai  elemen  terakhir  
#   list :  L •  e → L'}lkan sebuah List dari e dan L, dengan e sebagai  elemen pertama e 
#     :   e o L --> L'}

# last_element: list != [] --> element
#   {last_element(L): Menghasilkan elemen terakhir dari list L}

# head: list --> list
#   {head(L): menghasilkan list tanpa elemen terakhir list L, bisa kosong}

# is_member: List (tidak kosong ),elemen --> boolean
#   {is_member(L,e): benar apabila e adalah anggota dari list L}

# make_set(L) : list --> set 
#   {membuat sebuah set dari sebuah list} 
#   {yaitu membuang semua kemunculan yang lebih dari satu kali} 
#   {List kosong tetap menjadi list kosong }

# make_union  : 2 set --> set 
#   {make_union(H1,H2): Membuat  union  H1  dengan  H2  :  yaitu  set  baru  dengan  semua  
#    anggota elemen H1 dan anggota elemen H2 }
# REALISASI
def is_empty(L):
    return L == []

def konsi(L,e):
    if is_empty(L):
        return [e]
    else:
        return L + [e]

def last_elmnt(L):
    return L[-1]

def head(L):
    return L[:-1]

def is_member(e,L):
    if is_empty(L): # basis 0
        return False
    else:
        if last_elmnt(L) == e:
            return True
        else:#rekurens
            return False or is_member(e,head(L))

def make_set(L):
    if is_empty(L):#basis 0
        return []
    else:
        if is_member(last_elmnt(L),head(L)):
            return make_set(head(L))
        else:#rekurens
            return konsi(make_set(head(L)),last_elmnt(L),)

def make_union(H1,H2):
    if is_empty(H1) and is_empty(H2):
        return []
    elif is_empty(H1) and not is_empty(H2):
        return H2
    elif not is_empty(H1) and is_empty(H2):
        return H1
    else: #H1 and H2 not empty
        if is_member(last_elmnt(H2),H1): #skip
            return make_union(H1,head(H2))
        else:
            return konsi(make_union(H1,head(H2)),last_elmnt(H2))


# APLIKASI
print(make_union(make_set([1,2,2,3,6,1,0]),make_set([2,3])))
print(make_union(make_set([1,2,2,3,6,1,0]),make_set([])))
print(make_union(make_set([]),make_set([9,10])))