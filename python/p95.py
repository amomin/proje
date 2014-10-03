import math,sys, time
sys.path.insert(0,'./lib')
from NumberTheory import factor, sumProperDivisors

# Print the orbit
ORBITMAX=10**6
MIN=5
MAX=ORBITMAX

_tocheck = range(MIN,MAX)
max_len=0
min_elt=MAX
_record=[]
for d in _tocheck:
	if (d%10000==0):
		print "At d = ",d
	x = sumProperDivisors(d)
	orbit=[]
	_len=0
	while x not in orbit and x<ORBITMAX:
		orbit.append(x)
		x = sumProperDivisors(x)
		_len+=1
	
	#if x>=ORBITMAX:
		#print "Chain Exceeded orbital max of ", ORBITMAX
	if d in orbit:
		#print "Found an orbit chain of length", _len, orbit
		if _len>max_len:
			_min=min(orbit)
			print "New longest orbit with min elt found of length",_len,"min elt",_min,orbit
			max_len=_len
			min_elt=_min
			_record=orbit
	#print "Orbit of d ",d," is ",orbit

print "Record is length",max_len,"for orbit with minimum value",min_elt
print "Here is the orbit:"
print _record
