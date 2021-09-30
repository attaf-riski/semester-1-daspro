# Nama file : dpm.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 27 September 2021
# Deskripsi : Menyediakanan kebutuhan file date.py akan dpm(), dpm menghasilkan jumlah hari pada tahun ybs pda tanggal 1 bulan ybs.


# DESKRIPSI DAN SPESIFIKASI
# dpm : integer[1..12] -> integer[1..366]
# dpm(b) adalah jumlah hari pada tahun ybs pada tanggal 1 bulan B. Terhitung mulai satu januari: kumulatif jumlah hari dari tanggal 1 Januari s/d tanggal 1 bulan B, tanpa
#   memperhitungkan tahun kabisat


# REALISASI
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








    













    
