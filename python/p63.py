# Run from command line
>>> count = 0
>>> for n in range(1,25):
...     for k in range(1,11):
...             if ((n-1)*log(10) < n*log(k)) and (n*log(k) < n * log(10)):
...                     count += 1
...                     print n,k,k**n,10**(n-1)
# add one to count 1^1=1
count +=1

print count

#You get 49
