import time
import math

t0 = time.clock()

maxcheck = 100
def isInt(x):
# determines if a real number (float) x is an integer
	if x % 1 == 0:
		return True
	else:
		return False

def check(l1,l2,l3):
# Checks if the shortest path length for the cube of lenghts l1,l2,l3 is an integer (True if it is)
# Note that this quantity is always the value x given below
	x = math.sqrt(l1**2 + (l2 + l3)**2)
	if not isInt(x):
		return False
	else:
		return True
#		x = int(x)
#		if ((l2*x + l3*x) % (l2+l3)) == 0:
#			return True
#		else:
#			return False
M = 1
count = 0
while count < 1000000: #M < maxcheck + 1:
#	count = 0
	l1 = M
	for l2 in range(1,l1+1):
		for l3 in range(1,l2+1):
			if check(l1,l2,l3):
				count = count + 1
	if (M % 100) == 0:
		print M, count
	M = M+1


print M, count
print time.clock() - t0
