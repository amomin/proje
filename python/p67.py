f = open('triangle.txt')

L = f.readlines()
L2 = []

for x in L:
#	print x
	y = x
	yout = []
	while y != '\n':
#		print y[0:2]
		yout.append(int(y[0:2]))
		y = y[3:]
	L2.append(yout)

#for i in range(len(L2)-1):
#	for j in range(i+1):
#		print L2[i][j]
#	print len(x)
#print len(L)
N = len(L2)-1
for i in range(1,N+1):
	x=L2[N-i]
	L2[N-i] = []
	for j in range(len(x)):
		x[j] += max(L2[N+1-i][j],L2[N+1-i][j+1])
	L2[N-i] = x

print L2[0][0], L2[1][0], L2[1][1]
