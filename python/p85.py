import math, time
t1 = time.time()
sqrt = math.sqrt

def f(m,n):
	return n*(n+1)*m*(m+1)/4

for n in range(1,6):
	for m in range(1,6):
		print n,m,f(n,m)

closest = 100000000
minpair = [0,0]
m = 0
n = 1
while n < 2000:
	m = int((-1+sqrt(1+32000000/(n*(n+1))))/2)
	if (abs(f(n,m)-2000000) < closest) or (abs(f(n,m+1)-2000000) < closest):
		closest = min(abs(f(n,m)-2000000),abs(f(n,m+1)-2000000))
		minpair = [m,n]
	n+=1

print minpair, closest, f(minpair[0],minpair[1]), f(minpair[0]+1,minpair[1])
print minpair, minpair[0]*minpair[1], (minpair[0]+1)*minpair[1]

