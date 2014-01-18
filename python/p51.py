import time,math


def makePrimeList(N):
	# Define a list of primes up to n**2 = 10000
#	n = 500
#	N = n**2+1
	n = int(math.sqrt(N))
	pList = range(2,N)
	for p in range(2,n):
		if pList[p-2] != 0:
			x = pList[p-2]
			k = 2
			while x*k < N:
				pList[x*k-2] = 0
				k = k + 1
	p = 0
	while p < len(pList):
		if pList[p] == 0:
			pList.pop(p)
		else:
			p = p+1

	return pList
#	lenpList = len(pList)

def repDigits(n):
	digList = [0,0,0,0,0,0,0,0,0,0]	
	i = 0
	while n > 0:
		i = n % 10
		digList[i] += 1
		n = n/10
	return digList


P = 100000
pList = makePrimeList(P)
for x in pList:
	if 3 in repDigits(x):
		print x


