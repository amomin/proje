A0 = load('problem81_matrix.txt');
sizeA = 80;
A = A0(1:sizeA,1:sizeA);
B = zeros(size(A));
B(:,1) = A(:,1);
for rowm = 2:sizeA
	B(rowm,1) = B(rowm-1,1) + A(rowm,1);
end
for coln = 2:sizeA
	B(1,coln)= A(1,coln) + B(1,coln-1);
	for rowm = 2:sizeA
		if (A(rowm,coln) + B(rowm,coln-1) > A(rowm,coln) + B(rowm-1,coln))
			B(rowm,coln) = A(rowm,coln) + B(rowm-1,coln);
		else
			B(rowm,coln) = A(rowm,coln) + B(rowm,coln-1);
		endif
	end
end
A
B  
B(sizeA,sizeA)