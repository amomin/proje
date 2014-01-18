# Compute partitions mod 10**6:
# Use recursion:
# p(k,n) =  p(k+1,n) + p(k,n-k)
# and p(k,n) = 0 if k > n
# p(k,n) = 1 if k = n
# Should be doable to calculate p(n) up to about 1000 this way (matrix size is N**2).
# Might be better (space + time effective) to use coordinates n+k,n-k instead since p(1,N) is what w
# we are after and it never uses p(k,n) for n+k > N
# Note:  p[i][j] = p(j,i)
N = 2000
modulus = 10**6
p = [[], [0,1]] # p(1,1) = 1, p(0,1) = 0

for i in range(2,N):
	L = [] #p(i,i)
	j = i
	while 2*j > i:
		L.insert(0,1)
		j-=1
	while j > 0:
		L.insert(0,((L[0] + p[i-j][j]) % modulus))
#		L.insert(0,(L[0] + p[i-j][j]))
		j-=1
	L.insert(0,0)
#	for j in range(i-1,0,-1):
#		#p[i][j] = p[i][j+1] + p[i-j][j]
#		#p[j+1][i] = L[0]
#		if j > i-j:
#			L.insert(0,L[0])
#		else:
#			L.insert(0,((L[0] + p[i-j][j]) % modulus))
#	L.insert(0,0) #p(0,anthing) = 0
	if (L[1] % 1000) == 0:
		if (L[1] % 10000) == 0:
			if L[1] == 0:
				print i,L[1]
				print "This is an answer!"
			print i,L[1]
		print i,L[1]
	p.append(L)

#for x in p:
#	print x

for i in range(1,N):
	if p[i][1] == 0:
		print i,p[i][1]
