#faktorial
def faktorial_iteratif(n):
    fak=1
    for i in range(1,n+1):
        fak=fak*i
    return fak
#faktorial
def faktorial_rekursif(n):
    if n==1:
        return 1
    else:
        return n* faktorial_rekursif(n-1)
#fibonacci
def fibonacci_rekursif(n):
    if n==1 or n==0:
        return 1
    else: #n > 1
        return fibonacci_rekursif(n-1) + fibonacci_rekursif(n-2)


#NBElement
def is_empty(L):
    return L==[]

def first_element(L):
    if not(is_empty(L)):
        return L[0]

def tail(L):
    if not(is_empty(L)):
        return L[1:]
    
def NBElement(L):
    if is_empty(L):
        return 0
    else:
        return 1 + NBElement(tail(L))

L1 = []
L2 = [2,'a',-3,'semarang']

print(is_empty(L1))
print(is_empty(L2))
print(first_element(L2))
print(tail(L2))
print(NBElement(L1))
print(NBElement(L2))

