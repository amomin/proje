import itertools
import MillerTest

isPrime = MillerTest.MillerRabin

dlist = ['1','2','3','4','5','6']

maxsofar  = 0
for x in itertools.permutations(dlist):
	y = '7'
	for d in range(len(x)):
		y = y + x[d]
	if isPrime(int(y)) and int(y) > maxsofar:
		maxsofar = int(y) 

print maxsofar
