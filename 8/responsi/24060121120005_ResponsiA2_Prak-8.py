# Nama File : 24060121120005_ResponsiA2_Prak-8.py
# Deskripsi : Kumpulan fungsi-fungsi yang berhubungan dengan list dan rekursif
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 29 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# konso : elemen, List  --> List 
#   {konso(e,L): menghasilkan sebuah list dari e dan L, dengan e sebagai  elemen pertama e 
#   :   e o L --> L'}  

# konsi : List, elemen  -->  List 
#   {Konsi(L,e): menghasilkan sebuah list dari L dan e, dengan e sebagai elemen terakhir  
#   list : L i e --> L'}  

# first_elmnt: List tidak kosong  -->  elemen 
#    {first_elmnt(L) Menghasilkan elemen pertama list L }

# tail : List tidak kosong -->  List 
#    {tail(L) : Menghasilkan  list tanpa elemen pertama list L, mungkin kosong } 
 
# last_elmnt : List tidak kosong -->  elemen 
#    {last_elmnt(L) : Menghasilkan elemen terakhir list L } 
 
# head : List tidak kosong --> List 
#    {head(L) : Menghasilkan  list tanpa elemen terakhir list L,  mungkin kosong} 

# is_empty : List --> boolean 
#   {is_empty(L)  benar jika list kosong } 
 
# is_one_elmnt:  List  -->  boolean 
#    {is_one_elmnt(X,L) adalah benar jika list L hanya mempunyai satu elemen } 

# is_equal : 2 List  -->  boloean 
#   {  is_equal  (L1,L2)  benar    jika  semua  elemen  list  L1  sama  dengan  L2:  sama  urutan  dan  
#   sama nilainya } 

# nb_elmnt : List  -->  integer 
#   {nb_elmnt(L) : Menghasilkan banyaknya elemen list, nol jika kosong } 

# inverse : List  -->  List 
#   {  inverse(L)  :  Menghasilkan  list  L  yang  dibalik,  yaitu  yang  urutan  elemennya  adalah  
#   kebalikan dari list asal}

# is_member : elemen, List  -->  boolean 
#   {is_member(X,L) adalah benar jika X adalah elemen list L } 

# REALISASI
def konso(e,L):
    if L == []:
        return [e]
    else:
        return [e] + L

def konsi(L,e):
    if L == []:
        return [e]
    else:
        return L + [e]

def first_elmnt(L):
    if not L == []:
        return L[0]

def tail(L):
    if not L == []:
        return L[1:]

def last_elmnt(L):
    if not L == []:
        return L[-1]

def head(L):
    if not L == []:
        return L[:-1]

def is_empty(L):
    return L == []

def is_one_elmnt(X,L):
    return nb_elmnt(L) == X

def is_equal(L1,L2):
    if nb_elmnt(L1) == nb_elmnt(L2):
        if is_empty(L1) and is_empty(L2):
            return True
        elif first_elmnt(L1) == first_elmnt(L2):
            return True and is_equal(tail(L1),tail(L2))
        else:
            return False
    else:
        return False

def nb_elmnt(L):
    if is_empty(L): #basis 0
        return 0
    else:
        return 1 + nb_elmnt(tail(L))

def inverse(L):
    if is_empty(L):#basis 0
        return []
    else:#rekurens
        return konsi(inverse(tail(L)),first_elmnt(L))

def is_member(X,L):
    if is_empty(L): #basis 0
        return False
    elif first_elmnt(L) == X:
        return True
    else:
        return False or is_member(X,tail(L))

# APLIKASI
print("==========Program Started=========")
print("== konso")
print(konso(0,[1,2,3,4,5]))

print("\n== konsi")
print(konsi([1,2,3,4,5],6))

print("\n== first element")
print(first_elmnt(["Susu","Teh","Kopi","Jeruk","Jus"]))

print("\n== tail")
print(tail(["Susu","Teh","Kopi","Jeruk","Jus"]))

print("\n== last element")
print(last_elmnt(["Susu","Teh","Kopi","Jeruk","Jus"]))

print("\n== head")
print(head(["Susu","Teh","Kopi","Jeruk","Jus"]))

print("\n== is empty")
print(is_empty([]))
print(is_empty([1,2]))

print("\n== is one element")
print(is_one_elmnt(1,[1]))
print(is_one_elmnt(1,[]))

print("\n== is equal")
print(is_equal([1,2],[1,2]))
print(is_equal([1,2],[1,2,3]))

print("\n== is nb element")
print(nb_elmnt([1,2,4,5,6,75,42]))

print("\n== inverse")
print(inverse([1,2,3,4,5,6,7,8,9]))

print("\n== is member")
print(is_member(2,[1,2,3,4,5,6,7,8,9]))
print(is_member(100,[1,2,3,4,5,6,7,8,9]))
print("==========Program Finished========")