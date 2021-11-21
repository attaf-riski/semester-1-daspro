# Nama File : LevelOfX.py
# Deskripsi : 
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 20 Nop 2021

# DEFINISI DAN SPESIFIKASI

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