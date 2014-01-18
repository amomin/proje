import math
N = 600851475143 
factorslist =[1] 
i = 2
while i < N:
	if (N%i == 0):
		factorslist.append(i)
		N = N/i
	else:
		i = i +1
factorslist.append(N)
print(factorslist)		
