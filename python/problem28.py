N = 1001

count1 = 0
for i in range(1,N+1):
	T = 0
	for j in range(1,i):
		T = T + j
	count1 = count1 + 1 + 2*T

count2 = 0
doJump = 0
for i in range(1,N+1):
	S = 1
	jump = 4
	doJump = 0
	for j in range(1,i):
		S = S + jump
		if doJump==0:
			doJump = 1
		else:
			doJump = 0
			jump = jump+4
	print S, jump
	count2 = count2 + S

print count1
print count2
print count1 + count2 - 1
