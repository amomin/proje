import time
import math

t0 = time.clock()

D = 2
N = 10000000

j =1
flag = True
diff = 1
#while flag and diff < D:
if True:
	while (j < N) and flag:# and not raw_input():
		y = j*(3*j-1)/2
		x = (j+diff)*(3*j -1 + 3*diff)/2
		if ((((1 + math.sqrt(1+24*(x-y)))/6) % 1 ) == 0) and  ((((1 + math.sqrt(1+24*(x+y)))/6) % 1 ) == 0):
#		if False:
			print j, diff
			flag = False
#			j = j+1
#		elif raw_input():
#			flag = False
#			print j, diff
		else:
			j = j+1 
#	diff = diff + 1

print time.clock() - t0
print j, diff
