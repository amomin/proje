import time
import itertools

comb = itertools.combinations
prod = itertools.product
perm = itertools.permutations

squares = ['01','04','0x','1x','25','3x','4x','x4','81']
print squares
count = 0
for x in comb('012345x78x',6):
	for y in comb('012345x78x',6):
		L = []
		for z in prod(x,y):
			L.append(z[0]+z[1])
		for z in prod(y,x):
			L.append(z[0]+z[1])
		#print L
		if set(squares).issubset(L):
#			print 'here'
			count +=1

print count/2
# Notice: the digits on the two cubes CANNOT be the same because each of the digits 0,1,2,3,4,5,6,8,9 appear in some square.  However, we count two cubes A,B the same as the two cubes B,A.  So we should divide our final count by 2 (hence reporting count/2 above)
				
