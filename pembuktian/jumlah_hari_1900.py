# Nama file : jumlah_hari_1900.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 21 September 2021
# Deskripsi : menghitung hari absolut dari 1 januari 1900 sampai tanggal yang dimasukan dengan memperhitungkan kabisat

# DESKRIPSI DAN SPESIFIKASI
# is_kabisat : integer[0..99] -> boolean
#   is_kabisat(a) bernilai benar bila 1900+a / 4 = 0 dan 1900+a / 100 != 0. Atau 1900+a habis dibagi 400

# jumlah_tahun_kabisat : integer[0..99] -> integer[0..24]
#   jumlah_tahun_kabisat(y) mencari jumlah tahun kabisat dibawah tahun ybs.
#       Jumlah tahun kabisat dibawah tahun ybs = total hari tambahan setiap tahun kabisat. Karena setiap tahun kabisat hanya menambah 1 hari.
#       Ex : y = 5(1905), tahun kabisat dibawah 1905 adalah 1904 sehingga = 1 hari * 1. sehingga cukup ditulis 1(jumlah tahun kabisat).
#       Mencari jumlah tahun kabisat dibawah tahun ybs adalah:
#       (y - 1) % 4 = 3 -> untuk mencari tahun kabisat terdekat dibawah tahun ybs
#       (y - 1)- 3 = k(kabisat) / suku ke n di deret aritmatika tahun kabisat 1900 -- 1999
#       -> ditemukan tahun kabisat terdekat dengan dikurangi hasil modulo, hal ini berdasarkan pattern recognition dari tahun kabisat dari tahun 1900 - 1999 yang memiliki beda selalu 4 tahun
#       Deret tahun kabisat 1900 - 1999 bisa dibentuk dengan rumus mencari suku ke-n deret aritmatika
#       (1904,1908,1912,1916,...,1988,1992,1996)
#       Suku ke n = 4 + (n - 1)4 dengan persamaan ini lalu masukan k / suku yang sudah ditemukan
#       k = 4 + (n - 1)4 untuk mencari nilai n maka rumus dibentuk hingga menjadi
#       n = ((k - 4) / 4) + 1, n disini adalah urutan dimulai dari 1 atau bisa juga bisa diartikan sebagai total tahun kabisat
#       Sehingga n = total hari tambahan setiap tahun kabisat.        

# dpy : integer[0..99] -> integer[1..36524]
#   dpy(y) menghitung total hari dengan cara total tahun * 365 + jumlah_tahun_kabisat(y).
#       (y - 1 + 1) -> -1 karena tahun sekarang tidak ikut dihitung, +1 karena dimulai dari 1900 maka cukup menjadi y.
#       tahun ybs tidak diikutkan karena terdapat cara yang berbeda dalam menghitung hari di tahun ybs.

# dpm : integer[1..12] -> integer[1..366]
#   dpm(b) adalah jumlah hari pada tahun ybs pada tanggal 1 bulan B. Terhitung mulai satu januari: kumulatif jumlah hari dari tanggal 1 Januari s/d tanggal 1 bulan B, tanpa
#       memperhitungkan tahun kabisat

# hari_ke_1900 : integer[1..31], integer[1..12], integer[0..99] -> integer[1..36524]
#   hari_ke_1900(d,m,y) dari suatu tanggal <d,m,y> adalah hari 'absolut' dihitung mulai 1
#       Januari 1900. 1 Januari tahun 1900 adalah hari ke 1

# REALISASI{dengan memperhitungkan tahun kabisat}
def is_kabisat(a):
    if (1900+a) % 4 == 0 :
        if (1900+a) % 100 == 0 :
            if (1900+a) % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def jumlah_tahun_kabisat(y) :
    if (y - 1) >= 4:
       return ( ( ( y - 1 ) - ( ( y - 1 ) % 4 ) - 4 ) // 4) + 1
    else:
        # karena tahun dibawah 4(1904) maka tidak ada tahun kabisat
       return 0
       

def dpy(y) :
    return (y * 365) + jumlah_tahun_kabisat(y)  

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
   return dpy(y) + (dpm(m) + d if (m > 2 and is_kabisat(y)) else dpm(m) + d - 1)
          

# APLIKASI
print(hari_ke_1900(1,1,0)) # Hasilnya 1
print(hari_ke_1900(31,12,99)) # Hasilnya 36524
print(hari_ke_1900(5,6,92)) # Hasilnya 33759
print(hari_ke_1900(17,8,45) # Hasilnya 16665
    













    
