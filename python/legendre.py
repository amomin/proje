# Only if p is prime
# Use jacobi if p is not prime
#from http://point-at-infinity.org/ecc/Legendre_Symbol.html
def legendre(a, p):
	if a == 0: return 0
	x, y, L = a, p, 1
	while 1:
		if x > (y >> 1):
			x = y - x
			if y & 3 == 3: L = -L
		while x & 3 == 0:
			x = x >> 2
		if x & 1 == 0:
			x = x >> 1
			if y & 7 == 3 or y & 7 == 5: L = -L
		if x == 1: return L
		if x & 3 == 3 and y & 3 == 3: L = -L
		x, y = y % x, x
