# بسم الله الرحمن الرحيم
# Nama file : date.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 27 September 2021
# Deskripsi : Membuat tipe data bentukan date yang terdiri dari hari, bulan, dan tahun dan membentuk komposisi <Hr,Bln,Thn>.

from dpm import dpm #kebutuhan Harike1900()
import date_calculation_algorithms #kebutuhan NextNDays
import datetime #kebutuhan mencari tanggal hari ini

# DEFINISI TYPE 

# type Hr: integer[1..31]
#   {Definisi ini hanyalah untuk "menamakan" type integer dengan nilai tertentu supaya mewakili hari, sehingga jika dipunyai suatu nilai integer, kita dapat memeriksa apakah
#    nilai integer tersebut mewakili Hari yang absah}

# type Bln: integer[1..12]
#   {Definisi ini hanyalah untuk "menamakan" type integer dengan daerah nilai tertentu supaya mewakili Bulan}

# type Thn: integer>0
#   {Definisi ini hanyalah untuk "menamakan" type integer dengan daerah nilai tertentu supaya mewakili tahun}

# type date<d:Hr,m:Bln,y:Thn>
#   {<d,m,y> adalah tanggal d bulan m tahun y}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR

# MakeDate : <Hr,Bln,Thn> --> date
#   {MakeDate(d,m,y) adalah tanggal pada hari,bulan,tahun yang bersangkutan}
# REALISASI (dalam python)
class Date:
    def __init__(self,d,m,y):
        self.d = d
        self.m = m
        self.y = y

# DEFINISI DAN SPESIFIKASI SELEKTOR

# Day: date --> Hr
#   {Day(D) memberikan hari d dari D yang terdiri dari <d,m,y>}
# REALISASI (dalam python)
def day(D):
    return D.d

# Month: date --> Bln
#   {Month(D) memberikan bulan m dari D yang terdiri dari <d,m,y>}
# REALISASI (dalam python)
def month(D):
    return D.m

# Year: date --> Thn
#   {Year(D) memberikan tahun y dari D yang terdiri dari <d,m,y>}
# REALISASI (dalam python)
def year(D):
    return D.y

# DEFINISI DAN FUNGSI PREDIKAT
# {Operator Relasional date}

# IsEqD?: 2 date --> boolean
#   {IsEqD?(D1,D2) benar jika d1=d2, mengirimkan true jika d1=d2 and m1=m2 and y1=y2.
#    Contoh: IsEqD?(<1,1,1980>,<1,1,1980>) adalah True
#            IsEqD?(<1,1,1980>,<1,2,1980>) adalah False}
# REALISASI(dalam python)
def is_eq_d(D1,D2):
    return (day(D1) == day(D2) ) and (month(D1) == month(D2)) and (year(D1) == year(D2) ) 

# IsBefore?: 2 date --> boolean
#   {IsBefore?(D1,D2) benar jika D1 adalah sebelum D2, Mengirimkan true jika D1 adalah
#    "sebelum" D2:
#    Contoh:    IsBefore?(<1,1,1980>,<1,1,1981>) adalah False}
#               IsBefore?(<1,7,1990>,<2,5,1995>) adalah True}
# REALISASI(dalam python)
def is_before(D1,D2):
    if not is_eq_d(D1,D2):
        if year(D1) < year(D2):
            return True
        elif year(D1) == year(D2):
            if month(D1) < month(D2):
                return True
            elif month(D2) == month(D2):
                if day(D1) < day(D2):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

# IsAfter?: 2 date --> boolean
#   {IsAfter?(D1,D2) benar jika D1 adalah sesudah D2, mengirimkan true jika D1 adalah
#    "sesudah" D2:
#    Contoh:    IsAfter?(<1,1,2000>,<6,12,1999>) adalah True}
#               IsAfter?(<1,7,1990>,<2,5,1995>) adalah False}
# REALISASI(dalam python)
def is_after(D1,D2):
    if not is_eq_d(D1,D2) and not is_before(D1,D2):
        return True
    else:
        return False

