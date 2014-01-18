import time
t1 = time.time()

Nmax = 23000

def isInc(n): # determine if n is increasing
	prevdigit = 11
	while n > 0:
		if (n%10) > prevdigit:
			return False
		else:
			prevdigit = (n%10)
			n /= 10
	return True

def isDec(n): # determine if n is decreasing
	prevdigit = -1
	while n > 0:
		if (n%10) < prevdigit:
			return False
		else:
			prevdigit = (n%10)
			n /= 10
	return True
numbouncy = 0
flag = True
x = 99
#for x in range(99,Nmax):
while flag:
	if (not isInc(x)) and (not isDec(x)):
		numbouncy+=1
#		print x
	if (1.0*numbouncy)/(1.0*x) >= .99 and flag:
		print x, numbouncy
		flag = False
	x+=1

#print Nmax, numbouncy, (1.0*numbouncy)/(1.0*Nmax)
print x, numbouncy, (1.0*numbouncy)/(1.0*x)
#print isDec(3), isDec(13), isDec(31), isDec(1357), isDec(642), isDec(1546)

print time.time() - t1
