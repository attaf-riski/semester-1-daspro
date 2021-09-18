# Nama file : mean_olympique.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 4 September 2021
# Deskripsi : Menerima 4 bilangan bulat positif, menghasilkan harga rata-rata dari dua di antara empat buah bilangan tersebut,
#               dengan mengabaikan nilai terbesar dan nilai terkecil.

# Definisi dan spesifikasi
# MO : 4 integer > 0 --> real
#   MO(u,v,w,x) menghitung rata-rata dari dua buah bilangan integer, yang bukan maksimum dan bukan minimum dari 4 buah integer: (u+v+w+x-min_4(u,v,w,x)-max_4()) / 2

# max_4 : 4 integer > 0 --> integer
#   max_4(i,j,k,l) menentukan maksimum dari 4 buah bilangan integer

# min_4 : 4 integer > 0 --> integer
#   min_4(i,j,k,l) menentukan minimum dari 4 buah bilangan integer

# max_2 : 2 integer > 0 --> integer
#   max_2(a,b) menentukan maksimum dari 2 bilangan integer, hanya dengan ekspresi aritmatika: jumlah dari kedua bilangan ditambah dengan selisih kedua bilangan, hasilnya dibagi(div) 2

# min_2 : 2 integer > 0 --> integer
#   min_2(a,b) menentukan minimum dari 2 bilangan integer, hanya dengan ekspresi aritmatika: jumlah dari kedua bilangan - selisih kedua bilangan, hasilnya dibagi(div) 2

# Realisasi
def max_2(a,b) :
    return (a+b+abs(a-b)) // 2

def min_2(a,b) :
    return (a+b-abs(a-b)) // 2

def max_4(i,j,k,l) :
    return max_2(max_2(i,j),max_2(k,l))

def min_4(i,j,k,l) :
    return min_2(min_2(i,j),min_2(k,l))

def MO(u,v,w,x) :
    return (u+v+w+x - min_4(u,v,w,x) - max_4(u,v,w,x)) / 2

# Aplikasi
print(MO(8,12,10,20)) # hasilnya 11.0
print(MO(1,2,3,4)) #hasil harus 2.5
