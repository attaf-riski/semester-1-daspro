# Nama file : form_checkker.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 19 September 2021
# Deskripsi : Mengecek wujud air pada tekanan 1 atm berdasarkan temperatur air dalam derajat celcius



# DESKRIPSI DAN SPESIFIKASI
# form_checkker : real --> string["es","cair","uap"]
# form_checkker(t) akan menyatakan wujud air berdasarkan t : temperature air dalam derajat celcius. Keluaran dari fungsi ini adalah
#   antara es, cair, atau uap. Tekanan akan disetel pada 1 atm atau suhu tepat diatas permukaan laut.

# REALISASI
def form_checkker(t) :
    if t < 0.0:
        return "es"
    elif t >= 0.0 and t <= 100.0:
        return "cair"
    else:
        #t > 100.0
        return "uap"

# APLIKASI
print(form_checkker(-50.9)) # Hasilnya adalah es
print(form_checkker(30.5)) # Hasilnya adalah cair
print(form_checkker(240.0)) # Hasilnya adalah uap







    













    
