

for i in range(1,10):
	for j in range(1,10):
		for d in range (1,10):
			if (int(str(i) +str(d)) * j == i * int(str(j) + str(d))) and int(str(i) + str(d)) < int(str(j) + str(d)) :
				print str(i) +str(d),  str(j) + str(d)
			elif  int(str(d) +str(i)) * j == i * int(str(j) + str(d)) and int(str(d) + str(i)) < int(str(j) + str(d)) :
				print str(d) +str(i),  str(j) + str(d)
			elif  (int(str(d) +str(i)) * j == i * int(str(d) + str(j))) and int(str(d) + str(i)) < int(str(d) + str(j)) : 
				print str(d) +str(i),  str(d) + str(j)
			elif (int(str(i) +str(d)) * j == i * int(str(d) + str(j))) and int(str(i) + str(d)) < int(str(d) + str(j)) :
				print str(i) +str(d),  str(d) + str(j)


