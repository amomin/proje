import math,sys,time
import itertools

ops = ['+','-','*','/' ]

def compute (a,b,c):
	if c == '+':
		return a + b
	if c == '-':
		return a - b
	if c == '*':
		return a * b
	if c == '/':
		if b != 0:
			return a / b
		else:
			return False

def isInt(x):
	return abs(x - int(x)) < 0.000001


def do(a,b,c,d):
	_list=[]
	for x in itertools.permutations([float(a),float(b),float(c),float(d)],4):
		#print x
		for y in itertools.product(ops,ops,ops):
			#comp 1: (a_b)_c)_d
			a1=compute(x[0],x[1],y[0])
			if a1 != False:
				a2=compute(a1,x[2],y[1])
			else:
				a2=False
			if a2 != False:
				a3=compute(a2,x[3],y[2])
			else: 
				a3=False
			if a3!= False and isInt(a3):
				_list.append(int(a3))
			#print x,y, a3
			#comp 2: (a_b)_(c_d)
			a1=compute(x[0],x[1],y[0])
			a2=compute(x[2],x[3],y[1])
			if a1 != False and a2!=False: a3=compute(a1,a2,y[2])
			else: a3=False
			if a3!=False and isInt(a3):
				_list.append(int(a3))
			#print x,y, a3

	_list = filter(lambda(x): True if x>0 else False, _list)
	_list.sort()

	_ans=[False]*101
	for i in range(1,100):
		if i in _list:
			_ans[i]=True
	skip=0
	for i in range(1,100):
		if not _ans[i]:
			skip = i
			break
	print "This list ",[a,b,c,d]," skips at ",skip
	_st = set(_list)
	print _st
	return skip

curr_max = 0
curr_champ=[]
for a in range(1,7):
	for b in range(a+1,8):
		for c in range(b+1,9):
			for d in range(c+1,10):
				skipped = do(a,b,c,d)
				if skipped>curr_max:
					curr_max=skipped
					curr_champ = [a,b,c,d]
print "Champ is ", curr_champ, "with skip of",curr_max


