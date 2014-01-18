def isPalindrome10(n):
	x = str(n)
	answer = True
	while len(x) > 1 and answer:
		if x[0] != x[-1]:
			answer = False
		x = x[1:-1]
	return answer

def isPalindrome2(n):
	a = bin(n)
	x = str(a[2:])
	answer = True
	while len(x) > 1 and answer:
		if x[0] != x[-1]:
			answer = False
		x = x[1:-1]
	return answer

count =0
for i in range(1000000):
	if isPalindrome10(i) and isPalindrome2(i):
		count = count + i

print count	
