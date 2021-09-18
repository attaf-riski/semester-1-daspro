# Nama file : waktu_24_ke_detik.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 10 September 2021
# Deskripsi : Mencari jumlah detik dari waktu format 24 jam dimulai dari 00:00:00

# Definisi dan Spesifikasi
# waktu_24_ke_detik : integer [0..23], integer [0..59], integer [0..59] -> integer[0..86400]
# waktu_24_ke_detik (j,m,s) menghitung jumlah detik dari format waktu 24 jam dimulai dari
#  jam 00:00:00 pada suatu tanggal. j berarti jam, m berarti menit, s berarti detik.
#  00.00.01 = 1 detik.

# Realisasi
def waktu_24_ke_detik (j,m,s) :
    if 0 <= j <= 11 and 0 <= m <= 59 and 0 <= s <= 59 :
        return (j * 3600) + (m * 60) + s
    else:
        return 0
    

# Aplikasi
print(waktu_24_ke_detik(12,50,59)) # Hasilnya yaitu 46259
print(waktu_24_ke_detik(00,00,1)) # Hasilnya yaitu 1
