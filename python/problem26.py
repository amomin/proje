def repFraction(d):
	# returns a list representing the decimal expansion of 1/d
	r_0 = 1
	k = 1
	digitList = []
	remainderList = [1]
	doRepeat = 1
	while (doRepeat == 1):
		while (d > r_0*10**k):
			k = k+1
			digitList.append(0)
			remainderList.append('s')
		# Now d <= r_0*10^^k
		x = r_0*10**k/d
		rem = r_0*10**k - x*d
		if (rem == 0):
			doRepeat = 0
			digitList.append(x)
			remainderList.append(rem)
			return digitList, remainderList
		elif (rem in remainderList):
			doRepeat = 0
			digitList.append(x)
			digitList.append('r')
			remainderList.append(rem)
			return digitList, remainderList
		else:
			digitList.append(x)
			remainderList.append(rem)
			r_0 = rem
			k = 1

def lenRepeat(z):
	lengthList = []
#	z = repFraction(i)
	z0 = z[0]
	z1 = z[1]
	count = 0
	if z0.pop() != 'r':
#		lengthList.append(count)
		return 0
	else:
		lastRem = z1.pop()
		count = 1
		while z1.pop() != lastRem:
			count = count+1
		return count
#		lengthList.append(count)




x = []
for i in range(2,1000):
	x= repFraction(i)
#	print x
	if lenRepeat(x) == 982:
		print i	

