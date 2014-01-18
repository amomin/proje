import time
t1 = time.time()
def numsum(n,d):
# number of ways to write n as a sum of 2 or more positive integers less than d
	if d == 1 or d == 0:
		return 1
	else:
		answer = 0
		for x in range(1,d+1): # n = x + (n-x)
			if n-x <= x:
				answer += numsum(n-x,n-x)
			else:
				answer += numsum(n-x,x)
		return answer


for x in range(2,15):
	print x, numsum(x,x-1)

print numsum(100,99)
print time.time()-t1
