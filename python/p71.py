def gcd(m,n): # compute the gcd of m,n assuming m <= n
	if (n%m)==0:
		return m
	else:
		return gcd(n%m,m)

currentrecord = 0
currentpair = [0,0]
for d in range(8,35):
	n = (3*d)/7
#	print n,d, (1.0*n)/(1.0*d)
	if ((1.0*n)/(1.0*d) > currentrecord) and (gcd(n,d) == 1):
		currentrecord =	(1.0*n)/(1.0*d)
		currentpair = [n,d]

print currentpair
			
