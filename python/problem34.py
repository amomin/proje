def fac(n):
	x = 1
	for i in range(2,n+1):
		x = i*x
	return x

def digitList(n):
	returnlist = []
	while n != 0:
		returnlist.insert(0,n % 10)
		n = n/10
	return returnlist

def listfacsum(L):
	c = 0
	for x in L:
		c = c + fac(x)
	return c



for n in range(10,20000001):
	if n == listfacsum(digitList(n)):
		print n
