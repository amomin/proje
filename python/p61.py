# only need to check the octagonal numbers from 19 to 58
import math

def getPoly(symbol,i):
	if symbol==3:
		return i*(i+1)/2
	if symbol==4:
		return i*i
	if symbol==5:
		return i*(3*i-1)/2
	if symbol==6:
		return i*(2*i-1)
	if symbol==7:
		return i*(5*i-3)/2
	if symbol==8:
		return i*(3*i-2)

def inRange(f,x): 
	if (x>1000 and x<10000):
		return True
	else:
		return False

# Could compute once and forall but this program is quick enough as is
def getList(symbol):
	f = lambda(x):getPoly(symbol,x)
	g = lambda(x):inRange(f,x)
	x = range(20,200)
	return filter (g, map(f,range(20,200)))

# Recursively go through (remaining) polygonal number lists, if match found
# remove that list, add number to proposed solution set, and continue
# curr is just sofar.last() and numinlist is just len(left)
def solve(curr, sofar, left, numinlist):
	if numinlist==6:
		if sofar[0]/100 == sofar[numinlist-1] %100:
			return sofar
		else: 
			return False
	for t in left:
		_list = getList(t)
		for x in _list:
			if (x/100 == curr%100):
				newlist = list(sofar)
				newlist.append(x)
				newleft = list(left)
				newleft.remove(t)
				result = solve(x, newlist,newleft,numinlist+1)
				if result!=False:
					return result
	return False

_left = [7,6,5,4,3]
octs = getList(8)

for i in octs:
	result = solve(i,[i],_left,1)
	if result!=False:
		_sum=0
		for x in result:
			_sum+=x
		print "Sum is",_sum
		break
