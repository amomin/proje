from math import sqrt
import MillerTest
isPrime = MillerTest.MillerRabin
found = False

k = 9
while not found:
	if k % 100 == 0:
		print k
	j = 1
	if not isPrime(k):
		found = True
		while 1.0*j < sqrt(k/2.0)  and found:
			if isPrime(k - 2*j**2):
				found = False
			j = j + 1
	if found:
		print k	
	k = k + 2
