# Nama File : responsi_prak_11.py
# Deskripsi : Binary Tree beserta fungsi-fungsinya
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 19 Nop 2021

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
# { MakeBT(A,L,R): Membuat sebuah BinaryTree dengan A sebagai Akar  yang  berupa  elemen,  L  dan  R  adalah  BinaryTree  yang  
#    merupakan subtree kiri dan subtree kanan }
# REALISASI (dalam python)
def MakeBT(A,L,R):
    return BinaryTree(A,L,R)

# DEFINISI DAN SPESIFIKASI SELEKTOR
# root: BinaryTree tidak kosong --> Elemen
# {root(T): Menghasilkan sebuah root dari BinaryTree T}
# REALISASI (dalam python)
def root(T):
    return T.A

# left: BinaryTree tidak kosong --> BinaryTree
# {left(T): Menghasilkan subtree left dari child left BinaryTree T}
# REALISASI (dalam python)
def left(T):
    return T.L

# right: BinaryTree tidak kosong --> BinaryTree
# {right(T): Menghasilkan subtree right dari child right BinaryTree T}
# REALISASI (dalam python)
def right(T):
    return T.R

# DEFINISI PREDIKAT
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

# REALISASI (dalam python)
#   IsUnaryLeft : BinaryTrue --> boolean 
#   {IsUnaryLeft(P) true jika P hanya mengandung sub pohon kiri tidak kosong: (//L A \\) 
def IsUnaryLeft(T):
    if IsEmptyTree(T):
        return False
    else:
        return not IsEmptyTree(left(T)) and IsEmptyTree(right(T))

#   IsUnerRight : BinaryTree -->  boolean 
#   {IsUnerRight (P) true jika P hanya mengandung sub pohon kanan tidak kosong: (//A R\\) }
# REALISASI (dalam python)
def IsUnaryRight(T):
    if IsEmptyTree(T):
        return False
    else:
        return IsEmptyTree(left(T)) and not IsEmptyTree(right(T))

# IsBinary : PohonBiner  tidak kosong --> boolean 
# {IsBinary(T) true jika T  mengandung sub pohon kiri dan sub pohon kanan :  
# (//L A R\\) }
# REALISASI (dalam python)
def IsBinary(T):
    if IsEmptyTree(T):
        return False
    else:
        return not IsEmptyTree(left(T)) and not IsEmptyTree(right(T))

# DEFINISI DAN SPESIFIKASI OPERATOR
# NbElmt : BinaryTree --> integer ≥ 0 
#   {NbElmt(P) memberikan Banyaknya elemen dari BinaryTree P : 
#   Basis : NbElmt (//\ \) = 0 
#   Rekurens : NbElmt (/L,A,R\) = NbElmt(L) + 1 + NbELmt(R)   }
# REALISASI (dalam python)
def NbElmnt(P):
    if(IsEmptyTree(P)):
        return 0
    else:
        return NbElmnt(left(P)) + 1 + NbElmnt(right(P))

# konsoL : Elemen,List of List --> List of List
#   {konsoL(E,L): membuat list baru hasil konkatenasi Elemen E dengan List of List L, Elemen ditaruh di depan}
# REALISASI (dalam python)
def konsoL(E,L):
    if L == []:
        return [E]
    else:
        return [E] + L

# NbDaun : PohonBiner --> integer ≥ 0 
#   {NbDaun (P) memberikan Banyaknya daun  dari pohon P : 
#   Basis-0 : NbDaun  (//\ \) = 0 
#   Basis-1 : NbDaun  (//A\ \) = 1
#   Rekurens : NbElmt (/A,L,R\) = NBDaun(L) + NBDaun(R)
#      NbDaun1 (P)
# REALISASI (dalam python)
def NBDaun(P):
    if IsEmptyTree(P):
        return 0
    elif IsOneElement(P):
        return 1
    else:
        return NBDaun(left(P)) + NBDaun(right(P))

# RepPrefix: BinaryTree --> list of list 
#   {RepPrefix (P) memberikan representasi linier (dalam bentuk list), dengan urutan elemen 
#   list sesuai dengan urutan penulisan pohon secara prefix : 
#   Basis-0 : RepPrefix (//\ \) = [] 
#   Rekurens :RepPrefix (/A,L,R\) = [A] o RepPrefix(L) o  RepPrefix (R)   } 
#   REALISASI (dalam python)
def RepPrefix(P):
    if IsEmptyTree(P):
        return []
    else:
        return konsoL(konsoL(root(P),RepPrefix(left(P))),RepPrefix(right(P)))

# APLIKASI
print("=== Program Started ===")

print("\n*****MakeBT")
T = MakeBT(
    1,
    MakeBT(2,
            MakeBT(3,
                    None,None)
            ,MakeBT(4,
                    MakeBT(0,
                            None,None),
                    None)),
    MakeBT(5,
            None,None))

print(RepPrefix(T))

print("\n*****root")
print(root(T))

print("\n*****left")
print(left(T).A)

print("\n*****right")
print(right(T).A)

print("\n*****IsEmptyTree")
print(IsEmptyTree(T))
print(IsEmptyTree(left(left(left(T)))))

print("\n*****IsOneElement")
print(IsOneElement(left(left(T))))
print(IsOneElement(T))

print("\n*****IsUnaryLeft")
print(IsUnaryLeft(T))
print(IsUnaryLeft(right(left(T))))

print("\n*****IsUnaryRight")
print(IsUnaryRight(T))

print("\n*****IsBinary")
print(IsBinary(T))
print(IsBinary(right(T)))

print("\n*****NbElmnt")
print(NbElmnt(T))

print("\n*****NbDaun")
print(NBDaun(T))

print("\n*****RepPrefix")
print(RepPrefix(right(T)))

print("\n=== Program Finished ===")