f = open('roman.txt','r')
L = []
for x in f.readlines():
    L.append(x)
f.close()


def RomToNum(s):
#	# Converts a Roman numeral string to an integer
	num = 0
	while s != "":
#	while 'M' in s:
		if 'M' in s:
			i = s.find('M')
			j = s.rfind('M')
			if (j>0) and s[j-1] == 'C':
				if j!=i:
					num += (j-i-1)*1000+900
				else:
					num+= 900
			else:
				num += (j-i+1)*1000
			s= s[j+1:]
		elif 'D' in s:
			if len(s) == 1:
				num += 500
				s = ''
			elif s[1] == 'D':
				num+=400
				s = s[2:]
			else:
				num+=500
				s = s[1:]
		elif 'C' in s:
			i = s.find('C')
			j = s.rfind('C')
			if (j>0) and s[j-1] == 'X':
				if j!=i:
					num += (j-i-1)*100+90
				else:
					num+=90
			else:
				num += (j-i+1)*100
			s= s[j+1:]
		elif 'L' in s:
			if len(s) == 1:
				num +=50
				s = ''
			elif s[1] == 'L':
				num+=40
				s = s[2:]
			else:
				num+=50
				s = s[1:]
		elif 'X' in s: #only XVIs
			i = s.find('X')
			j = s.rfind('X')
			if (j>0) and  s[j-1] == 'I':
				if j!=i:
					num += (j-i-1)*10+9
				else:
					num+=9
			else:
				num += (j-i+1)*10
			s= s[j+1:]
		elif 'V' in s: #only VIs
			if len(s) == 1:
				num += 5
				s = ''
			elif s[1] == 'V':
				num+=4
				s = s[2:]
			else:
				num+=5
				s = s[1:]
		else: # only I's
			num += len(s)
			s = ""
	return num

def NumToRom(n):
	# Converts an integer into its minimal Roman numeral
	s = '' # output string
	s = s + 'M'*(n/1000)
	n -= 1000*(n/1000)
	if (((n/100) % 10) == 9):
		s= s+'CM'
		n-=900
	elif ((n/100)% 10) == 4:
		s = s+'CD'
		n-=400
	if n >= 500:
		s = s +'D'
		n -=500
	s = s + 'C'*(n/100)
	n-= 100*(n/100)
	if ( (n/10) %10) == 9:
		s += 'XC'
		n-=90
	elif ( (n/10) %10) == 4:
		s = s + 'XL'
		n-=40
	if n >= 50:
		s = s +'L'
		n-=50
	s = s + 'X'*(n/10)
	n-= 10*(n/10)
	if n == 9 :
		s = s + 'IX'
		n-=9
	elif n == 4:
		s = s + 'IV'
		n-=4
	if n >= 5:
		s = s + 'V'
		n-=5
	s = s + 'I'*n
	return s

#for x in range(1,10000):
#	if (x != RomToNum(NumToRom(x))):
#		print x, RomToNum(NumToRom(x)), NumToRom(x)

count = 0
for x in L:
#	if len(NumToRom(RomToNum(x))) < len(x):
#	count += len(NumToRom(RomToNum(x))) - len(x)
#		print x,NumToRom(RomToNum(x)), len(x), len(NumToRom(RomToNum(x)))
	count += (-len(NumToRom(RomToNum(x))) + len(x))

print count
