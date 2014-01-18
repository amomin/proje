import math, time

# Finds the Nth largest prime (define N below)
# Uses a brute search, not a sieve, so only use for N not too large
N = 10001 # We wish to find the Nth prime
i =3 #Start counting at 3, since we already know 1 is the first prime - we'll only look at odd numbers to simplify count slightly
counter =1 

t1 = time.clock() 

def isPrime(p): # input is assumed to be an integer bigger than or equal to 3
	answer = 1
	if p%2 == 0: # It is slighly faster if we rule out even numbers to begin with
		return 0
	else:
		if (p > 3):
			for j in range(3,int(math.sqrt(p))+1,2): #We only need to check against odd numbers
				if (p%j == 0):
					answer = 0
					break
		return answer

def isPrime1(p): # An (ad hoc) improvement on the above ad hoc test
	# return 0 if not and 1 if prime
	answer = 1 
	if (p < 2):
		answer = 0	
	elif (p < 4):
		answer = 1
	elif (p % 2 == 0):
		answer = 0	
	elif (p < 9):
		answer = 1
	elif (p % 3 == 0):
		answer = 0	
	else:
		n = 5
		while (n < math.sqrt(p)+1):
			if (p % n == 0):
				answer = 0	
				break
			elif (p% (n+2) ==0):
				answer = 0	
				break
			else:
				n = n + 6
	return answer

		
#for k in range(100):
#	print(k, isPrime1(k))

while counter < N :
	if isPrime1(i) == 1:
		counter = counter + 1
	i = i + 2  #Since we only need to look at odd numbers anyway

print 'The', N, 'th largest prime is', i-2, '.  Time took = ',  time.clock() - t1
