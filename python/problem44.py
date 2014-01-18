import math
import time

N = 100000
#p = []
tstart = time.time()

#for n in range(N):
#	p.append(n*(3*n-1)/2)

#k1 = 0
#flag = False
#
#while k1 < N and not flag:
#	k1 = k1 + 1
 #	k2 = k1 + 1
#	x = p[k1]
#	x = k1*(3*k1-1)/2
#	while k2 < (x - 1)/3 and not flag:
#		y = p[k2]
#		y = k2*(3*k2 - 1)/2
#		if (((1+math.sqrt(1+24*(x+y))/6) % 1) == 0) and (((1+math.sqrt(1+24*(x+2*y)))/6 % 1) == 0) :
#		if (x + y  in p) and (x + 2*y  in p) :
#		if False and False :
#			flag = True
#		else:
#

k2 = 2
flag = False
while k2 < N and not flag:
#	k1 =  int(math.sqrt((k2**2-k2)/2))
	k1 = k2 - max(k2-20, 1)
	while k1 < k2 and not flag:
		x = k1*(3*k1-1)/2
		y = k2*(3*k2-1)/2
		if (((1+math.sqrt(1+24*(x+y)))/6 % 1) == 0) and (((1+math.sqrt(1+24*(x+2*y)))/6 % 1) == 0) :
#		if (((1+math.sqrt(1+24*(x+2*y)))/6 % 1) == 0) :
#		if (x + y  in p) and (x + 2*y  in p) :
#		if False and False :
			flag = True
			print x,y, x+y
			k1 = k1 + 1
		else:
			k1 = k1 + 1
	k2 = k2 + 1
print time.time() -tstart	
print flag
print k1, k1*(3*k1-1)/2, k2, k2*(3*k2-1)/2
#print p[k2-1], p[k1] + p[k2-1], p[k1]+ 2*p[k2-1]
