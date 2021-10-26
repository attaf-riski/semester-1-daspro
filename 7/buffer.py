#catatan sementara
#jangan lupa dokumentasi
#iteratif VS rekursif?
#rekursif menang sederhana, komputasi belum tentu,apakah maknanya?
#basis gunanya biar rekursif tidak selamanya muter
#cara 1 dan 2 perbedaanya adalah basisnya
#cara menentukan basis yang tepat, tergantung kasus kah?
#cara 3 salah, karena basis tidak berguna

#def faciter bikin tambah rumit
#count jadi lebih fleksibel
#cara kerjanya mudeng, cuma kegunaanya kagak mudeng yang faciter

#pikir ditulis bila pusing

#konisi ketika stack overflow
#domain salah, basis salah

#fac3 status salah, status 3
#fac1 ngga nerima 0, fac2 nerima 0, 

# Mas Roy session
#fibonacci adalah contoh paling mudah,

#0 1 1 2 3 5 8 13 21
#bertanyalah ketika dipersilahkan atau ketika penjelasan berakhir
#visualisasi fibonacci
def fibonacci_rekursif(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rekursif(n-1) + fibonacci_rekursif(n-2)

print(fibonacci_rekursif(1))
print(fibonacci_rekursif(0)) 


#penjumlahan bilangan integer
def plus(x,y):
    if y == 0:
        return x
    else:
        return 1 + plus(x,y-1)

print(plus(4,0))
print(plus(4,1))
print(plus(5,5))


#aplikasi
print(plus(3,5))
# plus (3,5-1)
# 1 + plus(3,4-1)
# 1 + 1 + plus(3,3-1)
# 1 + 1 + 1 + plus(3,2-1)
# 1 + 1 + 1 + 1 + plus(3,1-1)
# 1 + 1 + 1 + 1 + 1 + 3


#penjelasan tugas
#file dipisah-pisah
#keluaran ikuti apa yang sudah diajari
#deadline responsi, besok
#


