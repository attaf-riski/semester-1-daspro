# Nama file : penanggalan_v2.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 17 September 2021
# Deskripsi : Tanggal, bulan tahun pada perioda tahun 1900 s/d 1999 dapat dituliskan dalam "tuple" dari tiga buah bilangan integer<d,m,y> sebagai berikut:
#               <3,4,93>: hari ke 3, pada bulan ke 4(April), pada tahun 1993. Program ini menghitung hari ke... pada suatu tahun 1900+y mula-mula tanpa memperhitungkan adanya
#               tahun kabisat. <1, 1, 82> -> 1


# DESKRIPSI DAN SPESIFIKASI
# is_kabisat : integer[0..99] -> boolean
# is_kabisat(a) bernilai benar jika tahun 1900+a adalah tahun kabisat: habis dibagi 4 tetapi tidak
# habis dibagi 100, atau habis dibagi 400

# dpm : integer[1..12] -> integer[1..366]
# dpm(b) adalah jumlah hari pada tahun ybs pada tanggal 1 bulan B. Terhitung mulai satu januari: kumulatif jumlah hari dari tanggal 1 Januari s/d tanggal 1 bulan B, tanpa
#   memperhitungkan tahun kabisat

# hari_ke_1900 : integer[1..31], integer[1..12], integer[0..99] -> integer[1..366]
# hari_ke_1900(d,m,y) dari suatu tanggal <d,m,y> adalah hari 'absolut' dihitung mulai 1
# Januari 1900+y. 1 Januari tahun 1900+y adalah hari ke 1

# REALISASI{dengan memperhitungkan tahun kabisat}
def is_kabisat(a):
    return (((a+1900) % 4 == 0) and ((a+1900) % 100 != 0)) or ((a+1900) // 400 == 0)
def dpm(b) : # analis kasus terhadap B
    if b == 1:
        return 1
    elif b == 2:
        return 32
    elif b == 3:
        return 60
    elif b == 4:
        return 91
    elif b == 5:
        return 121
    elif b == 6:
        return 152
    elif b == 7:
        return 182
    elif b == 8:
        return 213
    elif b == 9:
        return 244
    elif b == 10:
        return 274
    elif b == 11:
        return 305
    else:
        # b == 12
        return 335

def hari_ke_1900(d,m,y):
# if condition true return days with kabisat format else return normal days without kabisat
   return dpm(m) + d if (m > 2 and is_kabisat(y)) else dpm(m) + d - 1
        
    

# APLIKASI
print(hari_ke_1900(1,4,92)) # Hasilnya 92
print(hari_ke_1900(31,12,97)) # Hasilnya 365 karena bukan tahun kabisat
print(hari_ke_1900(31,12,92)) # Hasilnya 366 karena tahun kabisat
print(hari_ke_1900(1,4,91)) # Hasilnya 91






    













    
