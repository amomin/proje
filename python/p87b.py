## Following cruise02's comment in the thread, try instead
## to find all solutions, sort the list,
## and then got through the solution list sequentially
## adding the solution count each time the value in the list
## increases
##
##  This is just so much faster!  Because you only do 
## one intensive operation (the sort)

import math,sys,time
import MillerTest

isPrime1 = MillerTest.MillerRabin
sqrt = math.sqrt


prime_list = []
for k in range(2,8000):
	if isPrime1(k):
		prime_list.append(k)

def isPrime2(n):
	if n in prime_list: 
		return True
	else: 
		return False

p_list_1 = filter( lambda(x): True if x < 85 else False, prime_list)
p_list_2 = filter( lambda(x): True if x < 385 else False, prime_list)
p_list_3 = filter( lambda(x): True if x < 7999 else False, prime_list)

MAX = 50000000
N = int(pow(MAX,0.25))

sol_list = []

total_solutions_count = 0
for i in p_list_1:
	if i**4 > MAX:
		break
	for j in p_list_2:
		if i**4+j**3 > MAX:
			break;
		for k in p_list_3:
			if i**4+j**3+k**2 > MAX:
				break
			soln = i**4+j**3+k**2
			total_solutions_count+=1
			sol_list.append(soln)

sol_list.sort()
unique_solns = 1;
for i in range(1,total_solutions_count):
	if sol_list[i] != sol_list[i-1]:
		unique_solns+=1

print "Number of unique solutions is", unique_solns
print "Total Number of solutions is", total_solutions_count
