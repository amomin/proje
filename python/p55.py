import math

def listify(n):
 	m = n
	# Converts a number n into a list of its digits
	# The largest digit appears at the front of the list
	if m == 0:
		return [0]
	digitList = []
#	numDigits = int(math.log(n,10)) # gives  the numer of digits in n
#	for digit in range(numDigits):
	while m > 0:
		digitList.insert(0,(m%10))
		m /= 10
	return digitList

def intify(digitList):
	# Converts a digit list to a base 10 integer
	lenList = len(digitList)
	n = 0
	for digit in range(lenList):
		n = n + digitList[digit]*(10**(lenList-digit-1))
	return n

def reverse(digitList):
#`	returns the digitList in reverse order (which should be the number in reverse 
	x = []
	x.extend(digitList)
	y = []
	while x != []:
		y.append(x.pop())
	return y

def isPalindrome(dL): #Determine whether i is a palindrom
	a = dL
	b = reverse(a)
	if dL == b:
		return True
	else:
		return False

def listSum(dL1, dL2):
	#Sums two digit lists together
	# Cheap trick to convert to integer and then add - ideally you should do this at the level of lists
	n1 = intify(dL1)
	n2 = intify(dL2)
	return listify(n1+n2)

N = 10000 # Test for Lychrel numbers below N
count = 0 # Count of Lychrel numbers so far
for i in range(1,N):
	# Test whether i is Lychrel
	isLychrel = True
	j = 1 
	x = listify(i)
	# Test the first 50 iterations for palindromes
	while isLychrel and j < 50:
		temp = listSum(x, reverse(x))
		x = temp
		isLychrel = (not (x == reverse(x)))
		j += 1
	if isLychrel: #then count it
		print i
		count += 1

print "Number of Lychrel numbers less than N is"
print count	
