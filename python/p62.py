from collections import defaultdict

#L = [1,2,45,55,5,4,4,4,4,4,4,5456,56,6,7,67]
#d = defaultdict(int)
#for i in L:
#    d[i] += 1
#result = max(d.iteritems(), key=lambda x: x[1])
#print result

#L = [1,2,45,55,5,4,4,4,4,4,4,5456,56,6,7,67]
def maxoccur(L):
	dlist = defaultdict(int)
	for x in L:
   		dlist[x] = dlist.get(x, 0) + 1
	return max(dlist.iteritems(), key=lambda x: x[1])

def makeDigitList(n):
	L = [0,0,0,0,0,0,0,0,0,0]
	while n > 0:
		L[n % 10] += 1
		n /= 10
	return L
def makeDigitNum(n):
	retans = 0
	while n>0:
		retans += 10**(n%10)
		n /= 10
	return retans

print 1532432532, makeDigitNum(1532432532)

L = []
for n in range(10,8386):
	if makeDigitNum(n*n*n) == 1111212111:
		print n, n*n*n
	L.append(makeDigitNum(n*n*n))

print maxoccur(L)
