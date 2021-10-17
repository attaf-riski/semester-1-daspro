#1. harus pahami soalnya
#2. implementasi dulu di text editor lalu terjemahkan ke notasi fungsional
#3. yang bikin lama mikir algorithm-nya
#4. fungsi yang diberikan dalam diktat tidak kita definisikan sendiri
#5. pikirkan input dan output
#6. tidak tulis ulang notasi fungsional yang ada di diktat(fungsi bawaan ditulis)

# Nama
import string
# DEFINISI DAN SPESIFIKASI
# pc : integer, integer, integer --> real
#  {pc(bil)}

# REALISASI
#def campuran(bil,n,d):
#    if bil >= 0:
#        return (bil*d +n)/d
#    else:
#        return (bil*d -n)/d

# APLIKASI

# ===
# NikToDate: string -> string


def StrToInt(string):
    return int(string)

def Year():
    return 2021

def IntToStr(integer):
    return str(integer)

def SubStr(x,a,b):
    return x[a-1:b] # ???

def int_to_month(mm):
    if (mm == 1):
        return "Januari"
    elif (mm == 2):
        return "Februari"
    elif (mm == 3):
        return "Maret"
    elif (mm == 4):
        return "April"
    elif (mm == 5):
        return "Mei"
    elif (mm == 6):
        return "Juni"
    elif (mm == 7):
        return "Juli"
    elif (mm == 8):
        return "Agustus"
    elif (mm == 9):
        return "September"
    elif (mm == 10):
        return "Oktober"
    elif (mm == 11):
        return "November"
    elif (mm == 12):
        return "Desember"

#def tangal(x):
#     if StrToInt(SubStr(x,7,8)) > 40: # perempuan
#        return (StrToInt(SubStr(x,7,8)) - 40) + ' ' + int_to_month(StrToInt(SubStr(x,7,8)))
#    else:
#        return  0
#
#def nik_to_date(x):
#   return 0


# algorithm for number 3
#a. def&spek tipe => type square: <top: point, bottom: point> 
#b. def&spek selektor => def top,def bottom
#c. def&spek konstruktor => MakeSquare(top,bottom)
#d. def&spek operator => 
#d1. GetPanjang(S) => absis(top(S)) - absis(bottom(S))
#d2. GetLebar(S) => ordinat(top(S)) - ordinat(bottom(S))
#d3. GetLuas(S) => GetPanjang * GetLebar


