import math,time
t1 = time.time()
N = 5
sq = math.sqrt

phi = (1.0 + sq(5))/2.0
psi = (1.0 - sq(5))/2.0
def Fib(n):
	return int( (phi**n-psi**n)/sq(5) )

def firstDigits(n,k): #Return the first k decimal digits of n
	if n < 10**k:
		return n
	else:
		l = int(math.floor(math.log(n,10)))
		return int(n/(10**(l-k+1)))

def isPanDigital(n): # Determines if n is pandigital
	if n < 10**8 or n >= 10**10:
		return False
	else:
		digitlist= [0]*10
		while n > 0:
			digitlist[n%10] += 1
			n/=10
		if digitlist == [0]+[1]*9:
			return True
		else:
			return False

#TestList = [132458697,144238976,174392847,928157463]
#print TestList
#print map(isPanDigital,TestList)
	
#fib1mod=1
#fib2mod=1
fib1 = 1
fib2 = 1
Flag = False
Flag1 = False
Flag2 = False
k = 2
EndCheck= 1000000
while not Flag and k < EndCheck:
#	Flag1 = False
#	Flag2 = False
#	fib2mod = ((fib2mod + fib1mod) % 10**N)
#	fib1mod = ((fib2mod - fib1mod) % 10**N)
	fib2 = fib2 + fib1
	fib1 = fib2 - fib1
	if isPanDigital(fib1 % 10**9):
#		print "Last 9 digits", k 
#		Flag1 = True
		if isPanDigital(firstDigits(fib1,9)):
#		print "First 9 digits", k
#		Flag2 = True
#	Flag = Flag1 and Flag2
#	if Flag:
			print "SUCCESS!!!"
			print k, fib1 % 10**9, firstDigits(fib1,9)
			Flag = True
#	if k%30 == 0:
#		print k
#		print fib1mod,fib2mod, firstDigits(Fib(k),9), firstDigits(Fib(k+1),9)
#		print k,fib1mod, k+1, fib2mod
	k+=1
