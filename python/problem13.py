import math
# Note that we only need to use the first 12 or so digits (because the sum of 100 38 digit numbers is less than 10**40, actually 11 is ok already)
# However, Python doesn't seem to mind at all.


print 'Begin'

with open('problem13.txt','r') as f:
	numList = f.readlines()
print f.closed

carryover = 0

answerList = []
for digit in range(50):
	currentSum = carryover #start the current sum at the carried value
	for x in numList:
		currentSum = ((int(x)/(10**digit)) % 10) + currentSum
# 		print currentSum, (int(x)/(10**digit)) % 10 # FOR TESTING ONLY
#	answerList.append(currentSum % 10) #Take the last digit
	answerList.insert(0,currentSum % 10) #Take the last digit
	carryover = currentSum / 10 # carry over the rest
#	print digit, currentSum % 10, currentSum  # For testing only
#answerList.append(carryover)
answerList.insert(0,carryover)
print answerList
print len(answerList)
