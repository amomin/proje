import math, time

t1 = time.clock()

N = int(math.sqrt(2200000) )
#A = []
#zeros = []
#for i in range(N):
#	zeros.append(0)
#print zeros
#for j in range(N):
#	A.append(zeros)

A = []
for i in range(N):
	A.append([])
	for j in range(N):
		A[i].append(0)

A[0][0] = 1 
n = 2
#print A[0]
#print A[1]
for x in range(2,N):
	if A[0][x] == 0:
		n = 2
		while (n*x < N*N):
#			print n*x
			i = n*x/N
			j = n*x % N 
#			print i, j
			A[i][j] = 1
			n = n + 1

#print A

primeList = []
for i in range(N):
	for j in range(N):
		if A[i][j] == 0:
			#print N*i + j 
			primeList.append(N*i + j)

# print primeList

sumprimes = 0
for x in primeList:
#	print x
	if (x < 2000000):
		sumprimes = sumprimes + x
	else:
		break

print 'The sum of all primes less than 2 million is', sumprimes, ' calculated in', time.clock() - t1, 'seconds.'
