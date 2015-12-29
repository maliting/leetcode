def plusone(digits):
	n=len(digits)
	s=[]
	for i in range(n):
		s.append(str(digits[i]))
	z=''
	z=z.join(s)
	r=int(z)+1
	r=list(str(r))
	y=[]
	for i in range(len(r)):
		y.append(int(r[i]))
	return y		