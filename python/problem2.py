import math
temp = 0
t1 = 1
t2 = 2
runningsum = 0
while (t2 < 4000000):
	if t2%2 == 0:
		runningsum = runningsum + t2
	temp = t1
	t1 = t2
	t2 = t1 + temp
print(runningsum)

