x = 0
sum2 = 0
maxsofar = 0

for a in range(1,100):
	for b in range(1,100):
		sum2 = 0
		x = b**a
		while x > 0: #Compute the digit sum of x = b**a
			sum2 += (x % 10)
			x /= 10
		if sum2 > maxsofar: #WE have a new max, so store it
			maxsofar = sum2

print maxsofar	
