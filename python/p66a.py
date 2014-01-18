
import math
maxtocheck = 1000

def isSq(n):
	if n == int(math.sqrt(n))**2:
		return True
	else:
		return False

DList = []
for j in range(0,maxtocheck+1):
	DList.append(0)
DList[0]=1
DList[1]=1
DList[2]=1
DList[3]=1

numcheckedoff = 3

largestD = 3
x = 1
while numcheckedoff < maxtocheck:
	D = 3
	while (D<maxtocheck+1) and (D < x**2 -1):
		if isSq((x**2-1.0)/(D*1.0)):
			if DList[D] == 0:
				DList[D] = 1
				numcheckedoff+=1
				largestD=D
				print x,D,math.sqrt((x**2-1)/D), numcheckedoff
		D+=1
	x+=1
	if (x%100000) == 0:
		print x, numcheckedoff

print x
