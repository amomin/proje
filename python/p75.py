#USe the fact that pythagorean triples are generated by squares:
#
# m = a^2-b^2,
# n = 2ab
# p = a^2 + b^2
#
# m^2 +n^2 = p^2
#
# (and all pythagorean triples arise uniquely this way).
# m+n+p = 2a^2+2ab = 2a(a+b), and b < a
# so m+n+p < 4a^2, also
# m+n+p > 2a^2, which is what bounds our loop.

import math,time
t1 = time.time()

Lmax = 1500000
a = 2

def gcd(p1,p2):
	if (p2%p1) == 0:
		return p1
	else:
		return gcd((p2 % p1),p1)

L=[0]
for x in range(Lmax):
	L.append(0)

while a < int(math.sqrt(Lmax/2)):
	b=1
	while (b<a) and( 2*a*(a+b) <= Lmax):
		Labc = 2*a*(a+b)
		if (gcd(b,a) == 1) and ((b-a)%2)==1:
			k = 1
			while k*Labc < Lmax:
				L[k*Labc]+=1
				k+=1
		b+=1
	a+=1

#for x in range(len(L)):
#	print x, L[x]

count = 0
for x in range(len(L)):
	if L[x] == 1:
		count+=1

print count
print time.time()-t1
