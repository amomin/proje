import math

print 'Begin'

with open('problem11.txt','r') as f:
	numTables = f.readlines()
print f.closed

htnumTables = len(numTables)
widthnumTables = len(numTables[0])

print htnumTables, widthnumTables


prod = 1
maxprod = 1


# Across product
for i in range(htnumTables):
	for j in range((widthnumTables - 10)/3):
		prod =(10*int(numTables[i][3*j])+int(numTables[i][3*j+1]))*(10*int(numTables[i][3*j+3])+ int(numTables[i][3*j+4]))* (10*int(numTables[i][3*j+6])+int(numTables[i][3*j+7]))* (10*int(numTables[i][3*j+9])+int(numTables[i][3*j+10])) 
		if (prod > maxprod):
			maxprod = prod
#			print 10*int(numTables[i][3*j])+int(numTables[i][3*j+1]), 10*int(numTables[i][3*j+3])+ int(numTables[i][3*j+4]), 10*int(numTables[i][3*j+6])+int(numTables[i][3*j+7]), 10*int(numTables[i][3*j+9])+int(numTables[i][3*j+10]) 

# Down product (easier!)
for i in range(htnumTables-3):
	for j in range((widthnumTables - 1)/3):
		prod =(10*int(numTables[i][3*j])+int(numTables[i][3*j+1]))*(10*int(numTables[i+1][3*j])+ int(numTables[i+1][3*j+1]))* (10*int(numTables[i+2][3*j])+int(numTables[i+2][3*j]))* (10*int(numTables[i+3][3*j])+int(numTables[i+3][3*j+1])) 
		if (prod > maxprod):
			maxprod = prod
#			print  10*int(numTables[i][3*j])+int(numTables[i][3*j+1]), 10*int(numTables[i+1][3*j])+ int(numTables[i+1][3*j+1]), 10*int(numTables[i+2][3*j])+int(numTables[i+2][3*j]), 10*int(numTables[i+3][3*j])+int(numTables[i+3][3*j+1]) 

#DownAcross product
for i in range(htnumTables-3):
	for j in range((widthnumTables - 10)/3):
		prod =(10*int(numTables[i][3*j])+int(numTables[i][3*j+1]))*(10*int(numTables[i+1][3*j+3])+ int(numTables[i+1][3*j+4]))* (10*int(numTables[i+2][3*j+6])+int(numTables[i+2][3*j+7]))* (10*int(numTables[i+3][3*j+9])+int(numTables[i+3][3*j+10])) 
		if (prod > maxprod):
			maxprod = prod

#UpAcross product
for i in range(3,htnumTables):
	for j in range((widthnumTables - 10)/3):
		prod =(10*int(numTables[i][3*j])+int(numTables[i][3*j+1]))*(10*int(numTables[i-1][3*j+3])+ int(numTables[i-1][3*j+4]))* (10*int(numTables[i-2][3*j+6])+int(numTables[i-2][3*j+7]))* (10*int(numTables[i-3][3*j+9])+int(numTables[i-3][3*j+10])) 
		if (prod > maxprod):
			maxprod = prod


print maxprod	
