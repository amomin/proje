# Idea inspired by answer of Azii?

import time

t0 = time.clock()

def check(n):
	dlist = []
	for i in range(10):
		dlist.append(0)
	swap = n
	while swap > 0:
		dlist[swap % 10] += 1
		swap = swap/10
	i = 2
	while i < 7:
		swap = n*i
		while swap > 0:
			if dlist[swap % 10] == 0:
				return False
#			else:
#				dlist[swap % 10] -= 1
			swap = swap/10
		i += 1
	return True

print check(142857)

i = 2
found = False
while not found:
	x = 10**i
	while (x < 10**(i+1)) and not found:
		if check(x):
			found = True
			print x
		else:
			x = x+1
	i = i+1

print time.clock() - t0
