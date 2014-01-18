import math
def ltd_add(a,b):
	# takes two numbers and adds them together, returning only the last 10 digits.
	return (a % 10**10) + (b % 10**10) % 10

#print ltd_add(1234567898765, 54323454323432123)

def ltd_mult(a,b):
	return (a% 10**10) * (b % 10**10) % 10**10

#print ltd_mult(123456789908736482364, 38739249832749234923792)
#print 123456789908736482364 * 38739249832749234923792

def ltd_power(a,n):
	if n == 1:
		return a % 10**10
	else:
		k = int(math.log(n)/math.log(2))
		return ltd_mult(ltd_power(a,k), ltd_power(a,n-k)) % 10**10

#for n in range(1,9):
#	print ltd_power(2,n)
#	print ltd_power(3,n)

count = 0
for n in range(1,1001):
	count = (count + ltd_power(n,n)) % 10**10

print count
