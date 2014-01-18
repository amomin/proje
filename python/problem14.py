import math

chainLengthValues = [0,1,2,7,3] # creates a list to compute the chain length, i element is the length of the chain starting at i

n = 5
longestChainLength = 7
longestChainInteger = 3
while (n < 1000001):
	currNum = n
	currentChainLength = 1
	if currNum % 2 == 0:
		currNum = currNum/2
		currentChainLength = currentChainLength + 1
	else:
		currNum = 3*currNum + 1
		currentChainLength = currentChainLength + 1
	while (currNum > n):
		if currNum % 2 == 0:
			currNum = currNum/2
			currentChainLength = currentChainLength + 1
		else:
			currNum = 3*currNum + 1
			currentChainLength = currentChainLength + 1
	# Now we know that currNum is less than n, so use the value we've computed already!
	currentChainLength = currentChainLength + chainLengthValues[currNum] - 1
	chainLengthValues.append(currentChainLength) #Now the nth value in this list will be currentChainLength
	if (currentChainLength > longestChainLength):
		longestChainLength = currentChainLength
		longestChainInteger = n
	n = n+1

print longestChainInteger, longestChainLength

#print chainLengthValues
