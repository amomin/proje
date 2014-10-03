import math, time, sys
sys.path.insert(0,'./lib')
from NumberTheory import gcd
ceil=math.ceil
floor=math.floor

SIZE=50

def relPrime(x1,y1):
	g = gcd(x1,y1)
	return [x1/g, y1/g]

def lowBound(x1,y1):
	[x,y] = relPrime(x1,y1)
	lo1 = float(x1-SIZE)/float(y)
	lo2 = float(-y1)/float(x)
	lo = max(int(ceil(lo1)),int(ceil(lo2)))
	return lo
def upBound(x1,y1):
	[x,y] = relPrime(x1,y1)
	hi1 = float(SIZE-y1)/float(x)
	hi2 = float(x1)/float(y)
	hi = min(int(floor(hi1)),int(floor(hi2)))
	return hi

count = 0
for x1 in range(1,SIZE+1):
	for y1 in range(1,SIZE+1):
		lo = lowBound(x1,y1)
		hi = upBound(x1,y1)
		if hi>lo:
			count += (hi-lo)

print "COunted ", count, "triangles with a right angle at an interior point"
print "There are ",2*SIZE*SIZE, " triangles with a right angle at an edge point"
print "There are ",SIZE*SIZE," triangles with a right angle at O"
print "TOtal is ", 3*SIZE*SIZE + count
