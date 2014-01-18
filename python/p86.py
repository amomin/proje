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

def check(l1,a):
# Checks if the shortest path length for the cube of lenghts l1,l2,l3 is an integer (True if it is)
# Note that this quantity is always the value x given below
	x = math.sqrt(l1**2 + (a)**2)
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
while count < 1000000:#M < maxcheck + 1:
#	count = 0
	l1 = M
	for a in range(1,2*l1):
		if check(l1,a):
			count = count + a/2 - max(a-l1,1) + 1
	if (M % 100) == 0 or (M > 1800):
		print M, count
	M = M+1


print M, count
print time.clock() - t0
