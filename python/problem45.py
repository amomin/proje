from math import sqrt
def is_pent(n):
	if ((1 + sqrt(1 + 24*n))/6) % 1 == 0:
		return True
	else:
		return False

def is_Tri(n):
	if ((-1 + sqrt(1 + 8*n))/6) % 1 == 0:
		return True
	else:	
		return False

k = 287
flag = False
while not flag:
	if is_pent(k*(k+1)/2):
		print k, k*(k+1)/2
		flag = True
	k = k+2
