# Of course, one way to go would be to try prime numbers near the square root of the target until
# one gets a permutation.  Pretty ad hoc, but it seems to work well.  Nonetheless, we did it 
# by going (more or less) one by one.  It takes a while but isn't horribly bad.
# If you're willing to assume that the solution isn't too far from the target,
# you can reduce the run time quite a bit.  Also, for some reason it seems that
# numbers congruent 1 mod 6 produce better rations than ones congruent 5 mod 6, which
# also lets you save some time.

import time,MillerTest
isPrime = MillerTest.MillerRabin

maxtocheck = 10**7
t1 = time.time()
def phi(m): # Returns the value of Euler's Totient function phi(n)
	if isPrime(m):
		return m-1
	else:
		i = 2
		answer = 1
		while i*i <= m:
			k = 0
			while (m%i) == 0: #i divides m, count how many times
				k+=1
				m/=i
			if k > 0:
				answer *= (i**(k-1))*(i-1) #totient function is multiplicative, and equal to p^(k-1)(p-1) if m = p**(k)
			i+=1
		if m>1:
			return answer*(m-1)
		else:
			return answer


def digitarray(n):
	L = []
	for x in range(0,10):
		L.append(0)
	while n > 0:
		L[n%10]+=1
		n/=10
	return L


t1 = time.time()
winner = 2
minsofar = 2
#for x in range(5,maxtocheck+1,6):
#	if ((x%5) == 0) or ((x%7)==0) or ((x%11)==0) or ((x%13)==0):
#		continue
#	else:
#		if digitarray(x) == digitarray(phi(x)):
#			#print x,phi(x)
#			if (x*1.0)/(1.0*phi(x)) < minsofar:
#				minsofar = (x*1.0)/(1.0*phi(x))
#				winner = x
#print minsofar, winner
#print time.time()-t1
#IT SEEMS TO BE UNNECESSARY TO CHECK congruent 5 mod 6 for some reason (why???)
smallprimes = [5,7,11,13,17,19,23,29,31,37,41,43]
for x in range(7*10**6+3,maxtocheck+1,6):
	flag = True
	for p in smallprimes:
		if (x%p)==0:
			flag = False
			break #want to break the for loop, is this the right place?	
	if flag: # all divisors are fairly small, so it's worth a try	
		if digitarray(x) == digitarray(phi(x)):
		#print x,phi(x)
			if (x*1.0)/(1.0*phi(x)) < minsofar:
				minsofar = (x*1.0)/(1.0*phi(x))
				winner = x


print minsofar, winner
print time.time()-t1

# OUTUPT 
#1.03593740383 3904763
#485.278009176
#1.00070905112 8319823
#962.847380161

