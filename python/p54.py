##################
## Value of hand:
# We'll store it as a list [r,L]
# r =1,...9 represents the type of hand (high card,...,straight flush)
# L is a list storing the rank with the type of hand
# e.g. if r = two pairs, then L[a,b,c] where a > b is the value of the pairs, and c is the remaining card
# Thus [r1,L1] > [r2,L2] if either r1 > r2 or else r1 = r2 and L1 > L2 (comparing consecutive entries

# Card values go from 1-52
# Store 2,...,13 in order, Clubs, Diamonds, Hearts, Spades
# i.e. 1 = 2C, 2 = 3C, ..., 13 = AC, 14 = 2D, etc....


highcard = 1
onepair = 2
twopair = 3
threekind = 4
straight = 5
flush = 6
fullhouse = 7
fourkind = 8
straightflush = 9

def maxelt(L):
	# Return the highest card value in the list
	# This is an integer between 1 (deuce) and 13 (ace)
	ans = 1
	for x in L:
		if (x % 13) == 0:
			ans = 13
		else:
			if (ans != 13) and (x % 13) > ans:
				ans = (x % 13)
	return ans

#print [3,17,5,6,7], maxelt([3,17,5,6,7])
#print [20,21,22,23,24], maxelt([20,21,22,23,24])
#print [23,24,25,26,27], maxelt([23,24,25,26,27])

def isStraight(L):
	M = []
	for x in L:
		M.append(x % 13)
	M.sort()
	x = (M[0] % 13)
	if x > 9:
		answer = False
	else:
		answer = True
	for i in range(1,5):
		if (M[i] % 13) != ((x+i) % 13):
			answer = False
	return answer

print [3,17,5,6,7], isStraight([3,17,5,6,7])
print [20,34,22,23,24], isStraight([20,34,22,23,24])
print [23,24,25,34,22], isStraight([23,24,25,34,22])

def isFlush(L):
	x = (L[0]-1) / 13
	answer = True
	for i in range(1,5):
		if (L[i]-1) / 13 != x:
			answer = False
	return answer

#print [3,4,5,6,7], isFlush([3,4,5,6,7])
#print [12,13,14,15,16], isFlush([12,13,14,15,16])

def compareRank(R1,R2):
	if R1[0] > R2[0]:
		return 1
	elif R1[0] < R2[0]:
		return 2
	else:
		return ListRank(R1[1],R2[1])

def ListRank(L1,L2):
	n = len(L1) # Should be = len(L2)
	i = 0
	while i < n:
		if L1[i] > L2[i]:
			return 1
		elif L1[i] < L2[i]:
			return 2
		else:
			i = i + 1


#print [3,5,1], [3,4,5], ListRank([3,5,1],[3,4,5])


def rankHand(L):
	if isFlush(L):
		if isStraight(L):
			return [straightflush, [L[4]]]
		else:
			return [flush,[maxelt(L)]]
	else:
		if isStraight(L):
			return [straight, [maxelt(L)]]
		else: # Not a straight or a flush
			M = [0,0,0,0,0]
			for i in range(len(L)):
				M[i] = ((L[i]-1) % 13)+1
			M.sort()
			P = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
			for x in M:
				P[x] += 1
			rank = -1
			rankList = []
			if 4 in P:
				rank = fourkind
				rankList.append(P.index(4))
				rankList.append(P.index(1))
			elif 3 in P:
				rankList.append(P.index(3))
				if 2 in P:
					rank = fullhouse
					rankList.append(P.index(2))
				else:
					rank = threekind
					rankList.append(P.index(1))
					P[P.index(1)] = 0
					rankList.insert(1,P.index(1))
			elif 2 in P:
				rankList.append(P.index(2))
				#determine if two pairs or one
				P[P.index(2)] = 0
				if 2 in P:
					rank = twopair
					rankList.insert(0,P.index(2))
					rankList.append(P.index(1))
				else:
					rank = onepair
					for i in range(len(P)):
						if P[i] == 1:
							rankList.insert(1,i)
			else:
				rank = highcard
				rankList = M
				rankList.reverse()
			return [rank,rankList]
			

import fileinput
HandList = []
rawHandList = []
P1 = []
P2 = []
for line in fileinput.input('poker.txt'):
#    HandList.append(line)
	linestring = [  [line[0:2], line[3:5],  line[6:8], line[9:11], line[12:14]], [line[15:17], line[18:20], line[21:23], line[24:26], line[27:29] ]]
	P1 = []
	for x in linestring[0]:
		num = 0
		if x[0] in '123456789':
			num += int(x[0]) - 1
		elif x[0] == 'T':
			num += 9 
		elif x[0] == 'J':
			num +=10
		elif x[0] == 'Q':
			num +=11
		elif x[0] == 'K':
			num += 12
		elif x[0] == 'A':
			num += 13
		else:
			continue

		if x[1] == 'D':
			num += 13
		elif x[1] == 'H':
			num += 26
		elif x[1] == 'S':
			num += 39


		P1.append(num)	

	P2 = []
	for x in linestring[1]:
		num = 0
		if x[0] in '123456789':
			num += int(x[0]) - 1
		elif x[0] == 'T':
			num += 9 
		elif x[0] == 'J':
			num +=10
		elif x[0] == 'Q':
			num +=11
		elif x[0] == 'K':
			num += 12
		elif x[0] == 'A':
			num += 13
		else:
			continue

		if x[1] == 'D':
			num += 13
		elif x[1] == 'H':
			num += 26
		elif x[1] == 'S':
			num += 39


		P2.append(num)	
#	HandList.append(linestring)
	HandList.append([P1,P2])
	rawHandList.append(linestring)


print len(HandList)


#for i in range(1000):
#	print rawHandList[i], rankHand(HandList[i][0]), rankHand(HandList[i][1])
#	print compareRank(rankHand(HandList[i][0]), rankHand(HandList[i][1]))

#for i in range(1000):
#	if isStraight(HandList[i][0]) or isStraight(HandList[i][1]):
#		print i, rawHandList[i], HandList[i]
#		print rankHand(HandList[i][1])

count = 0
for i in range(1000):
	if  compareRank(rankHand(HandList[i][0]), rankHand(HandList[i][1])) == 1:
		count += 1

print count

