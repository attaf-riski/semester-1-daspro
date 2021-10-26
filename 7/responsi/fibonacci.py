# Nama File : fibonacci.py
# Deskripsi : Menghitung bilangan Fibonacci ke-n
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 21 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# fibonacci: integer >=0 --> integer > 0
#   {finonacci(n) menghitung bilangan fibonacci ke-n, sesuai definisi barisan fibonacci 0,1,1,2,3,5,...
#    jika n = 0 : finacci(n) = 0
#    jika n = 1 : finacci(n) = 1
#    jika n > 1 : fibonacci(n-1) + fibonacci(n-2)}

# REALISASI
def fibonacci(n):
    if n == 0: #basis 0
        return 0
    elif n == 1: #basis 1
        return 1
    else: #rekurens
        return fibonacci(n-1) + fibonacci(n-2)

# APLIKASI
print("===Program Start===")
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print("===Program End, Thanks===")
