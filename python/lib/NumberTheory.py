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

def gcd(a,b):
	m = min(a,b)
	n = max(a,b)
	return gcdminmax(m,n)

def gcdminmax(a,b):
	if (b%a) == 0:
		return a
	else:
		return gcdminmax(b%a,a)
