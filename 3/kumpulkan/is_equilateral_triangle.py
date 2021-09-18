# Nama file : is_equilateral_triangle.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 9 September 2021
# Deskripsi : Mengidentifikasi sebuah segitiga apakah berjenis sama sisi dengan cara mengidentifikasi sisi-sisinya.

# Definisi dan Spesifikasi
# is_equilateral_triangle : 3 integer -> boolean
# is_equilateral_triangle(a,b,c) menghasilkan benar apabila a, b, dan c bernilai sama selain itu menghasilkan salah. Dengan syarat a > 0, b > 0, c > 0.

# Realisasi
def is_equilateral_triangle(a,b,c):
    if a > 0 and b > 0 and c > 0:
        return (a == b) and (b == c) and (c == a)
    else:
        return False    
    
# Aplikasi
print(is_equilateral_triangle(1,2,3)) # Hasilnya adalah False
print(is_equilateral_triangle(10,10,10)) # Hasilnya adalah True
