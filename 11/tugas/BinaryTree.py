# Nama File : BinaryTree.py
# Deskripsi : Binary Tree beserta fungsi-fungsinya, Tugas ada di paling bawah
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 20 Nop 2021

# DEFINISI DAN SPESIFIKASI TYPE
# type Elemen :   { tergantung type node } 

# type  BinaryTree : < A : Elemen, L : BinaryTree, R : BinaryTree > {notasi prefix}
#    {BinaryTree  terdiri  dari  Akar  yang  berupa  elemen,  L  dan  R  adalah  BinaryTree  yang  
#    merupakan subtree kiri dan subtree kanan }
# REALISASI (dalam python)
class BinaryTree:
    def __init__(self,A,L,R):
        self.A = A
        self.L = L
        self.R = R


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR 
# MakeBT: Elemen, 2 BinaryTree --> BinaryTree
#   { MakeBT(A,L,R): Membuat sebuah BinaryTree dengan A sebagai Akar  yang  berupa  elemen,  L  dan  R  adalah  BinaryTree  yang  
#    merupakan subtree kiri dan subtree kanan }
# REALISASI (dalam python)
def MakeBT(A,L,R):
    return BinaryTree(A,L,R)

# DEFINISI DAN SPESIFIKASI SELEKTOR
# root: BinaryTree tidak kosong --> Elemen
#   {root(T): Menghasilkan sebuah root dari BinaryTree T}
# REALISASI (dalam python)
def root(T):
    return T.A

# left: BinaryTree tidak kosong --> BinaryTree
#   {left(T): Menghasilkan subtree left dari child left BinaryTree T}
# REALISASI (dalam python)
def left(T):
    return T.L

# right: BinaryTree tidak kosong --> BinaryTree
#   {right(T): Menghasilkan subtree right dari child right BinaryTree T}
# REALISASI (dalam python)
def right(T):
    return T.R

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmptyTree : BinaryTree --> boolean 
#   {IsEmptyTree (P) true jika P adalah BinaryTree kosong : (/ \) }
# REALISASI (dalam python)
def IsEmptyTree(T):
    return T == None

# IsOneElmt : BinaryTree --> boolean 
#   {IsOneElmt(T) true jika T hanya terdiri dari Akar } 
# REALISASI (dalam python)
def IsOneElement(T):
    if IsEmptyTree(T):
        return False
    else:
        return IsEmptyTree(left(T)) and IsEmptyTree(right(T))

# IsUnaryLeft : BinaryTrue --> boolean 
#   {IsUnaryLeft(P) true jika P hanya mengandung sub pohon kiri tidak kosong: (//L A \\) 
# REALISASI (dalam python)
def IsUnaryLeft(T):
    if IsEmptyTree(T):
        return False
    else:
        return not IsEmptyTree(left(T)) and IsEmptyTree(right(T))

# IsUnerRight : BinaryTree -->  boolean 
#   {IsUnerRight (P) true jika P hanya mengandung sub pohon kanan tidak kosong: (//A R\\) }
# REALISASI (dalam python)
def IsUnaryRight(T):
    if IsEmptyTree(T):
        return False
    else:
        return IsEmptyTree(left(T)) and not IsEmptyTree(right(T))

# IsBinary : PohonBiner  tidak kosong --> boolean 
#   {IsBinary(T) true jika T  mengandung sub pohon kiri dan sub pohon kanan :  
#   (//L A R\\) }
# REALISASI (dalam python)
def IsBinary(T):
    if IsEmptyTree(T):
        return False
    else:
        return not IsEmptyTree(left(T)) and not IsEmptyTree(right(T))

#DEFINISI DAN SPESIFIKASI FUNGSI LAIN
# RepPrefix: BinaryTree --> list of list 
#   {RepPrefix (P) memberikan representasi linier (dalam bentuk list), dengan urutan elemen 
#   list sesuai dengan urutan penulisan pohon secara prefix : 
#   Basis-0 : RepPrefix (//\ \) = [] 
#   Rekurens :RepPrefix (/A,L,R\) = [A] o RepPrefix(L) o  RepPrefix (R)   } 
#   REALISASI (dalam python)
from FungsiAntara import konsoL
def RepPrefix(P):
    if IsEmptyTree(P):
        return []
    else:
        return konsoL(konsoL(root(P),RepPrefix(left(P))),RepPrefix(right(P)))


