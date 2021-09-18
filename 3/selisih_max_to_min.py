# Nama file : selisih_max_to_min.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 9 September 2021
# Deskripsi : Menghitung nilai selisih dari nilai terbesar dan terkecil

# Definisi dan Spesifikasi
# selisih_max_to_min : 3 integer -> boolean
# selisih_max_to_min(j,k,l) akan menghasilkan nilai selisih dari
#  nilai terbesar dan nilai terkecil dari j,k, dan l.

# max_2 : 2 integer -> integer
# max_2(a,b) menghasilkan nilai terbesar dari a dan b

# max_3 : 3 integer -> integer
# max_3(a,b,c) menghasilkan nilai terbesar dari a,b, dan c

# min_2 : 2 integer -> integer
# min_2(a,b) menghasilkan nilai terbesar dari a dan b

# min_3 : 3 integer -> integer
# min_3(a,b,c) menghasilkan nilai terkecil dari a,b, dan c

# Realisasi
def max_2(a,b) :
    if a >= b : 
        return a
    else :
        return b
    
def max_3(a,b,c) :
    return max_2(a,max_2(b,c))

def min_2(a,b) :
    if a <= b :
        return a
    else :
        return b

def min_3(a,b,c) :
    return min_2(a,min_2(b,c))

def selisih_max_to_min(j,k,l) :
    return max_3(j,k,l) - min_3(j,k,l)


# Realisasi
print(selisih_max_to_min(2,6,10)) # Hasilnya adalah 8
print(selisih_max_to_min(100,49,50)) # Hasilnya adalah 51
