import math, time

finished = 0
a = 1
while (a < 1000) and (finished == 0):
	b = 1
	while (b < 1000) and (finished ==0):
		if a**2 + b **2 - (1000-a-b)**2 == 0:
			print a,b,1000-a-b, a*b*(1000-a-b)
			finished = 1
		b = b + 1
	a = a +1
