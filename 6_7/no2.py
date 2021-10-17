# Nama File : no2.py
# Nama Pembuat File : Attaf Riski Putra Ramadhan
# Tanggal Pembuatan : 8 Oktober 2021
# Deskripsi : Menghasilkan tanggal lahir dengan format "dd mm yyyy" dari NIK. Contoh : 3322082711020001 --> 27 November 2002

from datetime import datetime 

# DEFINISI DAN SPESIFIKASI
# StrToInt: string --> integer
#   {StrToInt(str) mengkonversi string str menjadi nilai integer yang bersesuaian.
#     Ex: StrToInt('01') adalah 1 }

# IntToStr: integer --> string
#   {IntToStr(x) mengkonversi integer x menjadi nilai string yang bersesuaian.
#    Ex: IntToStr(12) adalah '12'}

# Year: integer --> integer
#   {Year(yy) menghasilkan tahun saat ini yang terdiri dari 4 digit.
#    Ex: Year() adalah 2021}

# SubStr: string, integer > 0, integer > 0 --> string
#   {SubStr(str,a,b) mengambil karakter dari string str mulai dari posisi a hingga posisi b,
#    Ex: SubStr('siapa',1,4) adalah 'siap' }

# TanggalHari: integer[1..71] --> string
#   {TanggalHari(dd) Menghasilkan tanggal hari dengan pengecekan:
#    jika dd > 40 maka dd - 40,
#    jika dd < 40 maka dd.
#    Ex: TanggalHari(12) --> '12',
#        TanggalHari(52) --> '12'}

# NamaBulan: string --> string
#   {NamaBulan(mm) Menghasilkan nama suatu bulan secara lengkap berdasarkan mm.
#    Ex: NamaBulan('12') adalah 'Desember'}

# TahunBerapa: integer --> string
#   {TahunBerapa(yy) menghasilkan tahun saat ini yang terdiri dari 4 digit. Bila 2000 + yy > tahun ini
#    Ex: Sekarang tahun 2002, Year(50) artinya 2050, 2002 < 2050 sehingga hasilnya adalah 1950 }

# NIKToBirth: string --> string
#   {NIKToBirth(NIK) menghasilkan string "dd mmmm yyyy" dari NIK. Jika jenis kelamin wanita, maka tanggal lahir(dd) ditambah 40.
#    Jika angka tahun(yy) ditambah 2000 melebihi tahun saat ini, maka tahun lahir diawali dengan '19', sebaliknya tahun diawali dengan '20'
#    Ex: NIKToBirth('5722772711020010') adalah '27 November 2002',
#        NIKToBirth('5722776003820010') adalah '20 April 1982'}
  
# REALISASI

def str_to_int(str):
    return int(str)

def int_to_str(x):
    return str(x)

def year():
    return datetime.now().year

def sub_str(str,a,b):
    return str[a-1:b]

def tanggal_hari(dd):
    if dd > 40:
        return int_to_str(dd - 40)
    else: # dd <= 40
        return int_to_str(dd)

def nama_bulan(mm):
    if mm == "01":
        return "Januari"
    elif mm == "02":
        return "Februari"
    elif mm == "03":
        return "Maret"
    elif mm == "04":
        return "April"
    elif mm == "05":
        return "Mei"
    elif mm == "06":
        return "Juni"
    elif mm == "07":
        return "Juli"
    elif mm == "08":
        return "Agustus"
    elif mm == "09":
        return "September"
    elif mm == "10":
        return "Oktober"
    elif mm == "11":
        return "November"
    elif mm == "12":
        return "Desember"
    else: # mm > 12 atau mm < 1
        return "Out-Of-Range"

def tahun_berapa(yy):
    if yy + 2000 > year():
        return int_to_str(1900 + yy)
    elif yy + 2000 <= year():
        return int_to_str(2000 + yy)

def nik_to_birth(NIK):
    return tanggal_hari(str_to_int(sub_str(NIK,7,8))) + " " + nama_bulan(sub_str(NIK,9,10)) + " " + tahun_berapa(str_to_int(sub_str(NIK,11,12)))


# APLIKASI
print("\n===WELCOME TO NIK CONVERS TO DATE OF BIRTH===")
print(nik_to_birth("5722772711020010"))
print(nik_to_birth("5722775312010010"))
print(nik_to_birth("5722776003820010"))
print(nik_to_birth("5722771708450010"))
print("\n===THANKS===\n")

