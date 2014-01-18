# Remark: this problem can and probably should be done using Dijkstra's algorithm.  

import time
t1 = time.time()
#M = [[131, 673,234, 103, 18],
#[201,96,342,965,150],
#[630,803,746,422,111],
#[537,699,497,121, 956],
#[805,732,524,37, 331]]
#L = [[131, 673,	234, 103, 18],
#[201,96,342,965,150],
#[630,803,746,422,111],
#[537,699,497,121, 956],
#[805,732,524,37, 331]]


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
# Figure out the answer allowing only down moves
for j in range(N-1,-1,-1):
	for i in range(N-1,-1,-1):
		candidateList = []
		if j<N-1:
			candidateList.append(M[i][j] + L[i][j+1])
		if i<N-1:
			candidateList.append(M[i][j] + L[i+1][j])
		if candidateList != []:
			L[i][j] = min(candidateList)
#		else:
#			L[i][j] = M[i][j]
	
for x in M:
	print x
for x in L:
	print x
# Now allow some up,left,right,down moves
flag = False
while not flag:
	flag = True
	for i in range(0,N):
		for j in range(0,N):
			candidateList = []
			if i>0:
				candidateList.append(M[i][j]+L[i-1][j])
			if i < N-1:
				candidateList.append(M[i][j]+L[i+1][j])
			if j>0:
				candidateList.append(M[i][j]+L[i][j-1])
			if j < N-1:
				candidateList.append(M[i][j]+L[i][j+1])
#			print L[i][j], candidateList
			if min(candidateList) < L[i][j]:
				L[i][j] = min(candidateList)
				flag = False
#	for x in L:
#		print x
#	time.sleep(1)	

#for x in L:
#	print x
print L[0][0]
print time.time() - t1
