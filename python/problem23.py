from math import sqrt

#N = 2800 
N = 28123

def isSquare(n):
	if int(sqrt(n))*int(sqrt(n)) == n:
		return 1
	return 0

def sumdivisors(n):
	# Finds the sum of the proper divisors of n
	runningsum = 1
	a = 2
	if n == 1:
		return 1
	while (a < sqrt(n)):
		if (n % a == 0):
			runningsum = runningsum + a + n/a
		a = a +1
	if isSquare(n):
		runningsum = runningsum + int(sqrt(n))
	return runningsum

def isAbundant(n):
	# Determines if a positive integer n is abundant, meaning
	# that the sum of its proper divisors exceeds n
	# Example: 12 is abundant because 1+2+3+4+6 = 16 > 12, but
	# Counterexample: 8 is not because 1:2:4 = 7 < 8
	return (n < sumdivisors(n))

#print isAbundant(1), isAbundant(2), isAbundant(8), isAbundant(12)
#for n in range(0,30):
#	print n, sumdivisors(n), "\n"


#make a list of the even abundant numbers
EVENabundantList = []
n = 2
while n < N:
	if isAbundant(n):
		EVENabundantList.append(n)
	n = n+2
#print EVENabundantList
#print len(EVENabundantList)

ODDabundantList = []
n = 3
while n < N:
	if isAbundant(n):
		ODDabundantList.append(n)
	n = n+2
print ODDabundantList
print len(ODDabundantList)


XList = []
n = 1
while n < N:
	docount = 1
	for x in ODDabundantList:
		if n > x:
			if isAbundant(n-x):
				docount = 0
	if docount:
		XList.append(n)
	n = n + 2
print XList

ODDsum = 0
for x in XList:
	ODDsum = ODDsum + x
print ODDsum

YList = []
n = 2
while n < 80:
	docount = 1
	for x in EVENabundantList[0:40]:
		if n > x:
			if isAbundant(n-x):
				docount = 0
	if docount:			
		YList.append(n)
	n = n + 2
print YList

EVENsum = 0
for y in YList:
	EVENsum = EVENsum + y
print EVENsum


#for x in abundantList:
#	if x % 2 == 1:
#		print x


## Find first odd abundant number
#docontinue = 1
#count =  4
#while docontinue:
#	count = count + 6
#	if isAbundant(count):
#		print count
#		docontinue = 0



# Make a list of all numbers which are not the sum of two abundant numbers, 
#XList = []
#for n in range(1,N):
#	for x in abundantList:
#		if x > n:
#			break
#		elif n-x in abundantList:
#			if n not in XList:
#				XList.append(n)
#			break
#print XList
#dontcount = 1 
#count = 0
#for n in range(1,N/2):
#	dontcount = 1
#	for x in abundantList:
#		if x < 2*n:
#			if 2*n-x in abundantList:
#				dontcount = 0
#				break
#			if dontcount:
#				count = count + 2*n
#		else:
#			break
#
#print count
#print unlist	
