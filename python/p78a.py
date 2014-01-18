import time
t1 = time.time()
p = [1,1,2,3]
lenp = len(p)

Nmax = 100000
modulus = 10**6

# A test to check we are correctly generating generalized pentagonal numbers 1,2,5,7,12,15,22,26,etc.
#parity = 0
#m = 1
#while m < 11:
#	if parity == 0:
#		m2 = m
#	else:
#		m2 = -m
#	print (m2*(3*m2-1))/2
#	parity = (parity+1)%2
#	if parity == 0:
#		m+=1
i=lenp
flag = False
while not flag: #compute next partition number using the reccurrence formula
	count = 0
	m = 1
	parity = 0
	genpentm = 1
	while genpentm <= i:
		if ((-1)**m == -1 ):
#			print (-1)**m, genpentm
#			count += p[i - genpentm]
			count = (count + p[i - genpentm]) % modulus
		else:
#			count -= p[i - genpentm]
			count = (count - p[i - genpentm]) % modulus
#			print (-1)**m, genpentm
		parity = (parity+1)%2
		if parity == 0:
			m+=1
		if parity == 0:
			m2 = m
		else:
			m2 = -m
		genpentm = (m2*(3*m2-1))/2
	p.append(count)
	if count == 0:
		print i,count
		flag = True
	i+=1

print time.time() - t1

