def gcd(n,d): #assume n<d
	if (d%n) == 0:
		return n
	else:
		return gcd(d %n,n)

count = 0
for d in range(4,12001):
	if (d%3) == 0:
		a = d/3
	else:
		a = d/3 + 1
	for x in range(a,d/2+1):
		if gcd(x,d) == 1:
#			print x,d, gcd(x,d)==1
			count += 1
print count
