# Nama File : uas.py
# Deskripsi : latihan uas
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 5 Dec 2021


# NO 1 === DONE
def empty_list(L):
    return L == []

def first_element(L):
    return L[0]

def tail(L):
    return L[1:]

def is_one_element(L):
    if not empty_list(L) and empty_list(tail(L)):
        return True
    else:
        return False

def max2(a,b):
    if a>=b:
        return a
    else:
        return b

def min2(a,b):
    if a<=b:
        return a
    else:
        return b

# max_list: List of integer tidak kosong --> integer
def max_list(L): 
    if is_one_element(L): #basis 1
        return first_element(L)
    else: #rekurens
        return max2(first_element(L),max_list(tail(L)))

def min_list(L):
    if is_one_element(L):
        return first_element(L)
    else:
        return min2(first_element(L),min_list(tail(L)))

#L1 = [9,2,5,1,4,-3,10,-9,1]
L1 = [19,21,25,11,14,-13,10,-19,10]
#print(max_list(L1))
#print(min_list(L1))

# SOAL 2 === DONE

def root(T):
    return T[0]

def left(T):
    return T[1]

def right(T):
    return T[2]

def is_one_element(T):
    if empty_list(T):
        return False
    else:
        return empty_list(right(T)) and empty_list(left(T)) 

def is_uner_right(T):
    if empty_list(T):
        return False
    else:
        return not empty_list(right(T)) and empty_list(left(T))

def is_uner_left(T):
    if empty_list(T):
        return False
    else:
        return empty_list(right(T)) and not empty_list(left(T))

def is_biner(T):
    if empty_list(T):
        return False
    else:
        return not empty_list(right(T)) and not empty_list(left(T))

def total_elemen_daun(T):
    if is_one_element(T):
        return root(T)
    elif empty_list(T):
        return 0
    else: # is_binary or is_uner_left or is_uner_right
        return total_elemen_daun(left(T)) + total_elemen_daun(right(T))

def nb_elemen(T):
    if is_one_element(T):
        return 1
    elif empty_list(T):
        return 0
    else:
        return 1 + nb_elemen(left(T)) + nb_elemen(right(T)) 

def total_element_node(T):
    if is_one_element(T):
        return root(T)
    elif empty_list(T):
        return 0
    else:
        return root(T) + total_element_node(left(T)) + total_element_node(right(T)) 

def max_elemen_daun(T):
    if is_one_element(T):
        return root(T)
    elif empty_list(T):
        return 0
    else: # is_binary or is_uner_left or is_uner_right
        return max2(max_elemen_daun(left(T)),max_elemen_daun(right(T)))

def rata2_elemen_node(T):
    return total_element_node(T) / nb_elemen(T)

T1 = [8,
       [3,
          [1,[],[]],
          [6,
             [4,[],[]],
             [7,[],[]]
          ]
       ],
       [10,
          [],
          [14,
            [13,[],[]],
            []
          ]
        ]
     ]

T2 = [50,[17,[12,[9,[],[]],[14,[],[]]],[23,[19,[],[]],[]]],[72,[54,[],[67,[],[]]],[76,[],[]]]]

print(total_elemen_daun(T2))
print(total_element_node(T2))
print(max_elemen_daun(T2))
print(rata2_elemen_node(T2))

# C
# Dimasukan sebuah Binary tree T terurut
# Ingin mencari key berupa angka 7

# konsep, 
# root left child lebih kecil dari root
# root right child lebih besar dari root


# Cek apakah akar(T) yaitu 8 = 7? Salah.
# Cek apakah akar(T) yaitu 8 = []? Salah.
# Cek apakah T itu one_element? Salah
# Cek apakah akar(T) yaitu 8 > 7? Benar.
    #  Kembalikan child left(T), lakukan pengecakan lagi
# Cek apakah akar(T) yaitu 3 = 7? Salah.
# Cek apakah akar(T) yaitu 3 = []? Salah.
# Cek apakah T itu one_element? Salah
# Cek apakah akar(T) yaitu 3 > 7? Salah.
    # Kembalikan child right(T), lakukan pengecekan lagi
# Cek apakah akar(T) yaitu 6 = 7? Salah.
# Cek apakah akar(T) yaitu 6 = []? Salah.
# Cek apakah T itu one_element? Salah
# Cek apakah akar(T) yaitu 6 > 7? Salah.
    # Kembalikan child right(T), lakukan pengecekan lagi
# Cek apakah akar(T) yaitu 7 = 7? Benar.
    # Kembalikan True, hentikan rekursif

# No 3 == Done
def konso(e,L):
    if empty_list(L):
        return [e]
    else:
        return [e] + L

def kelipatan10(i):
    return i % 10 == 0

def bukan_kelipatan10(i):
    return not kelipatan10(i)

def Filter_List(Li,f):
    if empty_list(Li):
        return []
    elif f(first_element(Li)):
        return konso(first_element(Li),Filter_List(tail(Li),f))
    else: #skip karena tidak satisfy f
        return Filter_List(tail(Li),f)

L1 = [40,8,11,20,19,23,30]
L2=Filter_List(L1,kelipatan10)
L3=Filter_List(L1,bukan_kelipatan10)
#print(L2)
#print(L3)

L2 = Filter_List(L1, lambda x:x % 10 == 0)
L3 = Filter_List(L1, lambda x:x % 10 != 0)
#print(L2)
#print(L3)

# No 4 === Done
def is_member(x,S):
    if empty_list(S):
        return False
    elif x == first_element(S):
        return True
    else:
        return is_member(x,tail(S))
    
def is_sub_set(H1,H2):
    if empty_list(H1):
        return True
    else:
        if is_member(empty_list(H1),H2): #rekurens
            return is_sub_set(tail(H1),H2)
        else:
            return False

def minus(A,B):
    if empty_list(A):
        return []
    elif is_sub_set(A,B):
        return []
    elif is_member(first_element(A),B):
        return minus(tail(A),B)
    else: #suatu elemen A bukan elemen B
        return konso(first_element(A),minus(tail(A),B))

A = [5,2,6,7,9,15]
B = [2,7,15]

#print(minus(A,B))
    