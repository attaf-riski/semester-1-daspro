# nama
# nanti

# DEFINISI TYPE
# type Hr : integer[1..31]
#   {...}

# type Bln : integer[1..12]
#   {...}

# type Thn : integer>0
#   {...}

# type date<Hr:Hr,Hr:Bln,Hr:Thn>
#   {...}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeDate: <Hr,Bln,Thn> --> date
def make_date(Hr,Bln,Thn):
    return [Hr,Bln,Thn]

# DEFINISI DAN SPESIFIKASI SELEKTOR
def day(D):
    return D[0]

# DEFINISI DAN SPESIFIKASI PREDIKAT
def month(D):
    return D[1]


# DEFINISI DAN SPESIFIKASI OPERATOR
def year(D):
    return D[2]


# REALISASI
# APLIKASI