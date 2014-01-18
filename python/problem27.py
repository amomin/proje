import math

def isPrime(p): # input is assumed to be an integer bigger than or equal to 3
	answer = 1
	if (p < 2):
		return 0	
	if (p == 2):
		return answer
	else:		
		if p%2 == 0: # It is slighly faster if we rule out even numbers to begin with
			answer = 0
			return answer
		else:
			if (p > 3):
				for j in range(3,int(math.sqrt(p))+1,2): #We only need to check against odd numbers
					if (p%j == 0):
						answer = 0
						break
			return answer

# make a list of primes less than 1000:
primeList = [2]
for n in range(3,1000):
	if isPrime(n):
		primeList.append(n)
#print primeList

maxN = 1
n = 1
bmax = 2
amax = 0
for a in range(-999,1000,2):
	for b in primeList:
		n = 1
		while (isPrime(n**2 + a*n + b) == 1):
			n =  n + 1
		if (n > maxN):
			maxN =n 
			amax = a
			bmax = b

print(amax, bmax, maxN)

	

