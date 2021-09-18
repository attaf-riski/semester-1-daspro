# Nama file : is_scalane_triangle.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 9 September 2021
# Deskripsi : Mengidentifikasi sebuah segitiga apakah berjenis sembarang berdasarkan sisi-sisinya.

# Definisi dan Spesifikasi
# is_scalane_triangle : 3 integer -> boolean
# is_scalane_triangle(a,b,c) akan menghasilkan benar bila diantara(a,b,c) tidak terdapat nilai yang sama.Dengan syarat a > 0, b > 0, c > 0.

# Realisasi
def is_scalane_triangle(a,b,c):
    if a > 0 and b > 0 and c > 0 :
       return a != b and b != c and c != a
    else:
        return False

# Aplikasi
print(is_scalane_triangle(1,2,3)) # Hasilnya adalah True
print(is_scalane_triangle(20,30,20)) # Hasilnya adalah False
