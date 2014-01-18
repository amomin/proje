# Define a list of primes up to n**2 = 10000
n = 500
N = n**2+1
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

print pList
lenpList = len(pList)

def facList(n):
# Returns the list of the first 5 or fewer prime factors of n
	ansList = []
	k = 0
	while n > 1 and len(ansList) < 5 and k < lenpList:
		x = pList[k]
		if n % x == 0:
			ansList.append(x)
			n = n/x
			while n % x == 0:
				n = n/x
		k = k+1
	return ansList

print 2310, facList(2310)
#for i in range(4,65):
#	print i, facList(i)

k = 5
P2 = False
P3 = False
P4 = False
found = False
while not found:
	P1 = P2
	P2 = P3
	P3 = P4
	P4 = (len(facList(k)) == 4)
	if P1 and P2 and P3 and P4:
		found = True
		print k-3,k-2,k-1,k
	k = k+1			
		
		
	
