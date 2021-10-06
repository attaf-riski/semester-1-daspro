# Nama file : second_to_date.py
# Nama Pembuat file : Attaf Riski Putra Ramadhan
# Tanggal Pembuatan : 5 Oktober 2021
# Deskripsi : Mengimplementasikan fungsi utama dari type bentukan detik ke jam

# DESKRIPSI DAN SPESIFIKASI
# SecondToDate: integer --> <d,h,m,s>
#   {SecondToDate(s) Mengubah s berupa detik menjadi <d,h,m,s>}
# REALISASI (dalam python)
def second_to_date(s):
    return [s//86400,(s%86400) // 3600,((s%86400)%3600) // 60,((s%86400)%3600)%60]


# APLIKASI
print(second_to_date(270183))
