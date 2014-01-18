# Generates digits of the form nnxnxxn
# where n is a number and x is an unspecified digit
# then replace x with digits 0-9
# look at the 9 numbers generated
# if 8 are prime then print the pattern
# one of the patterns should be the answer
# the first result returned is not accepted because it replaces digits occuring before the first digit
# the second result returned is similar, but replacing x = 0 does not result in a prime, so you can take
# 	that as the answer replacing x = 1



import string
import itertools
import MillerTest

isPrime = MillerTest.MillerRabin

perm = itertools.permutations
comb = itertools.combinations
prod = itertools.product

digits = '0123456789'

#print isPrime(2342232)
N = 4
for x in prod(digits,repeat = N):
	for y in comb('0123456',N):
		s = ['x','x','x','x','x','x','x'] 
		for i in range(N):
			s[int(y[i])] = x[i]
		
#		print s
		count = 0
		for i in range(10):
			t = map(str,s)
			t = ''.join(t)
			t = string.replace(t,'x',str(i))
			n = int(t)
#			print n
#			if n > 1:
#				print isPrime(n)
#			print n
			if n > 1:
				if isPrime(n):
					count += 1
		if count > 7:
			print s
#			print t
