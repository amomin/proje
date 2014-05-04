import math, sys, time
import MillerTest

# Consider taking products of numbers instead of factorizing and then finding all divisors

MAX = 12000

prime_list = []
for i in range(2,120):
	if MillerTest.MillerRabin(i):
		prime_list.append(i)

print prime_list

def factorList(n):
	_list = []
	for i in prime_list:
		while n % i == 0:
			_list.append(i)
			n = n/i
		if n == 1:
			break
	if n > 1:
		_list.append(n)
	return _list
# This is WAAAY too inefficient e.g. on powers of 2
def factorizations(divisors,_flist):
	if len(_flist)==0:
		return [divisors]
	result = []
	for i in range(0,len(_flist)):
		_f = list(_flist)
		_d = list(divisors)
		x = _f.pop(i)
		_d.append(x)
		_y = factorizations(_d,_f)
		assert isinstance (_y, list)
		result.extend(_y)
	for j in range(0,len(divisors)):
		for i in range(0,len(_flist)):
			_f = list(_flist)
			_d = list(divisors)
			x = _f.pop(i)
			y = _d.pop(j)
			_d.insert(j,x*y)
			_res = factorizations(_d,_f)
			assert isinstance(_res,list)
			result.extend(_res)
	return result
			
for i in range(2,MAX):
	x = factorList(i)
	print "NUmber ",i," has factors ",x
	#y = factorizations([],x)
	#print "NUmber ",i," has factorizations ",y

