import time,math,decimal

sq = math.sqrt
ln = math.log

def get100digits(m):
#	return int((sq(m)-int(sq(m)))*10**(100))
#	offset = int(ln(10,sq(m)))
#	return int(sq(m)*10**(99-offset))
	return int(Decimal(m).sqrt()*10**(99))

def getdigitsum(n):
	count = 0
	while n > 0:
		count += (n%10)
		n/=10
	return count

for n in range(2,20):
	print n, get100digits(n), getdigitsum(get100digits(n))
	print n, getdigitsum(n)
#total = 0
#for n in range(2,100):
#	if abs(sq(n) - int(sq(n))) < 0.000001:
#		total += getdigitsum(get100digits(n))
#
#print total
