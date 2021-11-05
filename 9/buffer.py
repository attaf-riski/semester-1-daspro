#tidak ada tugas, hanya ada responsi

#list_is_member = is_member

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

def is_member(x,L):
    if is_empty(L):
        return False
    else: #rekurens
        if first_elmnt(L) == x:
            return True
        else: #rekurens #skip
            return is_member(x,tail(L))

# Aljabar boolean
# True ^ True ^ True == True
# 1 + 0 = 1
# 1 + 1 + 1 = 1


def is_set(L):
    if is_empty(L):
        return True
    else:
        if is_member(first_elmnt(L),tail(L)):
            return False
        else:
            return is_set(tail(L))

def make_set(L):
    if(is_empty(L)): #basis
        return L
    else:
        if is_member(first_elmnt(L),tail(L)): #skip
            return make_set(tail(L))
        else:
            return konso(first_elmnt(L),make_set(tail(L)))

def is_subset(H1,H2):
    if is_empty(H1):
        return True
    else:
        if is_member(first_elmnt(H1),H2): #rekurens
            #improvement dari True and True and ... logika aljabar
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

#singkatnya elemen H1 dimana merupakan elemen H2 dibuang bila sudah, tambahkan H1 dan H2
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


# masalah paradigma
# Bang Roy session
def rember(x,L):
    if is_empty(L):
        return L
    else:
        if not x == first_elmnt(L):
            return konso(first_elmnt(L),tail(L))
        else:
            return tail(L)

print(rember(1,[1,1,1,2,2,2]))

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

# is eq set
def is_eq_set(H1,H2):
    return is_subset(H1,H2) and is_subset(H2,H1)

# is_intersect
def is_intersect(H1,H2):
    if is_empty(H1):
        return False
    else: # tidak empty
        if is_member(first_elmnt(H1),H2):
            return True
        else:#rekurens
            return is_intersect(tail(H1),H2)

print(is_intersect)
