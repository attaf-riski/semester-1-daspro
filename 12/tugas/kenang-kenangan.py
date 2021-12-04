"""
NIM             : 24060121120005
Nama            : Attaf Riski Putra Ramadhan
Deskripsi       : Tugas terakhir praktikum dasar pemrograman kelas A2 Informatika'21
Tanggal         : 4 Dec 2021
"""
# Boleh menggunakan import fungsi-fungsi dasar (tree harus membuat ulang karena bentuknya fungsional)
from list import *
from list_of_list import *
from set import *

#LIST#
L1 = []
L2 = [1,2,3]
L3 = [1, [2,3], [4]]
L4 = ['u', 'n', 'd', 'i', 'p']

#MATRIX#
M2 = [[1,2,3],[4,5,6],[7,8,9]]
M1 = [
           [1,2,3],
           [4,5,6],
           [7,8,9]
        ]

#SET#
H1 = [4, 5, 6]
H2 = []

#TREE#
# Tree dibuat seperti list of list, dengan urutan [atom_root, list_of_list_kiri, list_of_list_kanan]
# List kosong = none, sehingga leaf = [atom, [], []]

# P1:
#       1
#      / \
#     2   5
#    / \   
#   3   4

P1 = [1,
            [2,
                [3, [], []],
                [4, [], []]
            ],
            [5, [], []]
        ]

# P2: hanya root saja, yaitu 2
#      2

P2= [2, [], []]

"""""""LIST"""""""
"""1"""
# DefSpek
# SumElmtX : Integer, List of integer --> integer
# SumElmtX (X, L) menjumlahkan nilai elemen list tanpa elemen bernilai X
L = [1,2,3,4,5]
# Aplikasi : SumElmtX(5, L) --> 10

# Realisasi
def SumElmtX(X,L):
    if IsEmpty(L): # basis 0
        return 0
    else:
        if FirstElmt(L) == X: #skip
            return SumElmtX(X,Tail(L))
        else:
            return FirstElmt(L) + SumElmtX(X,Tail(L))

# Aplikasi
print("\nSumElmntX")
print(SumElmtX(5,L))

"""2"""
# DefSpek 
# MaxList : List of integer --> Integer
# MaxList(L) menghasilkan nilai elemen terbesar dari list L
L = [2,4,5,1]
# Aplikasi : MaxList(L) --> 5
# Hint : Untuk memudahkan, buat fungsi untuk mengecek nilai maksimum

# Max2 : 2 integer --> integer
# Max2(n1, n2) menentukan di antara n1 dan n2, nilai mana yang lebih besaer

# Realisasi
def Max2(n1,n2):
    if n1 >= n2:
        return n1
    else:
        return n2 

def MaxList(L):
    if IsOneElmt(L): # basis 1
        return FirstElmt(L)
    else:
        return Max2(FirstElmt(L),MaxList(Tail(L)))

# Aplikasi
print("\nMaxList")
print(MaxList(L))

"""3"""
# DefSpek 
# MinList : List of integer --> Integer
# MinList(L) menghasilkan nilai elemen terkecil dari list L
L = [2,4,5,1]
# Aplikasi : MinList(L) --> 1

# Min2 : 2 integer --> integer
# Min2(n1, n2) menentukan di antara n1 dan n2, nilai mana yang lebih kecil

# Realisasi
def Min2(n1,n2):
    if n1 <= n2:
        return n1
    else:
        return n2

def MinList(L):
    if IsOneElmt(L): # basis 1
        return FirstElmt(L)
    else:
        return Min2(FirstElmt(L),MinList(Tail(L)))

# Aplikasi
print("\nMinList")
print(MinList(L))

"""4"""
# DefSpek
# UraikanListOfList : List of list --> List
# UraikanListOfList(L) menghasilkan hasil penguraian dari List of list L menjadi list biasa
L = [1, [2,3], 4, [5]]
# Aplikasi : UraikanListOfList(L) --> [1, 2, 3, 4, 5]

# Realisasi
def UraikanListOfList(L):
    if IsEmpty(L): # basis 0
        return []
    else:
        if IsList(FirstList(L)):
            return Union(UraikanListOfList(FirstList(L)),UraikanListOfList(TailList(L)))
        elif IsAtom(FirstList(L)):
            return Konso(FirstList(L),UraikanListOfList(TailList(L)))

