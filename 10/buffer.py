from typing import List


def is_atom(S):
    if type(S) != list:
        return True
    else:
        return False


def is_list(L):
    if type(L) == list:
        return True
    else:
        return False

def is_empty_LoL(L):
    return L == []

def konsLo(E,L):
    if is_empty_LoL(L):
        return [E]
    else:
        return [E] + L

def first_list(L):
    if not is_empty_LoL(L):
        return L[0]

def tail_list(S):
    return S[1:]

def last_list(S):
    return S[-1]

def head_list(S):
    return S[:-1]


#cara Pak Aris ngawur? 
# [[2],[3,2]] = sama lhoo
# [2,[3,2]] = sama lhoo

#[[1,2,3]] apakah sebuah atom pak?