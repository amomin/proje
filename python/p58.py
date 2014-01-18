import math

log = math.log

n =1
p=3
q=2

count = 0
while n<1000:
	n+=1
	q = p+q
	p = 2*q - p
#	print p,q, p/q
	if int(log(p,10)) - int(log(q,10)):
#		print p,q
		count +=1

print count
