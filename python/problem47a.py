# code due to user Brian
#Idea: first, create a list whose ith entry is the number of prime factors of i.
#  This is done as follows.  If a number has 0 factors it is prime.  For each multiple of it add +1 to the prime factor count.
#  If instead you encounter a count of 4, that number has exactly 4 prime factors.  +1 your count of consecutives.  if you now have 4 consecutives you are done!
#  If neither, go on to the next making sure your count of consecutives is 0
Limit=1000000     # Search under 1 million for now
factors=[0]*Limit # number of prime factors.
count=0
for i in xrange(2,Limit):
    if factors[i]==0:
        # i is prime
        count =0
        val =i
        while val < Limit:
            factors[val] += 1
            val+=i
    elif factors[i] == 4:
        count +=1
        if count == 4:
            print i-3 # First number
            break
    else:
        count = 0

