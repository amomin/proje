import math,sys, time
sys.path.insert(0,'../lib')
from NumberTheory import sumProperDivisors

for d in range(1,30):
	print "Sum of divisors of d ",d,sumProperDivisors(d)
