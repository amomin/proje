def fracinvert(M):
	return [M[1],M[0]]

def fracadd(M1,M2):
	return reducefrac([M1[0]*M2[1] + M1[1]*M2[0], M1[1]*M2[1]])

def reducefrac(M):
	a = gcd(M[0],M[1])
	return [M[0]/a,M[1]/a]

def gcd(a,b):
	m = min(a,b)
	n = max(a,b)
	return gcdminmax(m,n)

def gcdminmax(a,b):
	if (b%a) == 0:
		return a
	else:
		return gcdminmax(b%a,a)

L = [2]

counter = 1
while len(L) < 100: 
	L.extend([1,2*counter,1])
	counter +=1

print L

oldfrac = [1,L.pop()]
newfrac = []
while L !=[]:
	x = L.pop()
	newfrac = reducefrac(fracadd([x,1],fracinvert(oldfrac)))
	oldfrac = newfrac

print newfrac

x = newfrac[0]

sumdigitsx = 0
while x > 0:
	sumdigitsx += (x%10)
	x /= 10

print (1.0*newfrac[0])/(1.0*newfrac[1])
print sumdigitsx