# Aplikasi
print("\nUraikanListOfList")
print(UraikanListOfList(L))

"""5"""
# DefSpek
# ListMaxMin : List of integer --> List
# ListMaxMin(L) membuat List dengan anggotanya hanya 2 elemen yaitu elemen terbesar dan terkecil dari list L
L = [4, 2, 5, 3, 7, 1]
# Aplikasi : ListMaxMin(L) ---> [1, 7] 

# Realisasi
def ListMaxMin(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(MinList(L),[MaxList(L)])

# Aplikasi
print("\nListMaxMix")
print(ListMaxMin(L))

"""6"""
# DefSpek
# SetElmtXzero : Integer, list of integer --> list of integer
# SetElmtXzero(L,X) menghasilkan list baru yang mengganti setiap elemen x menjadi 0
L = [1, 2, 3, 4, 5]
# Aplikasi : SetElmtXzero(L,3) --> [1, 2, 0, 4, 5]

# Realisasi
def SetElmtXzero(L,X):
    if IsEmpty(L):
        return L
    else:
        if X == FirstElmt(L):
            return Konso(0,SetElmtXzero(Tail(L),X))
        else:
            return Konso(FirstElmt(L),SetElmtXzero(Tail(L),X))

# Aplikasi
print("\nSetElmtXzero")
print(SetElmtXzero(L,3))

"""7"""
# DefSpek
# XPos : List of char --> Integer
# XPos(L,X) menghasilkan posisi index dari char X yang dicari
# L = ['j', 'a', 'y', 'a']
# Aplikasi : XPos(L,'a') --> 1 
# Hint : Index dimulai dari 0. Huruf 'a' pada contoh di atas berada pada POSISI INDEX ke-1 dari list L
#          Jika ada lebih dari satu karakter yang sama, return index karakter pertama yang ketemu

# Realisasi
def Xpos(L,X):
    if IsEmpty(L):
        return -1
    else:
        if FirstElmt(L) == X:
            return 0
        else:
            return 1 + Xpos(Tail(L),X)

# Aplikasi
print("\nXpos")
print(Xpos(['j', 'a', 'y', 'a'],'a'))

"""8"""
# DefSpek
# SortMax(L) : list of integer --> list of integer
# SortMax(L) menghasilkan list baru dimana mengurutkan elemen dari yang terbesar ke terkecil
# Hint : Ada di diktat, tinggal ubah sedikit

# InsertXSorted: integer, list of integer --> list of integer
# InsertXSorted(x, L) memasukkan x ke dalam sebuah list of integer dan x dimasukkan terurut dari terbesar ke terkecil

# Realisasi
def SortMax(L):
    if IsOneElmt(L): #basis
        return [FirstElmt(L)]
    else: #rekursif
        return Konso(MaxList(L),SortMax(Rember(MaxList(L),L)))

def InsertXSorted(x,L):
    if IsEmpty(L):
        return [x]
    else:
        return SortMax(Konso(x,L))

# Aplikasi
print("\nSortMax & InsertXSorted")
print(SortMax([3,6,1,9,3,8,5,1]))
print(InsertXSorted(7,[3,6,1,9,3,8,5,1]))

"""""""SET"""""""
"""9"""
# DefSpek
# RemberAll : Set --> Empty Set
# RemberAll(H) menghapus semua elemen pada set H
H = [1, 2, 3, 4]
# Aplikasi : RemberAll(H) --> []
# Hint : Jangan langsung return []

# Realisasi
def RemberAll(H):
    if IsEmpty(H): #basis 0
        return H
    else: #rekurens
        return RemberAll(Rember(FirstElmt(H),H))

# Aplikasi
print("\nRemberAll")
print(RemberAll(H))
        
"""""""TREE"""""""
# Deskripsi: Berikut merupakan fungsi - fungsi dasar tree dalam bentuk list of list yang dibuat sebelum membuat fungsi - fungsi tree lainnya

# Definisi dan Spesifikasi

# Fungsi Selektor (Hint: gunakan konsep tipe bentukan versi fungsional)
# L = [1, 2, 3], L[0] = 1, L[1] = 2, L[2] = 3

# root: binary tree --> elemen
# root(T) merupakan fungsi selektor yang akan mengembalikan nilai akar binary tree T

# left: binary tree --> elemen
# left(T) merupakan fungsi selektor yang akan mengembalikan nilai anak kiri binary tree T

# right: binary tree --> elemen
# right(T) merupakan fungsi selektor yang akan mengembalikan nilai anak kanan binary tree T

# Fungsi Predikat
# IsTree: list of list --> boolean
# IsBinaryTree(T) mengembalikan nilai true bila T merupakan tree (list of list berbentuk atom(root), LoL(left), dan LoL(right))
# Hint: gunakan NbElmt, IsAtom, dan IsList dari fungsi list of list

# IsOneElement: binary tree --> boolean
# IsOneElement(T) mengembalikan nilai true bila tree T hanya terdiri dari akar saja 

# IsUnaryLeft: binary tree --> boolean
# IsUnaryLeft(T) mengembalikan nilai true bila tree T merupakan tree uner kiri

# IsUnaryRight: binary tree --> boolean
# IsUnaryRight(T) mengembalikan nilai true bila tree T merupakan tree uner kanan

# IsBinary: binary tree --> boolean
# IsBinary(T) mengembalikan nilai true bila tree T merupakan tree biner

# Fungsi Lain
# mutlak: integer --> integer
# mutlak(I) menghasilkan nilai mutlak dari I

# Realisasi Selektor
def root(T):
    return T[0]

def left(T):
    return T[1]

def right(T):
    return T[2]

# Realisasi Fungsi Predikat
def IsTree(T):
    if IsEmptyLoL(T):
        return False
    elif not NbElmt(T) == 3:
        return False
    elif IsAtom(root(T)):
        return IsList(left(T)) and IsList(right(T))
    else:
        return False

def IsOneElement(T):
    if IsEmptyLoL(T):
        return False
    else :
        return IsEmptyLoL(left(T)) and IsEmptyLoL(right(T))

def IsUnaryLeft(T):
    if IsEmptyLoL(T):
        return False
    else:
        return not IsEmptyLoL(left(T)) and IsEmptyLoL(right(T))

def IsUnaryRight(T):
    if IsEmptyLoL(T):
        return False
    else:
        return IsEmptyLoL(left(T)) and not IsEmptyLoL(right(T))

def IsBinary(T):
    if IsEmptyLoL(T):
        return False
    else:
        return not IsEmptyLoL(left(T)) and not IsEmptyLoL(right(T))

def mutlak(I):
    if I >=0:
        return I
    else:
        return -I

"""10"""
# DefSpek
# TinggiPohon : Binary Tree --> Integer
# TinggiPohon(P) menghasilkan tinggi dari pohon P (Tinggi pohon dimulai dari 1)
#                4              --Level 1
#             /     \
#           2         5         --Level 2
#         /
#       1                       --Level 3
# Aplikasi : TinggiPohon(P) --> 3 
# Hint : Hati-hati dengan perbedaan tinggi Left(P) dan Right(P)

# Realisasi
def TinggiPohon(P):
    if IsEmptyLoL(P):
        return 0
    elif IsOneElement(P):
        return 1
    else:
        return Max2(1 + TinggiPohon(left(P)), 1 + TinggiPohon(right(P)))

# Aplikasi
P = [4,
       [2,
          [1,
             [],[]],
          []],
       [5,[],[]]
    ]
print("\nTinggiPohon")
print(TinggiPohon(P))

"""11"""
# DefSpek
# IsBalanceTree : Binary Tree  --> Boolean
# IsBalanceTree(P) mengecek apakah pohon P merupakan balance tree
#                4              
#             /     \
#           2         5         
#         /             \
#       1                 6       
# Aplikasi : IsBalanceTree(P) --> True
# Hint : Balance tree bernilai true ketika selisih tinggi pohon Right dan Left tidak lebih dari 1
#        : ATAU selisih banyaknya node Right dan Left tidak lebih dari 1

# Realisasi
def IsBalanceTree(P):
    if IsEmptyLoL(P):
        return False
    else:
        return mutlak(TinggiPohon(left(P)) - TinggiPohon(right(P)))  <= 1 or mutlak(NbElmt(left(P)) - NbElmt(right(P))) <= 1

# Aplikasi
P = [4,
       [2,
          [1,[],[]],
          []
          ],
       [5,
        [],
        [6,[],[]]]
    ]
print("\nIsBalanceTree")
print(IsBalanceTree(P))


"""12"""
# DefSpek
# Terkiri : Binary Search Tree --> Node dalam integer
# Terkiri(P) menghasilkan node terkiri dari pohon P
#                7              
#             /     \
#           2         8         
#         /   \      /
#       1       3  6
#                  /
#                 5               
# Aplikasi : Terkiri(P) --> 1
# Hint : Node terkiri selalu node paling kecil dari BinarySearchTree

# Realisasi
def Terkiri(P):
    if IsOneElement(P):
        return root(P)
    elif IsUnaryLeft(P):
        return root(left(P))
    elif IsUnaryRight(P):
        return root(P)
    else: #binary
        return Terkiri(left(P))

# Aplikasi
P = [7,
       [2,
         [1,[],[2,[],[]]],
         [3,[],[]]
        ],
       [8,
         [6,
           [5,[],[]],
           []
         ],
         []
        ]
     ]
print("\nTerkiri")
print(Terkiri(P))

"""13"""
# DefSpek
# IsSkewRight : Binary Tree  --> Node atau integer
# IsSkewRight(P) mengecek apakah pohon P condong kanan 
# P1
#                7              
#                  \
#                    8         
#                      \
#                        9
#                         \ 
#                           10     
# Aplikasi : IsSkewRight(P1) --> True
# P2
#                7              
#             /     \
#           2         8         
#         /   \      /
#       1       3  6
#                  /
#                 5    
# Aplikasi : IsSkewRight(P2) --> False

# Realisasi
def IsSkewRight(P):
    if(IsEmptyLoL(P)): # basis-0
        return False
    elif IsOneElement(P): # basis-1
        return True
    elif IsUnaryRight(P): # rekurens
        return IsSkewRight(right(P))
    else: # Ditemukan left child
        return False

# Aplikasi
P1 = [7,
       [],
       [8,
         [],
         [9,
           [],
           [10,
              [],
              []
            ]
          ]
        ]
     ]

P2 = [7,
       [2,
         [1,[],[]],
         [3,[],[]]
        ],
       [8,
         [6,
           [5,[],[]],
           []
         ],
         []
        ]
     ]

print("\nIsSkewRight")
print(IsSkewRight(P1))
print(IsSkewRight(P2))

"""""""SOAL BONUS"""""""
"""Buat latihan aja, nggak usah dikumpulin"""
"""999"""
# DefSpek
# ReversePohon : Binary Tree  --> Tree
# ReversePohon(P) menghasilkan pohon P yang sudah di reverse
# P = [1,
#        [2,
#            [4, 
#                [8, [], []], 
#                [9, [], []]
#            ],
#            [5, [], []]
#       ],
#        [3, 
#            [6, [], []], 
#            [7, [], []]
#        ]
#      ]

#                1              
#             /      \
#           2          3         
#         /   \      /    \
#       4      5   6      7    
#      / \
#     8   9      

# Aplikasi : ReversePohon(P) --> 
# P = [1,
#           [3,
#               [7, [], []],
#               [6, [], []]
#            ],
#           [2, 
#               [5, [], []], 
#                   [4, 
#                        [9, [], []], 
#                        [8, [], []]
#                   ]
#            ]
#       ]    

#                1              
#             /      \
#           3          2         
#         /   \      /    \
#       7      6   5      4    
#                           / \
#                          9   8       

# Realisasi
def ReservePohon(P):
    if IsEmptyLoL(P):#basis 0
        return []
    elif IsOneElement(P): #basis 1
        return [root(P),[],[]]
    elif IsUnaryLeft(P):
        return [root(P),[],ReservePohon(left(P))]
    elif IsUnaryRight(P):
        return [root(P),ReservePohon(right(P)),[]]
    else: #binary
        return [root(P),ReservePohon(right(P)),ReservePohon(left(P))]

# Aplikasi
P = [1,
       [2,
         [4,
           [8,[],[]
           ],
           [9,[],[]
           ]
         ],
         [5,
           [],
           []
         ]
       ],
       [3,
         [6,[],[]
         ],
         [7,[],[]
         ]
       ]
    ]
print("\nReservePohon")
print(P)
print(ReservePohon(P))