f = open('roman.txt','r')
L = []
for x in f.readlines():
    L.append(x)
f.close()
print len(L)

count = 0
for x in L:
	if 'CCCC' in x:
		if 'DCCCC' in x:
			count += 3
		else:
			count+=2
	if 'XXXX' in x:
		if 'LXXXX' in x:
			count+=3
		else:
			count +=2
	if 'IIII' in x:
		if 'VIIII' in x:
			count +=3
		else:
			count+=2
	print x

print count
