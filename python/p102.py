f = open('triangles.txt','r')
L = []
for line in f.readlines():
	L.append( map( int, line.split(',')))
#	L.append(line)
f.close()

def minus(a,b):
	return b-a

def dot(M,N):
	return M[0]*N[0] + M[1]*N[1]

def neg(M):
	return map(minus, [0]*len(M),M)

def rot(M):
	return [-M[1],M[0]]

count = 0
for line in L:
	A = line[:2]
	B = line[2:4]
	C = line[4:]
	X = map(minus,A,B)
	Y = map(minus,B,C)
	Z = map(minus,C,A)
	Xrot = rot(X)
	Yrot = rot(Y)
	Zrot = rot(Z)
	if ((dot(Xrot,A) < 0) == (dot(Xrot,Y)>0)) and ((dot(Yrot,B) < 0) == (dot(Yrot,Z)>0)) and ((dot(Zrot,C) < 0) == (dot(Zrot,X)>0)):
#		print A,B,C
		count +=1

print count
		
	

