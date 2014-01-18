import time

t1 = time.time()
def l10dpower2(n):
	#Return the last 10 digits of 2^n
	x = 0
	if n == 0:
		return 1 
	if (n%2) == 1:
		return (2* l10dpower2(n-1)) % (10**10)
	else:
		x = l10dpower2(n/2)
		return (x*x) % (10**10)

print (28433*l10dpower2(7830457) + 1 )% (10**10)
print time.time() - t1
#for l in range(300):
#	print l, l10dpower2(l)
