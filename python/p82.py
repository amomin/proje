#M = [[131, 673,	234, 103, 18],
#[201,96,342,965,150],
#[630,803,746,422,111],
#[537,699,497,121, 956],
#[805,732,524,37, 331]]
#L = [[131, 673,	234, 103, 18],
#[201,96,342,965,150],
#[630,803,746,422,111],
#[537,699,497,121, 956],
#[805,732,524,37, 331]]

import time
t1 = time.time()

f = open("matrix.txt",'r')
M = []
for x in f.readlines():
	M.append(map( int, x.split(',') ))
f.close()
f = open("matrix.txt",'r')
L = []
for x in f.readlines():
	L.append(map( int, x.split(',') ))
f.close()

toobigtofail = 100000000
N = len(M)
#for i in range(0,len(M)):
#	tempsum = 0
#	for k in range(i,len(M)):
#		tempsum+= M[k][len(M)-1]
#	M[i][len(M)-1] = tempsum

for j in range(N-2,-1,-1):
	for i in range(N-1,-1,-1):
		minsum = toobigtofail
		tempsum = 0
		for k in range(0,N):
			if k < i:
				tempsum = L[k][j+1]
				for l in range(k,i+1):
					tempsum += M[l][j]
				if tempsum < minsum:
					minsum = tempsum
			else: # k >= i:
				tempsum = L[k][j+1]
				for l in range(i,k+1):
					tempsum += M[l][j]
				if tempsum < minsum:
					minsum = tempsum
		L[i][j] = minsum

#for x in M:
#	print x
#for x in L:
#	print x

minans = toobigtofail
for i in range(0,N):
	if L[i][0] < minans:
		minans = L[i][0]

print minans
print time.time()-t1			
			

