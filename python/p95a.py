import math
# Following ideas in the thread, perform using a Sieve method
# Make a list of length 100000, all set to 1 initially
# If at position i the value is 1, then for each index i*k up to one million add the 
# appropriate powers of p to it (actually if i**l divides k then mutliply by i**(l+2)-1/i-1
#
# Then calculate longest chains

# Well, may not bother to do this but it eliminates computing the sum of divisors function repeatedly so should be much faster than other solution
