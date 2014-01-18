import csv
import sys

f = open("names.txt", 'r')
try:
    reader = csv.reader(f)
    for row in reader:
        print row
finally:
    f.close()

row.sort()

counter = 0
score = 0
for x in row:
	counter = counter + 1
	for n in range(0, len(x)):
		score += counter*(ord(x[n])-64)

print row
print score
