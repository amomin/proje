# Game:  Given a list of 3 non-negative numbers, you must reduce exactly one number in the list and hand the list over to your opponent.  The player that reduces the list to 0,0,0 loses.  This generates the list of losing boards with maximum entry up to N.

# It appears that a losing board is exactly a board such that when you write the numbers in base 2, the larger number is obtained from the smaller numbers by bitwise addition (without carries!)
# Stated another, more convenient way, a board is losing precisely when, when each number is written in base 2, it holds for each bit i that the sum of the ith bit of the numbers is zero`


loseList = [[0,0,1],[1,1,1]]

N =  20

#for i in range(2,N+1):
#	loseList.append([0,i,i])

print loseList

for i in range(0,N):
	for j in range(i,N):
		FoundLoser = False
		for k in range(0,j+1):
			x = [i,j,k]
			x.sort()
			if x in loseList:
				FoundLoser = True # i,j,k is a loser but it's already represented in the list
		l = j
		while not FoundLoser:
			FoundLoser = True #so far we haven't found a winning move
			for a in range(j):
				x = [l,a,i]
				x.sort()
				if x in loseList: #x is a loser, so [l,j,i] is a winner, ie we found a winning move
					FoundLoser = False
			for b in range(i):
				x = [l,j,b]
				x.sort()
				if x in loseList: #x is a loser, ie we found a winning move
					FoundLoser = False
			if FoundLoser: # we have our loser, so we add it to the list
				x = [l,j,i]
				x.sort()
				loseList.append(x)
			else:
				l = l+ 1 #Go to next l since we haven't found our loser yet

for x in loseList:
	print x
					
			
			

