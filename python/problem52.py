import time
t0 = time.clock()

def getdiglist(n):
	anslist = []
	while n > 0:
		anslist.append(n % 10)
		n = n / 10
	anslist.sort()
	return anslist

i = 1
found = False
answer = 0
while not found:
	x = 10**i
	while x < 10**(i+1)/6 and not found:
		dList = getdiglist(x)
		found = True
		p = 2
		while p < 7 and found:
			if not getdiglist(p*x) == dList:
				found = False
			p = p + 1
			if found and p ==7:
				print x
				answer = x
		x = x+1
	i = i+1

print answer, 2*answer, 3*answer,4*answer, 5*answer, 6*answer
print time.clock() - t0
