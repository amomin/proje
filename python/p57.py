import MillerTest

isPrime = MillerTest.MillerRabin

numPrimesOnDiagonal = 3
numDiagElts = 5
ratio = (1.0*numPrimesOnDiagonal)/(1.0*numDiagElts)
n = 1

while ratio >= .1:#n<10: #ratio > .1:
	n += 1
	numDiagElts += 4
	numPrimesOnDiagonal += isPrime((2*n+1)**2 - 2*n) + isPrime((2*n+1)**2 - 4*n) + isPrime((2*n+1)**2 - 6*n)  
	ratio = (1.0*numPrimesOnDiagonal)/(1.0*numDiagElts)
	print n, 2*n+1, numDiagElts, numPrimesOnDiagonal, ratio

print n, 2*n+1, numPrimesOnDiagonal, numDiagElts, ratio

