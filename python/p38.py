
def isPandigital(n):
	x = [0,0,0,0,0,0,0,0,0]
	while n > 0:
		i = n % 10
		if i == 0:
			return False
		n = n/10
		x[i-1] += 1
	if 0 in x:
		return False
	else:
		return True

print isPandigital(143516789)
leader = 0

for n in range(2,6):
	flag = False
	x = 1
	while not flag:
		s = []
		for i in range(1,n+1):
			s.append(str(x*i))
		m = int(''.join(s))
#		print m
		if m > 1000000000:
			flag = True
		elif isPandigital(m) and m > leader:
			leader = m 
		x +=1
print leader
