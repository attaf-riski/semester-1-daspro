#usefull resource
# https://www.hpc-carpentry.org/hpc-python/03-lists/index.html

L1 = ['pisang','tomat','salak','telur','kurma']
L2 = ['esteh','kopi','susu','syrup','jus']

def first_elemen(L):
    return L[0]

print(first_elemen(L1))
print(first_elemen(L2))


def tail(L):
    return L[1:]

print(tail(L1))
print(tail(L2))


#[1] list pertama
#[-1] list terakhir
#[:1] list sebelum index, index ngga masuk
#[1:] list setelah index, index masuk
#[:-1] Semua-mya kecuali list 1 terakhir
#[-1:] ??? list setelah terakhir?
def last_elemen(L):
    return L[-1]

print(last_elemen(L1))
print(last_elemen(L2))

def head(L):
    return L[:-1]
print(head(L1))
print(head(L2))

L3 = []
def is_empty(L):
    return L == []
print(is_empty(L3))
print(is_empty(L2))

L3 = [1]
def is_one_element(L):
    return L[1:] == []
print(is_one_element(L1))
print(is_one_element(L3))

L3 = L2
def is_equal(L1,L2):
    return L1 == L2

def is_equal_2(L1,L2):
    if is_empty(L1) and is_empty(L2):
        return True
    else: # list tidak kosong
        if is_empty(L1): # indikasi L1 udah kosong, tapi L2 belum kosong
            return False
        elif L1[0] != L2[0]:
            return False
        else:
            return True and is_equal_2(tail(L1),tail(L2))

print("===")
print(is_equal_2(L3,L2))
print(is_equal_2(L3,L1))
print(is_equal(L3,L2))
print(is_equal(L3,L1))

L3 = []
def nbelement(L):
    if is_empty(L):
        return 0
    else: # L tidak kosong
        return 1 + nbelement(tail(L))
print(nbelement(L1))
print(nbelement(L3))

def element_ke_n(N,L):
    return L[N]
print(element_ke_n(1,L1))
#print(element_ke_n(1,L3))

def copy(L):
    return L
print(L3)
L3 = copy(L1)
print(L3)

def inverse(L):
    if is_empty(L):
        return L
    else:
        return [L[-1]] + inverse(head(L))
print(L3)
L3 = inverse(L1)
print(L3)

def konkat(L1,L2):
    return L1 + L2
print(L3)
L3 = konkat(L1,L2)
print(L3)

def is_member(X,L):
    if is_empty(L):
        return False
    else: # list tidak kosong
        if L[0] == X:
            return True
        else:
            return False or is_member(X,tail(L))
print(is_member('kurma',L3))

def is_nb_element(X,L):
    return X == nbelement(L)
print(is_nb_element(10,L3))
print(is_nb_element(11,L3))


def is_inverse(L1,L2):
    return L1 == inverse(L2)
L3 = inverse(L2)
print(is_inverse(L2,L3))


def is_x_elemen_ke_N(N,X,L):
    return X == L[N-1]
print(is_x_elemen_ke_N(1,'pisang',L1))