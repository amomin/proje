import math, sys, time
import MillerTest

isPrime = MillerTest.MillerRabin
tic = time.clock()

MIN = 2
MAX = 12201 
COUNTMAX=12000
def getDivSums(n,min=2):
	solns = [[n,1,[n]]]
	if isPrime(n):
		return solns
	for i in range(min,n/2+1):
		if n%i==0:
			res = getDivSums(n/i,i)
			for x in res:
				_l=x[2]+[i]
				new_soln=[x[0]+i,x[1]+1,_l]
				if new_soln not in solns:
					solns.append( new_soln )
	return solns

solns = [0]*MIN
for i in range(MIN,MAX):
	solns.append(False)

msns=[]
for i in range(MIN,MAX):
	x = getDivSums(i)
	for f in x:
		k=i-f[0]+f[1]
		if not solns[k] and k>1:
			solns[k]=i
			if k <= COUNTMAX:
				#print "Count solution for ",k," to be ",i
				if i not in msns:
					msns.append(i)

msns.sort()
k=MIN
#while k<COUNTMAX:
#while k<MAX:
	#print "f(",k,")=", solns[k]
	#if not solns[k]:
		#print "Havent solved for ",k,"yet"
	#k+=1
#print msns
print "Of the solutions found so far, the count up to ", COUNTMAX, " is ",sum(msns)

count2 = 0
for y in msns:
	count2+=y
print "Verifying the count is ",count2
toc = time.clock()
print "Time is ", toc-tic
