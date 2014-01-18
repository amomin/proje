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
	if L[n] == 0: #Only check if n is not already known to be bad
		X = getlist(n)
		if len(X) == 60:
			count +=1
		for j in X:
			if j < Nmax:
				L[j] = 1 # No need to check any of these values - we now 

print count

