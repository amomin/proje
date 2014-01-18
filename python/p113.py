import time
t1 = time.time()
X = 100
N = X  + 1
K = 10

p = [[0]*(N+1),[1]*(N+1)]

L = []
for k in range(2,K+1):
	L = [1] #p(k,0) = 1
	for n in range(1,N+1):
		count = 0
		for j in range(0,n):
			count += p[k-1][n-j]
		L.append(count)
	p.append(L)


#print p[10][3]-1
#print p[9][3]

#for x in p:
#	print x	

count1=0
for n in range(0,N+1):
	count1 += p[10][n]-1
print "number of decreasing numbers less than a googol"
count1 = count1
print count1

count2 = 0
for n in range(0,N+1):
	count2 += p[9][n]
print "number of increasing numbers less than a googol"
count2 = count2 -2
print count2 

print "number of increasing and decreasing numbers less than X"
count3 = 9*(X)
print count3

print "Total"
print count1 + count2-count3

print "Time"
print time.time() - t1
