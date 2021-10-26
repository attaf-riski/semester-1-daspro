# Nama File : toh.py
# Deskripsi : hasil nyontek geekgorgeeks
# Pembuat : ---
# Tanggal : 24 Oktober 2021

# DEFINISI DAN DESKRIPSI 
# toh


# Recursive Python function to solve the tower of hanoi
def TowerOfHanoi(n , source, destination, auxiliary):
	if n==1:
		print("Move disk 1 from source",source,"to destination",destination)
		return
	TowerOfHanoi(n-1, source, auxiliary, destination)
	print("Move disk",n,"from source",source,"to destination",destination)
	TowerOfHanoi(n-1, auxiliary, destination, source)
		
# Driver code
TowerOfHanoi(4,'A','B','C')
# A, C, B are the name of rods

# Contributed By Dilip Jain
