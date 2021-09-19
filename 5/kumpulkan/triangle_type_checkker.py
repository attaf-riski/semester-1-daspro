# Nama file : triangle_type_checkker.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 19 September 2021
# Deskripsi : Mengecek jenis sebuah segitiga berdasarkan input ketiga segitiga tersebut



# DESKRIPSI DAN SPESIFIKASI
# triangle_type_checkker : 3 integer > 0 --> string["segitiga sama sisi","segitiga sama sisi","segitiga sembarang","wrong input"]
# triangle_type_checkker(a,b,c) Menentukan sebuah jenis segitiga berdasarkan input ke-3 sisi segitiga tersebut. Input berupa integer dan harus lebih besar dari 0.


# REALISASI
def triangle_type_checkker(a,b,c):
    if a > 0 and b > 0 and c > 0:
        if a == b and b == c and c == a:
            return "segitiga sama sisi"
        else:
            if a == b or b == c or c == a:
                return "segitiga sama kaki"
            else:
                return "segitiga sembarang"
    else:
        print("Mohon masukkan sisi segitiga lebih besar dari 0")
        return "wrong input"

# APLIKASI
print(triangle_type_checkker(1,1,1)) #Hasilnya segitiga sama sisi
print(triangle_type_checkker(2,2,3)) #Hasilnya segitiga sama kaki
print(triangle_type_checkker(4,5,6)) #Hasilnya segitiga sembarang








    













    