# IsKabisat?: integer --> integer
#   {IsKabisat?(a) true jika a adalah tahun kabisat: habis bagi 4 tetapi tidak habis dibagi 100, atau habis dibagi 400}
# REALISASI(dalam python)
def is_kabisat(a):
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        return True
    else:
        return False
        


# DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI LAIN TERHADAP DATE
# {Operator aritmatika date}

# NextDay: date -> date
#   {NextDay(D): menghitung date yang merupakan keesokan hari dari date D yang diberikan:
#    Contoh:
#           NextDay(<1,1,2010>) adalah <2,1,2010>
#           NextDay(<31,12,2020>) adalah <1,1,2021>
#           NextDay(<28,2,80>) adalah <29,2,80>
#           NextDay(<28,2,81>) adalah <1,3,82>}
# REALISASI(dalam python)
def next_day(D):
    if month(D) == 1 or month(D) == 3 or month(D) == 5 or month(D) == 7 or month(D) == 8 or month(D) == 10:
        if day(D)<31:
            return Date(day(D)+1,month(D),year(D))
        else:
            return Date(1,month(D)+1,year(D))
    elif month(D) == 2:
        if day(D)<28:
            return Date(day(D1)+1,month(D),year(D))
        elif is_kabisat(year(D)):
            if day(D) == 28:
                return Date(day(D)+1,month(D),year(D))
            else:
                return Date(1,month(D)+1,year(D))
        else:
            return Date(1,month(D)+1,year(D))
    elif month(D) == 4 or month(D) == 6 or month(D) == 9 or month(D) == 11:
        if day(D)<30:
            return Date(day(D)+1,month(D),year(D))
        else:
            return Date(1,month(D)+1,year(D))
    elif month(D) == 12:
        if day(D)<31:
            return Date(day(D)+1,12,year(D))
        else:
            return Date(1,1,year(D)+1)

# Yesterday: date --> date
#   { Yesterday(D): Menghitung date yang merupakan 1 hari sebelum date D yang
#     diberikan:
#               Yesterday(<1,1,1980>) adalah <31,12,1979>
#               Yesterday(<14,2,2021>) adalah <13,2,2021>
#               Yesterday(<1,3,1996>) adalah <29,2,1996>}
# REALISASI(dalam python)
def yesterday(D):
    if month(D) == 1:
        if day(D) > 1:
            return Date(day(D)-1,1,year(D))
        else:
            return Date(31,12,year(D)-1)
    elif month(D) == 3:
        if day(D) > 1:
            return Date(day(D) - 1,month(D),year(D))
        else:
             if is_kabisat(year(D)):
                 return Date(29,month(D)-1,year(D))
             else:
                 return Date(28,month(D)-1,year(D))           
    elif month(D) == 2 or month(D) == 4 or month(D) == 6 or month(D) == 8 or month(D) == 9 or month(D) == 11:
        if day(D) > 1:
            return Date(day(D)-1,month(D),year(D))
        else:
            return Date(31,month(D)-1,year(D))
    elif month(D) == 5 or month(D) == 7 or month(D) == 10 or month(D) == 12:
        if day(D) > 1:
            return Date(day(D)-1,month(D),year(D))
        else:
            return Date(30,month(D)-1,year(D))

# NextNDay:date,integer --> date
#   {NextNDay(D,N): Menghitung date yang merupakanN hari(N adalah nilai integer) sesudah dari date D yang diberikan
#    hari mulai tidak dihitung tetapi hari terakhir dihitung.
#                   NextNDay(<1,10,2021>,10) adalah <11,10,2021>}
# REALISASI(dalam python)
def next_n_day(D,N):
    return Date(date_calculation_algorithms.days_to_date(date_calculation_algorithms.date_to_days(day(D),month(D),year(D)) + N)[0],date_calculation_algorithms.days_to_date(date_calculation_algorithms.date_to_days(day(D),month(D),year(D)) + N)[1],date_calculation_algorithms.days_to_date(date_calculation_algorithms.date_to_days(day(D),month(D),year(D)) + N)[2])


