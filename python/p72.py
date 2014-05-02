import math,sys,time
sys.path.insert(0,'./lib')
from NumberTheory import *

t1 = time.time()
N = 1000001
count = 0
for i in range(2,N):
	x = phi(i)
	#print "Totient of ",i," is ", x
	count += x

print "Sum up to ",N, " is ", count
t2 = time.time()
print "Time took is", t2-t1
