# Of course, you can do this one by hand
#
# Both Id(x), phi(x) are multiplicative and you know their values on the prime powers.  THe quotient is therefore
#
# prod p^k / (p^k - p^(k-1)) = prod p / (p-1)
#
# which you maximize by taking the smallest p's available.  There's no point in using p^k, so the answer will be of the form 2*3*5*7*11*13*...*p
import time
t1 = time.time()
import MillerTest
isP = MillerTest.MillerRabin

answer =1.0
prod = 1
counter = 2
while prod<1000000:
	if isP(counter):
		prod *= counter
		answer *= (1.0*counter)/(counter-1.0)
		print counter, prod, answer
	counter += 1 # Since the answer is small no need to be optimal in any way

print "The answer should be the second number on the second last line and took only this long to generate"
print time.time() - t1
