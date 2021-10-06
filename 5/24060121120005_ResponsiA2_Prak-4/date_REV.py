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
def make_date(d,m,y):
    return [d,m,y]


#BEFORE
#class Date:
#    def __init__(self,d,m,y):
#        self.d = d
#        self.m = m
#        self.y = y

# DEFINISI DAN SPESIFIKASI SELEKTOR

# Day: date --> Hr
#   {Day(D) memberikan hari d dari D yang terdiri dari <d,m,y>}
# REALISASI (dalam python)
def day(D):
    return D[0]

# Month: date --> Bln
#   {Month(D) memberikan bulan m dari D yang terdiri dari <d,m,y>}
# REALISASI (dalam python)
def month(D):
    return D[1]

# Year: date --> Thn
#   {Year(D) memberikan tahun y dari D yang terdiri dari <d,m,y>}
# REALISASI (dalam python)
def year(D):
    return D[2]

# DEFINISI DAN FUNGSI PREDIKAT
# {Operator Relasional date}

# IsEqD?: 2 date --> boolean
#   {IsEqD?(make_date(17,8,1945),make_date(27,11,2002)) benar jika make_date(17,8,1945)=make_date(27,11,2002), mengirimkan true jika make_date(17,8,1945)=make_date(27,11,2002) and m1=m2 and y1=y2.
#    Contoh: IsEqD?(<1,1,1980>,<1,1,1980>) adalah True
#            IsEqD?(<1,1,1980>,<1,2,1980>) adalah False}
# REALISASI(dalam python)
def is_eq_d(D1,D2):
    return (day(D1) == day(D2) ) and (month(D1) == month(D2)) and (year(D1) == year(D2) ) 

# IsBefore?: 2 date --> boolean
#   {IsBefore?(make_date(17,8,1945),make_date(27,11,2002)) benar jika make_date(17,8,1945) adalah sebelum make_date(27,11,2002), Mengirimkan true jika make_date(17,8,1945) adalah
#    "sebelum" make_date(27,11,2002):
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
#   {IsAfter?(make_date(17,8,1945),make_date(27,11,2002)) benar jika make_date(17,8,1945) adalah sesudah make_date(27,11,2002), mengirimkan true jika make_date(17,8,1945) adalah
#    "sesudah" make_date(27,11,2002):
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
            return make_date(day(D)+1,month(D),year(D))
        else:
            return make_date(1,month(D)+1,year(D))
    elif month(D) == 2:
        if day(D)<28:
            return make_date(day(make_date(17,8,1945))+1,month(D),year(D))
        elif is_kabisat(year(D)):
            if day(D) == 28:
                return make_date(day(D)+1,month(D),year(D))
            else:
                return make_date(1,month(D)+1,year(D))
        else:
            return make_date(1,month(D)+1,year(D))
    elif month(D) == 4 or month(D) == 6 or month(D) == 9 or month(D) == 11:
        if day(D)<30:
            return make_date(day(D)+1,month(D),year(D))
        else:
            return make_date(1,month(D)+1,year(D))
    elif month(D) == 12:
        if day(D)<31:
            return make_date(day(D)+1,12,year(D))
        else:
            return make_date(1,1,year(D)+1)

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
            return make_date(day(D)-1,1,year(D))
        else:
            return make_date(31,12,year(D)-1)
    elif month(D) == 3:
        if day(D) > 1:
            return make_date(day(D) - 1,month(D),year(D))
        else:
             if is_kabisat(year(D)):
                 return make_date(29,month(D)-1,year(D))
             else:
                 return make_date(28,month(D)-1,year(D))           
    elif month(D) == 2 or month(D) == 4 or month(D) == 6 or month(D) == 8 or month(D) == 9 or month(D) == 11:
        if day(D) > 1:
            return make_date(day(D)-1,month(D),year(D))
        else:
            return make_date(31,month(D)-1,year(D))
    elif month(D) == 5 or month(D) == 7 or month(D) == 10 or month(D) == 12:
        if day(D) > 1:
            return make_date(day(D)-1,month(D),year(D))
        else:
            return make_date(30,month(D)-1,year(D))

