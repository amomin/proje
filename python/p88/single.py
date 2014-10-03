import math, sys, time
import MillerTest

isPrime = MillerTest.MillerRabin
# Consider taking products of numbers instead of factorizing and then finding all divisors

tic = time.clock()

MIN = 2
MAX = 11000 #12201 should suffice
COUNTMAX=9999
def getDivSums(n,min=2):
	solns = [[n,1,[n]]]
	if isPrime(n):
		return solns
	for i in range(min,n/2+1):
		if n%i==0:
			res = getDivSums(n/i,i)
			for x in res:
				_l=x[2]+[i]
				new_soln=[x[0]+i,x[1]+1,_l]
				if new_soln not in solns:
					solns.append( new_soln )
	#print solns
	return solns

i=1782
x = getDivSums(i)
for f in x:
	k=i-f[0]+f[1]
	if k==1753:
		print k, f
