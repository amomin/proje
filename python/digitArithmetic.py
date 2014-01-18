import math

def convertToDigitList1(n):
	# Converts a number n into a list of its digits
	# The largest digit appears at the front of the list
	digitList = []
	numDigits = int(math.log(n,10)) # gives  the numer of digits in n
	for digit in range(numDigits+1):
		digitList.insert(0, (n/10**digit)%10)
	return digitList

def convertToInt1(digitList):
	# Converts a digit list to a base 10 integer
	lenList = len(digitList)
	n = 0
	for digit in range(lenList):
		n = n + digitList[digit]*(10**(lenList-digit-1))
	return n

#TESTING
#x = 13579
#xList = convertToDigitList(x)
#print x, xList, xList[1]
#print xList, convertToInt(xList), xList

def convertToDigitList(n):
	# Converts a number n into a list of its digits
	# The largest digit appears at the front of the list
	if n == 0:
		return []
	digitList = []
	numDigits = int(math.log(n,10)) # gives  the numer of digits in n
	for digit in range(numDigits+1):
		digitList.append((n/10**digit)%10)
	return digitList

def convertToInt(digitList):
	# Converts a digit list to a base 10 integer
	lenList = len(digitList)
	n = 0
	for digit in range(lenList):
		n = n + digitList[digit]*(10**(digit))
	return n


#TESTING
#x = 13579
#xList = convertToDigitList(x)
#print x, xList, xList[1]
#print xList, convertToInt(xList), xList

def scalarMult(x, dList):
	# multiplies the digit list dList by the integer x
	answerList = []
	for digit in range(len(dList)):
		answerList.append(x*int(dList[digit]))
	# Now we have to do the carries
	carryBit = 0
	for digit in range(len(dList)):
		answerList[digit] = int(answerList[digit]) + carryBit
		carryBit = int(answerList[digit])/10
		answerList[digit] = int(answerList[digit]) % 10
	answerList += convertToDigitList(carryBit)
	return answerList

print 97, 12543, convertToInt(scalarMult(97, convertToDigitList(12543)))

def sumDigitLists(dL1, dL2):
	#Sums two digit lists together
	if len(dL1) > len(dL2):
		a = dL1
		b = dL2
	else:
		a = dL2
		b = dL1
	minLength = len(b)
	maxLength = len(a)
	sumList = []
	for i in range(minLength):
		sumList.append(int(a[i]) + int(b[i]))
	sumList.extend(a[minLength:maxLength])
	carryBit = 0
	for digit in range(maxLength-1):
		sumList[digit] = int(sumList[digit]) + carryBit
		carryBit = int(sumList[digit])/10
		sumList[digit] = int(sumList[digit]) % 10
	sumList += convertToDigitList(carryBit)
	return sumList

print 1232193, 1532132178, sumDigitLists(convertToDigitList(1232193), convertToDigitList(1532132178)), 1232193+1532132178

def multDigitLists(dL1, dL2):
	sumList = []
	for i in range(len(dL1)):
		sumList = sumDigitLists(scalarMult(int(dL1[i])*(10**i),dL2),sumList)
	return sumList

print 97, 123, 97*123, multDigitLists([7,9], [3,2,1])

# Solution to problem 16
dL = [1]
for i in range(1,1001):
	dL = scalarMult(2,dL)
total = 0
for x in dL:
	total = total + int(x)
print total

# Solution to problem 20
total = 0
dL = [1]
for i in range(1,101):
	dL = scalarMult(i,dL)
for x in dL:
	total = total + int(x)
print total
