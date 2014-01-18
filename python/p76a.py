import time
t1 = time.time()
N = 102
#This time code it storing the values in a matrix
L = []
x = []
for i in range(N):
	L.append([])
	for j in range(N):
		L[i].append(0)

#for x in L:
#	print x
M = []
for i in range(1,N):
	x = L[i]
	for j in range(0,N):
		if j ==1 or j == 0:
			x[j] = 1
		elif i == 1:
			x[j] = 1
		elif j > i:
			x[j] = x[i]
		else:
			answer = 0
			for k in range(1,j+1):
				answer += L[i-k][k]
			x[j] = answer
	M.append(x)
	x =[]
		
#for y in M:
#	print y
#for i in range(N-1):
#	print i, M[i][i]-1
print M[100][100]-1
print time.time()-t1

