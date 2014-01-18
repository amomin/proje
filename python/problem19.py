daylistbeforeFeb = [2,5]
daylistafterFeb = [5,1,3,6,1,4,0,2,5,0]

numSundays = 0
for day in daylistbeforeFeb:
	counter = day
	print counter
	year = 1901
	while (year < 2001):
		if (counter % 7 == 0):
			numSundays = numSundays+1
		if (year %4 == 0):
			counter = counter +2
		else:
			counter = counter +1
		year = year+1

for day in daylistafterFeb:
	counter = day
	print counter
	year = 1901
	while (year < 2001):
		if (counter % 7 == 0):
			numSundays = numSundays+1
		if (year %4 == 3):
			counter = counter +2
		else:
			counter = counter +1
		year = year+1



print numSundays	
