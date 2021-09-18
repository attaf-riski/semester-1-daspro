# Nama file : jarak2titik.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 4 September 2021
# Deskripsi : Menerima 4 buah bilangan riil yang pengertiany adlah dua pasang titik pada koordinat kartesian, dan menghasilkan sebuah bilangan riil yang merupakan jarak dari
#               kedua titik tersebut(atau panjang garis yang dibentuk kedua titik tersebut), dengan melakukan aplikasi terhadap dua buah fungsi antara yang harus didefinisikan
#               terlebih dahulu sebagai berikut dif2 adalah sebuah fungsi yang menerima dua buah bilangan riil dan menghasilkan pangkat dua dari selisih kedua bilangan rill tersebut.
#               Pangkat dua dilakukan oleh fungsi fx2 yang menerima sebuah bilangan riil dan menghasilkan pangkat 2  dari bilangan riil tersebut. 

# Definisi dan spesifikasi 
# LS : 4 real --> real
#   LS(x1,x2,y1,y2) akan mencari jarak dari 2 titik yaitu (x1,y1) dengan (x2,y2)

# dif2 : 2 real --> real
# dif2(x,y) akan mencari kuadrat dari selisih antara x dan y

# fx2 : real -> real
# fx2(x) berfungsi untuk mencari kuadrat dari x

# Realisasi
import math # dibutuhkan untuk menggunakan fungsi kuadrat(sqrt()) di python

def fx2(x) :
    return x*x

def dif2(x,y) :
    return fx2(x-y)

def LS(x1,x2,y1,y2) :
    return math.sqrt(dif2(y1,y2) + dif2(x2,x1))

# Aplikasi
print(LS(1,3,5,6)) # hasilnya 2.23606797749979
