#=========================================
#konso
#type list harus tipe sama dengan elemen
# Konso : elemen, list -> list
# {Konso(e,L): menghasikan list dari e dan L, dengan e sebagai elemen pertama }

#ex
# list1 = [1,2,3,4,5,6] 
# kalau list kosong
# Realisas
def konso(e,L):
    if L == []:
        return [e]
    else:
        return [e] + L

#untuk list boleh ditulis langsung waktu pemanggilan fungsi tidak Mas? variabel masih tidak diperbolehkan kan sampai saat ini?
#kemarin Pak aris bolehin list isinya sama-sama tipe data primitif

#=======================================
#konsi
# konsi menghasilkan list dari L dan e, e sebagai elemen terakhir
def konsi(L,e):
    if L == []:
        return [e]
    else:
        return L + [e]

# firstelemen ==================================
def fe(L):
    if not L == []:
        return L[0]
# kalo umpamanya kalo diisi list kosong ngga diurus???

# last element =================================
def le(L):
     if not L == []:
        return L[-1]

# tail =========================================
# tanpa elemen pertamanya
# list[1:] indek ikut
# list[:4] index ngga ikut
def tail(L):
    if not L==[]:
        return L[1:]

#print(tail([1,2]))



# is_empty
def is_empty(L):
    return L == []

# akan ada fungsi-fungsi yang kepake
# nbelement ====================================
def nb_element(L):
    if is_empty(L):
        return 0
    else:
        return 1 + nb_element(tail(L))

# gimana cara nyebut dari basis

# is_one_element() =============================
# engga efektif
def is_one_element(L):
    return nb_element(L) == 1

L1 = [1,2,3,4,5,6,7]
L2 = [1]
#print(is_one_element(L1))
#print(is_one_element(L2))

# is_equal
def is_equal(L1,L2):
    if not nb_element(L1) == nb_element(L2):
        return False
    elif is_empty(L1) and is_empty(L2):
        return True
    else:
        return fe(L1) == fe(L2) and is_equal(tail(L1),tail(L2))

print(is_equal(L1,L2))
L2 = L1
print(is_equal(L1,L2))

# is_member() =========================================
def is_member(e,L):
    if is_empty(L):
        return False
    else:
        return fe(L) == e or is_member(e,tail(L))

# head =========================================
def head(L):
    if not L == []:
        return L[:-5]
#print(head([1,2,3,4,5]))

# inverse ======================================
def inverse(L):
    if is_empty(L):#basis 0
        return []
    else:#rekurens #konso
        #return konso(le(L),inverse(head(L)))
        return konsi(inverse(tail(L)),fe(L))

L1 = [1,2,3,4,5]
print(inverse(L1))

# tugas
#Tugas Praktikum :
#ElmtKeN
#Copy
#Concat
#IsFirst
#IsLast
#IsNbElmtN
#IsInverse
#IsXElmtkeN

#realisasikan fungsi-fungsi di atas dalam bahasa python menggunakan
#notasi fungsional sesuai dengan definisi dan spesifikasi yang
#diberikan di diktat

#kerjakan dalam satu file yang sama ( biar ngecek nya gampang hehe )
    
