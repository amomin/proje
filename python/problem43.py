import itertools

digitList = [0,1,2,3,4,5,6,7,8,9]
p = [2,3,5,7,11,13,17]

runtotal = 0
for x in itertools.permutations(digitList):
	n = []
	flag = True
	for i in range(0,7):
		n.append(100*x[i+1] + 10*x[i+2] + x[i+3])
		if (100*x[i+1] + 10*x[i+2] + x[i+3]) % p[i] != 0:
			flag = False
	if flag:
		temp = 0
		for i in range(0,10):
			temp = temp + 10**(9-i) * x[i]
		runtotal = runtotal + temp

print runtotal
