# Nama file : is_isoceless_triangle.py
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 9 September 2021
# Deskripsi : Mengidentifikasi sebuah segitiga apakah berjenis sama kaki berdasarkan sisi-sisinya.

# Definisi dan Spesifikasi
# is_isocelesss_triangle : 3 integer -> boolean
# is_isocelesss_triangle(a,b,c) akan menghasilkan benar bila diantara (a,b,c) terdapat 2 nilai yang sama
# tetapi tidak semuanya. Dengan syarat a > 0, b > 0, c > 0 .

# is_not_equilateral_triangle : 3 integer -> boolean
# is_not_equilateral_triangle(a,b,c) akan menghasilkan benar bila diantara a,b, dan c ada perbedaan nilai

# Realisasi
def is_not_equilateral_triangle(a,b,c) :
    return a != b or b != c or c != a

def is_isoceless_triangle(a,b,c) :
    if a > 0 and b > 0 and c > 0 :
        if is_not_equilateral_triangle(a,b,c) and (a == b or b == c or c == a) :
            return True
        else:
            return False
    else:
        return False

# Aplikasi
print(is_isoceless_triangle(1,2,3)) # Hasilnya False
print(is_isoceless_triangle(10,10,5)) # Hasilnya True

