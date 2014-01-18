import time
import math
t0 = time.clock()
pi = math.pi
e = math.e
count = 0
N =100
#def Ster(a):
#	return math.sqrt(2*pi*a) * math.exp(math.log(a/e) * a)
#print Ster(10), Ster(9)#, Ster(243)

def cnr(a,b):
	return math.factorial(a)/(math.factorial(a-b) * math.factorial(b))
#print cnr(95,33), cnr(52,25)

answerList = []
nocount = 0
yescount = 0
for n in range(1,N+1):
	rowcount = 0
	r=0
	while cnr(n,r) < 1000000 and r < (n)/2+.1:
		if (n % 2 == 0) and r == (n)/2:
			rowcount +=1
		else:
			rowcount += 2
#		if cnr(n,r) not in answerList:
#			answerList.append(cnr(n,r))
		r = r+1
	yescount += n+1-rowcount
	nocount += rowcount
ttl = 0
for n in range(1,N+1):
#	print n
	ttl = ttl + n+1
print yescount, nocount, ttl, time.clock() - t0

print cnr(23,10)
