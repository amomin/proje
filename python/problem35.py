import MillerTest
isPrime = MillerTest.MillerRabin

count = 0
for x in range(2,1000000):
	if isPrime(x):
		y = str(x)
		flag = True
		for i in range(len(y)):
			y = y[1:] + y[0]
			if not isPrime(int(y)):
				flag = False
		if flag:
#			print x	
			count = count + 1

print count