# NextNDay:date,integer --> date
#   {NextNDay(D,N): Menghitung date yang merupakanN hari(N adalah nilai integer) sesudah dari date D yang diberikan
#    hari mulai tidak dihitung tetapi hari terakhir dihitung.
#                   NextNDay(<1,10,2021>,10) adalah <11,10,2021>}
# REALISASI(dalam python)
def next_n_day(D,N):
    return make_date(date_calculation_algorithms.days_to_date(date_calculation_algorithms.date_to_days(day(D),month(D),year(D)) + N)[0],date_calculation_algorithms.days_to_date(date_calculation_algorithms.date_to_days(day(D),month(D),year(D)) + N)[1],date_calculation_algorithms.days_to_date(date_calculation_algorithms.date_to_days(day(D),month(D),year(D)) + N)[2])


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
print("Tanggal make_date(17,8,1945) terbentuk dengan: {}.{}.{}".format(day(make_date(17,8,1945)),month(make_date(17,8,1945)),year(make_date(17,8,1945))))
print("Tanggal make_date(27,11,2002) terbentuk dengan: {}.{}.{}".format(day(make_date(27,11,2002)),month(make_date(27,11,2002)),year(make_date(27,11,2002))))

print("\n===SESI FUNGSI PREDIKAT===\n")
print("Apakah make_date(17,8,1945) dan make_date(27,11,2002) itu sama tanggal-nya? {}".format(is_eq_d(make_date(17,8,1945),make_date(27,11,2002))))
print("Apakah make_date(17,8,1945) itu sebelum make_date(27,11,2002)? {}".format(is_before(make_date(17,8,1945),make_date(27,11,2002))))
print("Apakah make_date(27,11,2002) itu setelah make_date(27,11,2002)? {}".format(is_after(make_date(17,8,1945),make_date(27,11,2002))))
print("Apakah make_date(17,8,1945) itu tahun kabisat? {}".format(is_kabisat(year(make_date(17,8,1945)))))
print("Apakah make_date(27,11,2002) itu tahun kabisat? {}".format(is_kabisat(year(make_date(27,11,2002)))))
print("Apakah tahun {} itu tahun kabisat? {}".format(datetime.datetime.now().year,is_kabisat(datetime.datetime.now().year)))
print("\n===SESI FUNGSI OPERATOR===\n")
print("Mari kita ingat kembali tanggal make_date(17,8,1945) terbentuk dengan: {}.{}.{}".format(day(make_date(17,8,1945)),month(make_date(17,8,1945)),year(make_date(17,8,1945))))
print("Mari kita ingat kembali tanggal make_date(27,11,2002) terbentuk dengan: {}.{}.{}\n".format(day(make_date(27,11,2002)),month(make_date(27,11,2002)),year(make_date(27,11,2002))))
print("Tanggal pada 1 hari setelah tanggal make_date(17,8,1945) adalah {}.{}.{}".format(day(next_day(make_date(17,8,1945))),month(next_day(make_date(17,8,1945))),year(next_day(make_date(17,8,1945)))))
print("Tanggal pada 1 hari sebelum tanggal make_date(27,11,2002) adalah {}.{}.{}".format(day(yesterday(make_date(27,11,2002))),month(yesterday(make_date(27,11,2002))),year(yesterday(make_date(27,11,2002)))))
print("Tangal {0}.{1}.{2} adalah {3} hari setelah tanggal 1 Januari {2}.".format(day(make_date(17,8,1945)),month(make_date(17,8,1945)),year(make_date(17,8,1945)),hari_ke_1900(make_date(17,8,1945))))
D4 = make_date(datetime.datetime.now().day,datetime.datetime.now().month,datetime.datetime.now().year)
D3 = next_n_day(make_date(27,11,2002),100)
print("{6} hari dari tanggal {0}.{1}.{2} adalah tanggal? {3}.{4}.{5}".format(day(make_date(27,11,2002)),month(make_date(27,11,2002)),year(make_date(27,11,2002)),day(D3),month(D3),year(D3),100))
print("{3} hari dari {0}.{1}.{2} adalah {4}.{5}.{6}".format(day(make_date(17,8,1945)),month(make_date(17,8,1945)),year(make_date(17,8,1945)), date_calculation_algorithms.date_to_days(day(D4),month(D4),year(D4)) - date_calculation_algorithms.date_to_days(day(make_date(17,8,1945)),month(make_date(17,8,1945)),year(make_date(17,8,1945))),day(D4),month(D4),year(D4)))

print("\n===Spesial Stuff===\n")
print("Countdown day-1 UTS Semester Ganjil 2020/2021 Informatika-2021: {} Hari Lagi!".format(date_calculation_algorithms.date_to_days(day(make_date(11,10,2021)),month(make_date(11,10,2021)),year(make_date(11,10,2021))) - date_calculation_algorithms.date_to_days(day(D4),month(D4),year(D4))))

                   
print("\n=====PROGRAM BERAKHIR,TERIMAKASIH=====")









