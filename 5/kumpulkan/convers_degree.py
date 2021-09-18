# Nama file : convers_degree.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 18 September 2021
# Deskripsi : Mengubah nilai derajat celcius ke nilai derajat Reamur, Fahrenheit, atau Kelvin sesuai masukan


# DESKRIPSI DAN SPESIFIKASI
# convers_degree : real, character['F','K','R'] --> real
#    convers_degree(n,j) menerima nilai derajat celcius yang diwakilkan oleh parameter n dan akan di konversi ke bentuk derajat lain berdasarkan
#       masukan yang diwakilkan oleh j. j hanya boleh diisi F:Fahrenheit, K:Kelvin, R:Reamur.
#       <10.0,'K'> --> 283.0
#       <40.0,'F'> --> 104.0
#       <100.0,'R'> --> 80.0

# REALISASI
def convers_degree(n,j):
    if j == 'K':
        return n + 273.0
    elif j == 'F':
        return ((9/5) * n) + 32.0
    elif j == 'R':
        return (4/5) * n
    else:
        print("Mohon masukan kode derajat F,K,atau R. Inputan anda : "+j)

# APLIKASI
print(convers_degree(10.0,'K')) # Hasilnya adalah 283.0
print(convers_degree(40.0,'F')) # Hasilnya adalah 104.0
print(convers_degree(100.0,'R')) # Hasilnya adalah 80.0
print(convers_degree(47.5,'F')) # Hasilnya adalah 117.5






    













    
