# Nama file : max_n.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 22 September 2021
# Deskripsi : Menghitung nilai maksimal dari n bilangan

# DESKRIPSI DAN SPESIFIKASI
# max_n : n integer --> integer
#   max_n(v1,v2,..,vn)

# REALISASI
def max_5(v1,v2,v3,v4,v5):
    if v1 > v2 and v1 > v3 and v1 > v4 and v1 >v5:
        return v1
    elif v2 > v3 and v2 > v4 and v2 > v5 and v2 > v1:
        return v2
    elif v3 > v4 and v3 > v5 and v3 > v1 and v3 > v2:
        return v3
    elif v4 > v5 and v4 > v1 and v4 > v2 and v4 > v3:
        return v4
    elif v5 > v1 and v5 > v2 and v5 > v3 and v5 > v4:
        return v5


# APLIKASI
print(max_5(100,4,5000,33,5)) # 5
    













    
