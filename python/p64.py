import math
sq = math.sqrt
floor = math.floor

class Iteration:
	# assume it has the form val + (sqrt - n)/d
	def __init__(self,_s,_v,_n,_d):
		self.sqrt = _s
		self.v = _v
		self.num = _n
		self.denom = _d
	def getNextIterate(self):
		new_v = int(floor ( self.denom/(sq(self.sqrt) - self.num) ) )
		new_d = int ((self.sqrt - self.num**2)/self.denom)
		new_n = int (new_v*new_d - self.num)
		return Iteration(self.sqrt,new_v,new_n,new_d)
	def asList(self):
		return [int(self.v),int(self.num),int(self.denom)]

def getPeriod(n):
	_list = []
	x = Iteration(n,0,0,1)
	while (not (x.getNextIterate().asList() in _list) ):
		x = x.getNextIterate()
		_list.append( [x.v,x.num,x.denom])
	_l = x.getNextIterate().asList()
	matches = [i for i,_x in enumerate(_list) if _x==_l]
	match = matches[0]
	length = len(_list)
	return length-match

def isSquare(n):
	k = int(sq(n))
	if k*k==n:
		return True
	else:
		return False

period=0
count=0
period = getPeriod(14)
for i in range(1,10001):
	if not isSquare(i):
		period = getPeriod(i)
		if (period % 2 == 1):
			count += 1

print "COunt is ", count
