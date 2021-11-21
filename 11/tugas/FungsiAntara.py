# Nama File : FungsiAntara.py
# Deskripsi : Penyedia fungsi-fungsi untuk membantu type bentukan BinaryTree
# Pembuat : Attaf Riski Putra Ramadhan
# Tanggal : 20 Nop 2021

# DEFINISI DAN SPESIFIKASI 
# konsoL : Elemen,List of List --> List of List
#   {konsoL(E,L): membuat list baru hasil konkatenasi Elemen E dengan List of List L, Elemen ditaruh di depan}
# REALISASI (dalam python)
def konsoL(E,L):
    if L == []:
        return [E]
    else:
        return [E] + L


