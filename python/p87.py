import math,sys,time
import MillerTest
#import bisect

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
# Note: solutions are not unique, e.g. 145 has solutinos 2,2,11 and 2,5,2 or something
#non_unique_solutions = []

def reverse_insort(a,x):
	lo=0
	hi=len(a)
	while lo<hi:
		mid= (lo+hi)//2
		if x > a[mid]:hi = mid
		else: lo = mid+1
	a.insert(lo,x)

def inrevsearch(a,x):
	lo=0
	hi=len(a)
	if hi==0: return False
	while lo<hi:
		mid= (lo+hi)//2
		if x > a[mid]:hi = mid
		else: lo = mid+1
	#if x<150:
		#print a, x, " ?= ", a[lo-1]
	if a[lo-1]==x:
		return True
	return False


total_solutions_count = 0
unique_solutions_count = 0
for i in p_list_1:
	if i**4 > MAX:
		#print "i too big: ", i
		break
	for j in p_list_2:
		if i**4+j**3 > MAX:
			#print "j,i too big: ", i,j
			break;
		for k in p_list_3:
			if i**4+j**3+k**2 > MAX:
				#print "k, j,i too big: ", i,j,k
				break
			soln = i**4+j**3+k**2
			total_solutions_count+=1
			#print "i, j, k, and i**4+j**3+k**2 is ", i, j, k, soln
			#if not (soln in sol_list):
			if not inrevsearch(sol_list,soln):
				unique_solutions_count+=1
				#sol_list.append(soln)
				#bisect.insort_left(sol_list, soln)
				reverse_insort(sol_list, soln)
			#else:
				#non_unique_solutions.append([i,j,k,soln])

print sol_list
print "Number of unique solutions is", len(sol_list)," = ",unique_solutions_count
print "Total Number of solutions is", total_solutions_count
#print "Double solutions list", non_unique_solutions
