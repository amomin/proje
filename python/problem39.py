maxnumsolns = 0
maxnum = 3

def numsolns(p):
# x < y < p - x - y are supposed to be the sides of a triangle
# we count the number of right angled triangles of perimeter p and integer side lengths
	count = 0
	for x in range(1,p/3):
		for y in range(max(x+1,(p-2*x)/2),(p-x)/2):
			if x**2 + y**2 == (p-x-y)**2:
				count = count+ 1
#				print x,y,p-x-y
	return count

print 120, numsolns(120)
	
for p in range(1001):
	temp = numsolns(p)
	if temp > maxnumsolns:
		maxnumsolns = temp
		maxnum = p

print maxnum, maxnumsolns
