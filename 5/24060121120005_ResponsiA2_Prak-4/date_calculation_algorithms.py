# Nama file : date_calculation_algorithms.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 30 September 2021
# Deskripsi : Sebuah algoritma pencari jumlah hari yang telah ditemukan oleh orang lain

# DEFINISI DAN SPESIFIKASI

# DateToDays: 3 integer --> integer
#   {DateToDays(d,m,y): Menghitung jumlah hari dimulai dari tanggal 1 Januari 0001}

# DaysToDate: integer --> <d,m,y>
#   {DaysToDate(g): Menkonversi jumlah hari menjadi tanggal}


# REALISASI
# ref : https://web.archive.org/web/20170507133619/https://alcor.concordia.ca/~gpkatch/gdate-algorithm.html
def date_to_days(d,m,y):
    m = (m + 9) % 12
    y = (y - (m//10))
    return (365*y) + (y//4) - (y//100) + (y//400) + ((m*306 + 5)//10) + (d - 1)

def days_to_date(g):
    y = (10000*g + 14780) // 3652425
    ddd = g - ((365*y)+ (y//4) - (y//100) + (y//400))
    if (ddd < 0):
        y = y - 1
        ddd = g - (365*y + (y//4) - (y//100) + (y//400))
        
    mi = (100*ddd + 52)//3060
    mm = ((mi + 2)%12) + 1
    y = y + ((mi+2)//12)
    dd = ddd - ((mi*306 + 5)//10) + 1
    return [dd,mm,y]

