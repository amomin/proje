import MillerTest
isPrime = MillerTest.MillerRabin


def isPerm(L1,L2,L3):
	L = [L1,L2,L3]
	dL = [[],[],[]]
	for i in range(3):
#		dL[i] = []
		x = L[i]
		while x!=0:
			dL[i].insert(0,x % 10)
			x = x/10
		dL[i].sort()
	if dL[0] == dL[1] and dL[1] == dL[2]:
		return True
	else:
		return False

print isPerm(1034,1430,3410)
print isPerm(1000,1011,1001)

found = False
x0 = 1488
while x0 < 10000 and not found:
	d = 3
	if isPrime(x0):
		while d < (10000 - x0)/2 and not found:
			if isPrime(x0+d):
				if isPrime(x0+2*d):
					if x0 != 1487 and isPerm(x0,x0+d,x0+2*d):
						print x0,x0+d,x0+2*d
						found = True
						
			d = d + 3 
	x0 = x0 + 1

print isPrime(1009), isPrime(1021), isPrime(1033), isPerm(1009,1021,1033)
