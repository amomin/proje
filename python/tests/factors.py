import math,sys, time
sys.path.insert(0,'../lib')
from NumberTheory import factor

for i in range(1,1000):
	print "Factorize ",i,factor(i)
