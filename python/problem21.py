from math import sqrt

def sumdivisors(n):
	# Finds the sum of the proper divisors of n
	runningsum = 1
	a = 2
	while (a < sqrt(n) + 1):
		if (n % a == 0):
			runningsum = runningsum + a + n/a
		a = a +1
	return runningsum

print sumdivisors(30), sumdivisors(15), sumdivisors(16)

num = 0
x = 1
while (x < 10001):
	n = sumdivisors(x)
	if (n < 10001):
		if (x == sumdivisors(n)) and (x !=n):
			print x, n
			num = num+x
	x = x +1

print num
