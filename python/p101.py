import time
import itertools
comb = itertools.combinations

# Let p(x) be a polynomial
# Let q_k(x) be the polynomial (of degree k-1)
# which matches p(x) on the values
# x = 1, x = 2,..., x = k
#
# Let b(k) = q_k(k+1) if it disagrees with p(k+1), otherwise zero
# 
# Because q_k(x) = p(x) for k sufficiently large (k >= deg(p))
# the sum of the b(k) is finite.
#
# The problem is to find the sum of the b(k)

class Poly:
  _degree = 0
  coefficients = []

  def __init__(self, coeffs):
    self._degree = len(coeffs)
    self.coefficients = coeffs

  def degree(self):
    return self._degree

  def evl(self, n):
    sm = 0
    deg = 0
    for i in range(0,self._degree):
      sm += self.coefficients[deg]*(n)**deg
      deg = deg + 1
    return sm

  def toString(self):
    deg = 0
    str = ""
    #str = "%.2f" % (1.0*self.coefficients[deg])
    str = "%d" % (self.coefficients[deg])
    deg = 1
    for i in range(1,self._degree):
      #str = "%s + %.2f*x^%d" % (str, self.coefficients[deg], deg)
      str = "%s + %d*x^%d" % (str, self.coefficients[deg], deg)
      deg = deg + 1
    str = "%s \n" % (str)
    return str

  ## Fit polynomial to a list of values
  # Initially, assume the x-values are
  # 1,2,3,...n,n+1,...,
  # 
  # We will use the fact that the fit is 
  # an obvious linear combination of
  # polynomials like
  # (x-1)(x-2)..(x-k+1)(x-k-1)...(x-n)
  ##
  def fit(self, lst):
    deg = len(lst)
    xvals = range(1,deg+1)
    coeffs = [0.0] * deg
    # Sum over the terms, indexed by
    # k = the omitted value.  This term has coefficient
    # given by the value at k divided by the 
    # evaluation of this term at k.  It is then expanded
    # and accumulated to the coefficients accumulated so far
    for k in xvals:
      xvals.remove(k)
      num = lst[k-1] # Numerator is the value to match
      # Compute denominator
      denom = 1
      for i in xvals:
        denom = denom * (k-i)
      # Sum over degrees of the terms
      for currdeg in range(0,deg+1):
        # There are deg choose currdeg terms of degree currdeg,
	# use comb to iterate over all of them, and to
	# extract their product
        for terms in comb(xvals, currdeg):
          prod = 1
	  for p in terms:
	    prod = (-1) * prod * p
	  coeffs[deg - currdeg - 1] = coeffs[deg - currdeg - 1] + 1.0*num*prod/(1.0*denom)
      xvals.insert(0, k)
    # Optional - round to integer coefficient  
    for i in range(0,len(coeffs)):
      coeffs[i] = int(round(coeffs[i]))
    # Done, assign to coefficients
    self.coefficients = coeffs
    self._degree = deg

## Solution to problem

# p is the polynomial to fit
#p = Poly([0,0,0,1]) # From example
p = Poly([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])
pVals = []
for i in range(1, p.degree() + 1):
  pVals.append(p.evl(i))
print pVals

badVals = 0
for deg in range(1, p.degree() + 1):
  fitPoly = Poly([0])
  toFit = pVals[:deg]
  fitPoly.fit(toFit)
  print fitPoly.toString()

  if abs(p.evl(deg + 1) - fitPoly.evl(deg + 1)) > 0.00000001:
    badVals = badVals + fitPoly.evl(deg + 1)
  #for i in range(1,len(toFit) + 2):
    #print p.evl(i), fitPoly.evl(i)

print "Bad values sum = ", badVals
