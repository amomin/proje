import time
import MillerTest
isPrime = MillerTest.MillerRabin

t1 = time.time()
X = 10000
N = X  + 1

#p = [[0]*(N+1),[1]*(N+1)]

def square(a,n):
	return (a*a) % n

total=0
for k in range(3,N):
	n=k-1
	found = False
	if isPrime(k):
		n=1
	elif ((k % 2) == 0)  and isPrime(k/2):
		n=1
	elif ((k % 3) == 0 ) and isPrime(k/3):
		if square( 2*(k/3) + 1, k) == 1:
			n = 2*(k/3) + 1
		elif square( 2*(k/3) - 1, k) == 1:
			n = 2*(k/3) -1
		else:
			n=1
	else: 
		while (n >= k/2) and not found:
			n = n-1
			s = square(n,k)
			#print "Square", n, k, s
			if s == 1:
				found=True
		if not found:
			n=1
	total = total + n
	#print "For ", k, " largest sqrt is: ", n


print "Total"
print total

print "Time"
print time.time() - t1

