# Nama file : waktu_12_ke_detik.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 10 September 2021
# Deskripsi : Mencari jumlah detik dari waktu format 12 jam dimulai dari 00:00:00 am

# Definisi dan Spesifikasi
# waktu_12_ke_detik : integer [0..11], integer [0..59], integer [0..59], string ["am","pm"] -> integer [0..86400]
# waktu_12_ke_detik (j,m,s,k) Mengubah waktu dengan format 12 jam ke detik dengan cara mengecek parameter k
#  apabila berisi 'am' maka hasil konversi waktu ke detik dari fungsi antara tidak akan ditambah waktu
#  tambahan. apabila k berisi selain 'am' dalam konteks ini adalah 'pm' maka hasil detik dari fungsi antara akan ditambah 43200(detik).
#  00.00.01 pm = 43201

# jumlah_detik : integer[0..11], integer [0..59], integer [0..59] -> integer [0..43200]
# jumlah_detik (j,m,s) menghitung jumlah detik dari dimulai dari jam 00:00:00 hingga 11.59.59 pada suatu tanggal.
#  j berarti jam, m berarti menit, s berarti detik. Fungsi ini dibuat agar tidak terjadi pengulangan syntax yang sama.
#  00.00.01 = 1 detik

# Realisasi
def jumlah_detik(j,m,s) :
    return (j * 3600) + (m * 60) + s

# Menggunakan notasi if then else karena hanya ada 2 komplementer
def waktu_12_ke_detik(j,m,s,k) :
    if 0 <= j <= 11 and 0 <= m <= 59 and 0 <= s <= 59 and (k == 'am' or k == 'pm'):
        if k == 'am' :
            return jumlah_detik(j,m,s)
        else:
            return 43200 + jumlah_detik(j,m,s)
    else:
        return 0

    
    

# Aplikasi
print(waktu_12_ke_detik(10,11,45,'am')) #Hasilnya yaitu 36705
print(waktu_12_ke_detik(0,0,1,'pm')) #Hasilnya yaitu 43201
