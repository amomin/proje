import time
import MillerTest
import random
isPrime = MillerTest.MillerRabin

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
while p < len(pList):
        if pList[p] == 0:
                pList.pop(p)
        else:
                p = p+1

print pList

# Takes about 1-2 sec
t0 = time.clock()
count = 0
for i in range(1,10000):
	n = random.randint(1,N)
	if isPrime(n):
	        count = count + 1
print time.clock() - t0
print count

# Takes about 18 sec!!!
count = 0
t0 = time.clock()
for i in range(1,10000):
	n = random.randint(1,N)
	if n in pList:
	        count = count + 1
print time.clock() - t0
print count



