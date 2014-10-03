import math

MIN=1
MAX =MIN+10**7


#SOlutions are pythagorean triples (x,x+1,z)

n=MIN
while n<MAX:
	M = n+int(math.floor(math.sqrt(2*n*n-1/4)))
	for m in range(M-2,M+2):
		if abs(m**2-n**2-2*m*n)<2:
			x=max(m**2-n**2, 2*m*n)
			total = m**2+n**2  + 1
			if total>10**12:
				print "Number of blue discs is ",x," Total is",total
				odds = (float(x)/float(total))*(float(x-1)/float(total-1))
				print "The odds are ", odds
	n+=1
