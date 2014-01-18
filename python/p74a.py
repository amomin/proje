fact = [1,1,2,6,24,120,720,5040,40320,362880]

Nmax = 1000000

# Routine to get the next term
def nextterm(n):
	count = 0
	while n > 0:
		count += fact[n%10]
		n/=10
	return count


# Compute a cycle

def getlist(n):
	L = []
	flag = False
	i = 0
	while not flag:
		try: 
			i = L.index(n)
			flag = True	
		except ValueError:
			L.append(n)
			n = nextterm(n)
	return L

L = [0]*(Nmax+1)
count = 0
# L[n] is 0 if n is unknown, and 1 if n is known
for n in range(1,Nmax):
	count = 0
	m = nextterm(n)
	if m < Nmax and L[m] != 0:
		L[n] = L[m]+1
	else:
		while (count < 60) and (m > Nmax or (L[m] == 0)):
			count += 1
			m = nextterm(m)
			if (m < Nmax) and (L[m] != 0):
				m2 = n
				while count > 0:
					if m2 < Nmax:
						L[m2] = L[m] + count
					m2 = nextterm(m2)
					count-=1	
		if count == 60:	
			L[n]=61	
print count

