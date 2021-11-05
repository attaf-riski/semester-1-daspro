# Nama File : 24060121120005_ResponsiA2_Prak-9.py
# Deskripsi : Kumpulan fungsi-fungsi pada set 
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 5 November 2021

# DEFINISI DAN SPESIFIKASI
# konso : elemen, List  --> List 
#   {konso(e,L): menghasilkan sebuah list dari e dan L, dengan e sebagai  elemen pertama e 
#   :   e o L --> L'}  

# first_elmnt: List tidak kosong  -->  elemen 
#    {first_elmnt(L) Menghasilkan elemen pertama list L }

# tail : List tidak kosong -->  List 
#    {tail(L) : Menghasilkan  list tanpa elemen pertama list L, mungkin kosong } 
 
# is_empty : List --> boolean 
#   {is_empty(L)  benar jika list kosong } 
 
# make_set : List --> set 
#   {make_set(L): membuat sebuah set dari sebuah list  } 
#   { yaitu membuang semua kemunculan yang lebih dari satu kali} 
#   { List kosong tetap menjadi list kosong } 

# is_set : List --> boolean 
#   { is_set(L): true jika L adalah set } 

# is_sub_set : 2 set --> boolean 
#   {  is_sub_set(H1,H2):  true  jika    H1  adalah  subset  dari  H2:  semua  elemen  H1  adalah  juga  
#   merupakan elemen H2 }

# make_intersect : 2 set --> set 
#   {make_intersect(H1,H2):   membuat  interseksi  H1  dengan  H2  :  yaitu  set  baru  dengan  anggota  
#   elemen yang merupakan anggota H1 dan juga anggota H2 }

# make_union : 2 set --> set 
#   { make_union(H1,H2)  membuat union H1 dengan H2 : yaitu set baru dengan semua anggota 
#   elemen H1 dan anggota H2 }

# is_member  : elemen, List --> boolean 
# { is_member(e,L)   true jika e adalah elemen list L } 

# rember : elemen, List --> List 
#   { rember (x,L)  menghapus sebuah elemen bernilai x dari list  } 
#   { list yang baru berkurang SATU elemennya yaitu yang bernilai e } 
#   { List kosong tetap menjadi list kosong } 

# multi_rember : elemen, List --> List 
#   { multi_rember (x,L)  menghapus semua elemen bernilai x dari list  } 
#   { list yang baru tidak lagi mempunyai elemen yang bernilai x } 
#   { List kosong tetap menjadi list kosong } 

# is_eq_set : 2 set --> boolean 
#   {  is_eq_set(H1,H2):  true  jika  H1    "sama  dengan"  H2,  yaitu    jika  semua  elemen  H1  juga  
#    merupakan elemen H2, tanpa peduli urutannya } 
#   { H1==H2 jika dan hanya jika H1 adalah subset H2 dan H2 adalah subset H1}

# is_intersect : 2 set --> boolean 
# {  is_intersect(H1,H2):  true  jika  H1  berinterseksi  dengan  H2  :  minimal  ada  satu  anggota  
# yang  sama.  Himpunan  kosong  bukan  merupakan  himpunan  yang  berinterseksi  dengan  
# himpunan apapun } 

# REALISASI
def konso(e,L):
    if is_empty(L):
        return [e]
    else:
        return [e] + L

def first_elmnt(L):
    return L[0]

def tail(L):
    return L[1:]

def is_empty(L):
    return L == []

def make_set(L):
    if(is_empty(L)): #basis
        return L
    else:
        if is_member(first_elmnt(L),tail(L)): #skip
            return make_set(tail(L))
        else:
            return konso(first_elmnt(L),make_set(tail(L)))

def is_set(L):
    if is_empty(L):
        return True
    else:
        if is_member(first_elmnt(L),tail(L)):
            return False
        else:
            return is_set(tail(L))

def is_subset(H1,H2):
    if is_empty(H1):
        return True
    else:
        if is_member(first_elmnt(H1),H2): #rekurens
            return is_subset(tail(H1),H2)
        else:
            return False

def make_intersect(H1,H2):
    if is_empty(H1) or is_empty(H2):
        return []
    else:
        if is_member(first_elmnt(H1),H2):
            return konso(first_elmnt(H1),make_intersect(tail(H1),H2))
        else:
            return make_intersect(tail(H1),H2)

def make_union(H1,H2):
    if is_empty(H1):
        return H2
    elif is_empty(H2):
        return H1
    elif is_empty(H1) and is_empty(H2):
        return []
    else:
        if is_member(first_elmnt(H1),H2): #skip
            return make_union(tail(H1),H2)
        else:
            return konso(first_elmnt(H1),make_union(tail(H1),H2))

def is_member(x,L):
    if is_empty(L):
        return False
    else: #rekurens
        if first_elmnt(L) == x:
            return True
        else: #rekurens #skip
            return is_member(x,tail(L))

def rember(x,L):
    if is_empty(L):
        return L
    else:
        if not x == first_elmnt(L):
            return konso(first_elmnt(L),tail(L))
        else:
            return tail(L)

def multi_rember(x,L):
    if is_empty(L): #basis
        return L
    elif not is_member(x,L):
        return L
    else:
        if x == first_elmnt(L):#skip
            return multi_rember(x,tail(L))
        else: #rekurens
            return konso(first_elmnt(L),multi_rember(x,tail(L)))

def is_eq_set(H1,H2):
    return is_subset(H1,H2) and is_subset(H2,H1)

def is_intersect(H1,H2):
    if is_empty(H1):
        return False
    else: # tidak empty
        if is_member(first_elmnt(H1),H2):
            return True
        else:#rekurens
            return is_intersect(tail(H1),H2)

# APLIKASI
print("=====Program Started=====")

print("\n=||=====> Make Set")
print(make_set([1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5]))

print("\n=||=====> Is Set")
print(is_set([1,1,1,1]))
print(is_set([1,3,0,4]))

print("\n=||=====> Make Intersect")
print(make_intersect([1,2,3],[2,3,4]))

print("\n=||=====> Make Union")
print(make_union([0,1,2,3,4,5],[4,5,6,7,8,9,0]))

print("\n=||=====> Is Member")
print(is_member("sapi",["bebek","äyam","dara"]))
print(is_member("bebek",["bebek","äyam","dara"]))

print("\n=||=====> Rember")
print(rember(1,[1,1,2,3,4,1]))

print("\n=||=====> Multi Rember")
print(multi_rember(2,[1,2,3,4,2,10]))

print("\n=||=====> Is EQ Set")
print(is_eq_set([1,2],[2,1,1]))
print(is_eq_set([1,2],[3,2,1]))

print("\n=||=====> Is Intersect")
print(is_intersect([1,2],[2,3]))
print(is_intersect([100,200],[2,3]))

print("\n=====Program Ended=====")
