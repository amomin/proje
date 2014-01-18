import math,time

t1 = time.clock()

# Stores the digits 
digits = [1]

def multdigits(digitlist, n): #multiplies the digit list by the integer n
	for x in digitlist:
		x = x*n
	for i in range(len(digitlist)-1):
		if (digitlist[i] > 9):
			digitlist[i+1] = digitlist[i]/10
		if digitlist(len(digitlist) > 10:
			digitlist.append(digitlist(len(digitlist)) + 1)# THIS IS CLEARLY WRONG!!!
### TO BE CONTINUED!!!
