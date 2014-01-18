import math
f = open('base_exp.txt')

L = []
#for line in f.readlines()
#	L.append(line)
L = f.readlines()

f.close()

#print L
#for x in L:
#	print x

M = []
for x in L:
	b=int(x[:x.find(',')])
	e=int(x[x.find(',')+1:])
	M.append([b,e])
#print M

maxsofar = 0
maxpair = [0,0]
maxindex = 0
for i in range(len(M)):
	e = M[i][1]
	b = M[i][0]
	if e*math.log(b) > maxsofar:
		maxsofar = e*math.log(b)
		maxpair = [b,e]	
		maxindex = i

print maxindex, maxpair, M[maxindex]