#★░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░★
#★░░░░░░░░░███░██░░░░░░░░░░░░░░░░░░░░★
#★░░░░░░░░░██░░░█░░░░░░░░░░░░░░░░░░░░★
#★░░░░░░░░░██░░░██░░░░░░░░░░░░░░░░░░░★
#★░░░░░░░░░░██░░░███░░░░░░░░░░░░░░░░░★
#★░░░░░░░░░░░██░░░░██░░░░░░░░░░░░░░░░★
#★░░░░░░░░░░░██░░░░░███░░░░░░░░░░░░░░★
#★░░░░░░░░░░░░██░░░░░░██░░░░░░░░░░░░░★
#★░░░░░░░███████░░░░░░░██░░░░░░░░░░░░★
#★░░░░█████░░░░░░░░░░░░░░███░██░░░░░░★
#★░░░██░░░░░████░░░░░░░░░░██████░░░░░★
#★░░░██░░████░░███░░░░░░░░░░░░░██░░░░★
#★░░░██░░░░░░░░███░░░░░░░░░░░░░██░░░░★
#★░░░░██████████░███░░░░░░░░░░░██░░░░★
#★░░░░██░░░░░░░░████░░░░░░░░░░░██░░░░★
#★░░░░███████████░░██░░░░░░░░░░██░░░░★
#★░░░░░░██░░░░░░░████░░░░░██████░░░░░★
#★░░░░░░██████████░██░░░░███░██░░░░░░★
#★░░░░░░░░░██░░░░░████░███░░░░░░░░░░░★
#★░░░░░░░░░█████████████░░░░░░░░░░░░░★
#★░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░★

# TUGAS ==============================================================================

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsMember : BinaryTree, elemen --> boolean 
#   {IsMember(P,X) Mengirimkan true jika ada node  dari P yg bernilai X }
# REALISASI (dalam python)
def IsMember(P,X):
    if(IsEmptyTree(P)): # basis-0
        return False
    elif root(P) == X : # X ditemukan di P
        return True
    elif IsOneElement(P): # basis-1
        return False
    else: # rekurens
        return IsMember(left(P),X) or IsMember(right(P),X)    

# IsSkewLeft: BinaryTree --> boolean 
#   { IsSkewLeft(P) Mengirimkan true jika P adalah pohon condong kiri } 
# REALISASI (dalam python)
def IsSkewLeft(P):
    if(IsEmptyTree(P)): # basis-0
        return False
    elif IsOneElement(P): # basis-1
        return True
    elif IsUnaryLeft(P): # rekurens
        return IsSkewLeft(left(P))
    else: # Ditemukan right child
        return False

# IsSkewRight : BinaryTree --> boolean 
#   { IsSkewRight(P) Mengirimkan true jika P adalah pohon condong kanan } 
# REALISASI (dalam python)
def IsSkewRight(P):
    if(IsEmptyTree(P)): # basis-0
        return False
    elif IsOneElement(P): # basis-1
        return True
    elif IsUnaryRight(P): # rekurens
        return IsSkewRight(right(P))
    else: # Ditemukan left child
        return False

# DEFINISI DAN SPESIFIKASI OPERATOR
# AddDaunTerkiri : BinaryTree, elemen --> BinaryTree  
#   {AddDaunTerkiri(P,X):  mengirimkan  Pohon  Biner  P  yang  telah  bertambah  simpulnya,  
#   dengan X sebagai simpul daun terkiri }
# REALISASI (dalam python)
def AddDaunTerkiri(P,X):
    if IsBinary(P): # P mempunyai left dan right
        return MakeBT(root(P),AddDaunTerkiri(left(P),X),right(P))
    elif IsUnaryLeft(P): # P hanya punya left child
        return MakeBT(root(P),AddDaunTerkiri(left(P),X),None)
    elif IsUnaryRight(P): # P hanya punya right child
        return MakeBT(root(P),MakeBT(X,None,None),right(P))
    elif IsOneElement(P): # P tak punya anak
        return MakeBT(root(P),MakeBT(X,None,None),None)
    else: #BinaryTree Kosong
        return MakeBT(X,None,None)

# DEFINISI DAN SPESIFIKASI FUNGSI LAIN
# LevelOfX: BinaryTree, Elemen --> integer 
#   { LevelOfX(P,X) Mengirimkan level dari node  X yang merupakan salah satu simpul dari 
#     pohon biner P }
# REALISASI (dalam python)
def LevelOfX(P,X):
    if root(P) == X: # Ditemukan X dalam P
        return 0
    elif IsMember(left(P),X): # Ada X dalam left(P)
        return 1 + LevelOfX(left(P),X)
    elif IsMember(right(P),X): # Ada X dalam right(P)
        return 1 + LevelOfX(right(P),X)
    else: #BinaryTree kosong atau X bukan elemen P
        return -1

# APLIKASI
T = MakeBT(
    1,
    MakeBT(2,
            MakeBT(3,
                    None
                    ,None)
            ,MakeBT(4,
                    MakeBT(0,
                            None,None),
                    None)),
    MakeBT(5,
            None,None))

T2 = None 

T3 = MakeBT(
    1,
    MakeBT(2,
            MakeBT(3,
                    None,None)
            ,None),
   None)

T4 = MakeBT(
    1,
    None,
    MakeBT(3,
            None
            ,None))

print("=======Program Start=======")
print("\n*******LevelOfX")
print(LevelOfX(T,0))
print(LevelOfX(T4,3))

print("\n*******AddDaunTerkiri")
print(RepPrefix(T))
print(RepPrefix(AddDaunTerkiri(T,9)))

print("\n*******IsSkewLeft ")
print(IsSkewLeft(T3))
print(IsSkewLeft(T))

print("\n*******IsSkewRight")
print(IsSkewRight(T4))
print(IsSkewRight(T))

print("\n*******IsMember")
print(IsMember(T,0))
print(IsMember(T2,0))

print("\n=======Program Finish=======")