# HariKe1900:date --> integer[0..366]
#   {HariKe1900(D): Menghitung jumlah hari terhadap 1 Januari pada tahun y, dengan
#    memperhitungkan apakah y adalah tahun kabisat:
#       HariKe1900(<1,1,2010>) adalah 1
#       HariKe1900(<31,12,2000>) adalah 366
#       HariKe1900(<31,12,1999>) adalah 365}
# REALISASI(dalam python)
def hari_ke_1900(D):
    if is_kabisat(year(D)) and month(D) > 2:
        return dpm(month(D)) + day(D)
    else:
        return dpm(month(D)) + day(D) - 1
        
# APLIKASI
print("\n=====SELAMAT DATANG DI PROGRAM TIPE BENTUKAN Date=====\n")
D1 = Date(17,8,1945)
D2 = Date(27,11,2002)
print("Tanggal D1 terbentuk dengan: {}.{}.{}".format(day(D1),month(D1),year(D1)))
print("Tanggal D2 terbentuk dengan: {}.{}.{}".format(day(D2),month(D2),year(D2)))

print("\n===SESI FUNGSI PREDIKAT===\n")
print("Apakah D1 dan D2 itu sama tanggal-nya? {}".format(is_eq_d(D1,D2)))
print("Apakah D1 itu sebelum D2? {}".format(is_before(D1,D2)))
print("Apakah D2 itu setelah D2? {}".format(is_after(D1,D2)))
print("Apakah D1 itu tahun kabisat? {}".format(is_kabisat(year(D1))))
print("Apakah D2 itu tahun kabisat? {}".format(is_kabisat(year(D2))))
print("Apakah tahun {} itu tahun kabisat? {}".format(datetime.datetime.now().year,is_kabisat(datetime.datetime.now().year)))
print("\n===SESI FUNGSI OPERATOR===\n")
print("Mari kita ingat kembali tanggal D1 terbentuk dengan: {}.{}.{}".format(day(D1),month(D1),year(D1)))
print("Mari kita ingat kembali tanggal D2 terbentuk dengan: {}.{}.{}\n".format(day(D2),month(D2),year(D2)))
print("Tanggal pada 1 hari setelah tanggal D1 adalah {}.{}.{}".format(day(next_day(D1)),month(next_day(D1)),year(next_day(D1))))
print("Tanggal pada 1 hari sebelum tanggal D2 adalah {}.{}.{}".format(day(yesterday(D2)),month(yesterday(D2)),year(yesterday(D2))))
print("Tangal {0}.{1}.{2} adalah {3} hari setelah tanggal 1 Januari {2}.".format(day(D1),month(D1),year(D1),hari_ke_1900(D1)))
D4 = Date(datetime.datetime.now().day,datetime.datetime.now().month,datetime.datetime.now().year)
D3 = next_n_day(D2,100)
print("{6} hari dari tanggal {0}.{1}.{2} adalah tanggal? {3}.{4}.{5}".format(day(D2),month(D2),year(D2),day(D3),month(D3),year(D3),100))
print("{3} hari dari {0}.{1}.{2} adalah {4}.{5}.{6}".format(day(D1),month(D1),year(D1), date_calculation_algorithms.date_to_days(day(D4),month(D4),year(D4)) - date_calculation_algorithms.date_to_days(day(D1),month(D1),year(D1)),day(D4),month(D4),year(D4)))

print("\n===Spesial Stuff===\n")
D1 = Date(11,10,2021)
print("Countdown day-1 UTS Semester Ganjil 2020/2021 Informatika-2021: {} Hari Lagi!".format(date_calculation_algorithms.date_to_days(day(D1),month(D1),year(D1)) - date_calculation_algorithms.date_to_days(day(D4),month(D4),year(D4))))

                   
print("\n=====PROGRAM BERAKHIR,TERIMAKASIH=====")









