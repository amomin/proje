#Problem: find the largest palindrome which is a product of two 3 digit numbers
# (Below, we've generalized the problem to two l digit numbers)
import math

def reversesnum(n):
	#reverses the digits of the number n
	digitlist = []
	ans = 0
	while n > 0:
#		digitlist.insert(0, n%10)
		digitlist.append(n%10)
		n = (n - n%10)/10
	k = 0	
	for x in digitlist:
		ans = 10*ans + x
		k = k + 1
#	print(digitlist)	
	return ans

print(reversesnum(912)) #Check to see if reversesnum is working on an example

l =3 
A =10**l 
flag = 0
# Using (1000-x)(1000-y) - (1000 - x -y)*1000 + xy, we only need to check that xy is the reverse of 1000-x-y assuming xy is 3 digits or less.
# There should be an example of reasonably small size, so we'll just search for that and print the result
for N in range(A):
	for i in range(N/2):
		if ((N-i)*i == reversesnum(A-N)):
			print (A-i, A - N +i, (A-i)*(A-N+i))
			flag =1 
	if flag == 1:
		break
