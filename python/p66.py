import math
import sys
sys.path.insert(0,'./lib')
from ContinuedFraction import *

def notSquare(n):
	if n == int(math.sqrt(n))**2:
		return False
	else:
		return True

#_tests = [2,3,12,23]
N=1001
max_x=0
max_D=0
_tests = filter(notSquare, range(1,N))
for n in _tests:
	cf = SqRoot_ContinuedFraction(n)
	cf.nextIterate()
	_found=False	
	while not _found:	
		cf.nextIterate()
		frac = cf.asFraction()
		x = frac[0]
		y = frac[1]
		r = x*x - n*y*y
		if r==1:
			_found=True
			print "D,x,y: ", n,x,y
			if x > max_x:
				max_x=x
				max_D=n

print "Max found D is ",max_D," with x value of ",max_x
