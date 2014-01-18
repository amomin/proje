# Game:  Given a list of 4 non-negative numbers, you must reduce exactly one number in the list and hand the list over to your opponent.  The player that reduces the list to 0,0,0,0 loses.  This generates the list of losing boards with maximum entry up to N.

# It appears that a losing board is exactly a board such that when you write the numbers in base 2, the larger number is obtained from the smaller numbers by bitwise addition (without carries!)

loseList = [[0,0,0,1],[0,1,1,1]]

N = 13 

#for i in range(2,N+1):
#	loseList.append([0,i,i])

print loseList

for h in range(0,N):
	for i in range(h,N):
		for j in range(i,N):
			FoundLoser = False
			for k in range(0,j+1):
				x = [h,i,j,k]
				x.sort()
				if x in loseList:
					FoundLoser = True # i,j,k is a loser but it's already represented in the list
			l = j
			while not FoundLoser:
				FoundLoser = True #so far we haven't found a winning move
				for a in range(j):
					x = [l,a,i,h]
					x.sort()
					if x in loseList: #x is a loser, so [l,j,i] is a winner, ie we found a winning move
						FoundLoser = False
				for b in range(i):
					x = [l,j,b,h]
					x.sort()
					if x in loseList: #x is a loser, ie we found a winning move
						FoundLoser = False
				for c in range(h):
					x = [l,j,i,c]
					x.sort()
					if x in loseList: #x is a loser, ie we found a winning move
						FoundLoser = False
				if FoundLoser: # we have our loser, so we add it to the list
					x = [l,j,i,h]
					x.sort()
					loseList.append(x)
				else:
					l = l+ 1 #Go to next l since we haven't found our loser yet

for x in loseList:
	print x
					
			
			

