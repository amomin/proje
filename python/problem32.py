list1 = []

for i in range(10,100):
     for j in range(100,1000):
             flag = True
             for d in range(1,10):
                     if str(d) not in str(i) + str(j) + str(i*j):
                             flag = False
             if flag and i*j not in list1 and i*j < 10000:
##                    	list1.append([i,j,i*j])
                    	list1.append(i*j)

for i in range(1,10):
     for j in range(1000,5000):
             flag = True
             for d in range(1,10):
                     if str(d) not in str(i) + str(j) + str(i*j):
                             flag = False
             if flag and i*j not in list1 and i*j < 10000:
#                    	list1.append([i,j,i*j])
                    	list1.append(i*j)


total = 0
for x in list1:
	total = total + x

print list1

print total
