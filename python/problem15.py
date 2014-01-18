# Just compute 40C20 = 40!/20!20!
x = 1
for i in range(1,21):
	x = x*(20+i)/i
print x
