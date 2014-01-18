####
##
# ANSWER = 5482660
## (where k = 1912)
####


import time
import math
N = 3000
t0 = time.clock()
k = 1

#d = 2
d = 1
flag = True
while flag:
	Pd = d*(3*d-1)/2
	k = d+1
	while k < N and flag: #255404: #500000:
#  This is for d = 1
#	x = (3*k+1)*(9*k+2)/2
#	j =(x - 1)/3
# More generally for d
		Pk = k*(3*k-1)/2
		if ((Pk - Pd) % (3*d)) == 0: #j == int(j):
			j = (Pk - Pd)/(3*d)
			y = j*(3*j-1)/2
			z = (j+d)*(3*j + 3*d-1)/2
			if ((1+math.sqrt(1+24*(y+z)))/6) % 1 == 0:
				flag = False
        			print d,k,j,Pk,y,z,y+z
		k = k + 1
#	k = k + 3
	d = d+1

print time.clock() - t0
