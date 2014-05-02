import math
sq = math.sqrt
floor = math.floor

#initialize vila ListToFraction(_list,0,1)
def listToFraction(_list, p, q):
	if len(_list)==0:
		return [q,p]
	v=_list.pop()
	_q=q*v+p
	_p=q
	return listToFraction(_list,_p,_q)

class _SQR_Iteration:
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
		return _SQR_Iteration(self.sqrt,new_v,new_n,new_d)
	def asList(self):
		return [int(self.v),int(self.num),int(self.denom)]

class SqRoot_ContinuedFraction:
	def __init__(self,n):
		self.n=n
		self.list=[]
		self.iterate = _SQR_Iteration(n,0,0,1)
		self.iterate = self.iterate.getNextIterate()
	def getList(self):
		return self.list
	def nextIterate(self):
		self.iterate = self.iterate.getNextIterate()
		self.list.append(self.iterate.v)
		return self.iterate
	def asFraction(self):
		_l = list(self.list)
		return listToFraction(_l,0,1)

