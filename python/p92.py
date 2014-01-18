# See also the very fast solution by jackdied (not this solution)
# which uses creates a list of all the possible sums of squres of digits
# counts the number of x's < 10000000 which produce that square sum
# and then checks if that yields 89
# and then adds that count to the total count if so (???)

def findEnd(n):
	# determines if n ends at 1 or 89
	while n != 1 and n!=89:
		answer = 0
		while n > 0:
			answer += (n%10)**2
			n/=10
		n = answer
	return n

#for x in range(1,100):
#	print x, findEnd(x)

#count = 0
#x = 100
#L = [0,1]
#for i in range(2,100):
#	if findEnd(i) == 89:
#		count+=1
#		L.append(89)
#	else:
#		L.append(1)
#while x < 10000000:
#	n = x
#	answer = 0
#	while n > 0:
#		answer += (n%10)**2
#		n/=10
#	n = answer
#	if L[n] == 89:
#		count+=1
#		L.append(89)
#	else:
#		L.append(1)
#	x+=1
#print count

# Brute force
import time
t1 = time.time()
x = 2
count = 0
L = [0,1]
while x<570:
	if findEnd(x) == 89:
		L.append(89)
		count+=1
	else:
		L.append(1)
	x+=1
def sumsqdigits(n): # compute the sum of the squares of the digits of n
	answer = 0
	while n>0:
		answer+=(n%10)**2
		n/=10
	return answer

while x < 10000000:
	if L[sumsqdigits(x)] == 89:
		count+=1
	x+=1
	
print count
print time.time() - t1

# YOu can improve run time as follows.  It's easy to deduce that for each number < 10000000 the sum of squares will be at most 9^2*7<570
# So you can compute the answer up to 570 first.  Then, later, you need only compute the sum of the squares of the digits and then compare.
