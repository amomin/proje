import math, time
t1 = time.clock()

#
#
# Improvements?
# Can try an approach to guess the number n knowing that it should have about 500 factors...
# So it should be 2^large*3^less large*5^one or two*7*13*... or something like that... such that
# large +1 * less large + 1* tw or three * 2 * 2 * ...
#
#  Actually, this strategy is just not good for triangular numbers.  ON the other hand, for finding the 
# smallest number with a certain number of factors is probably the way to go...


# This method computes the number of divisors of an integer input n
def numDivisors(n):
	# Counts the number of divisors of n using the fact that numDivisors is
	# multiplicative.  We find factors of the form p**k, with k maximal.  The 
	# number of divisors of p**k is k+1.  So, numDivisors(n) = numDivisors(n/p**k)*numDivisors(p**k) = (k+1)* numDivisors(n/p**k)
	# Therefore, we can reset n = n/p**k and continue, using a variable countDivisors to keep track of the factors we've pulled out.
	# NOte that we don't have to look for factors p any smaller since we've already pulled them out, so p increases (and n may decrease)
	# Hence this algorithm is faster than a brute force search.  We could make it a little faster by only considering p = 1 or 5 mod 6, but for 
	# simplicity we'll avoid this tactic 
	countDivisors =1  # keeps count of the number of divisors
	n1 = n
	p = 1
	k = 1
	while (p < int(math.sqrt(n1)) + 2) and (n1 > 1):
		p = p+1
		if (n1 % p == 0): #Then n1 is not prime, take out the largest factor p**k, update count by multiplying by k+1, and keep going
			k = 1
			while (n1 % p**(k+1) == 0):
				k = k + 1
			countDivisors = countDivisors*(k+1)
			n1 = n1/(p**k)
	if (n1 != 1): #then n1 is prime; it is a factor so we have to multiply the count by 2
		countDivisors = countDivisors*2
	return countDivisors 

				
# For testing purposes only
#print 2, '-', numDivisors(2), 6, '-', numDivisors(6), 45, '-', numDivisors(45), 119, '-', numDivisors(119), 120, '-', numDivisors(120), 17297280, '-', numDivisors(17297280)
#
#print 3, numDivisors(3), 6, numDivisors(6),    10, numDivisors(10),      15, numDivisors(15),      21, numDivisors(21),      28, numDivisors(28), 73920, numDivisors(73920)

# This algorithm uses the fact that the triangular numbers are of the form n*n+1/2.  It further uses the fact
# that n, n+1 are relatively prime and that numDivisors is multiplicative i.e. nD(ab) = nD(a)*nD(b).  The
# division by two is to divide the even number by two i.e. N = (n/2)*(n+1) or n*((2+1)/2) depending on 
# whether n or n+1 is even
n = 4 
Found = 0
prevnumDivisors = 2
currentnumDivisors = 2 # because n = 4 is even, we count number of divisors of n/2 instead
while 1: # (not (Found == 1)):
	if (n% 2 == 0):
		currentnumDivisors = numDivisors(int(n/2))
	else:
		currentnumDivisors = numDivisors(n)
	if (prevnumDivisors * currentnumDivisors < 500):
		n = n+1
		prevnumDivisors = currentnumDivisors
	else:
		print n-1, n, n*(n-1)/2, prevnumDivisors, currentnumDivisors
		#Found = 1
		break
	

print 'Time took was ',  time.clock()-t1	
