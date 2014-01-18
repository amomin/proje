import time
import MillerTest
isPrime = MillerTest.MillerRabin


t0 = time.clock()


# Define a list of primes up to n**2 
n = 100 
N = n**2+1
Limit = 1000000
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

#print pList
lenpList = len(pList)

primeSumPrime = 2
lengthSum = 1
firstPrime = 2
listEntry = 0

currentEntry = 0
while currentEntry + lengthSum +1< lenpList:
	L = lengthSum + 1
	runTotal = 0
	for x in range(L+1):
		runTotal = runTotal + pList[currentEntry + x]
	while currentEntry + L < lenpList and runTotal < Limit:
		if isPrime(runTotal):
			lengthSum = L+1
			firstPrime = pList[currentEntry]
			listEntry = currentEntry
			primeSumPrime = runTotal
#			print primeSumPrime, currentEntry,lengthSum
		L = L+1
		runTotal = runTotal + pList[currentEntry + L]
	currentEntry += 1

#print primeSumPrime, isPrime(primeSumPrime), listEntry, lengthSum, pList[listEntry:listEntry+lengthSum]
#sum = 0
#for x in pList[listEntry:listEntry+lengthSum]:
#	sum = sum + x
#print sum, isPrime(sum)
print primeSumPrime
print time.clock() - t0
