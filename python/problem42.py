import csv

f = open("words.txt", 'r')
try:
    reader = csv.reader(f)
    for row in reader:
        print row
#	continue
finally:
    f.close()
#f = open("names.txt", 'r')
# wordlist = f.read()
# An alternate way to get the list
#eval( '[' + open(".../words.txt").readlines()[ 0 ]


TriList = []
for n in range(30):
	TriList.append(n*(n+1)/2)

TriCount = 0
wordcount = 0
for x in row:
	wordcount = wordcount + 1
	wordscore = 0
	while x != "":
		wordscore = wordscore + ord(x[0]) - 64 
		x = x[1:]
	if wordscore in TriList:
		TriCount = TriCount+1
print TriList

print TriCount, wordcount
