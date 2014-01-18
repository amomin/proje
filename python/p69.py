import time,MillerTest
isPrime = MillerTest.MillerRabin
t1 = time.time()
def phi(m): # Returns the value of Euler's Totient function phi(n)
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

maxsofar = 0.1
record = 0
L = [0,0]
for x in range(2,1000000):
#	print x,phi(x)
	if isPrime(x):
		L.append(x-1)
	else:
		m = x
		i = 2
		flag = False
		while not flag: 
			k = 0
			while (m%i) == 0: #i divides m, count how many times
				flag = True
				k+=1
				m/=i
			if flag:
				if m > 1:
					L.append((i**(k-1)*(i-1))*L[m])
				else:
					L.append(i**(k-1)*(i-1))
			i+=1
	if ((1.0*x)/((1.0*L[x])) > maxsofar):
		maxsofar = (1.0*x)/(1.0*L[x])
		record = x

print record, maxsofar
print time.time() - t1
#Takes about 100 secs
