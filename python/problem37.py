# The list should be

# 739397
# 3797 , 3137
# 797,373,317,313
#23, 37, 53, 73

import string
import MillerTest
import itertools

numDigits = 3
plist = ['2','3','5','7']
dlist = plist+['0','1','4','6','8','9']
oddlist = ['1','3','5','7','9']

isPrime = MillerTest.MillerRabin
for d0 in plist:
#	for d1 in oddlist:
#		for d2 in oddlist:
#			for d3 in oddlist:
	for digit in itertools.product(oddlist,repeat = numDigits-2):
				for dlast in ['3','7']:
					x = d0
					for i in range(numDigits-2):
						x = x + digit[i]
					x = x + dlast
#					x = d0+digit[0]+digit[1] + dlast

#					x = d0 + d3
					y = x
					z = x
					while (x != '') and (isPrime(int(x))):
						x = x[:-1]
					while (y != '') and (isPrime(int(y))):
						y = y[1:]
					if x == '' and y == '':
						print z


						
