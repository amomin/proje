def irrdig(n):
	count = 0
	d = 1
	flag = False
	while not flag:
		if n < count:
			flag = True 
		else:
			count = count + 9*d*10**(d-1)
			d = d+1
	count = count - 9*(d-1)*10**(d-2)	
	d = d-1
	x = str(10**(d-1)  + (n - count-1)/d)
	d = len(x)
#	return d, count, x, ((n - count-1)  % d), x[((n - count-1)  % d)]
	return   x[((n - count-1)  % d)]

	
#print 10, irrdig(10), 11, irrdig(11), 12, irrdig(12), 188, irrdig(188), 189, irrdig(189), 190, irrdig(190)

count = 1
for i in range(0,7):
	print i
	count = count * int(irrdig(10**i))

print count
